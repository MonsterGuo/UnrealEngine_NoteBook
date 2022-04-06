# Copyright Epic Games, Inc. All Rights Reserved.

import os
from pathlib import Path

from PySide2 import QtCore, QtGui, QtUiTools, QtWidgets

from switchboard.config import CONFIG, SETTINGS, list_config_files
import switchboard.switchboard_widgets as sb_widgets

#获取相对路径
RELATIVE_PATH = os.path.dirname(__file__)


class SettingsDialog(QtCore.QObject):
    def __init__(self):
        super().__init__()

        # Set the UI object
        # 设置UI对象
        loader = QtUiTools.QUiLoader()
        self.ui = loader.load(os.path.join(RELATIVE_PATH, "ui/settings.ui"))

        # Load qss file for dark styling
        # 载入qss 暗黑模式样式
        qss_file = os.path.join(RELATIVE_PATH, "ui/switchboard.qss")
        with open(qss_file, "r") as styling:
            self.ui.setStyleSheet(styling.read())
        #设置窗口标签（设置）
        self.ui.setWindowTitle("Settings")
        #最大位数
        max_port = (1 << 16) - 1
        #服务端 端口号
        self.ui.osc_server_port_line_edit.setValidator(QtGui.QIntValidator(0, max_port))
        #服务端 客户端
        self.ui.osc_client_port_line_edit.setValidator(QtGui.QIntValidator(0, max_port))

        # Store the current config names
        # 存储配置名
        self._config_names = [CONFIG.config_file_name_to_name(x) for x in list_config_files()]
        self._current_config_name = CONFIG.config_file_name_to_name(SETTINGS.CONFIG)

        #项目浏览按键 点击
        self.ui.uproject_browse_button.clicked.connect(self.uproject_browse_button_clicked)
        # 引擎目录 点击
        self.ui.engine_dir_browse_button.clicked.connect(self.engine_dir_browse_button_clicked)
        # 配置文件名 文字更改
        self.ui.config_name_line_edit.textChanged.connect(self.config_name_text_changed)

        # update settings in CONFIG when they are changed in the SettingsDialog
        # 在配置中更新设置 当他们在设置对话中更改时 （lambda表达式用来传值，将部件中的值传递过去）
        # 引擎目录 编辑结束
        self.ui.engine_dir_line_edit.editingFinished.connect(lambda widget=self.ui.engine_dir_line_edit: CONFIG.ENGINE_DIR.update_value(widget.text()))
        # 构建检查盒子 状态更改
        self.ui.build_engine_checkbox.stateChanged.connect(lambda state: CONFIG.BUILD_ENGINE.update_value(True if state == QtCore.Qt.Checked else False))
        # 项目：编辑结束
        self.ui.uproject_line_edit.editingFinished.connect(lambda widget=self.ui.uproject_line_edit: CONFIG.UPROJECT_PATH.update_value(widget.text()))
        # 地图：编辑结束
        self.ui.map_path_line_edit.editingFinished.connect(lambda widget=self.ui.map_path_line_edit: CONFIG.MAPS_PATH.update_value(widget.text()))
        # 地图筛选编辑结束
        self.ui.map_filter_line_edit.editingFinished.connect(lambda widget=self.ui.map_filter_line_edit: CONFIG.MAPS_FILTER.update_value(widget.text()))
        # OSC 服务端口
        self.ui.osc_server_port_line_edit.editingFinished.connect(lambda widget=self.ui.osc_server_port_line_edit: CONFIG.OSC_SERVER_PORT.update_value(int(widget.text())))
        # OSC 客户端口
        self.ui.osc_client_port_line_edit.editingFinished.connect(lambda widget=self.ui.osc_client_port_line_edit: CONFIG.OSC_CLIENT_PORT.update_value(int(widget.text())))
        # P4项目路径
        self.ui.p4_project_path_line_edit.editingFinished.connect(lambda widget=self.ui.p4_project_path_line_edit: CONFIG.P4_PROJECT_PATH.update_value(widget.text()))
        # P4引擎路径
        self.ui.p4_engine_path_line_edit.editingFinished.connect(lambda widget=self.ui.p4_engine_path_line_edit: CONFIG.P4_ENGINE_PATH.update_value(widget.text()))
        # 源码控制
        self.ui.source_control_workspace_line_edit.editingFinished.connect(lambda widget=self.ui.source_control_workspace_line_edit: CONFIG.SOURCE_CONTROL_WORKSPACE.update_value(widget.text()))

        # 新增两个连接 到UI的部分
        self.ui.auto_open_groupbox.stateChanged.connect(lambda state: CONFIG.AUTO_OPEN_ALL.update_value(True if state == QtCore.Qt.Checked else False))
        self.ui.delay_time_spin_box.editingFinished.connect(lambda widget = self.ui.delay_time_spin_box: CONFIG.AUTO_OPEN_ALL.update_value(int(widget.text())))
        
        self._device_groupbox = {}

    #配置名
    def config_name(self):
        return self.ui.config_name_line_edit.text()
    #设置配置名
    def set_config_name(self, value):
        self.ui.config_name_line_edit.setText(value)
    #配置名更改
    def config_name_text_changed(self, value):
        # 没值
        if not value:
            valid_name = False
        else:
            #如果当前值在所有配置名 中
            if value in self._config_names:
                # 如果 值 等于 当前配置名
                if value == self._current_config_name:
                    valid_name = True  #值有效
                else:
                    valid_name = False #值无效
            else:
                valid_name = True #值有效
        #没搞明白
        if valid_name:
            #switchborad部件.设置qt参数（）
            sb_widgets.set_qt_property(self.ui.config_name_line_edit, "input_error", False)
        else:
            sb_widgets.set_qt_property(self.ui.config_name_line_edit, "input_error", True)
            #矩形
            rect = self.ui.config_name_line_edit.parent().mapToGlobal(self.ui.config_name_line_edit.geometry().topRight())
            QtWidgets.QToolTip().showText(rect, 'Config name must be unique')
    #项目浏览按键点击
    def uproject_browse_button_clicked(self):
        #文件名 = 文件对话框 获取打开带有（“”）后缀的文件
        file_name, _ = QtWidgets.QFileDialog.getOpenFileName(parent=self.ui, filter='*.uproject')
        if file_name:
            file_name = os.path.normpath(file_name)
            self.set_uproject(file_name)
            #配置 项目路径更新值
            CONFIG.UPROJECT_PATH.update_value(file_name)
    #引擎目录浏览按键点击
    def engine_dir_browse_button_clicked(self):
        #获取引擎目录名
        dir_name = QtWidgets.QFileDialog.getExistingDirectory(parent=self.ui)
        if dir_name:
            dir_name = os.path.normpath(dir_name)
            self.set_engine_dir(dir_name)
            #配置;更新引擎目录
            CONFIG.ENGINE_DIR.update_value(dir_name)

    # 获取：ip地址
    def ip_address(self):
        return self.ui.ip_address_line_edit.text()
    # 设置：ip地址
    def set_ip_address(self, value):
        self.ui.ip_address_line_edit.setText(value)
    # 获取：传送路径
    def transport_path(self):
        return self.ui.transport_path_line_edit.text()
    # 设置：传送路径
    def set_transport_path(self, value):
        self.ui.transport_path_line_edit.setText(value)
    # 获取 ：监听exe
    def listener_exe(self):
        return self.ui.listener_exe_line_edit.text()
    # 设置：监听exe
    def set_listener_exe(self, value):
        self.ui.listener_exe_line_edit.setText(value)
    # 获取 ：项目名
    def project_name(self):
        return self.ui.project_name_line_edit.text()
    # 设置：项目名
    def set_project_name(self, value):
        self.ui.project_name_line_edit.setText(value)
    # 获取 ：项目
    def uproject(self):
        return self.ui.uproject_line_edit.text()
    # 设置：项目
    def set_uproject(self, value):
        self.ui.uproject_line_edit.setText(value)
    # 获取：引擎目录
    def engine_dir(self):
        return self.ui.engine_dir_line_edit.text()
    # 设置：引擎目录
    def set_engine_dir(self, value):
        self.ui.engine_dir_line_edit.setText(value)

    # 设置：构架引擎
    def set_build_engine(self, value):
        self.ui.build_engine_checkbox.setChecked(value)

    # 获取：P4启用
    def p4_enabled(self):
        return self.ui.p4_group_box.isChecked()
    # 设置：P4启用
    def set_p4_enabled(self, enabled):
        self.ui.p4_group_box.setChecked(enabled)

    # 获取：P4项目路径
    def p4_project_path(self):
        return self.ui.p4_project_path_line_edit.text()
    # 设置：P4项目路径
    def set_p4_project_path(self, value):
        self.ui.p4_project_path_line_edit.setText(value)
    # 获取：P4引擎路径
    def p4_engine_path(self):
        return self.ui.p4_engine_path_line_edit.text()
    # 设置：P4引擎路径
    def set_p4_engine_path(self, value):
        self.ui.p4_engine_path_line_edit.setText(value)
    # 获取：源控制工作空间
    def source_control_workspace(self):
        return self.ui.source_control_workspace_line_edit.text()
    # 设置：源控制工作空间
    def set_source_control_workspace(self, value):
        self.ui.source_control_workspace_line_edit.setText(value)
    # 获取：地图路径
    def map_path(self):
        return self.ui.map_path_line_edit.text()
    # 设置：地图路径
    def set_map_path(self, value):
        self.ui.map_path_line_edit.setText(value)
    # 获取：地图筛选
    def map_filter(self):
        return self.ui.map_filter_line_edit.text()
    # 设置：地图筛选
    def set_map_filter(self, value):
        self.ui.map_filter_line_edit.setText(value)

    # OSC设置
    # OSC Settings
    # 设置：OSC服务端口
    def set_osc_server_port(self, port):
        self.ui.osc_server_port_line_edit.setText(str(port))
    # 设置：OSC客户端口
    def set_osc_client_port(self, port):
        self.ui.osc_client_port_line_edit.setText(str(port))

    # MU SERVER Settings
    # 获取：多用户设置
    def mu_server_name(self):
        return self.ui.mu_server_name_line_edit.text()
    # 设置：多用户设置
    def set_mu_server_name(self, value):
        self.ui.mu_server_name_line_edit.setText(value)
    # 获取：多用户命令行数组
    def mu_cmd_line_args(self):
        return self.ui.mu_cmd_line_args_line_edit.text()
    # 设置：多用户命令行数组
    def set_mu_cmd_line_args(self, value):
        self.ui.mu_cmd_line_args_line_edit.setText(value)
    
    # 获取 ：多用户自动启动状态值
    def mu_auto_launch(self):
        return self.ui.mu_auto_launch_check_box.isChecked()
    # 设置 ：多用户自动启动状态值
    def set_mu_auto_launch(self, value):
        self.ui.mu_auto_launch_check_box.setChecked(value)

    # 获取 ：多用户自动加入
    def mu_auto_join(self):
        return self.ui.mu_auto_join_check_box.isChecked()
    # 设置 ：多用户自动加入
    def set_mu_auto_join(self, value):
        self.ui.mu_auto_join_check_box.setChecked(value)
    # 获取：多用户清理历史
    def mu_clean_history(self):
        return self.ui.mu_clean_history_check_box.isChecked()
    # 设置：多用户清理历史
    def set_mu_clean_history(self, value):
        self.ui.mu_clean_history_check_box.setChecked(value)
    # 获取：多用户exe
    def mu_server_exe(self):
        return self.ui.muserver_exe_line_edit.text()
    # 设置：多用户exe
    def set_mu_server_exe(self, value):
        self.ui.muserver_exe_line_edit.setText(value)
    # 获取：多用户自动构建
    def mu_server_auto_build(self) -> bool:
        return self.ui.muserver_auto_build_check_box.isChecked()
    # 设置：多用户自动构建的值
    def set_mu_server_auto_build(self, value: bool):
        self.ui.muserver_auto_build_check_box.setChecked(value)


    # Devices 设备部分
    # 为插件添加分段
    def add_section_for_plugin(self, plugin_name, plugin_settings, device_settings):
        # 获取任意设备设置
        any_device_settings = any([device[1] for device in device_settings]) or any([device[2] for device in device_settings])
        # 为空就跳过
        if not any_device_settings:
            return # no settings to show

        # Create a group box per plugin
        # 为每个插件创建一个 Groupbox（也就是分组盒子）
        # 先注册了
        device_override_group_box = self._device_groupbox.setdefault(plugin_name, QtWidgets.QGroupBox())
        # 走的就是下面这些栏
        # 如果设备的重载分组盒子的父类为空
        if device_override_group_box.parent() is None:
            #设置标签
            device_override_group_box.setTitle(f'{plugin_name} Settings')
            #设置层级
            device_override_group_box.setLayout(QtWidgets.QVBoxLayout())
            # 设备覆盖层.添加部件() 这就是将列表添加的关键
            self.ui.device_override_layout.addWidget(device_override_group_box)

        # 插件布局 = 网格布局
        plugin_layout = QtWidgets.QFormLayout()
        # 设备覆盖 盒子 给一个网格布局
        device_override_group_box.layout().addLayout(plugin_layout)

        # add widgets for settings shared by all devices of a plugin
        # 为设置添加部件 所有共享小部件
        for setting in plugin_settings:
            if not setting.show_ui:
                continue
            #值的类别 = 
            value_type = type(setting.get_value())
            # 如果传入的值是列表
            if value_type is list:
                # 那就选择多选的 组合盒子
                self.create_device_setting_multiselect_combobox(setting, plugin_layout)
            elif len(setting.possible_values) > 0:
                # 创建设备设置 组合盒子
                self.create_device_setting_combobox(setting, plugin_layout)
            #如果值是 字符串 或者 整形
            elif value_type in [str, int]:
                # 创建 设备文本输入框  
                self.create_device_setting_line_edit(setting, plugin_layout)
            # 如果输入类型是 bool类型 就创建 复选盒子
            elif value_type == bool:
                self.create_device_setting_checkbox(setting, plugin_layout)

        # add widgets for settings and overrides of individual devices
        # 为 设置 和 覆盖的个别设备添加 小部件
        # 这里拿的是 设备设置中的 设备名 设置 覆盖
        for device_name, settings, overrides in device_settings:
            #组合盒子 
            group_box = QtWidgets.QGroupBox()
            group_box.setTitle(device_name)
            group_box.setLayout(QtWidgets.QVBoxLayout())
            #设备覆盖组合盒子添加添加.布局.这就是添加子布局
            device_override_group_box.layout().addWidget(group_box)
            
            #申明布局：布局方式：矩形布局
            layout = QtWidgets.QFormLayout()
            #添加布局：group盒子
            group_box.layout().addLayout(layout)

            # regular "instance" settings
            # 注册“实例”设置
            for setting in settings:
                # 如果设置.显示UI为假 跳出这个继续
                if not setting.show_ui:
                    continue
                # 值得类别 = 类型（根据设备名获取设置值）
                value_type = type(setting.get_value(device_name))
                # 如果 值的类别是列表
                if value_type is list:
                    self.create_device_setting_multiselect_combobox(setting, layout)
                # 长度（设置.可能的值）
                elif len(setting.possible_values) > 0:
                    self.create_device_setting_combobox(setting, layout)
                # 值的类别 如果是 字符串或者整形
                elif value_type in [str, int]:
                    self.create_device_setting_line_edit(setting, layout)
                # 如果值是bool类型
                elif value_type == bool:
                    self.create_device_setting_checkbox(setting, layout)
            # 遍历 覆盖里的设置 
            for setting in overrides:
                if not setting.show_ui:
                    continue
                # 获取值的类别
                value_type = type(setting.get_value(device_name))
                # 值的类别 如果是 字符串或者整形
                if value_type in [str, int]:
                    self.create_device_setting_override_line_edit(setting, device_name, layout)
                # 如果值是bool类型
                elif value_type == bool:
                    self.create_device_setting_override_checkbox(setting, device_name, layout)

    # 创建涉笔设置 多选项 组合框
    def create_device_setting_multiselect_combobox(self, setting, layout):
        # 设置标签名

        label = QtWidgets.QLabel()
        label.setText(setting.nice_name)
        # 组合框
        combo = sb_widgets.MultiSelectionComboBox()
        # 选定的值
        selected_values = setting.get_value()
        # 可能的值
        possible_values = setting.possible_values if len(setting.possible_values) > 0 else selected_values
        # 组合框：添加元素
        combo.add_items(selected_values, possible_values)
        # 层添加一个行两个对象（标签，组合框）
        layout.addRow(label, combo)
        #设置的工具提示
        if setting.tool_tip:
            # 标签 的提示
            label.setToolTip(setting.tool_tip)
            # 组合框 的提示
            combo.setToolTip(setting.tool_tip)
        # 组合框.信号 选择更改了（将当前值些到配置文件中）
        combo.signal_selection_changed.connect(lambda entries, setting=setting: setting.update_value(entries))

    # 有多种可能值时调用这个函数
    def create_device_setting_combobox(self, setting, layout):
        # 标签 定义一个标签
        label = QtWidgets.QLabel()
        label.setText(setting.nice_name)
        # 组合框 = switchbroad部件.无滚动类型
        combo = sb_widgets.NonScrollableComboBox()
        # 设置的可能值里 的值
        for value in setting.possible_values:
            combo.addItem(str(value), value)
        # 组合框 设置当前编号（组合框，查找数据从设置中获取的值）
        combo.setCurrentIndex(combo.findData(setting.get_value()))

        # update the widget if the setting changes, but only when the value is actually different (to avoid endless recursion)
        # 如果设置更改时 更新部件 ，但是仅当 值有不同时
        # this is useful for settings that will change their value based on the input of the widget of another setting
        # 这是一个有效的设置 它将更改他们的值 基于输入部件的其他设置
        def on_setting_changed(new_value, combo):
            # 如果当前文字 不等于 新的值
            if combo.currentText() != new_value:
                # 将组合框设置成当前值
                combo.setCurrentIndex(combo.findText(new_value))
        # 将新值和 久值添加到 设置中
        setting.signal_setting_changed.connect(lambda old, new, widget=combo: on_setting_changed(new, widget)) 
        # 添加行（标签，组合框）
        layout.addRow(label, combo)
        #设置提示文本
        if setting.tool_tip:
            label.setToolTip(setting.tool_tip)
            combo.setToolTip(setting.tool_tip)
        #文本更改时 将值更新到设置中
        combo.currentTextChanged.connect(lambda text, setting=setting: setting.update_value(text))

    #字符串 参数 路径筛选器 = （ndisplay配置文件：.cfg.ndisplay）
    _str_attr_path_filters = { 'ndisplay_cfg_file': 'nDisplay Config (*.cfg;*.ndisplay)' }
    def path_filter_for_setting(self, setting):
        # 返回 字符串参数筛选器[设置参数名] 如果 设置.参数名 在/
        return self._str_attr_path_filters[setting.attr_name] if setting.attr_name in self._str_attr_path_filters else None

    # 添加浏览按键
    def add_browse_button(self, layout, setting, filter_str):
        # 注册浏览按键
        browse_btn = QtWidgets.QPushButton('Browse')
        # 添加到部件中
        layout.addWidget(browse_btn)
        # 定义浏览事件
        def browse_clicked():
            start_path = str(Path.home())
            # 如果最后浏览路径 并且 系统路径存在（设置最后浏览路径）
            if SETTINGS.LAST_BROWSED_PATH and os.path.exists(SETTINGS.LAST_BROWSED_PATH):
                start_path = SETTINGS.LAST_BROWSED_PATH #路径赋值
            #文件路径 = 文件对话框获取 打开文件名（）
            file_path, _ = QtWidgets.QFileDialog.getOpenFileName(parent=self.ui, dir=start_path, filter=filter_str)
            #如果 长度（文件路径）大于0 系统路径存在
            if len(file_path) > 0 and os.path.exists(file_path):
                file_path = os.path.normpath(file_path)
                setting.update_value(file_path)
                # 设置.最后浏览路径 = 系统路径.目录名
                SETTINGS.LAST_BROWSED_PATH = os.path.dirname(file_path)
                # 保存设置
                SETTINGS.save()
        # 将按键点击连接到函数
        browse_btn.clicked.connect(browse_clicked)

    # 创建设备设置 文本输入框
    def create_device_setting_line_edit(self, setting, layout):
        #编辑_布局 = 水平盒子 
        edit_layout = QtWidgets.QHBoxLayout()
        #标签 
        label = QtWidgets.QLabel(setting.nice_name)
        # 文本输入框
        line_edit = QtWidgets.QLineEdit()
        #值
        value = setting.get_value()
        value_type = type(value)
        # 如果是整数 就转成 字符串
        if value_type == int:
            value = str(value)
        #文本编辑框 
        line_edit.setText(value)
        line_edit.setCursorPosition(0)
        edit_layout.addWidget(line_edit)
        #添加行
        layout.addRow(label, edit_layout)
        # 设置工具提示
        if setting.tool_tip:
            label.setToolTip(setting.tool_tip)
            line_edit.setToolTip(setting.tool_tip)
        #如果值是字符串
        if value_type == str:
            # 文本编辑器 ，编辑结束后 将这些值更新设置
            line_edit.editingFinished.connect(lambda field=line_edit, setting=setting: setting.update_value(field.text()))

            # If this setting is recognized as a path, add a "Browse" button.
            # 如果设置 认定为一个路径 就添加一浏览按键
            path_filter = self.path_filter_for_setting(setting)
            if path_filter:
                self.add_browse_button(edit_layout, setting, path_filter)
        # 如果值的类型 是整数
        elif value_type == int:
            # 定义 文本编辑整数_编辑结束（领域，设置）
            def le_int_editingFinished(field, setting):
                try:
                    #文本 = 区域文本
                    text = field.text()
                    # 设置 更新值
                    setting.update_value(int(text))
                except ValueError:
                    field.setText(str(setting.get_value()))
            # 文本编辑框 编辑结束 连接到 上面的函数
            line_edit.editingFinished.connect(lambda field=line_edit, setting=setting : le_int_editingFinished(field=line_edit, setting=setting))
        # 设置更改了
        def on_setting_changed(new_value, line_edit):
            # 如果 文本编辑框 不为新的值
            if line_edit.text() != new_value:
                line_edit.setText(str(new_value))
                line_edit.setCursorPosition(0)
        # 设置.信号设置更改连接到（新老设置 ，启用设置更改）
        setting.signal_setting_changed.connect(lambda old, new, widget=line_edit: on_setting_changed(new, widget))

    # 创建设备设置 复选盒子
    def create_device_setting_checkbox(self, setting, layout):
        # 注册盒子
        check_box = QtWidgets.QCheckBox()
        # 设置值
        check_box.setChecked(setting.get_value())
        # 添加行
        layout.addRow(f"{setting.nice_name}", check_box)
        # 工具提示
        if setting.tool_tip:
            check_box.setToolTip(setting.tool_tip)
        # 复选盒子在状态更改时，更新setting的值
        check_box.stateChanged.connect(lambda state, setting=setting: setting.update_value(bool(state)))

    # 创建设备设置 覆盖文本编辑
    def create_device_setting_override_line_edit(self, setting, device_name, layout):
        #标签
        label = QtWidgets.QLabel()
        label.setText(setting.nice_name)
        line_edit = QtWidgets.QLineEdit()
        # 如果 是覆盖类型
        if setting.is_overriden(device_name):
            sb_widgets.set_qt_property(line_edit, "override", True)
        #获取值  setting 是设置名
        value = setting.get_value(device_name)
        line_edit.setText(str(value))
        line_edit.setCursorPosition(0)
        #添加 布局
        layout.addRow(label, line_edit)
        # 设置工具提示
        if setting.tool_tip:
            label.setToolTip(setting.tool_tip)
            line_edit.setToolTip(setting.tool_tip)
        # 文本框 编辑结束之后
        line_edit.editingFinished.connect(lambda field=line_edit, setting=setting, device_name=device_name: self._on_line_edit_override_editingFinished(field, setting, device_name))
        # 基础值更改
        def on_base_value_changed(setting, device_name, line_edit):
            # 新的基础值 = 从设置选项获取而来 
            new_base_value = setting.get_value()
            # 如果 设置对象的.是否覆盖
            if not setting.is_overriden(device_name):
                line_edit.setText(str(new_base_value))      #设置新的值
                line_edit.setCursorPosition(0)              #设置当前鼠标位置
                # 如果 新的基础值 == 设置项中获取的值
                if new_base_value == setting.get_value(device_name):
                    # if the setting was overriden but the new base value happens to be the same as the override we can remove the override
                    # 如果 设置被覆盖了 但是 新的基础值与覆盖的值 我们能移除 覆盖值
                    sb_widgets.set_qt_property(line_edit, "override", False)
                    # 设置移除覆盖值（设备名）
                    setting.remove_override(device_name)
        # 设置.信号 设置 更改 。连接到 （老的值 新的值，设置，设备名，文本框）
        setting.signal_setting_changed.connect(lambda old, new, setting=setting, device_name=device_name, widget=line_edit: on_base_value_changed(setting, device_name, widget))

    # 文本编辑框 覆盖  编辑结束（部件，设置,设备名）
    def _on_line_edit_override_editingFinished(self, widget, setting, device_name):
        # 旧的值 = 从设置中获取的值
        old_value = setting.get_value(device_name)
        # 新的值 = 部件中获取的值
        new_value = widget.text()
        #  旧的值
        if type(old_value) == int:
            try:
                # 新的值 = 把新的值转整形
                new_value = int(new_value)
            except ValueError:
                # 新的值 = 设置.原来的值
                new_value = setting._original_value
        # 新的值 不等于 久的值
        if new_value != old_value:
            #让设置用新的值覆盖旧的值
            setting.override_value(device_name, new_value)
        # 如果 设置.是否覆盖（设备名）
        if setting.is_overriden(device_name):
            sb_widgets.set_qt_property(widget, "override", True)
        else:
            sb_widgets.set_qt_property(widget, "override", False)
            # 设置 移除覆盖
            setting.remove_override(device_name)

    # 创建设备设置 覆盖 复选盒子
    def create_device_setting_override_checkbox(self, setting, device_name, layout):
        # 注册复选盒子
        check_box = QtWidgets.QCheckBox()
        # 设置它的复选状态 
        check_box.setChecked(setting.get_value(device_name))
        # 设置.是否覆盖
        if setting.is_overriden(device_name):
            # 设置qt参数值（复选盒子，覆盖，为真）
            sb_widgets.set_qt_property(check_box, "override", True)
        # 布局。添加（“设置.好名字”，复选盒子）
        layout.addRow(f"{setting.nice_name}", check_box)
        # 如果 有 设置工具提示
        if setting.tool_tip:
            # 复选盒子
            check_box.setToolTip(setting.tool_tip)
        # 复选盒子 状态更改（状态 ，复选盒子，设置，设备名，启用复选盒子覆盖的状态更改）
        check_box.stateChanged.connect(lambda state, widget=check_box, setting=setting, device_name=device_name: self._on_checkbox_override_stateChanged(widget, setting, device_name))
        # 基础值更改（新的值，复选盒子）
        def on_base_value_changed(new_value, check_box):
            # 复选盒子 设置为新值
            check_box.setChecked(new_value)
            # reset checkbox override state, as the checkbox has only two states there is no override anymore when the base value changes
            # 重置 复选盒子状态，作为复选盒子仅有两种状态，这儿没有别的状态了。当基础值更改
            sb_widgets.set_qt_property(check_box, "override", False)
            setting.remove_override(device_name)    #设置 移除覆盖（设备名）
        #设置。信号_设置_更改。连接（旧值，新值，部件，基础值更改）
        setting.signal_setting_changed.connect(lambda old, new, widget=check_box: on_base_value_changed(new, widget))
   
    # 复选盒子 - 覆盖 - 状态更改
    def _on_checkbox_override_stateChanged(self, widget, setting, device_name):
        # 老的值 = 设置中 获取值
        old_value = setting.get_value(device_name)
        # 新的值 = 从部件获取的复选状态
        new_value = bool(widget.checkState())
        # 假如 新的值 不等于 旧的值
        if new_value != old_value:
            # 将设置的值覆盖掉
            setting.override_value(device_name, new_value)
        # 如果 设置中 是否被覆盖（设备名）
        if setting.is_overriden(device_name):
            # switchbroad 设置 qt参数 （部件 覆盖 为真）
            sb_widgets.set_qt_property(widget, "override", True)
        else:
            # switchbroad 设置 qt参数 （部件 覆盖 为假）
            sb_widgets.set_qt_property(widget, "override", False)
            setting.remove_override(device_name)
