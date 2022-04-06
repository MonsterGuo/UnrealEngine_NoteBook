# Copyright Epic Games, Inc. All Rights Reserved.
from . import message_protocol
from .switchboard_logging import LOGGER

import datetime, select, socket, uuid, traceback, typing

from collections import deque
from threading import Thread

# 监听器客户端
class ListenerClient(object):
    '''
    Connects to a server running SwitchboardListener.
    连接到一个运行Switchboardlistener服务器
    Runs a thread to service its socket, and upon receiving complete messages,
    运行一个线程 去服务他的socket，并且收到完整的消息之后
    invokes a handler callback from that thread (`handle_connection()`).
    # 调用一个处理程序的回调 从那个线程（‘句柄连接’）
    `disconnect_delegate` is invoked on `disconnect()` or on socket errors.
    处理程序 在 代理字典中 通过了一个 包含的字典 来自监听程序的整个JSON响应。根据命令字段字符串值进行路由。
    所有新的消息并且 处理程序应当跟随这个方式。
    Handlers in the `delegates` map are passed a dict containing the entire
    JSON response from the listener, routed according to the "command" field
    string value. All new messages and handlers should follow this pattern.
    另一个是传统(VCS/FILE)委托，每个委托传递不同的(或无)参数；有关详细信息，请参阅`ROUTE_MESSAGE()`。
    The other, legacy (VCS/file) delegates are each passed different (or no)
    arguments; for details, see `route_message()`.
    '''
    # 初始化（ip地址，端口，缓冲尺寸）
    def __init__(self, ip_address, port, buffer_size=1024):
        self.ip_address = ip_address                            # ip地址
        self.port = port                                        # 端口
        self.buffer_size = buffer_size                          # 缓冲尺寸

        self.message_queue = deque()                            # 消息列队
        self.close_socket = False                               # 关闭插座

        self.socket = None                                      # 插座
        self.handle_connection_thread = None                    # 句柄连接线程

        #TODO: Consider converting these delegates to Signals and sending dict.

        self.disconnect_delegate = None                         # 断开连接的代理

        self.command_accepted_delegate = None                   # 命令接受代理
        self.command_declined_delegate = None                   # 命令拒绝代理

        self.vcs_init_completed_delegate = None                 # VCS初始化完成代理
        self.vcs_init_failed_delegate = None                    # VCS初始化失败代理
        self.vcs_report_revision_completed_delegate = None      # VCS报告修改完成代理
        self.vcs_report_revision_failed_delegate = None         # VCS报告修改失败代理
        self.vcs_sync_completed_delegate = None                 # VCS同步完成代理
        self.vcs_sync_failed_delegate = None                    # VCS同步失败代理

        self.send_file_completed_delegate = None                # 发送文件完成代理
        self.send_file_failed_delegate = None                   # 发送文件失败代理
        self.receive_file_completed_delegate = None             # 接收文件完成代理
        self.receive_file_failed_delegate = None                # 接收文件失败代理

        #自己的代理:类型 字典【字符串，类型可选[类型.可调用[[类型.字典]，空]]] = {状态 ： 空，获取同步状态 ：空}
        self.delegates: typing.Dict[ str, typing.Optional[ typing.Callable[[typing.Dict], None] ] ] = {
            "state" : None,
            "get sync status" : None,
        }
        # 最后激活时间 
        self.last_activity = datetime.datetime.now()
    
    # 参数： 服务端地址
    @property
    def server_address(self):
        if self.ip_address:
            return (self.ip_address, self.port)
        return None

    # 参数：是否连接
    @property
    def is_connected(self):
        # I ran into an issue where running disconnect in a thread was causing the socket maintain it's reference
        # But self.socket.getpeername() fails because socket is sent to none. I am assuming that is due
        # it python's threading. Adding a try except to handle this
        try:
            if self.socket and self.socket.getpeername():   # 如果 插座 并且 插座获取对等的连接
                return True
        except:
            return False
        return False

    # 连接
    def connect(self, ip_address=None):
        # 断开连接
        self.disconnect()
        # ip地址
        if ip_address:
            self.ip_address = ip_address
        elif not self.ip_address:       # 如果不存在ip地址
            LOGGER.debug('No ip_address has been set. Cannot connect')
            return False
        # 关闭插座 = 假
        self.close_socket = False
        # 最后激活时间
        self.last_activity = datetime.datetime.now()

        try:
            # 日志 （连接（ip地址：端口））
            LOGGER.info(f"Connecting to {self.ip_address}:{self.port}")
            # 注册插座
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # 插座连接
            self.socket.connect(self.server_address)

            # Create a thread that waits for messages from the server
            # 创建一个线程 为线程 等待消息（句柄连接）
            self.handle_connection_thread = Thread(target=self.handle_connection)
            # 线程启动
            self.handle_connection_thread.start()
        # 系统错误
        except OSError:
            # 插座错误：ip地址：端口
            LOGGER.error(f"Socket error: {self.ip_address}:{self.port}")
            self.socket = None
            return False

        return True

    # 断开连接（不可意料，意料的）
    def disconnect(self, unexpected=False, exception=None):
        # 是否连接
        if self.is_connected:
            # 消息 = 消息协议.创建断连信息
            _, msg = message_protocol.create_disconnect_message()
            # 发送消息
            self.send_message(msg)
            # 关闭插座
            self.close_socket = True
            # 连接线程的句柄加入
            self.handle_connection_thread.join()

    # 连接句柄
    def handle_connection(self):
        # 缓冲区
        buffer = []
        # 保证连接 超时
        keepalive_timeout = 1.0
        # 是否连接
        while self.is_connected:
            try:
                rlist = [self.socket]           # r列表
                wlist = []                      # w列表
                xlist = []                      # x列表
                read_timeout = 0.1              # 读取 超时

                # 读取插座 = 选择（r列表，w列表，x列表，读取超时）
                read_sockets, _, _ = select.select(rlist, wlist, xlist, read_timeout)
                # 消息列队长度
                while len(self.message_queue):
                    # 消息的位数
                    message_bytes = self.message_queue.pop()
                    # 插座.发送所有（消息位）
                    self.socket.sendall(message_bytes)
                    # 最后激活时间
                    self.last_activity = datetime.datetime.now()
                
                # 读取插座中的所有
                for rs in read_sockets:
                    # 收到的数据 =读取的插座.回收消息（缓冲尺寸).解码
                    received_data = rs.recv(self.buffer_size).decode()
                    # 进程接收的数据（数据，接收的数据）
                    self.process_received_data(buffer, received_data)
                # 时间增量 = 当前时间 - 最后时间
                delta = datetime.datetime.now() - self.last_activity
                # 时间增量 大于 保持连接的超时
                if delta.total_seconds() > keepalive_timeout:
                    # 消息 = 消息协议.创建保持连接的消息
                    _, msg = message_protocol.create_keep_alive_message()
                    # 插座 发送所有
                    self.socket.sendall(msg)
                # 关闭插座 并且 消息列队的长度 = 0
                if self.close_socket and len(self.message_queue) == 0:
                    # 插座终止
                    self.socket.shutdown(socket.SHUT_RDWR)
                    # 插座关闭·
                    self.socket.close()
                    # 插座对象清空
                    self.socket = None
                    # 如果存在 断开连接的代理
                    if self.disconnect_delegate:
                        # 断开连接的代理 （意料之外：假 ，意料中的:空）
                        self.disconnect_delegate(unexpected=False, exception=None)

                    break
            # 连接重置错误
            except ConnectionResetError as e:
                # 插座断连
                self.socket.shutdown(socket.SHUT_RDWR)
                # 插座关闭
                self.socket.close()
                # 插座对象清空
                self.socket = None
                # 断连的代理
                if self.disconnect_delegate:
                    # 断连代理（不可预知为真）
                    self.disconnect_delegate(unexpected=True, exception=e)

                return # todo: this needs to send a signal back to the main thread so the thread can be joined
            # 系统错误
            except OSError as e: # likely a socket error, so self.socket is not useable any longer
                # 插座清空
                self.socket = None
                # 断开连接的代理
                if self.disconnect_delegate:
                    # 断开连接的代理（）
                    self.disconnect_delegate(unexpected=True, exception=e)

                return
    # 路由消息
    def route_message(self, message):
        '''
         Routes the received message to its delegate 
        路由收到的消息到它的代理
        '''
        # 代理 = 代理获取（消息[命令]，空）
        delegate = self.delegates.get(message['command'], None)
        # 代理
        if delegate:
            # 代理消息
            delegate(message)
            return

        # 如果 消息中存在 “命令接受”
        if "command accepted" in message:
            # 消息id = uuid。uuid（消息中的id）
            message_id = uuid.UUID(message['id'])
            # 如果消息[消息接受] 为真
            if message['command accepted'] == True:
                # 如果 命令接收的代理
                if self.command_accepted_delegate:
                    # 命令接收代理（消息id）
                    self.command_accepted_delegate(message_id)
            else:
                # 命令拒绝代理
                if self.command_declined_delegate:
                    # 命令拒绝代理（消息id，消息[错误]）
                    self.command_declined_delegate(message_id, message["error"])

        # 消息中 “VCS 初始化完成”
        elif "vcs init complete" in message:
            # 消息 VCS初始化完成 为真
            if message['vcs init complete'] == True:
                # VCS初始化完成的代理
                if self.vcs_init_completed_delegate:
                    # VCS初始化完成的代理
                    self.vcs_init_completed_delegate()
            else:
                # VCS初始化失败的代理
                if self.vcs_init_failed_delegate:
                    # VCS初始化失败代理#
                    self.vcs_init_failed_delegate(message['error'])

        # 如果 “VCS报道修改完成” 在消息中
        elif "vcs report revision complete" in message:
            # 如果 消息【VCS报道修改完成】 为真
            if message['vcs report revision complete'] == True:
                # 如果 VCS报道修改完成代理
                if self.vcs_report_revision_completed_delegate:
                    # VCS报道修改完成代理（消息【修改】）
                    self.vcs_report_revision_completed_delegate(message['revision'])
            else:
                # VCS报道修改失败的代理
                if self.vcs_report_revision_failed_delegate:
                    # VCS报道修改失败代理[消息【错误】]
                    self.vcs_report_revision_failed_delegate(message['error'])

        # “VCS 同步完成”
        elif "vcs sync complete" in message:
            # 如果 [VCS 同步完成 ] 为真
            if message['vcs sync complete'] == True:
                # VCS同步完成代理
                if self.vcs_sync_completed_delegate:
                    # VCS同步完成代理（消息[修改]）
                    self.vcs_sync_completed_delegate(message['revision'])
            else:
                # VCS同步失败代理
                if self.vcs_sync_failed_delegate:
                    # VCS同步失败代理（消息[错误]）
                    self.vcs_sync_failed_delegate(message['error'])
        # 发送文件完成 在 消息中
        elif "send file complete" in message:
            # 如果 消息['发送文件完成'] = 真
            if message['send file complete'] == True:
                # 发送文件完成的代理
                if self.send_file_completed_delegate:
                    # 发送文件完成代理（消息[目的]）
                    self.send_file_completed_delegate(message['destination'])
            else:
                # 发送文件失败代理
                if self.send_file_failed_delegate:
                    #发送文件失败代理（消息[目的]，消息[错误]）
                    self.send_file_failed_delegate(message['destination'], message['error'])
        # 接收文件完成 在 消息中            
        elif "receive file complete" in message:
            # 如果 消息中[接收文件完成] = 真
            if message['receive file complete'] == True:
                # 接收文件完成代理
                if self.receive_file_completed_delegate:
                    # 接收文件完成代理（消息[源]，消息[内容]）
                    self.receive_file_completed_delegate(message['source'], message['content'])
            else:
                # 接受文件失败代理
                if self.receive_file_failed_delegate:
                    # 接收文件失败代理（消息[源]，消息[内容]）
                    self.receive_file_failed_delegate(message['source'], message['error'])
        else:
            # 错误日志
            LOGGER.error(f'Unhandled message: {message}')
            raise ValueError

    # 进程接收数据
    def process_received_data(self, buffer, received_data):
        # 接受数组中的符号
        for symbol in received_data:
            buffer.append(symbol)
            # 如果符号是结束符
            if symbol == '\x00': # found message end
                # 将缓冲弹出
                buffer.pop() # remove terminator
                # 消息 = 消息协议.解码消息（缓冲）
                message = message_protocol.decode_message(buffer)
                # 缓冲清空
                buffer.clear()

                # route message to its assigned delegate
                # 远程消息
                try:
                    self.route_message(message)
                except:
                    # 日志错误（表示错误的消息）
                    LOGGER.error(f"Error while parsing message: \n\n=== Traceback BEGIN ===\n{traceback.format_exc()}=== Traceback END ===\n")

    # 发送消息
    def send_message(self, message_bytes):
        # 自己是否连接
        if self.is_connected:
            # 连接上了（消息：发送（ip地址：消息位））
            LOGGER.message(f'Message: Sending ({self.ip_address}): {message_bytes}')
            # 消息列队。拼接（消息位）
            self.message_queue.appendleft(message_bytes)
        else:
            # 日志 错误
            LOGGER.error(f'Message: Failed to send ({self.ip_address}): {message_bytes}. No socket connected')
            # 断开连接代理
            if self.disconnect_delegate:
                # 断开连接代理（不可预知的为真,可预知为空）
                self.disconnect_delegate(unexpected=True, exception=None)
