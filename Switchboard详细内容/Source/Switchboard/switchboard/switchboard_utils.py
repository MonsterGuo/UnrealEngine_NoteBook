# Copyright Epic Games, Inc. All Rights Reserved.
from .switchboard_logging import LOGGER

from enum import Enum
import datetime
import subprocess
import os
import threading
import sys

# 优先级修饰符
class PriorityModifier(Enum):
    '''
     Corresponds to `int32 PriorityModifier` parameter to `FPlatformProcess::CreateProc`.
    对应于 “32整形 参数优先级” 参数 对应到 “平台进程::创建进程”
    '''
    Low = -2
    Below_Normal = -1
    Normal = 0
    Above_Normal = 1
    High = 2

# 获取隐藏SP启动信息
def get_hidden_sp_startupinfo():
    ''' 
    Returns subprocess.startupinfo and avoids extra cmd line window in Windows. 
    返回子进程的启动信息，并避免在Windows中额外的命令行窗口。
    '''
    # 启动信息  = 子进程.启动信息（）
    startupinfo = subprocess.STARTUPINFO()
    # 系统平台.启动自 （win）
    if sys.platform.startswith("win"):
        # 启动信息.dw标识 
        startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    # 返回启动信息
    return startupinfo

# 重复函数
class RepeatFunction(object):
    """
    Repeate a function every interval until timeout is reached or the function returns True
    每隔一段时间重复一个函数，直到超时或该函数返回True
    """
    def __init__(self, interval, timeout, function, *args, **kwargs):
        self.interval = interval                                            # 间隔
        self.timeout = datetime.timedelta(seconds=timeout)                  # 超时
        self.function = function                                            # 函数
        self.args = args                                                    # 参数
        self.kwargs = kwargs                                                # 带名字的参数
        # 结果函数
        self.results_function = None
        # 结束函数
        self.finish_function = None
        # 结束参数
        self.finish_args = None
        # 结束带名字的参数
        self.finish_kwargs = None
        # 超时函数
        self.timeout_function = None
        # 超时参数
        self.timeout_args = None
        # 超时带参数名参数
        self.timeout_kwargs = None

        #启动时间
        self.start_time = None
        # 启动标识
        self._started = False
        # 结束标识
        self._stop = False

    # 添加结束的回调
    def add_finish_callback(self, function, *args, **kwargs):
        # When finish is succesfull
        # 当结束是成功的
        self.finish_function = function
        self.finish_args = args
        self.finish_kwargs = kwargs

    # 添加超时的回调
    def add_timeout_callback(self, function, *args, **kwargs):
        self.timeout_function = function
        self.timeout_args = args
        self.timeout_kwargs = kwargs

    # 启动（结果函数）
    def start(self, results_function=None):
        # 启动时间 = 时间获取：当前时间
        self.start_time = datetime.datetime.now()
        # 结果函数 = 结果函数
        self.results_function = results_function
        # 运行函数()
        self._run()
    # 停止
    def stop(self):
        #停止标识符
        self._stop = True
    # 运行
    def _run(self):
        # 如果 停止标识 为 真
        if self._stop:
            return
        # 时间增量 = （当前时间值 - 启动时间）
        time_delta = (datetime.datetime.now() - self.start_time)
        # 如果 "时间增量"大于“超时值”并且“启动了的标识”
        if time_delta > self.timeout and self._started:
            # 超时函数
            if self.timeout_function:
                # 超时函数（超时参数，超时参数键值组）
                self.timeout_function(*self.timeout_args, **self.timeout_kwargs)
            return

        # Be sure the function runs atleast 1 time
        # 确认函数已经运行了一次
        # 返回了 ：启动的标识符为真
        self._started = True

        # Run the function 实际函数
        results = self.function(*self.args, **self.kwargs)
        # 如果 有结果 并且 有自己的结果函数
        if results and self.results_function:
            # 把结果丢到结果函数
            if self.results_function(results):
                # 如果存在结束函数
                if self.finish_function:
                    # 结束函数 （结束参数，结束对值参数）
                    self.finish_function(*self.finish_args, **self.finish_kwargs)
                return
        # 线程.时间（间隔，运行）.启动  循环触发
        threading.Timer(self.interval, self._run).start()

# 轮询 进程
class PollProcess(object):
    '''
    Have the same signature as a popen object as a backup if a ue4 process is already running
    on the machine
    如果ue4进程已经在机器上运行，是否有与popen对象相同的签名作为备份
    '''
    # 初始化
    def __init__(self, task_name: str):
        # 任务名
        self.task_name = task_name

    def poll(self):
        # 'list' output format because default 'table' truncates imagename to 25 characters
        # “列表” 输出格式 因为 默认的“table”截断 图像名 到 25个字符
        # 这里的“f”是字符串
        # tasklist 是命令行 
        # /FI显示一系列符合筛选器指定的进程  
        # IMAGENAME 映像名称
        # /FO指定输出格式，有效值: "TABLE"、"LIST"、"CSV"
        tasklist_cmd = f"tasklist /FI \"IMAGENAME eq {self.task_name}\" /FO list"
        #了解此处发生的情况操作系统错误：[WinError 6]句柄无效
        try: # Figure out what is happening here OSError: [WinError 6] The handle is invalid
            tasklist_output = subprocess.check_output(tasklist_cmd, startupinfo=get_hidden_sp_startupinfo()).decode()

            #p = re.compile(f"{self.task_name} (.*?) Console")
            # Some process do not always list the .exe in the name
            if os.path.splitext(self.task_name)[0].lower() in tasklist_output.lower():
                return None
            return True
        except:
            return True
    #终止进程
    def kill(self):
        try:
            # 子进程 控制台操作（任务关闭 /F /IM ）
            # /F 是强制关闭 
            # /IM 是映像名
            subprocess.check_output(f"taskkill.exe /F /IM {self.task_name}")
        except:
            pass

# 下载文件（地址，本地文件名）
def download_file(url, local_filename):
    import requests                                                 # 用于下载的库
    with requests.get(url, stream=True) as r:                       # 获取下载
        r.raise_for_status()                                        # 提升状态
        with open(local_filename, 'wb') as f:                       # 打开本文
            for chunk in r.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)                                  # 文件写入
    return local_filename                                           # 返回本地文件名

# 抓取名 拼接的“{场记板}_T{镜头编号}”
def capture_name(slate, take):                                      
    return f'{slate}_T{take}'

# 时间转换成字符串
def date_to_string(date):
    # 输出字符串形式的时间（年月日）
    return date.strftime("%y%m%d")

# 移除前缀（字符串，前缀）
def remove_prefix(str, prefix):
    # 如果 字符串.开始带有（前缀）
    if str.startswith(prefix):
        # 返回 字符串（从前缀开始以后的值）
        return str[len(prefix):]
    return str #不然就直接移除