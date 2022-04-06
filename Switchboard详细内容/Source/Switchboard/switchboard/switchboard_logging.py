# Copyright Epic Games, Inc. All Rights Reserved.
import os
import sys
import time
import logging
import tempfile             #临时文件
import calendar             #日历
import datetime             #数据时间

# 从pyside2 中导入 qt的内核
from PySide2 import QtCore
#信息层级数  = 日志DEBUG倒数第二位
logging.MESSAGE_LEVEL_NUM = logging.DEBUG - 2
#OSC层级数 = 日志的倒数第一位
logging.OSC_LEVEL_NUM = logging.DEBUG - 1
#成功层级数 = 日志的信息 前进2位
logging.SUCCESS_LEVEL_NUM = logging.INFO + 2

#定义Qt句柄 （日志句柄）
class QtHandler(logging.Handler):
    # 初始化
    def __init__(self):
        logging.Handler.__init__(self)
        self.record = None

        html = """<span style="margin: 0px; display: block"><font color="grey">[{}][{}]:</font> 
        <font color="{}">{}</font></span>"""
        self.html_format = html

    # 发送消息
    def emit(self, record):
        self.record = self.format(record)
        #如果这记录不为空
        if record:
            #控制台的流输出
            ConsoleStream.stdout().write('{}'.format(self.record))
            ConsoleStream.stderr().write('{}'.format(self.record))

    #这里就是日志的内容了 record是消息，这玩意看外面怎么给
    def format(self, record):
        levelName = record.levelname

        if levelName == 'DEBUG':
            initial = 'D'
            color = '#66D9EF'
        elif levelName == 'INFO':
            initial = 'I'
            color = 'white'
        elif levelName == 'WARNING':
            initial = 'W'
            color = 'yellow' #E6DB74
        elif levelName == 'CRITICAL':
            initial = 'C'
            color = '#FD971F'
        elif levelName == 'ERROR':
            initial = 'D'
            color = '#F92672'
        elif levelName == 'OSC':
            initial = 'O'
            color = '#4F86C6'
        elif levelName == 'MESSAGE':
            initial = 'M'
            color = '#7b92ad'
        elif levelName == 'SUCCESS':
            initial = 'S'
            color = '#A6E22E'
        #html格式.格式（当前时间.然后格式是("%H:%M:%S")，然后标识号，然后接消息）
        return self.html_format.format(datetime.datetime.now().strftime("%H:%M:%S"), initial, color, record.msg)

    #获取记录
    def get_record(self):
        return self.record

#控制台流
class ConsoleStream(QtCore.QObject):
    _stdout = None
    _stderr = None
    message_written = QtCore.Signal(str)

    def write(self, message):
        if not self.signalsBlocked():
            self.message_written.emit(message)
    #静态方法
    @staticmethod
    def stdout():
        if not ConsoleStream._stdout:
            ConsoleStream._stdout = ConsoleStream()
            sys.stdout = ConsoleStream._stdout
        return ConsoleStream._stdout
    #静态方法
    @staticmethod
    def stderr():
        if not ConsoleStream._stderr:
            ConsoleStream._stderr = ConsoleStream()
            sys.stdout = ConsoleStream._stderr
        return ConsoleStream._stderr
    #清空
    def flush(self):
        pass


class HTMLogger(object):
    """This overrides the logging verbosity levels with an HTML layer for console coloring."""
    #这将用一个用于控制台着色的HTML层覆盖日志详细级别。
    def __init__(self, logger):
        #super() 函数是用于调用父类(超类)的一个方法。
        super(HTMLogger, self).__init__()
        self.logger = logger
        self.file_handler = None

        self.info(self.logger.getEffectiveLevel())
        self.add_custom_levels()

    #添加自定义层级
    def add_custom_levels(self):
        #添加一个日志级别：定义一个osc日志
        logging.addLevelName(logging.OSC_LEVEL_NUM, "OSC")
        
        def __log_osc(s, message, *args, **kwargs):
            if s.isEnabledFor(logging.OSC_LEVEL_NUM):
                s._log(logging.OSC_LEVEL_NUM, message, args, **kwargs)
        #注册
        logging.Logger.osc = __log_osc

        #添加一个日志级别：定义一个success日志
        logging.addLevelName(logging.SUCCESS_LEVEL_NUM, "SUCCESS")

        def __log_success(s, message, *args, **kwargs):
            if s.isEnabledFor(logging.SUCCESS_LEVEL_NUM):
                s._log(logging.SUCCESS_LEVEL_NUM, message, args, **kwargs)
        logging.Logger.success = __log_success

        #添加一个日志级别：定义一个Message日志
        logging.addLevelName(logging.MESSAGE_LEVEL_NUM, "MESSAGE")

        def __log_message(s, message, *args, **kwargs):
            if s.isEnabledFor(logging.MESSAGE_LEVEL_NUM):
                s._log(logging.MESSAGE_LEVEL_NUM, message, args, **kwargs)
        logging.Logger.message = __log_message

    #定义函数
    def debug(self, message, exc_info=False, current_time_only=True):
        self.logger.debug(message, exc_info=exc_info)

    def success(self, message, exc_info=False, current_time_only=True):
        self.logger.success(message, exc_info=exc_info)

    def info(self, message, exc_info=False, current_time_only=True):
        self.logger.info(message, exc_info=exc_info)

    def warning(self, message, exc_info=False, current_time_only=True):
        self.logger.warning(message, exc_info=exc_info)

    def critical(self, message, exc_info=False, current_time_only=True):
        self.logger.critical(message, exc_info=exc_info)

    def error(self, message, exc_info=False, current_time_only=True):
        self.logger.error(message, exc_info=exc_info)

    def osc(self, message, exc_info=False, current_time_only=True):
        self.logger.osc(message, exc_info=exc_info)

    def message(self, message, exc_info=False, current_time_only=True):
        self.logger.message(message, exc_info=exc_info)
        
    #获取时间戳（这个主要是 周几—天-当前时间）
    def get_timestamp(self, current_time_only=True):
        current_time = self.get_current_time()
        if current_time_only:
            return current_time

        weekday = list(calendar.day_abbr)[int(datetime.date.today().weekday())]
        day = str(datetime.date.today()).replace("-", "/")
        return " ".join([weekday, day, current_time])
    #获取当前时间：格式（小时：分钟：秒）
    @staticmethod
    def get_current_time():
        return datetime.datetime.now().strftime("%H:%M:%S")

    #启用文件日志（输入日志路径）
    def enable_file_logging(self, log_path=None):
        #先查看是不是有这个路径
        if not log_path: 
            #没有就添加
            if not os.path.isdir(DEFAULT_LOG_PATH):
                os.makedirs(DEFAULT_LOG_PATH)
            #日志路径 = 临时系统路径 下 “switchboard_时间”
            log_path = os.path.join(DEFAULT_LOG_PATH, "switchboard_{}.html".format(str(time.time())))
        #文件句柄
        self.file_handler = logging.FileHandler(log_path)
        self.logger.addHandler(self.file_handler)
        #添加日志.debug（存储所有信息）
        self.logger.setLevel(logging.DEBUG)  # Log everything.
    #设置层级
    def setLevel(self, value):
        self.logger.setLevel(value)
    #禁用文件日志 
    def disable_file_logging(self):
        #如果没有文件日志
        if not self.file_handler:
            #返回 “没有文件句柄”
            return self.logger.warning("No file handler found!")
        #移除句柄
        self.logger.removeHandler(self.file_handler)
        #把句柄关了
        self.file_handler.close()

# 1.
_LOGGER = logging.getLogger("switchboard")
#默认日志存放位置  = 系统.路径下添加（临时文件.获取临时文件，命名）   这里的就是：C:\Users\Monster\AppData\Local\Temp\switchboard 而且默认存储方式是html文件
DEFAULT_LOG_PATH = os.path.join(tempfile.gettempdir(), "switchboard")

#用宏定义替代函数调用
QT_HANDLER = QtHandler()
#日志流的句柄
PYTHON_HANDLER = logging.StreamHandler()
#日志格式
formatter = logging.Formatter('[%(levelname)s]: %(message)s')
#设置日志流的格式
PYTHON_HANDLER.setFormatter(formatter)
#2
_LOGGER.addHandler(QT_HANDLER)
_LOGGER.addHandler(PYTHON_HANDLER)
#给日志设置级别
_LOGGER.setLevel(logging.DEBUG)

PYTHON_HANDLER.setLevel(logging.DEBUG)

#通过宏定义把类的一系列操作转移到这里来
LOGGER = HTMLogger(_LOGGER)
