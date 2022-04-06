# Copyright Epic Games, Inc. All Rights Reserved.
import os                                               #系统
import os.path                                          #系统路径
import json
from pickle import FALSE
import socket                                           #网络socket
from .switchboard_logging import LOGGER
import switchboard.switchboard_utils as sb_utils        #sb单元
import shutil                                           #对文件和目录操作的一个库
import fnmatch                                          # 文件名匹配库
import sys

from PySide2 import QtCore
#配置路径
CONFIG_DIR = os.path.normpath(os.path.join(os.path.dirname(__file__), '..', "configs"))
#默认地图文本
DEFAULT_MAP_TEXT = '-- Default Map --'
# 设置
class Setting(QtCore.QObject):
    # 设置更改的信号
    signal_setting_changed = QtCore.Signal(object, object)
    # 设置覆盖的信号
    signal_setting_overriden = QtCore.Signal(str, object, object)

    """
    允许设备 返回参数 那些在设置菜单中被命名的
    参数：
        参数名： 内部名
        nice name ：显示名
        value ：设置初始的值
        possble_values ；可能的值被用做复选框
        placholder_text： 占位符
        tool_tip ：提示文本
        show_ui ：是否显示UI
        filtervalueset_fn ：筛选值得函数
    """
    """
    Allows Device to return paramters that are meant to be set in the settings menu

    Args:
        attr_name             (str): Internal name.
        nice_name             (str): Display name.
        value                      : The initial value of this setting.
        possible_values            : Possible values for this Setting. Useful with e.g. combo boxes.
        placholder_text       (str): Placeholder for this setting's value in the UI (if applicable)
        tool_tip              (str): Tooltip to show in the UI for this setting.
        show_ui              (bool): Determines if this Setting will be shown inthe Settings UI.
        filtervalueset_fn (function): This function will validate and modify the settings value being set. None is allowed.
    """
    #初始化
    def __init__(
        self, 
        attr_name, 
        nice_name, 
        value, 
        possible_values=[], 
        placholder_text=None, 
        tool_tip=None, 
        show_ui=True, 
        filtervalueset_fn=None
    ):
        super().__init__()
        #筛选值函数 = 筛选值函数
        self.filtervalueset_fn = filtervalueset_fn
        # 参数名
        self.attr_name = attr_name
        # 显示名
        self.nice_name = nice_name
        # 如果筛选函数 存在
        if self.filtervalueset_fn:
            value = self.filtervalueset_fn(value)
        # 原来得值
        self._original_value = self._value = value
        # 可能的值
        self.possible_values = possible_values

        # todo-dara: overrides are identified by device name right now. this should be changed to the hash instead.
        # 目前，覆盖由设备名称标识。这应该改hash值替代
        # that way we could avoid having to patch the overrides and settings in CONFIG when a device is renamed.
        self._overrides = {}                            #覆盖
        self.placholder_text = placholder_text          #占位符文本
        self.tool_tip = tool_tip                        #工具提示
        self.show_ui = show_ui                          #显示UI

    # 是否覆盖
    def is_overriden(self, device_name):
        try:
            return self._overrides[device_name] != self._value
        except KeyError:
            return False

    # 移除覆盖：移除最后一个值
    def remove_override(self, device_name):
        self._overrides.pop(device_name, None)

    #更新值
    def update_value(self, new_value):
        if self.filtervalueset_fn:
            new_value = self.filtervalueset_fn(new_value)
        # 如果之前的值等于新值
        if self._value == new_value:
            return
        # 这是旧值
        old_value = self._value
        #这是新值
        self._value = new_value
        #信号设置更改.发送
        self.signal_setting_changed.emit(old_value, self._value)

    # 覆盖值
    def override_value(self, device_name, override):
        # 筛选值设置
        if self.filtervalueset_fn:
            override = self.filtervalueset_fn(override)
        # 设备名 在 覆盖里面 并且 覆盖【设备名】 == 覆盖
        if device_name in self._overrides and self._overrides[device_name] == override:
            return
        # 覆盖[设备名]
        self._overrides[device_name] = override
        self.signal_setting_overriden.emit(device_name, self._value, override)

    # 获取值
    def get_value(self, device_name=None):
        try:
            return self._overrides[device_name]
        except KeyError:
            #直接拿值
            return self._value 

    # 启用设备名更改
    def on_device_name_changed(self, old_name, new_name):
        # 如果 老名字 在覆盖的值里面
        if old_name in self._overrides.keys():
            #覆盖值【新名字】 = 覆盖值 弹出【旧值】
            self._overrides[new_name] = self._overrides.pop(old_name)
    
    # 重置
    def reset(self):
        #自己的值 = 原有的值
        self._value = self._original_value
        #把覆盖值清空
        self._overrides = {}


# Store engine path, uproject path
# 存储引擎路径和项目路径

# 配置类
class Config(object):

    saving_allowed = True
    saving_allowed_fifo = []
    # push是压一个值到栈顶
    def push_saving_allowed(self, value):
        '''
         Sets a new state of saving allowed, but pushes current to the stack
         设置 一个新的状态 保存允许 但是压个值到当前栈顶
        '''
        #保存允许 先入先出.添加进去（保存允许）
        self.saving_allowed_fifo.append(self.saving_allowed)
        self.saving_allowed = value

    # pop移除保存允许的顶端
    def pop_saving_allowed(self):
        '''
         Restores saving_allowed flag from the stack
         恢复保存允许标识 从堆栈
        '''
        self.saving_allowed = self.saving_allowed_fifo.pop()
    # 通过文件名初始化
    def __init__(self, file_name):
        self.init_with_file_name(file_name)

    #静态方式
    @staticmethod
    # 清理 P4路径 干净的p4路径
    def clean_p4_path(path):
        ''' 
        Clean p4 path. e.g. strip and remove trailing '/'
        清理 p4 路径  剥离并移除 拖尾’/‘
        '''
        # 没有路径
        if not path:
            return ''
        # 路径 = 路径剥离
        path = path.strip()

        while len(path) and path[-1] == '/':
            path = path[:-1]
        
        return path

    # 初始化新配置
    def init_new_config(self, project_name, uproject, engine_dir, p4_settings):
        ''' 
        Initialize new configuration
        初始化 新的配置
        '''
        # 项目名
        self.PROJECT_NAME = project_name
        # 项目路径  
        self.UPROJECT_PATH = Setting("uproject", "uProject Path", uproject, tool_tip="Path to uProject")
        # Switchborad目录
        self.SWITCHBOARD_DIR = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../'))
        # 引擎目录
        self.ENGINE_DIR = Setting("engine_dir", "Engine Directory", engine_dir, tool_tip="Path to UE4 engine directory")
        # 构建引擎
        self.BUILD_ENGINE = Setting("build_engine", "Build Engine", False, tool_tip="Is Engine built from source?")
        # 地图路径
        self.MAPS_PATH = Setting("maps_path", "Map Path", "", tool_tip="Relative path from Content folder that contains maps to launch into.")
        # 地图过滤器
        self.MAPS_FILTER = Setting("maps_filter", "Map Filter", "*.umap", tool_tip="Walk every file in the Map Path and run a fnmatch to filter the file names")
        # P4启用
        self.P4_ENABLED = Setting("p4_enabled", "Perforce Enabled", p4_settings['p4_enabled'], tool_tip="Toggle Perforce support for the entire application")
        # 源控制
        self.SOURCE_CONTROL_WORKSPACE = Setting("source_control_workspace", "Workspace Name", p4_settings['p4_workspace_name'], tool_tip="SourceControl Workspace/Branch")
        # P4项目路径
        self.P4_PROJECT_PATH = Setting(
            attr_name="p4_sync_path", 
            nice_name="Perforce Project Path", 
            value=p4_settings['p4_project_path'],
            filtervalueset_fn=Config.clean_p4_path,
        )
        # P4引擎路径
        self.P4_ENGINE_PATH = Setting(
            attr_name="p4_engine_path", 
            nice_name="Perforce Engine Path", 
            value=p4_settings['p4_engine_path'],
            filtervalueset_fn=Config.clean_p4_path,
        )
        # 当前关卡
        self.CURRENT_LEVEL = DEFAULT_MAP_TEXT
        # OSC服务端口
        self.OSC_SERVER_PORT = Setting("osc_server_port", "OSC Server Port", 6000)
        self.OSC_CLIENT_PORT = Setting("osc_client_port", "OSC Client Port", 8000)

        # MU Settings
        # 多用户设置
        self.MULTIUSER_SERVER_EXE = 'UnrealMultiUserServer'                         #多用户服务
        self.MUSERVER_COMMAND_LINE_ARGUMENTS = ""                                   #多用户命令行参数集
        self.MUSERVER_SERVER_NAME = f'{self.PROJECT_NAME}_MU_Server'                #多用户服务名
        self.MUSERVER_AUTO_LAUNCH = True                                            #多用户自动启动
        self.MUSERVER_AUTO_JOIN = False                                             #多用户自动加入
        self.MUSERVER_CLEAN_HISTORY = True                                          #多用户清理历史
        self.MUSERVER_AUTO_BUILD = True                                             #多用户自动构建

        self.LISTENER_EXE = 'SwitchboardListener'                                   #监听程序

        self._device_data_from_config = {}                                          # 设备数据 来自配置
        self._plugin_data_from_config = {}                                          # 插件数据 来自配置
        self._plugin_settings = {}                                                  # 插件 设置
        self._device_settings = {}                                                  # 设备 设置
        
        # 新增值
        self.AUTO_OPEN_ALL = Setting("auto_open_all","Auto Open All",False)
        self.DELAY_TIME = Setting("delay_time","Delay Time",1000)
        # 文件路径
        self.file_path = os.path.normpath(os.path.join(CONFIG_DIR, self.name_to_config_file_name(project_name, unique=True)))
        # 文件名
        file_name = os.path.basename(self.file_path)
        # 设置.配置 = 文件名
        SETTINGS.CONFIG = file_name
        LOGGER.info(f"Creating new config saved in {SETTINGS.CONFIG}")
        # 保存 设置 和 配置
        SETTINGS.save()
        CONFIG.save()

    # 通过文件名初始化
    def init_with_file_name(self, file_name):
        # 如果文件名
        if file_name:
            # 文件路径 
            self.file_path = os.path.normpath(os.path.join(CONFIG_DIR, file_name))

            # Read the json config file
            # 读取json配置文件
            try:
                #打开文件
                with open(self.file_path) as f:
                    LOGGER.debug(f'Loading Config {self.file_path}')
                    data = json.load(f) #读取到数据
            except FileNotFoundError as e:
                # 日志。错误（）
                LOGGER.error(f'Config: {e}')
                #文件路径清空
                self.file_path = None
                data = {}
        else:
            # 文件路径为空 数据为空
            self.file_path = None
            data = {}
        #项目路径 清空
        project_settings = []

        # 读取 项目名
        self.PROJECT_NAME = data.get('project_name', 'Default')
        # 读取 项目路径
        self.UPROJECT_PATH = Setting("uproject", "uProject Path", data.get('uproject', ''), tool_tip="Path to uProject")
        # 项目设置添加
        project_settings.append(self.UPROJECT_PATH)

        # Directory Paths
        # 直接路径
        # sb目录
        self.SWITCHBOARD_DIR = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../'))
        # 读取 引擎路径
        self.ENGINE_DIR = Setting("engine_dir", "Engine Directory", data.get('engine_dir', ''), tool_tip="Path to UE4 engine directory")
        # 项目设置 添加
        project_settings.append(self.ENGINE_DIR)
        # 读取构建引擎
        self.BUILD_ENGINE = Setting("build_engine", "Build Engine", data.get('build_engine', False), tool_tip="Is Engine built from source?")
        project_settings.append(self.BUILD_ENGINE)
        # 读取 地图路径
        self.MAPS_PATH = Setting("maps_path", "Map Path", data.get('maps_path', ''), placholder_text="Maps", tool_tip="Relative path from Content folder that contains maps to launch into.")
        # 添加到项目设置里
        project_settings.append(self.MAPS_PATH)
        # 读取 项目筛选
        self.MAPS_FILTER = Setting("maps_filter", "Map Filter", data.get('maps_filter', '*.umap'), placholder_text="*.umap", tool_tip="Walk every file in the Map Path and run a fnmatch to filter the file names")
        # 添加到项目设置
        project_settings.append(self.MAPS_FILTER)

        # OSC settings
        # OSC设置
        # 读取 OSC服务端口 OSC客户端口
        self.OSC_SERVER_PORT = Setting("osc_server_port", "OSC Server Port", data.get('osc_server_port', 6000))
        self.OSC_CLIENT_PORT = Setting("osc_client_port", "OSC Client Port", data.get('osc_client_port', 8000))
        # 添加到项目设置中
        project_settings.extend([self.OSC_SERVER_PORT, self.OSC_CLIENT_PORT])

        # 新增值
        self.AUTO_OPEN_ALL = Setting("auto_open_all","Auto Open All",data.get('auto_open_all', False))
        self.DELAY_TIME = Setting("delay_time","Delay Time",data.get('delay_time',1000))
        project_settings.extend([self.AUTO_OPEN_ALL,self.DELAY_TIME])
        
        # Perforce settings
        # P4 设置 
        # P4启用
        self.P4_ENABLED = Setting("p4_enabled", "Perforce Enabled", data.get("p4_enabled", False), tool_tip="Toggle Perforce support for the entire application")
        # 源码控制工作空间
        self.SOURCE_CONTROL_WORKSPACE = Setting("source_control_workspace", "Workspace Name", data.get("source_control_workspace"), tool_tip="SourceControl Workspace/Branch")
        # p4项目路径
        self.P4_PROJECT_PATH = Setting(
            "p4_sync_path", 
            "Perforce Project Path", 
            data.get("p4_sync_path", ''), 
            placholder_text="//UE4/Project",
            filtervalueset_fn=Config.clean_p4_path,
        )
        # p4引擎路径
        self.P4_ENGINE_PATH = Setting(
            "p4_engine_path", 
            "Perforce Engine Path", 
            data.get("p4_engine_path", ''), 
            placholder_text="//UE4/Project/Engine",
            filtervalueset_fn=Config.clean_p4_path,
        )
        # 拓展项目设置
        project_settings.extend([self.P4_ENABLED, self.SOURCE_CONTROL_WORKSPACE, self.P4_PROJECT_PATH, self.P4_ENGINE_PATH])

        # EXE names
        # 多用户服务exe
        self.MULTIUSER_SERVER_EXE = data.get('multiuser_exe', 'UnrealMultiUserServer')
        # 监听器 exe
        self.LISTENER_EXE = data.get('listener_exe', 'SwitchboardListener')

        # MU Settings
        # 多用户设置
        # 多用户命令行参数
        self.MUSERVER_COMMAND_LINE_ARGUMENTS = data.get('muserver_command_line_arguments', '')
        #多用户 服务名
        self.MUSERVER_SERVER_NAME = data.get('muserver_server_name', f'{self.PROJECT_NAME}_MU_Server')
        # 多用户给 自动启动
        self.MUSERVER_AUTO_LAUNCH = data.get('muserver_auto_launch', True)
        # 多用户 自动加入
        self.MUSERVER_AUTO_JOIN = data.get('muserver_auto_join', False)
        # 多用户 清理历史
        self.MUSERVER_CLEAN_HISTORY = data.get('muserver_clean_history', True)
        # 多用户 自动构建
        self.MUSERVER_AUTO_BUILD = data.get('muserver_auto_build', True)

        # MISC SETTINGS 杂项 设置
        self.CURRENT_LEVEL = data.get('current_level', DEFAULT_MAP_TEXT)

        # automatically save whenever a project setting is changed or overriden by a device
        # 自动保存 当一个项目设置已经更改 或者 覆盖一个值
        for setting in project_settings:
            setting.signal_setting_changed.connect(lambda: self.save())
            setting.signal_setting_overriden.connect(self.on_device_override_changed)

        # Devices 设备
        self._device_data_from_config = {}
        self._plugin_data_from_config = {}
        self._device_settings = {}
        self._plugin_settings = {}

        # Convert devices data from dict to list so they can be directly fed into the kwargs
        # 将设备数据从dict转换为list，这样它们就可以直接输入到kwargs中
        for device_type, devices in data.get('devices', {}).items():
            for device_name, data in devices.items():
                # 设备名 “设置”
                if device_name == "settings":
                    self._plugin_data_from_config[device_type] = data
                else:
                    ip_address = data["ip_address"]
                    device_data = {"name": device_name, "ip_address": ip_address}
                    #设备数据【“kwags”】
                    device_data["kwargs"] = {k: v for (k,v) in data.items() if k != "ip_address"}
                    self._device_data_from_config.setdefault(device_type, []).append(device_data)

    # 载入插件设置
    def load_plugin_settings(self, device_type, settings):
        ''' 
        Updates plugin settings values with those read from the config file.
        更新插件设置值 那些从配置文件中读取
        '''
        # 读取设置 = 插件数据来自配置（设备类型）
        loaded_settings = self._plugin_data_from_config.get(device_type, [])
        # 载入设置
        if loaded_settings:
            for setting in settings:
                # 设置参数名
                if setting.attr_name in loaded_settings:
                    # 设置 更新值
                    setting.update_value(loaded_settings[setting.attr_name])
            del self._plugin_data_from_config[device_type]

    # 注册插件设置
    def register_plugin_settings(self, device_type, settings):
        #插件设置[设备类型] = 设置
        self._plugin_settings[device_type] = settings
        # 设置遍历
        for setting in settings:
            setting.signal_setting_changed.connect(lambda: self.save())
            setting.signal_setting_overriden.connect(self.on_device_override_changed)
    # 注册设备设置
    def register_device_settings(self, device_type, device_name, settings, overrides):
        #设备设置
        self._device_settings[(device_type, device_name)] = (settings, overrides)
        for setting in settings:
            setting.signal_setting_changed.connect(lambda: self.save())
    # 设备覆盖更改
    def on_device_override_changed(self, device_name, old_value, override):
        # only do a save operation when the device is known (has called register_device_settings)
        # otherwise it is still loading and we want to avoid saving during device loading to avoid errors in the cfg file.
        known_devices = [name for (_, name) in self._device_settings.keys()]
        if device_name in known_devices:
            self.save()
    # 是否可写
    def is_writable(self):
        if not self.file_path:
            return False
        # 路径.存在 路径.是文件
        if os.path.exists(self.file_path) and os.path.isfile(self.file_path):
            return os.access(self.file_path, os.W_OK)

        return False
    # 重命名
    def rename(self, new_config_name):
        """
        Move the file
        """
        #新文件路径
        new_file_path = os.path.normpath(os.path.join(CONFIG_DIR, new_config_name))

        if self.file_path:
            #文件 重命名
            shutil.move(self.file_path, new_file_path)
        # 配置中文件路径重新设置为新的
        self.file_path = new_file_path
        # 保存
        self.save()
    # 保存数据
    def save(self):
        if not self.saving_allowed:
            return

        data = {}

        # General settings
        data['project_name'] = self.PROJECT_NAME                                                        #项目名
        data['uproject'] = self.UPROJECT_PATH.get_value()                                               #项目
        data['engine_dir'] = self.ENGINE_DIR.get_value()                                                #引擎目录
        data['build_engine'] = self.BUILD_ENGINE.get_value()                                            #构建引擎
        data["maps_path"] = self.MAPS_PATH.get_value()                                                  #地图路径
        data["maps_filter"] = self.MAPS_FILTER.get_value()                                              #地图筛选
        data["listener_exe"] = self.LISTENER_EXE                                                        #监听exe
        
		# OSC settings
        data["osc_server_port"] = self.OSC_SERVER_PORT.get_value()                                      #服务端口
        data["osc_client_port"] = self.OSC_CLIENT_PORT.get_value()                                      #客户端口

        # Source Control Settings
        data["p4_enabled"] = self.P4_ENABLED.get_value()                                                #p4启用
        data["p4_sync_path"] = self.P4_PROJECT_PATH.get_value()                                         #p4同步路径
        data["p4_engine_path"] = self.P4_ENGINE_PATH.get_value()                                        #p4引擎路径
        data["source_control_workspace"] = self.SOURCE_CONTROL_WORKSPACE.get_value()                    #源控制工作空间
        
        # MU Settings
        data["multiuser_exe"] = self.MULTIUSER_SERVER_EXE                                               #多用户exe
        data["muserver_command_line_arguments"] = self.MUSERVER_COMMAND_LINE_ARGUMENTS                  #多用户命令行数组
        data["muserver_server_name"] = self.MUSERVER_SERVER_NAME                                        #多用户服务名
        data["muserver_auto_launch"] = self.MUSERVER_AUTO_LAUNCH                                        #多用户自动启动
        data["muserver_auto_join"] = self.MUSERVER_AUTO_JOIN                                            #多用户自动加入
        data["muserver_clean_history"] = self.MUSERVER_CLEAN_HISTORY                                    #多用户清理历史
        data["muserver_auto_build"] = self.MUSERVER_AUTO_BUILD                                          #多用户自动构建

        # Current Level 当前关卡
        data["current_level"] = self.CURRENT_LEVEL

        # Devices
        data["devices"] = {}

        # 新增延时
        data["auto_open_all"]=self.AUTO_OPEN_ALL.get_value()
        data["delay_time"]=self.DELAY_TIME.get_value()

        # Plugin settings 插件设置
        for device_type, plugin_settings in self._plugin_settings.items():
            # 如果没有插件设则
            if not plugin_settings:
                continue

            settings = {}
            #插件设置
            for setting in plugin_settings:
                #设置【设置.参数名】 = 设置.获取值
                settings[setting.attr_name] = setting.get_value()
            
            # 数据[设备][设备类型] 简单的说就是把数据打包放进去
            data["devices"][device_type] = {
                "settings" : settings,
            }

        # Device settings 
        # 设备设置
        for (device_type, device_name), (settings, overrides) in self._device_settings.items():
            # 如果  不是设备类型 在 数据[设备].键值
            if not device_type in data["devices"].keys():
                data["devices"][device_type] = {}
            # 创建 序列化设置
            serialized_settings = {}
            # 如果是普通设置
            for setting in settings:
                serialized_settings[setting.attr_name] = setting.get_value()
            # 如果是覆盖类型
            for setting in overrides:
                if setting.is_overriden(device_name):
                    serialized_settings[setting.attr_name] = setting.get_value(device_name)
            # 数据[设备][设备类型][设备类型] = 序列化设置
            data["devices"][device_type][device_name] = serialized_settings

        # Save to file
        # 保存到文件
        with open(f'{self.file_path}', 'w') as f:
            json.dump(data, f, indent=4)
            LOGGER.debug(f'Config File: {self.file_path} updated')

    # 设备名字更改
    def on_device_name_changed(self, old_name, new_name):
        #先将旧值清空
        old_key = None
        # 更新进入设备设置 作为他们的身份通过名字
        # update the entry in device_settings as they are identified by name
        for (device_type, device_name), (_, overrides) in self._device_settings.items():
            #如果 设备名 == 老名字
            if device_name == old_name:
                old_key = (device_type, old_name)
                # we also need to patch the overrides for the same reason
                # 因为同样的原因，我们也需要修补覆盖
                for setting in overrides:
                    setting.on_device_name_changed(old_name, new_name)
                break
        #新的键
        new_key = (old_key[0], new_name)
        #设备设置【新的键】 = 设备设置弹出的（旧值）
        self._device_settings[new_key] = self._device_settings.pop(old_key)

        self.save()

    # 设备移除
    def on_device_removed(self, _, device_type, device_name, update_config):
        if not update_config:
            return
        # 设备设置（设备类型，设备名）
        del self._device_settings[(device_type, device_name)]
        self.save()

    def maps(self):
        # 地图路径 = 路径（路径+（系统路径（项目路径+content+地图路径宏的值）））
        maps_path = os.path.normpath(os.path.join(os.path.dirname(self.UPROJECT_PATH.get_value().replace('"','')), 'Content', self.MAPS_PATH.get_value()))
        # 地图
        maps = []
        # 
        for _, _, files in os.walk(maps_path):
            #找到与名字匹配的
            for name in files:
                # 如果不匹配就跳过
                if not fnmatch.fnmatch(name, self.MAPS_FILTER.get_value()):
                    continue
                # 根名 = 系统路径 分割文字
                rootname, _ = os.path.splitext(name)
                # 根名字 不在 地图里
                if rootname not in maps:
                    maps.append(rootname)
        # 地图排序
        maps.sort()
        return maps
    # 多用户服务器路径
    def multiuser_server_path(self):
        return self.engine_exe_path(self.ENGINE_DIR.get_value(), self.MULTIUSER_SERVER_EXE)
    #监听器路径
    def listener_path(self):
        # 返回 引擎exe 路径
        return self.engine_exe_path(self.ENGINE_DIR.get_value(), self.LISTENER_EXE)

    # todo-dara: find a way to do this directly in the LiveLinkFace plugin code
    # 在LiveLinkFace插件代码中找到一种直接实现这一点的方法
    def unreal_device_ip_addresses(self):
        #虚幻ip地址
        unreal_ips = []
        #
        for (device_type, device_name), (settings, overrides) in self._device_settings.items():
            # 设备类型 == 虚幻
            if device_type == "Unreal":
                #设置
                for setting in settings:
                    # 如果 设置.参数名 == “ip地址”
                    if setting.attr_name == "ip_address":
                        unreal_ips.append(setting.get_value(device_name))
        return unreal_ips

    #静态方式
    @staticmethod
    # 引擎exe路径
    def engine_exe_path(engine_dir: str, exe_basename: str):
        # 返回平台依赖路径 到 指定 特定引擎可知执行文件
        ''' Returns platform-dependent path to the specified engine executable. '''
        # 可执行名
        exe_name = exe_basename
        #平台bin子目录
        platform_bin_subdir = ''
        # 系统平台启动
        if sys.platform.startswith('win'):
            # 平台bin子目录
            platform_bin_subdir = 'Win64'
            # 平台bin路径
            platform_bin_path = os.path.normpath(os.path.join(engine_dir, 'Binaries', platform_bin_subdir))
            # 给到的路径
            given_path = os.path.join(platform_bin_path, exe_basename)
            if os.path.exists(given_path):
                return given_path

            # Use %PATHEXT% to resolve executable extension ambiguity.
            # 使用%PATHEXT%来解决可执行扩展的歧义。
            pathexts = os.environ.get('PATHEXT', '.COM;.EXE;.BAT;.CMD').split(';')
            for ext in pathexts:
                testpath = os.path.join(platform_bin_path, f'{exe_basename}{ext}')
                if os.path.isfile(testpath):
                    return testpath

            # Fallback despite non-existence.
            #虽然不存在，但还是要撤退。
            return given_path
        else:
            if sys.platform.startswith('linux'):
                platform_bin_subdir = 'Linux'
            elif sys.platform.startswith('darwin'):
                platform_bin_subdir = 'Mac'

            return os.path.normpath(os.path.join(engine_dir, 'Binaries', platform_bin_subdir, exe_name))

    # 名字到配置文件名
    @staticmethod
    def name_to_config_file_name(name, unique=False):
        """
        Given a name like My_Project return config_My_Project.json
        给一个名字像 我的项目 返回 config_我的项目.json
        """
        # 如果不是唯一
        if not unique:
            #返回 config_名字.json
            return f'config_{name}.json'

        i = 1
        # 文件名
        file_name = f'config_{name}.json'
        # 文件路径
        file_path = os.path.normpath(os.path.join(CONFIG_DIR, file_name))
        # 文件名遍历 有同样的就在后缀+1
        while os.path.isfile(file_path):
            file_name = f'config_{name}_{i}.json'
            file_path = os.path.normpath(os.path.join(CONFIG_DIR, file_name))
            i+=1

        return file_name

    # 静态方式： 配置文件名到名字
    @staticmethod
    def config_file_name_to_name(file_name):
        """
        Given a file name like config_My_Project.json return My_Project
         给个一个文件名像 config_我的项目.json 返回 我的项目
        """
        name = sb_utils.remove_prefix(file_name, 'config_')
        return os.path.splitext(name)[0]

# 用户设置
class UserSettings(object):
    # 初始化 赋值过程
    def __init__(self, file_name='user_settings.json'):
        # 文件路径（配置路径+文件名）
        self.file_path = os.path.normpath(os.path.join(CONFIG_DIR, file_name))

        try:
            # 打开文件路径作为 f
            with open(self.file_path) as f:
                LOGGER.debug(f'Loading Settings {self.file_path}')
                # 读取数据
                data = json.load(f)
        # Create a default user_settings
        # 没有的话创建一个默认的用户设置
        except FileNotFoundError:
            data = {}
            LOGGER.debug(f'Creating default user settings')
        # 配置文件 = 列出配置文件
        config_files = list_config_files()
        # 如果有配置文件 就打开第一个
        if config_files:
            # 配置文件 = 配置文件【0】
            config_files = config_files[0]
        else:
            config_files = ''
        # 配置 = 从数据中 获取 （config）
        self.CONFIG = data.get('config', config_files)
        # IP Address of the machine running Switchboard
        # ip 地址 运行switchboard的机器
        self.IP_ADDRESS = data.get('ip_address', socket.gethostbyname(socket.gethostname()))
        # 转移路径
        self.TRANSPORT_PATH = data.get('transport_path', '')

        # UI Settings
        # UI设置
        self.MUSERVER_SESSION_NAME = data.get('muserver_session_name', f'MU_Session')           #多用户会话名
        self.CURRENT_SEQUENCE = data.get('current_sequence', 'Default')                         #多用户的sequnce
        self.CURRENT_SLATE = data.get('current_slate', 'Scene')                                 #当前的slate
        self.CURRENT_TAKE = data.get('current_take', 1)                                         #当前的take
        self.CURRENT_LEVEL = data.get('current_level', None)                                    #当前的level
        self.LAST_BROWSED_PATH = data.get('last_browsed_path', None)                            #最后浏览路径
        # 新增两个变量
        #self.AUTO_OPEN_ALL = data.get('auto_open_all',True)
        #self.DELAY_TIME = data.get('delay_time',1000)

        # Save so any new defaults are written out
        self.save()                                                                             #保存事件

    def save(self):
        data = {}                                                                               #新建一个data
        data['config'] = self.CONFIG                                                            #数据：配置
        data['ip_address'] = self.IP_ADDRESS                                                    #数据：IP地址
        data['transport_path'] = self.TRANSPORT_PATH                                            #数据：转移路径
        data["muserver_session_name"] = self.MUSERVER_SESSION_NAME                              #数据：多用户会话名
        data["current_sequence"] = self.CURRENT_SEQUENCE                                        #数据：当前sequnce
        data["current_slate"] = self.CURRENT_SLATE                                              #数据：当前slate
        data["current_take"] = self.CURRENT_TAKE                                                #数据：当前take
        data["current_level"] = self.CURRENT_LEVEL                                              #数据：当前level
        data["last_browsed_path"] = self.LAST_BROWSED_PATH                                      #数据：最后浏览路径
        # 新增两个保存变量
        #data["auto_open_all"] = self.AUTO_OPEN_ALL
        #data["delay_time"] = self.DELAY_TIME
        with open(f'{self.file_path}', 'w') as f:                                               #打开文件作为f
            json.dump(data, f, indent=4)                                                        #将数据存储到文件中


# Return a path to the user_settings.json file
# 返回一个路径 到 user_setting.json 文件
def user_settings_file():
    return os.path.join(CONFIG_DIR, 'user_settings.json')


# Return all the config files in config_dir()
# 返回所有的配置文件 在 config目录中
def list_config_files():
    #创建目录
    os.makedirs(CONFIG_DIR, exist_ok=True)
    # 文件以config_开始 以 .json为尾
    return [x for x in os.listdir(CONFIG_DIR) if x.endswith('.json') and x.startswith('config_')]


# Get the user settings and load their config
# 获取 用户设置 并且 读取他们的配置
SETTINGS = UserSettings()
CONFIG = Config(SETTINGS.CONFIG)
