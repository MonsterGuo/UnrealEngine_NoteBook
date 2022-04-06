# Copyright Epic Games, Inc. All Rights Reserved.
from switchboard.config import CONFIG

from PySide2 import QtCore, QtWidgets

import os

# 添加 配置对话框
class AddConfigDialog(QtWidgets.QDialog):
    # 初始化（样式表，项目搜索路径，预览引擎目录，父类）
    def __init__(self, stylesheet, uproject_search_path, previous_engine_dir, parent):
        # 继承自父类的对话框（点击关闭按钮）
        super().__init__(parent=parent, f=QtCore.Qt.WindowCloseButtonHint)

        self.config_name = None             # 配置名
        self.uproject = None                # 项目
        self.engine_dir = None              # 引擎目录

        self.setStyleSheet(stylesheet)      # 样式表

        self.setWindowTitle("Add new Switchboard Configuration")                    # 设置窗口标题
        #作为参数
        self.form_layout =  QtWidgets.QFormLayout()                                 # 网格布局
        self.name_line_edit = QtWidgets.QLineEdit()                                 # 配置名 文本编辑框
        self.name_line_edit.textChanged.connect(self.on_name_changed)               # 配置名 文本更改之后连接（名字更改）
        self.form_layout.addRow("Name", self.name_line_edit)                        # 矩形布局 添加行（名字，文本内容）

        self.uproject_line_edit = QtWidgets.QLineEdit()                             # 注册一个 项目编辑文本
        self.uproject_line_edit.textChanged.connect(self.on_uproject_changed)       # 项目编辑文本 更改（启用项目更改）
        self.uproject_browse_button = QtWidgets.QPushButton("Browse")               # 注册一个 项目浏览按键
        self.uproject_browse_button.clicked.connect(lambda: self.on_browse_uproject_path(uproject_search_path)) #将项目点击连接到（浏览项目路径）

        uproject_layout = QtWidgets.QHBoxLayout()                                   # 注册一个水平布局 的 项目布局
        uproject_layout.addWidget(self.uproject_line_edit)                          # 给 项目布局添加 文本编辑框部件
        uproject_layout.addWidget(self.uproject_browse_button)                      # 给 项目布局添加 项目浏览按键
        self.form_layout.addRow("uProject", uproject_layout)                        # 给布局添加行（项目 项目层）

        self.engine_dir_line_edit = QtWidgets.QLineEdit()                           # 注册 引擎目录编辑文本
        if os.path.exists(previous_engine_dir): # re-use previous engine dir        # 如果存在 预览引擎目录
            self.engine_dir_line_edit.setText(previous_engine_dir)                  # 引擎目录文本框设置文本（预览的引擎目录）
            self.engine_dir = previous_engine_dir                                   # 引擎目录= 预览引擎目录
        self.engine_dir_line_edit.textChanged.connect(self.on_engine_dir_changed)   # 引擎目录文本框.当文本更改（调用 应勤目录更改）
        self.engine_dir_browse_button = QtWidgets.QPushButton("Browse")             # 注册一个浏览引擎目录浏览按键（“浏览”）
        self.engine_dir_browse_button.clicked.connect(self.on_browse_engine_dir)    # 将引擎浏览按键点击绑定到 （浏览引擎目录）

        engine_dir_layout = QtWidgets.QHBoxLayout()                                 # 注册一个引擎目录布局  水平布局盒子
        engine_dir_layout.addWidget(self.engine_dir_line_edit)                      # 引擎目录布局.添加（引擎目录文本编辑框）
        engine_dir_layout.addWidget(self.engine_dir_browse_button)                  # 引擎目录布局.添加（引擎目录浏览按键）
        self.form_layout.addRow("Engine Dir", engine_dir_layout)                    # 布局添加一行（引擎目录，引擎目录层）

        layout = QtWidgets.QVBoxLayout()                                            # 新建一个布局 = 一个垂直盒子布局
        layout.insertLayout(0, self.form_layout)                                    # 将当前布局添加到（0，矩形布局）
        # 这里要作为一个局部变量所以要这么写
        self.p4_group = QtWidgets.QGroupBox("Perforce")                             # 注册一个 组合盒子（“perforce”）
        self.p4_group.setCheckable(True)                                            # 设置可复选
        self.p4_group.setChecked(bool(CONFIG.P4_ENABLED.get_value()))               # 设置复选（从配置中读取的值）

        self.p4_project_path_line_edit = QtWidgets.QLineEdit(CONFIG.P4_PROJECT_PATH.get_value())        # p4项目路径文本编辑框
        self.p4_engine_path_line_edit = QtWidgets.QLineEdit(CONFIG.P4_ENGINE_PATH.get_value())          # p4引擎路径文本编辑框
        self.p4_workspace_line_edit = QtWidgets.QLineEdit(CONFIG.SOURCE_CONTROL_WORKSPACE.get_value())  # p4工作空间文本编辑框
        p4_layout = QtWidgets.QFormLayout()                                                             # 注册一个p4的网格布局
        p4_layout.addRow("P4 Project Path", self.p4_project_path_line_edit)                             # 添加行（p4项目路径，）
        p4_layout.addRow("P4 Engine Path", self.p4_engine_path_line_edit)                               # 添加行（p4引擎路径，）
        p4_layout.addRow("Workspace Name", self.p4_workspace_line_edit)                                 # 添加行（工作空间名，）
        self.p4_group.setLayout(p4_layout)                                                              # 设置布局
        layout.addWidget(self.p4_group)                                                                 # 布局.添加部件（p4组合）

        # 按键盒子 = qt部件 对话框按键盒子 （对话按键 ok|对话按键 cancel）
        self.button_box = QtWidgets.QDialogButtonBox(QtWidgets.QDialogButtonBox.Ok | QtWidgets.QDialogButtonBox.Cancel)
        self.button_box.button(QtWidgets.QDialogButtonBox.Ok).setEnabled(False)                         # 日志按键盒子ok.设置启用（假）
        self.button_box.accepted.connect(self.accept)                                                   # 接受.连接到（接受）
        self.button_box.rejected.connect(self.reject)                                                   # 拒绝.连接到 (拒绝)
        layout.addWidget(self.button_box)                                                               # 布局.添加部件（按键盒子）

        self.setLayout(layout)                                                                          #设置布局（布局）

        self.setMinimumWidth(450)
    # 定义 p4设置
    def p4_settings(self):
        settings = {}                                                                                                   # 申请一个数组
        settings['p4_enabled'] = self.p4_group.isChecked()                                                              # p4是否启用
        settings['p4_workspace_name'] = self.p4_workspace_line_edit.text() if self.p4_group.isChecked() else None       # p4的工作空间
        settings['p4_project_path'] = self.p4_project_path_line_edit.text() if self.p4_group.isChecked() else None      # p4项目名
        settings['p4_engine_path'] = self.p4_engine_path_line_edit.text() if self.p4_group.isChecked() else None        # p4引擎路径
        return settings

    # 名字更改
    def on_name_changed(self, text):           
        self.config_name = text
        self.update_button_box()
    # 项目更改
    def on_uproject_changed(self, text):
        self.uproject = os.path.normpath(text)
        self.update_button_box()
    # 浏览项目路径
    def on_browse_uproject_path(self, uproject_search_path):
        self.uproject, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Select uProject file", self.engine_dir, "uProject (*.uproject)")
        self.uproject = os.path.normpath(self.uproject)
        self.uproject_line_edit.setText(self.uproject)      # 更新文本框
    # 引擎目录更改
    def on_engine_dir_changed(self, text):
        self.engine_dir = os.path.normpath(text)
        self.update_button_box()
    # 引擎浏览按键点击触发
    def on_browse_engine_dir(self):
        self.engine_dir = QtWidgets.QFileDialog.getExistingDirectory(self, "Select UE4 engine directory")
        self.engine_dir = os.path.normpath(self.engine_dir)
        self.engine_dir_line_edit.setText(self.engine_dir)
    # 更新按键盒子
    def update_button_box(self):
        # 按键盒子.按键（日志按键ok）,设置为禁用
        self.button_box.button(QtWidgets.QDialogButtonBox.Ok).setEnabled(False)
        # 如果 配置名 和 项目名 和 引擎目录 都有值
        if self.config_name and self.uproject and self.engine_dir:
            # 如果项目路径 和引擎路径 都存在
            if os.path.exists(self.uproject) and os.path.exists(self.engine_dir):
                # 就把 按键盒子设置成 启用
                self.button_box.button(QtWidgets.QDialogButtonBox.Ok).setEnabled(True)
