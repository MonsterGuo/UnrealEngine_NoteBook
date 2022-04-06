# Copyright Epic Games, Inc. All Rights Reserved.
import subprocess
import socket
import re
import os
import marshal
import sys
from .switchboard_logging import LOGGER
from functools import wraps
from .config import CONFIG

# 获取子进程启动信息
def get_sp_startupinfo():
    ''' 
    Returns subprocess.startupinfo and avoids extra cmd line window in windows.
    返回 子进程.启动信息 并且 避免额外的命令行窗口 在窗口中
    '''
    # 启动信息 = 子进程.启动信息（）构造函数
    startupinfo = subprocess.STARTUPINFO()
    # 系统平台.启动自（“win”）
    if sys.platform.startswith("win"):
        # 启动信息的标识
        startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    # 启动信息
    return startupinfo

# p4_登录
def p4_login(f):
    @wraps(f)       # 为了返回正常的函数名
    def wrapped(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except Exception as e:
            LOGGER.error(f'{e}')
            LOGGER.error('Error running P4 command. Please make sure you are logged into Perforce and environment variables are set')
            return None

    return wrapped


@p4_login   #P4_login修饰了下面面的函数
def p4_stream_root(client):
    """ 
    Returns stream root of client. 
    返回 客户端 流的根
    """
    # p4命令行
    p4_command = f'p4 -ztag -F "%Stream%" -c {client} stream -o'
    # 日志
    LOGGER.info(f"Executing: {p4_command}")
    # p4 的结果 （执行p4命令）
    p4_result = subprocess.check_output(p4_command, startupinfo=get_sp_startupinfo()).decode()
    # 如果没有结果
    if p4_result:
        return p4_result.strip()    # 结果去除
    return None


@p4_login   #P4_login修饰了下面面的函数
def p4_where(client, local_path):
    """
        Returns depot path of local file.
        返回本地文件的存放路径。
    """
    # p4命令行
    p4_command = f'p4 -ztag -c {client} -F "%depotFile%" where {local_path}'
    # 日志
    LOGGER.info(f"Executing: {p4_command}")
    # p4 的结果 （执行p4命令）
    p4_result = subprocess.check_output(p4_command, startupinfo=get_sp_startupinfo()).decode()
    if p4_result:
        return p4_result.strip()  # 以空格为分割
    return None

# 获取p4 最后的更改列表
@p4_login
def p4_latest_changelist(p4_path, working_dir, num_changelists=10):
    """
    Return (num_changelists) latest CLs
    """
    # p4命令行
    p4_command = f'p4 -ztag -F "%change%" changes -m {num_changelists} {p4_path}/...'
    # 日志
    LOGGER.info(f"Executing: {p4_command}")
    # p4 的结果 （执行p4命令）
    p4_result = subprocess.check_output(p4_command, cwd=working_dir, startupinfo=get_sp_startupinfo()).decode()

    if p4_result:
        return p4_result.split()    # 以空格为分割

    return None

# 获取p4 用户名
@p4_login
def p4_current_user_name():
    # p4命令行
    p4_command = f'p4 set P4USER'
    # p4 的结果 （执行p4命令）
    p4_result = subprocess.check_output(p4_command, startupinfo=get_sp_startupinfo()).decode().rstrip()
    # re 
    p = re.compile("P4USER=(.*)\\(set\\)")
    matches = p.search(p4_result)
    if matches:
        return matches.group(1).rstrip()
    return None

# P4 编辑
@p4_login
def p4_edit(file_path):
    # p4命令行
    p4_command = f'p4 edit "{file_path}"'
    # p4 的结果 （执行p4命令）
    p4_result = subprocess.check_output(p4_command, startupinfo=get_sp_startupinfo()).decode()
    LOGGER.debug(p4_result)
