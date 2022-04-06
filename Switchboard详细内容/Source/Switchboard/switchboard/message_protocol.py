# Copyright Epic Games, Inc. All Rights Reserved.
# 这里是消息协议

import base64, json, uuid

# 创建启动进程消息
def create_start_process_message(
    prog_path: str,                                         # 进程路径
    prog_args: str,                                         # 进程数组
    prog_name: str,                                         # 进程名字
    caller: str,                                            # 呼叫者
    update_clients_with_stdout: bool,                       # 更新客户带有输出
    working_dir: str = "",                                  # 工作目录
    priority_modifier: int = 0                              # 优先级修饰符
):
    cmd_id = uuid.uuid4()                                   # cmd的id = 唯一标识符
    # 启动cmd
    start_cmd = {
        'command': 'start',                                             # 命令:启动
        'id': str(cmd_id),                                              # id:命令行id
        'exe': prog_path,                                               # exe: 程序路径
        'args': prog_args,                                              # 数组：程序数组
        'name': prog_name,                                              # 名字：程序名字
        'caller': caller,                                               # 呼叫者：呼叫者
        'working_dir': working_dir,                                     # 工作目录：工作目录
        'bUpdateClientsWithStdout' : update_clients_with_stdout,        # 更新客户端带有 字符串输出 ： 更新客户端带有 字符串输出
        'priority_modifier': priority_modifier,                         # 优先级修饰符 ： 优先级修饰符
    }
    message = json.dumps(start_cmd).encode() + b'\x00'                  # 消息 = json.dumps(将python对象编码成Json字符串)编码（）+结束符
    # 返回（cmd_id，消息）
    return (cmd_id, message)

# 创建 终止进程 消息（程序id）
def create_kill_process_message(program_id):
    # 控制台_id
    cmd_id = uuid.uuid4()
    # 终止_控制台 = {'command': 'kill', 'id': str(cmd_id), 'uuid': str(program_id)}
    kill_cmd = {'command': 'kill', 'id': str(cmd_id), 'uuid': str(program_id)}
    # 消息 = json.编码成json（kill_cmd）编码+结束码
    message = json.dumps(kill_cmd).encode() + b'\x00'
    # 返回（cmd_id，消息）
    return (cmd_id, message)

# 创建VCS初始化消息（提供者，VCS设置）
def create_vcs_init_message(provider, vcs_settings):
    # 控制台id
    cmd_id = uuid.uuid4()
    # vcs初始化控制台
    vcs_init_cmd = {'command': 'vcs init', 'id': str(cmd_id), 'provider': provider, 'vcs settings': vcs_settings}
    # 消息 = json.编码成json（vcs_init_cmd）编码+结束码
    message = json.dumps(vcs_init_cmd).encode() + b'\x00'
    # 返回（cmd_id，消息）
    return (cmd_id, message)

# 创建VCS报告修复消息
def create_vcs_report_revision_message(path):
    # 控制台id
    cmd_id = uuid.uuid4()
    # VCS修复控制台 
    vcs_revision_cmd = {'command': 'vcs report revision', 'id': str(cmd_id), 'path': path}
    # 消息 = json.编码成json（vcs_revision_cmd）编码+结束码
    message = json.dumps(vcs_revision_cmd).encode() + b'\x00'
    # 返回（cmd_id，消息）
    return (cmd_id, message)

# 创建VCS同步消息
def create_vcs_sync_message(revision, path):
    # 控制台ID
    cmd_id = uuid.uuid4()
    # VCS同步控制台
    vcs_sync_cmd = {'command': 'vcs sync', 'id': str(cmd_id), 'revision': revision, 'path': path}
    # 消息 = json.编码成json（vcs_sync_cmd）编码+结束码
    message = json.dumps(vcs_sync_cmd).encode() + b'\x00'
    # 返回（cmd_id，消息）
    return (cmd_id, message)

# 创建断连消息
def create_disconnect_message():
    # 控制台ID
    cmd_id = uuid.uuid4()
    # VCS同步控制台
    disconnect_cmd = {'command': 'disconnect', 'id': str(cmd_id)}
    # 消息 = json.编码成json（disconnect_cmd）编码+结束码
    message = json.dumps(disconnect_cmd).encode() + b'\x00'
    # 返回（cmd_id，消息）
    return (cmd_id, message)

# 创建发送文件消息（源文件路径，目的路径）
def create_send_file_message(path_to_source_file, destination_path):
    # 打开文件作为f 其实就是拿到文件的句柄
    with open(path_to_source_file, 'rb') as f:
        # 文件连接 = f.读取（）
        file_content = f.read()
    # 编码-内容 = base64编码（文件内容）
    encoded_content = base64.b64encode(file_content)
    # 控制台id
    cmd_id = uuid.uuid4()
    # 转移文件的cmd('命令行'：‘发送文件’，‘id’：字符串（控制台id），目的：目的路径，内容：编码内容.解码)
    transfer_file_cmd = {'command': 'send file', 'id': str(cmd_id), 'destination': destination_path, "content": encoded_content.decode()}
    # 消息 = json.编码成json（transfer_file_cmd）编码+结束码
    message = json.dumps(transfer_file_cmd).encode() + b'\x00'
    # 返回（cmd_id，消息）
    return (cmd_id, message)

# 创建 拷贝文件 从 监听消息（）
def create_copy_file_from_listener_message(path_on_listener_machine):
    # 控制台ID
    cmd_id = uuid.uuid4()
    # 拷贝文件控制台 = {命令行：接受文件，id：字符串，源：路径监听机器}
    copy_file_cmd = {'command': 'receive file', 'id': str(cmd_id), 'source': path_on_listener_machine}
    # 消息 = json.编码成json（copy_file_cmd）编码+结束码
    message = json.dumps(copy_file_cmd).encode() + b'\x00'
    # 返回（cmd_id，消息）
    return (cmd_id, message)

# 创建保持连接的消息
def create_keep_alive_message():
    # 控制台ID
    cmd_id = uuid.uuid4()
    # 拷贝文件控制台 = {命令行：保持连接，id：字符串}
    keep_alive_cmd = {'command': 'keep alive', 'id': str(cmd_id)}
    # 消息 = json.编码成json（keep_alive_cmd）编码+结束码
    message = json.dumps(keep_alive_cmd).encode() + b'\x00'
    # 返回（cmd_id，消息）
    return (cmd_id, message)

# 创建获取同步状态消息（程序id）
def create_get_sync_status_message(program_id):
    # 控制台ID
    cmd_id = uuid.uuid4()
    # 命令行 = {命令行：获取同步状态，id：字符串，uuid:程序id，是否反馈：假}
    cmd = {'command': 'get sync status', 'id': str(cmd_id), 'uuid': str(program_id), 'bEcho': False}
    # 消息 = json.编码成json（cmd）编码+结束码
    message = json.dumps(cmd).encode() + b'\x00'
    # 返回（cmd_id，消息）
    return (cmd_id, message)

# 创建重新部署监听器消息（base64监听器：字符串，sha1digest摘要：字符串）
def create_redeploy_listener_message(base64listener: str, sha1digest: str):
    '''
     Sends a command to replace the remote server's listener executable. 
     发送一个命令 去 替换 远程服务监听器exe
    '''
    # 控制台ID
    cmd_id = uuid.uuid4()
    # 重新布局命令行 = {命令行：重新部署监听器，id：字符串（cmd_id），uuid:程序id，内容：base64listener}
    redeploy_cmd = {'command': 'redeploy listener', 'id': str(cmd_id), 'sha1': sha1digest, 'content': base64listener}
    # 消息 = json.编码成json（redeploy_cmd）编码+结束码
    message = json.dumps(redeploy_cmd).encode() + b'\x00'
    # 返回（cmd_id，消息）
    return (cmd_id, message)

# 创建修复exe标识_消息（puuid）
def create_fixExeFlags_message(puuid):
    # 控制台ID
    cmd_id = uuid.uuid4()
    # 命令行 = {命令行：修复exe标识，id：字符串（cmd_id），uuid:puuid}
    cmd = {'command': 'fixExeFlags', 'id': str(cmd_id), 'uuid': str(puuid)}
    # 消息 = json.编码成json（cmd）编码+结束码
    message = json.dumps(cmd).encode() + b'\x00'
    # 返回（cmd_id，消息）
    return (cmd_id, message)

# 解码消息（消息的字节）
def decode_message(msg_in_bytes):
    # 消息作为字符串 = ‘’.加入（消息的字节）
    msg_as_str = ''.join(msg_in_bytes)
    #  json消息 = json 载入（消息作为字符串）
    msg_json = json.loads(msg_as_str)
    # 返回 消息的json文件
    return msg_json
