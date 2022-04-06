# Copyright Epic Games, Inc. All Rights Reserved.

from .config import CONFIG, SETTINGS, DEFAULT_MAP_TEXT                                  #配置 看似变量，实际上是宏的对象
from . import config
from . import config_osc as osc                                                         #从config_osc作为OSC
from . import p4_utils                                                                  #P4单元
from . import recording                                                                 #导入记录
from . import resources                                                                 #导入资源
from . import switchboard_application                                                   #Swithboard应用
from switchboard.add_config_dialog import AddConfigDialog                               #添加配置对话框
from switchboard.device_list_widget import DeviceListWidget, DeviceWidgetHeader         #设备列表部件
from switchboard.devices.device_base import DeviceStatus                                #设备部件下的，部件基础
from switchboard.devices.device_manager import DeviceManager                            #添加设备管理器
from .switchboard_logging import ConsoleStream, DEFAULT_LOG_PATH, LOGGER                #Switchboard日志 导入 控制台流，默认配置路径，日志
from switchboard.settings_dialog import SettingsDialog                                  #设置配置框
from . import switchboard_utils                                                         #switchboard实用程序
import switchboard.switchboard_widgets as sb_widgets                                    #switchboard的部件组

import datetime                             #时间日志
from enum import IntEnum, unique, auto      #枚举类型
import logging                              #日志
import os                                   #系统IO
import threading                            #进程

#从pyside2中导入 qt内核 qtGui qtUi工具 qt部件
from PySide2 import QtCore, QtGui, QtUiTools, QtWidgets

ENGINE_PATH = "../../../../.."                              #引擎路径
RELATIVE_PATH = os.path.dirname(__file__)                   #当前文件的相对路径
EMPTY_SYNC_ENTRY = "-- None --"                             #清空异步进入

#一维
@unique
class ApplicationStatus(IntEnum):
    DISCONNECTED = auto()       #断连
    CLOSED = auto()             #关闭
    SYNCING = auto()            #异步
    OPEN = auto()               #打开


class SwitchboardDialog(QtCore.QObject):
    #switch对话框初始化过程
    def __init__(self):
        super().__init__()
        #字体
        fontDB = QtGui.QFontDatabase()
        fontDB.addApplicationFont(os.path.join(ENGINE_PATH, 'Content/Slate/Fonts/Roboto-Bold.ttf'))
        fontDB.addApplicationFont(os.path.join(ENGINE_PATH, 'Content/Slate/Fonts/Roboto-Regular.ttf'))
        fontDB.addApplicationFont(os.path.join(ENGINE_PATH, 'Content/Slate/Fonts/DroidSansMono.ttf'))

        #控制台流
        ConsoleStream.stderr().message_written.connect(self._console_pipe)

        # Set the UI object
        # 设置UI对象
        loader = QtUiTools.QUiLoader()
        loader.registerCustomWidget(sb_widgets.FramelessQLineEdit)      #无边框 条状可编辑框
        loader.registerCustomWidget(DeviceWidgetHeader)                 #注册设备部件头部
        loader.registerCustomWidget(DeviceListWidget)                   #注册设备部件
        loader.registerCustomWidget(sb_widgets.ControlQPushButton)      #在sb_widget中注册其余两个部件

        #自己的窗口添加 = 从QtUi工具中载入 UI
        self.window = loader.load(os.path.join(RELATIVE_PATH, "ui/switchboard.ui"))
        #初始化事件筛选 
        self.window.installEventFilter(self) # used to shut down services cleanly on exit  这玩意用在当关闭服务时清理工作

        # Load qss file for dark styling  为暗黑模式载入qss文件
        qss_file = os.path.join(RELATIVE_PATH, "ui/switchboard.qss")
        self.stylesheet = None
        with open(qss_file, "r") as styling:
            self.stylesheet = styling.read()
            self.window.setStyleSheet(self.stylesheet)

        # Get the available configs   这里获取可用的配置文件
        self.available_configs = config.list_config_files()

        #定义一堆对象
        self._shoot = None
        self._sequence = None
        self._slate = None
        self._take = None
        self._project_changelist = None
        self._engine_changelist = None
        self._level = None
        self._multiuser_session_name = None
        self._is_recording = False
        self._description = 'description'

        # Recording Manager
        self.recording_manager = recording.RecordingManager(CONFIG.SWITCHBOARD_DIR)
        # 信号：记录管理保存.链接到（recording_manager_saved）
        self.recording_manager.signal_recording_manager_saved.connect(self.recording_manager_saved)

        # DeviceManager   初始化设备管理器
        self.device_manager = DeviceManager()
        # 信号：设备添加
        self.device_manager.signal_device_added.connect(self.device_added)

        # Transport Manager
        #self.transport_queue = recording.TransportQueue(CONFIG.SWITCHBOARD_DIR)
        #self.transport_queue.signal_transport_queue_job_started.connect(self.transport_queue_job_started)
        #self.transport_queue.signal_transport_queue_job_finished.connect(self.transport_queue_job_finished)

        
        self.shoot = 'Default'
        self.sequence = SETTINGS.CURRENT_SEQUENCE   #从设置中获取当前sequence
        self.slate = SETTINGS.CURRENT_SLATE         #从设置中获取当前slate
        self.take = SETTINGS.CURRENT_TAKE           #从设置中获取当前Take

        # Device List Widget  这里是注册设备列表
        self.device_list_widget = self.window.device_list_widget
        # When new widgets are added, register the signal/slots


        # 注册信号槽事件 包括注册，连接 所有插件设备，打开所有插件设备
        self.device_list_widget.signal_register_device_widget.connect(self.register_device_widget)
        self.device_list_widget.signal_connect_all_plugin_devices_toggled.connect(self.on_all_plugin_devices_connect_toggled)
        self.device_list_widget.signal_open_all_plugin_devices_toggled.connect(self.on_all_plugin_devices_open_toggled)

        # forward device(widget) removal between ListWidget and DeviceManager
        #这个是设备管理器 信号事件 设备列表：移除设备（hash值），设备管理：设备移除
        self.device_list_widget.signal_remove_device.connect(self.device_manager.remove_device_by_hash)
        self.device_manager.signal_device_removed.connect(self.on_device_removed)

        # DeviceManager initialize with from the config
        # 写入保存允许
        CONFIG.push_saving_allowed(False)
        try:
            #重置设置，然后从配置中读取设备
            self.device_manager.reset_plugins_settings(CONFIG)
            self.device_manager.add_devices(CONFIG._device_data_from_config)
        finally:
            CONFIG.pop_saving_allowed()

        # add menu for adding new devices 为添加新的设备 添加菜单
        self.device_add_menu = QtWidgets.QMenu()
        self.device_add_menu.setStyleSheet(self.stylesheet)                                         #添加样式表
        self.device_add_menu.aboutToShow.connect(lambda: self.show_device_add_menu())               #关于先hi
        self.window.device_add_tool_button.setMenu(self.device_add_menu)                            #设置菜单
        self.window.device_add_tool_button.clicked.connect(lambda: self.show_device_add_menu())     #点击之后显示菜单
        self.device_add_menu.triggered.connect(self.on_triggered_add_device)                        #在菜单栏中选完后 添加菜单

        # Start the OSC server 启动OSC服务
        self.osc_server = switchboard_application.OscServer()                                       #初始化OSC对象
        self.osc_server.launch(SETTINGS.IP_ADDRESS, CONFIG.OSC_SERVER_PORT.get_value())             #启动OSC服务

        # Register with OSC server 注册OSC服务   调度映射
        self.osc_server.dispatcher_map(osc.TAKE, self.osc_take)
        self.osc_server.dispatcher_map(osc.SLATE, self.osc_slate)
        self.osc_server.dispatcher_map(osc.SLATE_DESCRIPTION, self.osc_slate_description)
        self.osc_server.dispatcher_map(osc.RECORD_START, self.osc_record_start)
        self.osc_server.dispatcher_map(osc.RECORD_STOP, self.osc_record_stop)
        self.osc_server.dispatcher_map(osc.RECORD_CANCEL, self.osc_record_cancel)
        self.osc_server.dispatcher_map(osc.RECORD_START_CONFIRM, self.osc_record_start_confirm)
        self.osc_server.dispatcher_map(osc.RECORD_STOP_CONFIRM, self.osc_record_stop_confirm)
        self.osc_server.dispatcher_map(osc.RECORD_CANCEL_CONFIRM, self.osc_record_cancel_confirm)
        self.osc_server.dispatcher_map(osc.UE4_LAUNCH_CONFIRM, self.osc_ue4_launch_confirm)
        self.osc_server.dispatcher.map(osc.OSC_ADD_SEND_TARGET_CONFIRM, self.osc_add_send_target_confirm, 1, needs_reply_address=True)      #osc添加目标确认
        self.osc_server.dispatcher.map(osc.ARSESSION_START_CONFIRM, self.osc_arsession_start_confrim, 1, needs_reply_address=True)          #会话开始
        self.osc_server.dispatcher.map(osc.ARSESSION_STOP_CONFIRM, self.osc_arsession_stop_confrim, 1, needs_reply_address=True)            #会话结束
        self.osc_server.dispatcher_map(osc.BATTERY, self.osc_battery)                                                                       #OSC电量
        self.osc_server.dispatcher_map(osc.DATA, self.osc_data)                                                                             #OSC数据

        # Connect UI to methods 连接UI方式
        self.window.multiuser_session_lineEdit.textChanged.connect(self.set_multiuser_session_name)                     # 更改多用户会话的名称
        self.window.slate_line_edit.textChanged.connect(self._set_slate)                                                # 设置slate的名称
        self.window.take_spin_box.valueChanged.connect(self._set_take)                                                  # 设置take的值
        self.window.sequence_line_edit.textChanged.connect(self._set_sequence)                                          # 设置sequnce
        self.window.level_combo_box.currentTextChanged.connect(self._set_level)                                         # 关卡选择
        self.window.project_cl_combo_box.currentTextChanged.connect(self._set_project_changelist)                       # 引擎的更改列表
        self.window.engine_cl_combo_box.currentTextChanged.connect(self._set_engine_changelist)                         # 项目的更改列表
        self.window.logger_level_comboBox.currentTextChanged.connect(self.logger_level_comboBox_currentTextChanged)     # 日志层级的选择盒子
        self.window.record_button.released.connect(self.record_button_released)                                         # 记录按键
        self.window.sync_all_button.clicked.connect(self.sync_all_button_clicked)                                       # 同步所有的按键
        self.window.build_all_button.clicked.connect(self.build_all_button_clicked)                                     # 构建所有的按键
        self.window.sync_and_build_all_button.clicked.connect(self.sync_and_build_all_button_clicked)                   # 同步并且构建所有的按键
        self.window.refresh_project_cl_button.clicked.connect(self.refresh_project_cl_button_clicked)                   # 刷新项目更新的按键
        self.window.refresh_engine_cl_button.clicked.connect(self.refresh_engine_cl_button_clicked)                     # 刷新引擎更改的按键
        self.window.connect_all_button.clicked.connect(self.connect_all_button_clicked)                                 # 链接所有的按键触发事件
        self.window.launch_all_button.clicked.connect(self.launch_all_button_clicked)                                   # 启动所有的按键点击

        # TransportQueue Menu
        #self.window.transport_queue_push_button.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        #self.transport_queue_menu = QtWidgets.QMenu(self.window.transport_queue_push_button)
        #self.transport_queue_menu.aboutToShow.connect(self.transport_queue_menu_about_to_show)
        #self.window.transport_queue_push_button.setMenu(self.transport_queue_menu)

        # entries will be removed from the log window after the number of maximumBlockCount entries has been reached
        # 达到maximumBlockCount条目数后，条目将从日志窗口中删除 日志达到1000后清除
        self.window.base_console.document().setMaximumBlockCount(1000)

        # Menu items 菜单部分
        self.window.menu_new_config.triggered.connect(self.menu_new_config)                                         #菜单新的配置（新建配置）
        self.window.menu_delete_config.triggered.connect(self.menu_delete_config)                                   #菜单删除配置（删除配置）
        self.window.update_settings.triggered.connect(self.menu_update_settings)                                    #菜单更新配置（对应setting部分）

        # Plugin UI
        self.device_manager.plug_into_ui(self.window.menu_bar, self.window.tabs_main)

        # If starting up with new config, open the menu to create a new one
        # 如果启动 带一个新的配置，打开菜单去创建一个新的
        if not CONFIG.file_path:
            self.menu_new_config()  #这里就弹出一个新建配置
        else:
            self.toggle_p4_controls(CONFIG.P4_ENABLED.get_value())          #如果配置获取到了，就检测p4,然后刷新关卡，更新配置菜单 """  """
            self.refresh_levels()
            self.update_configs_menu()

        #设置配置钩子 捆绑链接作用
        self.set_config_hooks()
        #设置 多用户会话名
        self.set_multiuser_session_name(f'{SETTINGS.MUSERVER_SESSION_NAME}')

        # Run the transport queue
        #self.transport_queue_resume()
    # 设置配置UI钩子
    def set_config_hooks(self):                                                                                     #钩子的实际内容
        CONFIG.P4_PROJECT_PATH.signal_setting_changed.connect(lambda: self.p4_refresh_project_cl())                 #将P4项目路径链接到p4刷新项目更改列表
        CONFIG.P4_ENGINE_PATH.signal_setting_changed.connect(lambda: self.p4_refresh_engine_cl())                   #将P4引擎路径链接到p4刷新项目更改列表
        CONFIG.BUILD_ENGINE.signal_setting_changed.connect(lambda: self.p4_refresh_engine_cl())                     #将构建引擎链接到p4刷新项目更改列表
        CONFIG.P4_ENABLED.signal_setting_changed.connect(lambda _, enabled: self.toggle_p4_controls(enabled))       #将p4启用链接到 触发p4控制
        CONFIG.MAPS_PATH.signal_setting_changed.connect(lambda: self.refresh_levels())                              #将 地图路径 更新到刷新关卡
        CONFIG.MAPS_FILTER.signal_setting_changed.connect(lambda: self.refresh_levels())                            #地图筛选 链接到刷新关卡

    def show_device_add_menu(self):                                                                                 #显示设备添加菜单
        self.device_add_menu.clear()                                                                                #先清除设备的菜单
        plugins = sorted(self.device_manager.available_device_plugins(), key=str.lower)                             #排序允许的设备插件，字符串从小到大
        for plugin in plugins:                                                                                      #遍历所有可用插件
            icons = self.device_manager.plugin_icons(plugin)                                                        #获取插件的图标
            icon = icons["enabled"] if "enabled" in icons.keys() else QtGui.QIcon()
            self.device_add_menu.addAction(icon, plugin)                                                            # 将插件和图标添加到菜单
        self.window.device_add_tool_button.showMenu()                                                               #将菜单显示（Qt的操作）

    #触发添加设备
    def on_triggered_add_device(self, action):
        device_type = action.text()
        dialog = self.device_manager.get_device_add_dialog(device_type)         #日志 = 从设备管理器那获取的设备种类
        dialog.exec()                                                           #日志 = 执行

        if dialog.result() == QtWidgets.QDialog.Accepted:                       #如果日志接受
            for device in dialog.devices_to_remove():                           #如果设备在要移除的设备中 就把这些设备移除
                # this is pretty specific to nDisplay. It will remove all existing nDisplay devices before the devices of a new nDisplay config are added.
                # this offers a simple way to update nDisplay should the config file have been changed.
                self.device_manager.remove_device(device)
            #将设备添加（日志.设备添加）
            self.device_manager.add_devices({device_type : dialog.devices_to_add()})
            CONFIG.save()                                                       #保存

    #启用设备移除
    def on_device_removed(self, device_hash, device_type, device_name, update_config):
        #首先从设备列表中删除
        self.device_list_widget.on_device_removed(device_hash, device_type, device_name, update_config)
        #从配置中删除
        CONFIG.on_device_removed(device_hash, device_type, device_name, update_config)

    #事件筛选器
    def eventFilter(self, obj, event):
        #如果 是窗口 或者 事件类别为Qt的关闭
        if obj == self.window and event.type() == QtCore.QEvent.Close:
            #执行关闭
            self.on_exit()  
        #否则就返回 窗口事件
        return self.window.eventFilter(obj, event)

    # 退出
    def on_exit(self):
        #osc服务关闭
        self.osc_server.close()
        #遍历设备管理器
        for device in self.device_manager.devices():
            #设备 断连所有监听
            device.disconnect_listener()
        #这里就相当于关闭窗口
        self.window.removeEventFilter(self)

    def transport_queue_menu_about_to_show(self):
        self.transport_queue_menu.clear()

        action = QtWidgets.QWidgetAction(self.transport_queue_menu)
        action.setDefaultWidget(TransportQueueHeaderActionWidget())
        self.transport_queue_menu.addAction(action)

        for job_name in self.transport_queue.transport_jobs.keys():
            action = QtWidgets.QWidgetAction(self.transport_queue_menu)
            action.setDefaultWidget(TransportQueueActionWidget(job_name))
            self.transport_queue_menu.addAction(action)

    #更新配置菜单 1.先清空载入配置 2.匹配配置菜单
    def update_configs_menu(self):
        from functools import partial
        
        self.window.menu_load_config.clear()

        for c in config.list_config_files():
            config_name = c.replace('.json', '')
            config_action = self.window.menu_load_config.addAction(config_name, partial(self.set_current_config, c))
            #但是当 是设置配置时，操作就不启用
            if c == SETTINGS.CONFIG:
                config_action.setEnabled(False)

    #设置当前配置 1.先保存设置  2.更新新的配置 3.当载入时禁用保存 4.移除所有设备/插件设置/所有配置钩子/添加设备/ 当上面完成后重新启用保存 
    def set_current_config(self, config_name):

        SETTINGS.CONFIG = config_name
        SETTINGS.save()

        # Update to the new config
        config_name = CONFIG.config_file_name_to_name(SETTINGS.CONFIG)
        CONFIG.init_with_file_name(CONFIG.name_to_config_file_name(config_name))

        # Disable saving while loading
        CONFIG.push_saving_allowed(False)

        try:
            # Remove all devices
            self.device_manager.clear_device_list()
            self.device_list_widget.clear_widgets()

            # Reset plugin settings
            self.device_manager.reset_plugins_settings(CONFIG)

            # Set hooks to this dialog's UI  挂起UI
            self.set_config_hooks()

            # Add new devices               添加新的设备
            self.device_manager.add_devices(CONFIG._device_data_from_config)
        finally:
            # Re-enable saving after loading.
            CONFIG.pop_saving_allowed()

        self.p4_refresh_project_cl()
        self.p4_refresh_engine_cl()
        self.refresh_levels()
        self.update_configs_menu()

    # 菜单 新的 配置
    def menu_new_config(self):
        #项目搜索路径 = 系统路径（配置中.项目路径）
        uproject_search_path = os.path.dirname(CONFIG.UPROJECT_PATH.get_value().replace('"',''))
        #假如路径不存在
        if not os.path.exists(uproject_search_path):
            #项目搜索路径 = 设置的最后保存路径
            uproject_search_path = SETTINGS.LAST_BROWSED_PATH
        #日志 = 添加配置日志（样式，项目搜索路径，预览引擎目录 = 配置中获取值，父类是自己的窗口） 代码执行
        dialog = AddConfigDialog(self.stylesheet, uproject_search_path=uproject_search_path, previous_engine_dir=CONFIG.ENGINE_DIR.get_value(), parent=self.window)
        dialog.exec() #弹出日志
        #输入确认时
        if dialog.result() == QtWidgets.QDialog.Accepted:
            #初始化新的配置
            CONFIG.init_new_config(project_name=dialog.config_name, uproject=dialog.uproject, engine_dir=dialog.engine_dir, p4_settings=dialog.p4_settings())

            # 当载入时禁用保存
            # Disable saving while loading
            CONFIG.push_saving_allowed(False)
            try:
                # Remove all devices    移除所有设备
                self.device_manager.clear_device_list() 
                self.device_list_widget.clear_widgets()

                # Reset plugin settings 重置插件设置
                self.device_manager.reset_plugins_settings(CONFIG)

                # Set hooks to this dialog's UI     挂起UI
                self.set_config_hooks()
            finally:
                # Re-enable saving after loading    载入后重新启用保存
                CONFIG.pop_saving_allowed()

            # Update the UI 启用P4控制 刷新关卡 更新配置菜单
            self.toggle_p4_controls(CONFIG.P4_ENABLED.get_value())
            self.refresh_levels()
            self.update_configs_menu()

    #删除配置的操作
    def menu_delete_config(self):
        """
        Delete the current loaded config
        After deleting, it will load the first config found by config.list_config_files()
        Or it will create a new config
        """
        #回复 = qt的消息盒子（是不是删除配置？）
        reply = QtWidgets.QMessageBox.question(self.window, 'Delete Config',
                        f'Are you sure you would like to delete config "{SETTINGS.CONFIG}"?',
                        QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No)
        # 回复的返回值 为Yes
        if reply == QtWidgets.QMessageBox.Yes:
            # 拿取路径值
            file_to_delete = os.path.normpath(os.path.join(config.CONFIG_DIR, SETTINGS.CONFIG))
            # 移除老的配置
            # Remove the old config
            try:
                os.remove(file_to_delete)   #移除配置
            except FileNotFoundError as e:
                LOGGER.error(f'menu_delete_config: {e}')

            # Grab a new config to lead once this one is delted
            # 在这个配置被删除后，获取一个新的配置来引导它
            config_files = config.list_config_files()

            if config_files:
                self.set_current_config(config_files[0])
            else:
                # Create a blank config
                self.menu_new_config()

            # Update the config menu更新配置菜单
            self.update_configs_menu()

    # 菜单更新设置
    def menu_update_settings(self):
        """
        Settings window 设置窗口 
        """
        # TODO: VALIDATE RECORD PATH
        settings_dialog = SettingsDialog()                                                                      #启用设置菜单

        config_name = CONFIG.config_file_name_to_name(SETTINGS.CONFIG)                                          #配置名
        settings_dialog.set_config_name(config_name)                                                            #设置配置名
        settings_dialog.set_ip_address(SETTINGS.IP_ADDRESS)                                                     #设置IP地址
        settings_dialog.set_transport_path(SETTINGS.TRANSPORT_PATH)                                             #转移路径
        settings_dialog.set_listener_exe(CONFIG.LISTENER_EXE)                                                   #监听程序
        settings_dialog.set_project_name(CONFIG.PROJECT_NAME)                                                   #项目名
        settings_dialog.set_uproject(CONFIG.UPROJECT_PATH.get_value())                                          #项目路径
        settings_dialog.set_engine_dir(CONFIG.ENGINE_DIR.get_value())                                           #引擎路径
        settings_dialog.set_build_engine(CONFIG.BUILD_ENGINE.get_value())                                       #构建引擎
        settings_dialog.set_p4_enabled(bool(CONFIG.P4_ENABLED.get_value()))                                     #p4启用
        settings_dialog.set_source_control_workspace(CONFIG.SOURCE_CONTROL_WORKSPACE.get_value())               #源控制
        settings_dialog.set_p4_project_path(CONFIG.P4_PROJECT_PATH.get_value())                                 #p4项目路径
        settings_dialog.set_p4_engine_path(CONFIG.P4_ENGINE_PATH.get_value())                                   #p4引擎路径
        settings_dialog.set_map_path(CONFIG.MAPS_PATH.get_value())                                              #地图路径
        settings_dialog.set_map_filter(CONFIG.MAPS_FILTER.get_value())                                          #地图筛选器
        settings_dialog.set_osc_server_port(CONFIG.OSC_SERVER_PORT.get_value())                                 #osc服务端口
        settings_dialog.set_osc_client_port(CONFIG.OSC_CLIENT_PORT.get_value())                                 #osc监听接口
        settings_dialog.set_mu_server_name(CONFIG.MUSERVER_SERVER_NAME)                                         #多用户服务名
        settings_dialog.set_mu_cmd_line_args(CONFIG.MUSERVER_COMMAND_LINE_ARGUMENTS)                            #多用户命令行
        settings_dialog.set_mu_clean_history(CONFIG.MUSERVER_CLEAN_HISTORY)                                     #多用户清理历史
        settings_dialog.set_mu_auto_launch(CONFIG.MUSERVER_AUTO_LAUNCH)                                         #多用户自动启动
        settings_dialog.set_mu_auto_join(CONFIG.MUSERVER_AUTO_JOIN)                                             #多用户自动加入
        settings_dialog.set_mu_server_exe(CONFIG.MULTIUSER_SERVER_EXE)                                          #多用户服务应用
        settings_dialog.set_mu_server_auto_build(CONFIG.MUSERVER_AUTO_BUILD)                                    #多用户自动构建
        #settings_dialog.set_

        #获取插件名，并且排序插件
        for plugin_name in sorted(self.device_manager.available_device_plugins(), key=str.lower):
            #返回设备实例
            device_instances = self.device_manager.devices_of_type(plugin_name)
            #设备设置 将设备的这些属性遍历出来
            device_settings = [(device.name, device.device_settings(), device.setting_overrides()) for device in device_instances]
            settings_dialog.add_section_for_plugin(plugin_name, self.device_manager.plugin_settings(plugin_name), device_settings)


        # avoid saving the config all the time while in the settings dialog
        # 避免进入设置对话框的同时 保存配置
        CONFIG.push_saving_allowed(False)
        try:
            # Show the Settings Dialog 显示设置的日志
            settings_dialog.ui.exec()
        finally:
            # 恢复可以保存
            # Restore saving, which should happen at the end of this function
            CONFIG.pop_saving_allowed()

        # 新的配置名 设置日志:配置名
        new_config_name = settings_dialog.config_name()
        # 比如打开之后 我们将这个名字改了
        if config_name != new_config_name:
            #将配置中的设置为最新的
            new_config_name = CONFIG.name_to_config_file_name(new_config_name)
            #将设置中的配置 给予新的配置 （存的就是一个路径）
            SETTINGS.CONFIG = new_config_name
            #配置保存
            SETTINGS.save()
            #需要将 配置 重命名 
            CONFIG.rename(new_config_name)
            self.update_configs_menu()

        #IP地址 = 先从设置对话框中读一遍
        ip_address = settings_dialog.ip_address()
        # 如果 ip地址 不等于 设置中存的IP地址  就把地址给新的并且重新赋值
        if ip_address != SETTINGS.IP_ADDRESS:
            SETTINGS.IP_ADDRESS = ip_address
            SETTINGS.save()

            # Relaunch the OSC server  重新启动OSC服务 ，先关后 再启动
            self.osc_server.close()
            self.osc_server.launch(SETTINGS.IP_ADDRESS, CONFIG.OSC_SERVER_PORT.get_value())

        #转移路径 读取对话框中的设置配置 不同的话重新给值
        transport_path = settings_dialog.transport_path()
        if transport_path != SETTINGS.TRANSPORT_PATH:
            SETTINGS.TRANSPORT_PATH = transport_path
            SETTINGS.save()

        # todo-dara, when these project settings have been converted into actual Settings
        # these assignments are not needed anymore, as the settings would be directly connected to their widgets
        
        #刷新项目名
        project_name = settings_dialog.project_name()
        if project_name != CONFIG.PROJECT_NAME:
            CONFIG.PROJECT_NAME = project_name

        #刷新监听器名
        listener_exe = settings_dialog.listener_exe()
        if listener_exe != CONFIG.LISTENER_EXE:
            CONFIG.LISTENER_EXE = listener_exe

        #刷新多用户配置 ，包括 多用户名/命令行数组/清除历史/自动启动/自动加入/服务器程序/自动构建等等
        # Multi User Settings
        mu_server_name = settings_dialog.mu_server_name()
        if mu_server_name != CONFIG.MUSERVER_SERVER_NAME:
            CONFIG.MUSERVER_SERVER_NAME = mu_server_name

        mu_cmd_line_args = settings_dialog.mu_cmd_line_args()
        if mu_cmd_line_args != CONFIG.MUSERVER_COMMAND_LINE_ARGUMENTS:
            CONFIG.MUSERVER_COMMAND_LINE_ARGUMENTS = mu_cmd_line_args

        mu_clean_history = settings_dialog.mu_clean_history()
        if mu_clean_history != CONFIG.MUSERVER_CLEAN_HISTORY:
            CONFIG.MUSERVER_CLEAN_HISTORY = mu_clean_history

        mu_auto_launch = settings_dialog.mu_auto_launch()
        if mu_auto_launch != CONFIG.MUSERVER_AUTO_LAUNCH:
            CONFIG.MUSERVER_AUTO_LAUNCH = mu_auto_launch

        mu_auto_join = settings_dialog.mu_auto_join()
        if mu_auto_join != CONFIG.MUSERVER_AUTO_JOIN:
            CONFIG.MUSERVER_AUTO_JOIN = mu_auto_join

        mu_server_exe = settings_dialog.mu_server_exe()
        if mu_server_exe != CONFIG.MULTIUSER_SERVER_EXE:
            CONFIG.MULTIUSER_SERVER_EXE = mu_server_exe

        mu_auto_build = settings_dialog.mu_server_auto_build()
        if mu_auto_build != CONFIG.MUSERVER_AUTO_BUILD:
            CONFIG.MUSERVER_AUTO_BUILD = mu_auto_build
        #配置更新 P4是否启用
        CONFIG.P4_ENABLED.update_value(settings_dialog.p4_enabled())
        #保存配置
        CONFIG.save()
    # 同步所有 按键按下
    def sync_all_button_clicked(self):
        if not CONFIG.P4_ENABLED.get_value():
            return
        device_widgets = self.device_list_widget.device_widgets()
        #同步设备 中能同步的部分
        for device_widget in device_widgets:
            if device_widget.can_sync():
                #设备部件.ton
                device_widget.sync_button_clicked()
    # 构建所有 按键点击
    def build_all_button_clicked(self):
        device_widgets = self.device_list_widget.device_widgets()

        for device_widget in device_widgets:
            if device_widget.can_build():
                device_widget.build_button_clicked()
    #同步/构建 所有
    def sync_and_build_all_button_clicked(self):
        if not CONFIG.P4_ENABLED.get_value():
            return
        device_widgets = self.device_list_widget.device_widgets()

        for device_widget in device_widgets:
            if device_widget.can_sync() and device_widget.can_build():
                device_widget.sync_button_clicked()
                device_widget.build_button_clicked()

    #刷新项目变更 其实就是通过P4来实现
    def refresh_project_cl_button_clicked(self):
        self.p4_refresh_project_cl()
    #刷新引擎变更 其实就是通过P4来实现
    def refresh_engine_cl_button_clicked(self):
        self.p4_refresh_engine_cl()

    # 链接所有 （通过按键控制）
    def connect_all_button_clicked(self, button_state):
        devices = self.device_manager.devices()
        self.set_device_connection_state(devices, button_state)
    # 启动所有（通过按键控制）
    def launch_all_button_clicked(self, button_state):
        devices = self.device_manager.devices()
        self.set_device_launch_state(devices, button_state)
    # 设置设备的连接状态
    def set_device_launch_state(self, devices, launch_state):
        for device in devices:
            try:
                #如果设备状态 并且 设备部件打开按键已经启用 
                if launch_state and device.widget.open_button.isEnabled():
                    device.widget._open()
                # 如果不是在启动状态 并且已经挂起了 那就
                elif not launch_state and device.widget.open_button.isChecked():
                    #设备 部件关闭
                    device.widget._close()
            except:
                pass
    # 设置设备链接状态
    def set_device_connection_state(self, devices, connection_state):
        for device in devices:
            try:
                if connection_state:
                    device.widget._connect()
                else:
                    device.widget._disconnect()
            except:
                pass

    #信号槽
    @QtCore.Slot(object)
    def recording_manager_saved(self, recording):
        """
        When the RecordingManager saves a recording
        """
        pass

    # START HERE  这儿开始
    # TODO 开干
    # If JOB IS ADDED, RESUME 如果工作已经条件 就恢复
    # If DEVICE CONNECTS, RESUME
    #转移列队 恢复
    def transport_queue_resume(self):
        # Do not allow transport while recording
        if self._is_recording:
            return

        # Do not transport if the active queue is full #如果传输列队满了就不传了
        if self.transport_queue.active_queue_full():
            return

        for _, transport_job in self.transport_queue.transport_jobs.items():
            # Do not transport if the device is disconnected
            # 如果设备断连了也不要传
            device = self.device_manager.device_with_name(transport_job.device_name)
            if device.status < DeviceStatus.OPEN:
                continue

            # Only Transport jobs that are ready 只有当传输状态好了才传输
            if transport_job.transport_status != recording.TransportStatus.READY_FOR_TRANSPORT:
                continue

            # Transport the file 转移文件
            self.transport_queue.run_transport_job(transport_job, device)

            # Bail if active queue is full 如果活动队列已满，则回滚
            if self.transport_queue.active_queue_full():
                break
    
    #传输列队完成 就输出日志
    @QtCore.Slot(object)
    def transport_queue_job_finished(self, transport_job):
        """
        When the TransportQueue finished a job
        """
        LOGGER.debug(f'transport_queue_job_finished {transport_job.job_name}')
        '''
        # If the device is connected, set that status as READY_FOR_TRANSPORT
        transport_job.transport_status = recording.TransportStatus.READY_FOR_TRANSPORT
        #transport_queue_job_added
        '''

    #传输列队工作开始
    @QtCore.Slot(object)
    def transport_queue_job_started(self, transport_job):
        """
        When the TransportQueue is ready to transport a new job
        Grab the device and send it back to the transport queue
        """
        LOGGER.debug(f'transport_queue_job_started')
    #设备添加的信号槽
    @QtCore.Slot(object)
    def device_added(self, device):
        """
        When a new device is added to the DeviceManger, connect its signals
        当一个新的设备添加到设备管理器，链接他的信号
        """
        device.device_qt_handler.signal_device_connect_failed.connect(self.device_connect_failed, QtCore.Qt.QueuedConnection)
        device.device_qt_handler.signal_device_client_disconnected.connect(self.device_client_disconnected, QtCore.Qt.QueuedConnection)
        device.device_qt_handler.signal_device_project_changelist_changed.connect(self.device_project_changelist_changed, QtCore.Qt.QueuedConnection)
        device.device_qt_handler.signal_device_engine_changelist_changed.connect(self.device_engine_changelist_changed, QtCore.Qt.QueuedConnection)
        device.device_qt_handler.signal_device_status_changed.connect(self.device_status_changed, QtCore.Qt.QueuedConnection)
        device.device_qt_handler.signal_device_sync_failed.connect(self.device_sync_failed, QtCore.Qt.QueuedConnection)
        device.device_qt_handler.signal_device_is_recording_device_changed.connect(self.device_is_recording_device_changed, QtCore.Qt.QueuedConnection)
        device.device_qt_handler.signal_device_build_update.connect(self.device_build_update, QtCore.Qt.QueuedConnection)
        device.device_qt_handler.signal_device_sync_update.connect(self.device_sync_update, QtCore.Qt.QueuedConnection)

        # Add the view
        self.device_list_widget.add_device_widget(device)
    #注册设备的信号槽
    @QtCore.Slot(object)
    def register_device_widget(self, device_widget):
        """
        When a new DeviceWidget is added, connect all the signals
        """
        device_widget.signal_device_widget_connect.connect(self.device_widget_connect)
        device_widget.signal_device_widget_disconnect.connect(self.device_widget_disconnect)
        device_widget.signal_device_widget_open.connect(self.device_widget_open)
        device_widget.signal_device_widget_close.connect(self.device_widget_close)
        device_widget.signal_device_widget_sync.connect(self.device_widget_sync)
        device_widget.signal_device_widget_build.connect(self.device_widget_build)
        device_widget.signal_device_widget_trigger_start_toggled.connect(self.device_widget_trigger_start_toggled)
        device_widget.signal_device_widget_trigger_stop_toggled.connect(self.device_widget_trigger_stop_toggled)

        # KiPro Signal Support  kiPro提供另外两个参数
        try:
            device_widget.signal_device_widget_play.connect(self.device_widget_play)
            device_widget.signal_device_widget_stop.connect(self.device_widget_stop)
        except:
            pass
    
    #所有插件设备连接
    def on_all_plugin_devices_connect_toggled(self, plugin_name, button_state):
        devices = self.device_manager.devices_of_type(plugin_name)
        self.set_device_connection_state(devices, button_state)
    #所有插件设备打开
    def on_all_plugin_devices_open_toggled(self, plugin_name, button_state):
        devices = self.device_manager.devices_of_type(plugin_name)
        self.set_device_launch_state(devices, button_state)
    #多用户会话名
    def multiuser_session_name(self):
        return self._multiuser_session_name
    #设置多会话名
    def set_multiuser_session_name(self, value):
        self._multiuser_session_name = value
        #外部值不一样时
        if self.window.multiuser_session_lineEdit.text() != value:
            self.window.multiuser_session_lineEdit.setText(value)
        #于设置里值不一样时
        if value !=SETTINGS.MUSERVER_SESSION_NAME:
            SETTINGS.MUSERVER_SESSION_NAME = value
            SETTINGS.save() #保存

    @property   #这个可以直接通过名字访问
    def shoot(self):
        return self._shoot

    @shoot.setter   #对上面的数据进行处理
    def shoot(self, value):
        self._shoot = value

    @property   #这里打个比方：就是调用sequnce就会调用下面的参数
    def sequence(self):
        return self._sequence

    @sequence.setter  
    def sequence(self, value):
        self._set_sequence(value)

    def _set_sequence(self, value):
        self._sequence = value
        self.window.sequence_line_edit.setText(value)

        # Reset the take number to 1 if setting the sequence
        self.take = 1

    #访问slate
    @property
    def slate(self):
        return self._slate

    @slate.setter
    def slate(self, value):
        self._set_slate(value, reset_take=False)

    
    def _set_slate(self, value, exclude_ip_addresses=[], reset_take=True):
        """
        Internal setter that allows exclusion of ip addresses
        内联的setter 允许暴露IP地址
        """
        # Protect against blank slates
        if value == '':
            return
        #值没变化就直接返回
        if self._slate == value:
            return
        #赋予新值
        self._slate = value
        SETTINGS.CURRENT_SLATE = value
        SETTINGS.save()

        # Reset the take number to 1 if setting the slate 重置slate到1
        if reset_take:
            self.take = 1

        # UI out of date with control means external message 让UI上同步显示
        if self.window.slate_line_edit.text() != self._slate:
            self.window.slate_line_edit.setText(self._slate)
        #创建一个线程 去干这个事
        thread = threading.Thread(target=self._set_slate_all_devices, args=[value], kwargs={'exclude_ip_addresses':exclude_ip_addresses})
        thread.start()

    def _set_slate_all_devices(self, value, exclude_ip_addresses=[]):
        """
        Tell all devices the new slate 告诉所有设备新的slate（计划）
        """
        for device in self.device_manager.devices(): #过滤排除ip
            if device.ip_address in exclude_ip_addresses:
                continue

            # Do not send updates to disconnected devices 不要提交断连设备
            if device.status == DeviceStatus.DISCONNECTED:
                continue

            device.set_slate(self._slate)

    # 镜头
    @property
    def take(self):
        return self._take

    @take.setter
    def take(self, value):
        self._set_take(value)

    #设置take
    def _set_take(self, value, exclude_ip_addresses=[]):
        """
        Internal setter that allows exclusion of ip addresses
        """
        requested_take = value

        # TODO: Add feedback in UI
        # Check is that slate/take combo has been used before
        # 当记录管理器
        while not self.recording_manager.slate_take_available(self._sequence, self._slate, requested_take):
            requested_take += 1
        # 请求_镜头  假如没变化就返回
        if requested_take == value == self._take:
            return
        # 请求的take不一样 
        if requested_take != value:
            LOGGER.warning(f'Slate: "{self._slate}" Take: "{value}" have already been used. Auto incremented up to take: "{requested_take}"')
            # Clear the exclude list since Switchboard changed the incoming value
            exclude_ip_addresses = []
        
        #保存当前take的值
        self._take = requested_take
        SETTINGS.CURRENT_TAKE = value
        SETTINGS.save()
        # 如果 UI上的值不等于当前的值才推出
        if self.window.take_spin_box.value() != self._take:
            self.window.take_spin_box.setValue(self._take)
        #创建线程
        thread = threading.Thread(target=self._set_take_all_devices, args=[value], kwargs={'exclude_ip_addresses':exclude_ip_addresses})
        thread.start()
    # 和上面的slate类似
    def _set_take_all_devices(self, value, exclude_ip_addresses=[]):
        """
        Tell all devices the new take
        """
        # Tell all devices the new take
        for device in self.device_manager.devices():
            # Do not send updates to disconnected devices
            if device.status == DeviceStatus.DISCONNECTED:
                continue

            if device.ip_address in exclude_ip_addresses:
                continue

            device.set_take(self._take)
   
    #把“描述”当作参数
    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = f'{self.level} {self.slate} {self.take}\nvalue'

    # 把关卡当作参数
    @property
    def level(self):
        return self._level
    
    @level.setter
    def level(self, value):
        self._set_level(value)

    def _set_level(self, value):
        ''' Called when level dropdown text changes
        '''
        self._level = value
        #配置中的关卡 与本地关卡对比
        if CONFIG.CURRENT_LEVEL != value:
            #覆盖 之前的关卡值
            CONFIG.CURRENT_LEVEL = value
            CONFIG.save()
        #修正UI的值
        if self.window.level_combo_box.currentText() != self._level:
            self.window.level_combo_box.setCurrentText(self._level)

    #把项目更改列表
    @property
    def project_changelist(self):
        return self._project_changelist

    @project_changelist.setter
    def project_changelist(self, value):
        self._set_project_changelist(value)

    def _set_project_changelist(self, value):
        self._project_changelist = value
        #如果项目更改列表 ！= 之前的项目更改列表
        if self.window.project_cl_combo_box.currentText() != self._project_changelist:
            #设置 项目更改列表的合并盒子的文本
            self.window.project_cl_combo_box.setText(self._project_changelist)

        # Check if all of the devices are on the right changelist
        # 检查 所有设备是否都在对的更改列表上 
        for device in self.device_manager.devices():
            if not device.project_changelist:
                continue
            #设备部件 = 从设备列表部件上的设备部件（根据hash值检索）
            device_widget = self.device_list_widget.device_widget_by_hash(device.device_hash)
            #值 为空
            if value == EMPTY_SYNC_ENTRY:
                device_widget.project_changelist_display_warning(False)  #不弹
            else:
                if device.project_changelist == self.project_changelist:
                    device_widget.project_changelist_display_warning(False) #不弹
                else:
                    device_widget.project_changelist_display_warning(True) #弹

    # 引擎的更改列表
    @property
    def engine_changelist(self):
        return self._engine_changelist

    @engine_changelist.setter
    def engine_changelist(self, value):
        self._set_engine_changelist(value)

    def _set_engine_changelist(self, value):
        self._engine_changelist = value
        #校验本地的值
        if self.window.engine_cl_combo_box.currentText() != self._engine_changelist:
            self.window.engine_cl_combo_box.setText(self._engine_changelist)

        # Check if all of the devices are on the right changelist
        #  检查 所有设备是否都在对的更改列表上 
        for device in self.device_manager.devices():
            if not device.engine_changelist:
                continue

            device_widget = self.device_list_widget.device_widget_by_hash(device.device_hash)
            if value == EMPTY_SYNC_ENTRY:
                device_widget.engine_changelist_display_warning(False)  #不警告
            else:
                if device.engine_changelist == self.engine_changelist:
                    device_widget.engine_changelist_display_warning(False) #不警告
                else:
                    device_widget.engine_changelist_display_warning(True) #警告

    # 信号槽：设备部件链接
    @QtCore.Slot(object)
    def device_widget_connect(self, device_widget):
        device = self.device_manager.device_with_hash(device_widget.device_hash)
        if not device:
            return
        # livelinkFace 另算
        if device.device_type == 'LiveLinkFace':
            device.look_for_device = True  #将查找设备设置为“真”
        else:
            #链接到监听器
            device.connect_listener()

    # 信号槽：设备连接失败
    @QtCore.Slot(object)
    def device_connect_failed(self, device):
        #拿到设备部件 这个根据不同的设备拥有不同的函数实际调用。所以当然得这样用
        device_widget = self.device_list_widget.device_widget_by_hash(device.device_hash)

        if not device_widget:
            return
        #设备部件的断连
        device_widget._disconnect()
        #日志输出（提示失败）
        LOGGER.warning(f'{device.name}: Could not connect to device')

    # 信号槽：设备断连的实现
    @QtCore.Slot(object)
    def device_widget_disconnect(self, device_widget):
        device = self.device_manager.device_with_hash(device_widget.device_hash)
        if not device:
            return

        if device.device_type == 'LiveLinkFace':
            device.look_for_device = False #将查找设备设置为“假”
        else:
            #设备 断开监听器
            device.disconnect_listener()


    #信号槽：设备 客户端 断连
    @QtCore.Slot(object)
    def device_client_disconnected(self, device):
        device_widget = self.device_list_widget.device_widget_by_hash(device.device_hash)
        #设备部件 -断开链接
        device_widget._disconnect()
        LOGGER.warning(f'{device.name}: Client disconnected')

    #信号槽：设备部件打开
    @QtCore.Slot(object)
    def device_widget_open(self, device_widget):
        device = self.device_manager.device_with_hash(device_widget.device_hash)
        #设备启动（输入的是关卡值）
        device.launch(self.level)

    @QtCore.Slot(object)
    def device_widget_close(self, device_widget):
        device = self.device_manager.device_with_hash(device_widget.device_hash)
        device.close(force=True)

    #信号槽：设备部件同步
    @QtCore.Slot(object)
    def device_widget_sync(self, device_widget):
        #假如P4不存在 就直接退出
        if not CONFIG.P4_ENABLED.get_value():
            return
        device = self.device_manager.device_with_hash(device_widget.device_hash)
        project_cl = None if self.project_changelist == EMPTY_SYNC_ENTRY else self.project_changelist
        engine_cl = None if self.engine_changelist == EMPTY_SYNC_ENTRY else self.engine_changelist
        #设备同步（引擎和项目）
        device.sync(engine_cl, project_cl)

    # 信号槽：设备部件的构建
    @QtCore.Slot(object)
    def device_widget_build(self, device_widget):
        device = self.device_manager.device_with_hash(device_widget.device_hash)
        device.build()  #设备构建
    # 信号槽：设备部件的启动
    @QtCore.Slot(object)
    def device_widget_play(self, device_widget):
        device = self.device_manager.device_with_hash(device_widget.device_hash)
        device.play()   #设备运行
    # 信号槽：设备部件的停止
    @QtCore.Slot(object)
    def device_widget_stop(self, device_widget):
        device = self.device_manager.device_with_hash(device_widget.device_hash)
        device.stop()   #设备停止
    # 信号槽：设备同步失败
    @QtCore.Slot(object)
    def device_sync_failed(self, device):
        #LOGGER.debug(f'{device.name} device_sync_failed')
        # CHANGE THE SYNC ICON HERE
        pass
    # 信号槽：设备构建更新
    @QtCore.Slot(object)
    def device_build_update(self, device, step, percent):
        device_widget = self.device_list_widget.device_widget_by_hash(device.device_hash)
        device_widget.update_build_status(device, step, percent) #设备部件：更新构建状态

    # 信号槽：设备同步更新
    @QtCore.Slot(object)
    def device_sync_update(self, device, progress):
        device_widget = self.device_list_widget.device_widget_by_hash(device.device_hash)
        device_widget.update_sync_status(device, progress) #设备部件：更新同步状态

    # 信号槽：设备项目更改列表 更改
    @QtCore.Slot(object)
    def device_project_changelist_changed(self, device):
        device_widget = self.device_list_widget.device_widget_by_hash(device.device_hash)
        device_widget.update_project_changelist(device.project_changelist)  #更新项目更改列表

        if self.project_changelist == EMPTY_SYNC_ENTRY: #为空
            device_widget.project_changelist_display_warning(False) #不警告
        else:
            if device.project_changelist == self.project_changelist:
                device_widget.project_changelist_display_warning(False) #不警告
            else:
                device_widget.project_changelist_display_warning(True)  #警告

    # 信号槽：设备引擎更改列表
    @QtCore.Slot(object)
    def device_engine_changelist_changed(self, device):
        device_widget = self.device_list_widget.device_widget_by_hash(device.device_hash)
        device_widget.update_engine_changelist(device.engine_changelist)

        if self.engine_changelist == EMPTY_SYNC_ENTRY:
            device_widget.engine_changelist_display_warning(False)
        else:
            if device.engine_changelist == self.engine_changelist:
                device_widget.engine_changelist_display_warning(False)
            else:
                device_widget.engine_changelist_display_warning(True)
    
    # 信号槽：设备状态更改
    @QtCore.Slot(object)
    def device_status_changed(self, device, previous_status):

        # Update the device widget
        # 更新 设备部件
        device.widget.update_status(device.status, previous_status)

        devices = self.device_manager.devices_of_type(device.device_type)
        #更新类别状态
        self.device_list_widget.update_category_status(device.category_name, devices)
        #更新连接 并且 打开按键状态
        self.update_connect_and_open_button_states()

        # 如果预览到的状态 不等于 设备状态时
        if previous_status != device.status:
            LOGGER.debug(f'{device.name}: device status change: {device.status.name}')
        # 如果预览到的状态 等于 设备状态.记录中 并且 设备状态 大于等于 设备状态打开
        if previous_status == DeviceStatus.RECORDING and device.status >= DeviceStatus.OPEN:
            self.device_record_stop_confirm(device) #停止
        # 如果预览到的状态 等于 设备状态.准备好了 并且 设备状态 大于等于 设备状态.记录中
        elif previous_status == DeviceStatus.READY and device.status >= DeviceStatus.RECORDING:
            self.device_record_start_confirm(device)    #启动

        # Send Slate/Take to the device when it connects
        # 发送 Slate/Take 到 设备 当连接的时候
        if previous_status <= DeviceStatus.OPEN and device.status >= DeviceStatus.READY:
            device.set_take(self.take)
            device.set_slate(self.slate)

    #更新 连接 并且 打开 按键状态
    def update_connect_and_open_button_states(self):
        """ Refresh states of connect-all and start-all buttons. """
        # 刷新状态 （所有连接 和 启动按键）
        devices = self.device_manager.devices()
        # 任意连接
        any_connected = any(device.status != DeviceStatus.DISCONNECTED for device in devices)
        # 任意启动
        any_started = any(device.status > DeviceStatus.CLOSED for device in devices)
        # 更新.连接所有按键
        self.update_connect_all_button_state(any_connected)
        # 更新.启动所有按键
        self.update_start_all_button_state(any_connected, any_started)

    #更新.连接所有按键状态
    def update_connect_all_button_state(self, any_devices_connected):
        """ Refresh state of connect-all button. """
        # 刷新连接所有状态 按键
        self.window.connect_all_button.setChecked(any_devices_connected)
        # 根据两种状态 设置两种提示
        if any_devices_connected:
            self.window.connect_all_button.setToolTip("Disconnect all connected devices")
        else:
            self.window.connect_all_button.setToolTip("Connect all devices")
    #更新.启动所有按键的状态
    def update_start_all_button_state(self, any_devices_connected, any_devices_started):
        """ Refresh state of start-all button. """
        # 刷新 启动所有按键的状态
        self.window.launch_all_button.setEnabled(any_devices_connected)
        self.window.launch_all_button.setChecked(any_devices_started)
        # 更改提示字符
        if any_devices_started:
            self.window.launch_all_button.setToolTip("Stop all running devices")
        else:
            self.window.launch_all_button.setToolTip("Start all connected devices")


    # 信号槽：设备是否记录设备更改
    @QtCore.Slot(object)
    def device_is_recording_device_changed(self, device, is_recording_device):
        """
        When the is_recording_device bool changes, fresh the device status to force the repositioning
        of the device in the UI
        当 是否记录设备 bool值更改，刷新设备状态强制重新定位
        """
        # 设备状态改为启用
        self.device_status_changed(device, DeviceStatus.OPEN)
    # 设备记录启动确认
    def device_record_start_confirm(self, device):
        """
        Callback when the device has started recording
        """
        LOGGER.info(f'{device.name}: Recording started') # {timecode}
    # 设备记录停止确认
    def device_record_stop_confirm(self, device):
        """
        Callback when the device has stopped recording
        """
        LOGGER.info(f'{device.name}: Recording stopped')
        #上次记录 = 记录管理.上次管理值
        latest_recording = self.recording_manager.latest_recording
        #设备记录 = 设备获取设备记录
        device_recording = device.get_device_recording()

        # Add the device to the latest recording 添加最后一次记录到设备
        self.recording_manager.add_device_to_recording(device_recording, latest_recording)
        '''
        # TransportJob
        # If the device produces transport paths, create a transport job
        paths = device.transport_paths(device_recording)
        if not paths:
            return

        # If the status is not on device, do not create jobs
        if device_recording.status != recording.RecordingStatus.ON_DEVICE:
            return

        device_name = device_recording.device_name
        slate = latest_recording.slate
        take = latest_recording.take
        date = latest_recording.date
        job_name = self.transport_queue.job_name(slate, take, device_name)

        # Create a transport job
        transport_job = recording.TransportJob(job_name, device_name, slate, take, date, paths)
        self.transport_queue.add_transport_job(transport_job)
        '''

    #信号槽：设备部件触发器启动触发
    @QtCore.Slot(object)
    def device_widget_trigger_start_toggled(self, device_widget, value):
        device = self.device_manager.device_with_hash(device_widget.device_hash)
        device.trigger_start = value

    #信号槽：设备部件触发器停止触发
    @QtCore.Slot(object)
    def device_widget_trigger_stop_toggled(self, device_widget, value):
        device = self.device_manager.device_with_hash(device_widget.device_hash)
        device.trigger_stop = value
    
    # 控制台通道
    def _console_pipe(self, msg):
        """
        Pipes the emiting message from the QtHandler to the base_console widget.
        从QtHander到基础 console部件发送消息的管道
        Scrolls on each emit signal.
        逐行的滚动消息
        :param msg: This is a built in event, QT Related, not given.
        消息参数：一个事件的构建，Qt联系，没给到
        """
        #添加消息到html中
        self.window.base_console.appendHtml(msg)

        # Only moving to StartOfLine/Down or End often causes the cursor to be stuck in the middle or the end of a line
        # 只移动到startoline /Down或End通常会导致光标卡在一行的中间或末尾
        # when the lines are longer than the widget. This combination keeps the cursor at the bottom left corner in all cases.
        # 当行的长度大于小部件时。这个组合在所有情况下都保持光标在左下角。
        self.window.base_console.moveCursor(QtGui.QTextCursor.Down)
        self.window.base_console.moveCursor(QtGui.QTextCursor.StartOfLine)

    # Allow user to change logging level
    # 允许用户去更改日志的层级
    def logger_level_comboBox_currentTextChanged(self):
        value = self.window.logger_level_comboBox.currentText()

        if value == 'Message':
            LOGGER.setLevel(logging.MESSAGE_LEVEL_NUM)
        elif value == 'OSC':
            LOGGER.setLevel(logging.OSC_LEVEL_NUM)
        elif value == 'Debug':
            LOGGER.setLevel(logging.DEBUG)
        else:
            LOGGER.setLevel(logging.INFO)

    # Update UI with latest CLs
    # 更新UI 到最后的 变更列表
    def p4_refresh_project_cl(self):
        # 如果P4的配置还未启用 直接跳出
        if not CONFIG.P4_ENABLED.get_value():
            return
        # 日志信息 （刷新p4项目更改列表）
        LOGGER.info("Refreshing p4 project changelists")
        # 工作目录（项目路径）
        working_dir = os.path.dirname(CONFIG.UPROJECT_PATH.get_value())
        # 获取更改列表
        changelists = p4_utils.p4_latest_changelist(CONFIG.P4_PROJECT_PATH.get_value(), working_dir)
        # 清空项目更改列表合并盒子。清除
        self.window.project_cl_combo_box.clear()
        # 如果有值
        if changelists:
            self.window.project_cl_combo_box.addItems(changelists)      #添加元素
            self.window.project_cl_combo_box.setCurrentIndex(0)         #刷新编号
        self.window.project_cl_combo_box.addItem(EMPTY_SYNC_ENTRY)      #添加空的

    # 刷新引擎更改列表
    def p4_refresh_engine_cl(self):
        #没启用就跳过
        if not CONFIG.P4_ENABLED.get_value():
            return
        #清空盒子
        self.window.engine_cl_combo_box.clear()
        # if engine is built from source, refresh the engine cl dropdown
        # 如果引擎是构建自源码，刷新引擎更改列表下拉
        if CONFIG.BUILD_ENGINE.get_value():
            # 日志（刷新p4引擎更改列表）
            LOGGER.info("Refreshing p4 engine changelists")
            self.window.engine_cl_label.setEnabled(True)                                                #引擎更改列表标签设置启用
            self.window.engine_cl_combo_box.setEnabled(True)                                            #引擎更改列表合并盒子 设置启用
            self.window.engine_cl_combo_box.setToolTip("Select changelist to sync the engine to")       #引擎更改列表合并盒子 设置提示文字
            self.window.refresh_engine_cl_button.setEnabled(True)                                       #刷新引擎更改列表按键 设置启用
            self.window.refresh_engine_cl_button.setToolTip("Click to refresh changelists")             #刷新引擎更改列表按键 设置提示文字
            #引擎p4路径 = 配置.p4引擎路径.获取值
            engine_p4_path = CONFIG.P4_ENGINE_PATH.get_value()
            # 引擎p4路径
            if engine_p4_path:
                #工作路径
                working_dir = os.path.dirname(CONFIG.UPROJECT_PATH.get_value())
                #拿到更改列表
                changelists = p4_utils.p4_latest_changelist(engine_p4_path, working_dir)
                #更新 盒子元素，更新排序
                if changelists:
                    self.window.engine_cl_combo_box.addItems(changelists)
                    self.window.engine_cl_combo_box.setCurrentIndex(0)
            else:
                #不然输出报错日志
                LOGGER.warning('"Build Engine" is enabled in the settings but the engine does not seem to be under perforce control.')
                LOGGER.warning("Please check your perforce settings.")
        else:
            # disable engine cl controls if engine is not built from source
            # 禁用引擎更改列表 如果引擎不是构建自源码
            self.window.engine_cl_label.setEnabled(False)                                                                   #引擎更改列表标签 禁用
            self.window.engine_cl_combo_box.setEnabled(False)                                                               #引擎更改列表合并盒子 禁用
            tool_tip = "Engine is not build from source. To use this make sure the Engine is on p4 and 'Build Engine' "     #工具提示
            tool_tip += "is enabled in the Settings."
            self.window.engine_cl_combo_box.setToolTip(tool_tip)                                                            #工具提示
            self.window.refresh_engine_cl_button.setEnabled(False)                                                          #刷新引擎更改列表按键 禁用
            self.window.refresh_engine_cl_button.setToolTip(tool_tip)                                                       #刷新引擎更改列表按键 提示
        self.window.engine_cl_combo_box.addItem(EMPTY_SYNC_ENTRY)

    #刷新关卡
    def refresh_levels(self):
        #当前关卡 ：从配置中拿到的当前关卡
        current_level = CONFIG.CURRENT_LEVEL
        #关卡合并盒子清空
        self.window.level_combo_box.clear()
        #添加元素（默认地图+配置中保存的地图）
        self.window.level_combo_box.addItems([DEFAULT_MAP_TEXT] + CONFIG.maps())
        # 如果当前关卡 并且 配置中的当前关卡   都有值
        if current_level and current_level in CONFIG.maps():
            #当前关卡S
            self.level = current_level

    #触发P4控制
    def toggle_p4_controls(self, enabled):
        self.window.engine_cl_label.setEnabled(enabled)                                     #引擎更改列表标签 启用
        self.window.engine_cl_combo_box.setEnabled(enabled)                                 #引擎更改列表合并盒子 启用
        self.window.refresh_engine_cl_button.setEnabled(enabled)                            #刷新引擎更改列表按键 启用

        self.window.project_cl_label.setEnabled(enabled)                                    #项目更改列表标签 启用
        self.window.project_cl_combo_box.setEnabled(enabled)                                #项目更改列表合并盒子 启用
        self.window.refresh_project_cl_button.setEnabled(enabled)                           #刷新项目更改列表按键 启用

        self.window.sync_all_button.setEnabled(enabled)                                     #同步所有按键 启用
        self.window.sync_and_build_all_button.setEnabled(enabled)                           #同步并且构建所有按键 启用
        # 启用就 刷新P4 控制的列表
        if enabled:
            self.p4_refresh_engine_cl()
            self.p4_refresh_project_cl()
    # OSC_镜头
    def osc_take(self, ip_address, command, value):
        device = self._device_from_ip_address(ip_address, command, value=value)
        #没设备 就直接返回了
        if not device:
            return
        #有的话就设置
        self._set_take(value, exclude_ip_addresses=[device.ip_address])

    # OSC: Set Slate
    # OSC_设置计划
    def osc_slate(self, ip_address, command, value):
        device = self._device_from_ip_address(ip_address, command, value=value)
        #没设备 就直接返回了
        if not device:
            return
        #有的话就设置
        self._set_slate(value, exclude_ip_addresses=[device.ip_address], reset_take=False)

    # OSC ：设置描述 更新这个 让他工作
    # OSC: Set Description UPDATE THIS TO MAKE IT WORK
    def osc_slate_description(self, ip_address, command, value):
        self.description = value

    # 记录按键的释放
    def record_button_released(self):
        """
        User press record button
        用户按下 记录按键
        """
        # 如果正在记录
        if self._is_recording:
            LOGGER.debug('Record stop button pressed')
            self._record_stop(1)    #取消记录
        else:
            LOGGER.debug('Record start button pressed')
            # 记录开始
            self._record_start(self.slate, self.take, self.description)

    # 从ip地址获取设备
    def _device_from_ip_address(self, ip_address, command, value=''):
        device = self.device_manager.device_with_ip_address(ip_address[0])
        #如果设备不存在
        if not device:
            # 提示警告
            LOGGER.warning(f'{ip_address} is not registered with a device in Switchboard')
            return None

        # Do not recieve osc from disconnected devices
        # 不要从断连的设备获取OSC消息
        if device.status == DeviceStatus.DISCONNECTED:
            LOGGER.warning(f'{device.name}: is sending OSC commands but is not connected. Ignoring "{command} {value}"')
            return None

        LOGGER.osc(f'OSC Server: Received "{command} {value}" from {device.name} ({device.ip_address})')
        return device       #返回设备

    # OSC: Start a recording
    # OSC：开始记录
    def osc_record_start(self, ip_address, command, slate, take, description):
        '''
        OSC message Recieved /RecordStart
         OSC信息 接收/记录开始
        '''
        device = self._device_from_ip_address(ip_address, command, value=[slate, take, description])
        if not device:
            return

        # There is a bug that causes a slate of None. If this occurs, use the stored slate in control
        # 有一个错误导致了一系列没有错误的事情，如果发生这种情况，请使用控件中存储的计划
        # Try to track down this bug in sequencer
        # 尝试 去追踪这个bug在sequncer中
        if not slate or slate == 'None':
            LOGGER.critical(f'Slate is None, using {self.slate}')
        else:
            self.slate = slate #赋值 并且带操作那种
        
        self.take = take    #赋值 并且带操作那种
        self.description = description #赋值 并且带操作那种
        #记录开始 实际操作
        self._record_start(self.slate, self.take, self.description, exclude_ip_address=device.ip_address)

    # 记录开始
    def _record_start(self, slate, take, description, exclude_ip_address=None):
        LOGGER.success(f'Record Start: "{self.slate}" {self.take}')

        # Update the UI button 
        # 更新UI按键
        pixmap = QtGui.QPixmap(":/icons/images/record_start.png")
        self.window.record_button.setIcon(QtGui.QIcon(pixmap))

        # Pause the TransportQueue
        #self.transport_queue.pause()

        # Start a new recording 
        # 启用一个新的记录
        self._is_recording = True

        # TODO: Lock SLATE/TAKE/SESSION/CL

        # Return a Recording object
        # 返回一个记录对象
        new_recording = recording.Recording()                                                       #新建一个新的 对象
        new_recording.project = CONFIG.PROJECT_NAME                                                 #新的记录 项目值
        new_recording.shoot = self.shoot                                                            #新的记录 拍摄
        new_recording.sequence = self.sequence                                                      #新的记录 序列
        new_recording.slate = self.slate                                                            #新的记录 计划
        new_recording.take = self.take                                                              #新的记录 拍摄
        new_recording.description = self.description                                                #新的记录 描述
        new_recording.date = switchboard_utils.date_to_string(datetime.date.today())                #新的记录 时间
        new_recording.map = self.level                                                              #新的记录 关卡
        new_recording.multiuser_session = self.multiuser_session_name()                             #新的记录 多用户名
        new_recording.changelist = self.project_changelist                                          #新的记录 项目更改列表

        self.recording_manager.add_recording(new_recording)                                         #添加记录到 记录管理器

        # 发送 消息到 所有记录设备
        # Sends the message to all recording devices
        #从设备管理器拿到所有得设备
        devices = self.device_manager.devices()
        for device in devices:
            # Do not send a start record message to whichever device sent it
            # 有排除的设备就排除
            if exclude_ip_address and exclude_ip_address == device.ip_address:
                continue

            # Do not send updates to disconnected devices
            # 断连的设备断连
            if device.status == DeviceStatus.DISCONNECTED:
                continue

            LOGGER.debug(f'Record Start {device.name}')
            # 设备的记录开始
            device.record_start(slate, take, description)

    # 记录停止
    def _record_stop(self, exclude_ip_address=None):
        LOGGER.success(f'Record Stop: "{self.slate}" {self.take}')
        #拿到pixmap，设置记录按钮图标
        pixmap = QtGui.QPixmap(":/icons/images/record_stop.png")
        self.window.record_button.setIcon(QtGui.QIcon(pixmap))

        # Resume the transport queue
        #self.transport_queue.resume()

        # End the recording
        # 结束记录
        self._is_recording = False

        # Pull the latest recording down
        # 拉下最后的记录
        new_recording = self.recording_manager.latest_recording
        # Start the auto_save timer
        # 记录管理器 自动保存
        self.recording_manager.auto_save(new_recording)

        # TODO: If no UE4 auto incriment 

        # TODO: Unlock SLATE/TAKE/SESSION/CL

        # 设备 = 设备管理器里的所有设备
        devices = self.device_manager.devices()

        # Sends the message to all recording devices
        # 发送消息到 所有记录设备
        for device in devices:
            # Do not send a start record message to whichever device sent it
            if exclude_ip_address and exclude_ip_address == device.ip_address:
                continue

            # Do not send updates to disconnected devices
            if device.status == DeviceStatus.DISCONNECTED:
                continue

            device.record_stop() #设备记录停止

    # 记录取消：就是调用记录停止 但是为了方便拓展所以预留了接口
    def _record_cancel(self, exclude_ip_address=None):
        self._record_stop(exclude_ip_address=exclude_ip_address)

        # Incriment Take
        #new_recording = self.recording_manager.latest_recording
        #self.take = new_recording.take + 1

    # OSC记录开始确认
    def osc_record_start_confirm(self, ip_address, command, timecode):
        #拿到设备
        device = self._device_from_ip_address(ip_address, command, value=timecode)
        if not device:
            return
        #记录开始确认（时间码）
        device.record_start_confirm(timecode)

    # 记录停止
    def osc_record_stop(self, ip_address, command):
        device = self._device_from_ip_address(ip_address, command)
        if not device:
            return
        #调用记录停止
        self._record_stop(exclude_ip_address=device.ip_address)

    # 记录停止确认
    def osc_record_stop_confirm(self, ip_address, command, timecode, *paths):
        device = self._device_from_ip_address(ip_address, command, value=timecode)
        if not device:
            return

        if not paths:
            paths = None
        #设备.记录停止确认
        device.record_stop_confirm(timecode, paths=paths)

    # OSC记录取消
    def osc_record_cancel(self, ip_address, command):
        """
        This is called when record has been pressed and stopped before the countdown in take recorder
        has finished
        """
        device = self._device_from_ip_address(ip_address, command)
        if not device:
            return
        #记录取消 带IP地址的那种
        self._record_cancel(exclude_ip_address=device.ip_address)

    # OSC记录取消确认
    def osc_record_cancel_confirm(self, ip_address, command, timecode):
        pass
        #device = self._device_from_ip_address(ip_address, command, value=timecode)
        #if not device:
        #    return

        #self.record_cancel_confirm(device, timecode)

    # OSC_UE4_启动_确认
    def osc_ue4_launch_confirm(self, ip_address, command):
        #拿到设备
        device = self._device_from_ip_address(ip_address, command)
        if not device:
            return

        # If the device is already ready, bail
        if device.status == DeviceStatus.READY:
            return

        # Set the device status to ready
        device.status = DeviceStatus.READY

    # OSC添加发送目标确认
    def osc_add_send_target_confirm(self, ip_address, command, value):
        # 拿取第一设备
        device = self.device_manager.device_with_ip_address(ip_address[0])
        if not device:
            return
        #调用设备的：“OSC添加发送目标确认”
        device.osc_add_send_target_confirm()

    # OSC_AR会话_停止_确认
    def osc_arsession_stop_confrim(self, ip_address, command, value):
        LOGGER.debug(f'osc_arsession_stop_confrim {value}')
    
    # OSC_AR会话_开始_确认
    def osc_arsession_start_confrim(self, ip_address, command, value):
        device = self._device_from_ip_address(ip_address, command, value=value)
        if not device:
            return
        # 设备：连接监听器
        device.connect_listener()
    
    # OSC_电池
    def osc_battery(self, ip_address, command, value):
        # The Battery command is used to handshake with LiveLinkFace. Don't reject it if it's not connected 
        # 这个电池命令被用于 和LiveLinkFace 握手.如果没有连接，不要拒绝它
        device = self.device_manager.device_with_ip_address(ip_address[0])
        
        if not device:
            return

        # Update the device
        # 更新设备
        device.battery = value

        # Update the UI
        # 更新UI
        device_widget = self.device_list_widget.device_widget_by_hash(device.device_hash)
        device_widget.set_battery(value)
    # OSC 数据
    def osc_data(self, ip_address, command, value):
        device = self._device_from_ip_address(ip_address, command)
        if not device:
            return

# 转移列队句柄操作部件
class TransportQueueHeaderActionWidget(QtWidgets.QWidget):
    # 初始化
    def __init__(self, parent=None):
        super().__init__(parent)
        #自己的层 = QT部件.垂直盒子层
        self.layout = QtWidgets.QHBoxLayout()
        #自己的层设置内容边距为0
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout)
        # 标签 
        def __label(label_text):
            #标签 = Qt部件.标签
            label = QtWidgets.QLabel()
            label.setText(label_text)                                           #标签：设置标签文本
            label.setAlignment(QtCore.Qt.AlignCenter)                           #标签：设置对齐（中心对齐）
            label.setStyleSheet("font-weight: bold")                            #标签：设置（字体样式）
            return label                                                        #返回标签

        self.name_label = __label('Transport Queue')                            #名字标签： 标签为（转移列队）

        self.layout.addWidget(self.name_label)                                  #自己的层.添加部件（名字标签）
    
    def paintEvent(self, event):                                                #绘制事件
        opt = QtWidgets.QStyleOption()                                          #qt部件.qt样式
        opt.initFrom(self)                                                      #opt初始化（）
        painter = QtGui.QPainter(self)                                          # qt绘制器
        self.style().drawPrimitive(QtWidgets.QStyle.PE_Widget, opt, painter, self)      #样式.下达绘制命令（PE部件，opt，绘制）


class TransportQueueActionWidget(QtWidgets.QWidget):
    #初始化
    def __init__(self, name, parent=None):
        super().__init__(parent)
        #初始化层
        self.layout = QtWidgets.QHBoxLayout()                   #注册个垂直层
        self.layout.setContentsMargins(20, 2, 20, 2)            #设置边距
        self.layout.setSpacing(2)                               #设置空白
        self.setLayout(self.layout)                             #设置层

        # Job Label                                             #添加标签
        label = QtWidgets.QLabel(name)
        self.layout.addWidget(label)                            #添加部件
       
        #分隔符
        spacer = QtWidgets.QSpacerItem(0, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layout.addItem(spacer)

        # Remove button 
        # 移除按键
        button = sb_widgets.ControlQPushButton()            #注册一个按键
        button.setProperty("no_background", True)           #参数“无背景”
        button.setStyle(button.style())                     #设置按键样式

        icon = QtGui.QIcon()
        pixmap = QtGui.QPixmap(f":/icons/images/icon_close_disabled.png")  #禁用
        icon.addPixmap(pixmap, QtGui.QIcon.Normal, QtGui.QIcon.Off)
        pixmap = QtGui.QPixmap(f":/icons/images/icon_close.png")            #关闭
        icon.addPixmap(pixmap, QtGui.QIcon.Normal, QtGui.QIcon.On)
        pixmap = QtGui.QPixmap(f":/icons/images/icon_close_hover.png")      #关闭覆盖
        icon.addPixmap(pixmap, QtGui.QIcon.Active, QtGui.QIcon.Off)

        button.setIcon(icon)                                                #设置按键图标
        button.setIconSize(pixmap.rect().size()*0.75)                       #设置图标尺寸
        button.setMinimumSize(QtCore.QSize(20, 20))                         #设置最小大小

        button.setCheckable(False)                                          #设置按键是否可check
        #button.clicked.connect(self.device_button_clicked)
        self.layout.addWidget(button)                                       #将按键添加到层里
    
    #测试 能不能跑
    def test(self):
        LOGGER.debug('BOOM!')
    # 绘制事件
    def paintEvent(self, event):
        opt = QtWidgets.QStyleOption()                      #注册样式
        opt.initFrom(self)                                  #初始化自自己
        painter = QtGui.QPainter(self)                      # 绘制自己
        self.style().drawPrimitive(QtWidgets.QStyle.PE_Widget, opt, painter, self) #设置自己的样式 
