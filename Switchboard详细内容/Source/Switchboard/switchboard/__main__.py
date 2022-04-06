# Copyright Epic Games, Inc. All Rights Reserved.
from .switchboard_dialog import SwitchboardDialog
from .switchboard_logging import LOGGER

import signal
import sys

from PySide2 import QtCore, QtWidgets

# Build resources
# "C:\Program Files (x86)\Python37-32\Lib\site-packages\PySide2\pyside2-rcc" -o D:\Switchboard\switchboard\resources.py D:\Switchboard\switchboard\ui\resources.qrc

#负责运行“独立”或者“在另一个应用里”
def launch():
    """
    Main for running standalone or in another application.
    """

    if sys.platform == 'win32':
        # works around some windows quirks so we can show the window icon
        import ctypes           #用于类型转换
        #应用ID
        app_id = u'epicgames.virtualproduction.switchboard.0.1'
        #设置当前进程的显示用户模式ID
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(app_id)
    # 启用一些Qt的属性
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    # app 标记为 Qt部件App
    app = QtWidgets.QApplication(sys.argv)
    # 主窗口对象给与 这里走的构造函数
    main_window = SwitchboardDialog()

    #如果窗口注册 就直接返回了
    if not main_window.window:
        return

    # 这里注册了一个信号槽，大致就是收到了消息，收到消息
    # closure so we can access main_window and app
    def sigint_handler(*args):
        LOGGER.info("Received SIGINT, exiting...")
        main_window.on_exit()
        app.quit()

    # install handler for SIGINT so it's possible to exit the app when pressing ctrl+c in the terminal.
    # 注册信号槽给到捕获器 比如这就给了个Ctrl+C
    signal.signal(signal.SIGINT, sigint_handler)

    #显示窗口
    main_window.window.show()

    # Enable file logging.  启用文件日志
    LOGGER.enable_file_logging()

    # Logging start.        开启一个日志信息
    LOGGER.info('----==== Switchboard ====----')

    # 这将使事件循环每200毫秒一次，这样我们就可以在SIGINT上做出更快的反应。
    # this will pump the event loop every 200ms so we can react faster on a SIGINT.
    # otherwise it will take several seconds before sigint_handler is called.
    timer = QtCore.QTimer()
    timer.start(200)
    timer.timeout.connect(lambda: None)
    # python的推出函数
    sys.exit(app.exec_())

#如果名字==“主”就启动
if __name__ == "__main__":
    launch()   #启动了