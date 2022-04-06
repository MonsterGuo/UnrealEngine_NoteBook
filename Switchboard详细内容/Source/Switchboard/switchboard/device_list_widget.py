# Copyright Epic Games, Inc. All Rights Reserved.

from switchboard.devices.device_base import DeviceStatus, PluginHeaderWidgets
import switchboard.switchboard_widgets as sb_widgets

from PySide2 import QtCore, QtGui, QtWidgets

# 设备列表部件
class DeviceListWidget(QtWidgets.QListWidget):
    # 注册设备部件的信号 
    signal_register_device_widget = QtCore.Signal(object)
    # 移除设备的信号
    signal_remove_device = QtCore.Signal(object)
    # 连接所有插件设备的开关 信号
    signal_connect_all_plugin_devices_toggled = QtCore.Signal(str, bool)
    # 打开所有插件设备的开关 信号
    signal_open_all_plugin_devices_toggled = QtCore.Signal(str, bool)
    # 初始化
    def __init__(self, name, parent=None):
        super().__init__(parent)
        # 设置编辑触发（不编辑触发）
        self.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        # 设置聚焦策略（不聚焦）
        self.setFocusPolicy(QtCore.Qt.NoFocus)
        #self.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        # 设置选择模式（多选）
        self.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        # 设备部件（私有的）
        self._device_widgets = {}
        # 类名的数据头
        self._header_by_category_name = {}
        self.setMinimumSize(self.minimumSize().width(), 5)

    # Override all mouse events so that selection can be used for qss styling
    # 覆盖所有鼠标事件选项 能使用qss样式
    # 鼠标按下事件
    def mousePressEvent(self, e):
        pass
    # 鼠标释放事件
    def mouseReleaseEvent(self, e):
        pass
    # 鼠标双击事件
    def mouseDoubleClickEvent(self, e):
        pass
    # 鼠标移动事件 
    def mouseMoveEvent(self, e):
        pass
    # 关联菜单事件
    def contextMenuEvent(self, event):
        # 注册一个菜单对象
        device_context_menu = QtWidgets.QMenu(self)
        # 关联菜单.添加操作（请求确认设备删除）
        device_context_menu.addAction("Remove Device", lambda: self.ask_to_confirm_device_removal(event.pos()))
        # 关联菜单.执行（事件.全局位置）
        device_context_menu.exec_(event.globalPos())
        # 事件接受
        event.accept()

    # 请求确认设备移除
    def ask_to_confirm_device_removal(self, pos):
        # 元素 = 元素所在位置（）
        item = self.itemAt(pos)
        # 元素部件
        item_widget = self.itemWidget(item)
        # 确认 = qt部件.消息盒子.问题（设备移除确认,你是否想要删除设备）
        confirmation = QtWidgets.QMessageBox.question(self, "Device Removal Confirmation", "Are you sure you want to delete this device?")
        # 确认信息 == Qt部件.消息.YES
        if confirmation == QtWidgets.QMessageBox.Yes:
            # 信号移除设备.发送（元素部件.设备Hash值）
            self.signal_remove_device.emit(item_widget.device_hash)
    # 设备类别
    def devices_in_category(self, category):
        # 头部项 = 通过类别名获取类
        header_item = self._header_by_category_name[category]
        # 头部行 = 行（头部项）
        header_row = self.row(header_item)
        # 设备部件
        device_widgets = []
        # 
        for row in range(header_row+1, self.count()):
            # 部件 = 元素部件
            widget = self.itemWidget(self.item(row))
            # 如果 部件类别 = 设备部件的头部
            if type(widget) == DeviceWidgetHeader:
                break
            # 就向设备部件中添加 当前部件
            device_widgets.append(widget)
        return device_widgets

    # 设备移除
    def on_device_removed(self, device_hash, device_type, *args):
        # 设备部件从栈顶弹出
        self._device_widgets.pop(device_hash)
        # 设备部件的数目遍历
        for i in range(self.count()):
            item = self.item(i)
            # 部件的部件
            widget = self.itemWidget(item)
            # 假如这个设备的hash = 设备hash
            if widget.device_hash == device_hash:

                self.takeItem(self.row(item))
                break
        # 类别 = 设备类别
        category = device_type
        # 保存的设备在设备类别中
        remaining_devices_in_category = self.devices_in_category(category)
        # 如果当前设备类型的余量为0
        if len(remaining_devices_in_category) == 0:
            #元素抬头 = 本地的 头部类别名（类型）
            header_item = self._header_by_category_name[category]
            # 从列表中移除
            self.takeItem(self.row(header_item))
            # 从 本地数组中移除
            self._header_by_category_name.pop(category)

    # 连接所有开关
    def on_connect_all_toggled(self, plugin_name, state):
        # 连接所有插件设备的开关信号 发送（插件名，状态）
        self.signal_connect_all_plugin_devices_toggled.emit(plugin_name, state)
    # 打开所有开关
    def on_open_all_toggled(self, plugin_name, state):
        # 连接所有插件设备的开关信号 发送（插件名）
        self.signal_connect_all_plugin_devices_toggled.emit(plugin_name, state)     

    # 添加页眉（标签名，显示按键，显示连接按键，显示更改列表）
    def add_header(self, label_name, show_open_button, show_connect_button, show_changelist):
        # 页面部件 = 设备部件页眉（标签名，显示打开按键，显示连接按键，显示更改列表）
        header_widget = DeviceWidgetHeader(label_name, show_open_button, show_connect_button, show_changelist)
        # 页眉部件.信号连接所有按键.连接（信号连接所有插件设备开关）
        header_widget.signal_connect_all_toggled.connect(self.signal_connect_all_plugin_devices_toggled)
        # 页眉部件.信号打开所有按键.连接（信号打开所有插件设备开关）
        header_widget.signal_open_all_toggled.connect(self.signal_open_all_plugin_devices_toggled)
        # 设备项 = 注册一个qt列表部件
        device_item = QtWidgets.QListWidgetItem()
        # 页眉 元素的尺寸 = （页眉部件.缺省大小.宽  sb部件中.设备页眉列表宽度高度）
        header_item_size = QtCore.QSize(header_widget.sizeHint().width(), sb_widgets.DEVICE_HEADER_LIST_WIDGET_HEIGHT)
        # 设备项.设置缺省大小
        device_item.setSizeHint(header_item_size)
        # 添加项
        self.addItem(device_item)
        # 设置项部件 （设备项，页眉部件）
        self.setItemWidget(device_item, header_widget)
        # 设备项
        return device_item

    # 添加设备部件
    def add_device_widget(self, device):
        # 类别获取
        category = device.category_name
        # 如果 通过类别名获取的页眉的键值中没有找到 类
        if category not in self._header_by_category_name.keys():
            # 页眉部件配置  = 设备.插件页眉部件配置
            header_widget_config = device.plugin_header_widget_config()
            # 显示打开按键 = 插件的页眉部件.打开按键 在 页眉部件的配置
            show_open_button = PluginHeaderWidgets.OPEN_BUTTON in header_widget_config
            # 显示连接按键 = 插件的页眉部件.连接按键 在 页眉部件的配置
            show_connect_button = PluginHeaderWidgets.CONNECT_BUTTON in header_widget_config
            # 显示更改列表 = 插件的页眉部件.更改标签 在 页眉部件的配置
            show_changelist = PluginHeaderWidgets.CHANGELIST_LABEL in header_widget_config
            # 类别名的页眉【类别】 = 添加页眉（类被，显示打开按键，显示连接按键，显示更改列表）
            self._header_by_category_name[category] = self.add_header(category, show_open_button, show_connect_button, show_changelist)

        # 页眉项 = 类别名页眉【类别】
        header_item = self._header_by_category_name[category]
        # 页眉行 = 行（页眉项）
        header_row = self.row(header_item)

        # 设备项 = 列表部件项
        device_item = QtWidgets.QListWidgetItem()
        # 设备项的尺寸
        device_item_size = QtCore.QSize(device.widget.sizeHint().width(), sb_widgets.DEVICE_LIST_WIDGET_HEIGHT)
        # 省略尺寸
        device_item.setSizeHint(device_item_size)
        # 插入项
        self.insertItem(header_row+1, device_item)
        # 设置项部件
        self.setItemWidget(device_item, device.widget)

        # Keep a dict for quick lookup
        # 保留一个磁盘用于快速浏览
        self._device_widgets[device.device_hash] = device.widget
        # 信号注册设备部件.发送（设备.部件）
        self.signal_register_device_widget.emit(device.widget)
        # force the widget to update, to make sure status is correct
        # 设备部件.更新状态
        device.widget.update_status(device.status, device.status)

        return device.widget

    # 清理部件
    def clear_widgets(self):
        self.clear()                                # 清空
        self._device_widgets = {}                   # 设备部件清空
        self._header_by_category_name = {}          # 类别页眉清空

    # 设备的 部件项
    def widget_item_by_device(self, device):
        # 自己的部件数目
        for i in range(self.count()):
            # 获取项
            item = self.item(i)
            # 获取部件
            widget = self.itemWidget(item)
            # 部件为空跳过 
            if not widget:
                continue
            # 部件的设备hash值 == 设备的hash值
            if widget.device_hash == device.device_hash:
                return item #返回项
        return None

    # 通过hash 拿到 设备部件
    def device_widget_by_hash(self, device_hash):
        if device_hash not in self._device_widgets:
            return None

        return self._device_widgets[device_hash]

    # 设备部件
    def device_widgets(self):
        return self._device_widgets.values()

    # 更新类别状态
    def update_category_status(self, category_name, devices):
        # 任意连接了
        any_connected = False
        # 任意打开了
        any_opened = False
        # 遍历所有设备的状态
        for device in devices:
            any_connected |= (device.status != DeviceStatus.DISCONNECTED)
            any_opened |= (device.status > DeviceStatus.CLOSED)
        #获取页眉项 = 根据项来
        header_item = self._header_by_category_name[category_name]
        header_widget = self.itemWidget(header_item)
        header_widget.update_connection_state(any_connected)                #更新连接状态
        header_widget.update_opened_state(any_connected, any_opened)        #更新打开状态

# 设备部件的页眉
class DeviceWidgetHeader(QtWidgets.QWidget):
    # 连接所有开关信号
    signal_connect_all_toggled = QtCore.Signal(str, bool) # params: plugin_name, toggle_state
    # 打开所有的开关信号
    signal_open_all_toggled = QtCore.Signal(str, bool) # params: plugin_name, toggle_state
    # 初始化（名称 显示打开按键，显示连接按键，显示更改列表）
    def __init__(self, name, show_open_button, show_connect_button, show_changelist, parent=None):
        super().__init__(parent)

        self.name = name                                    # 名字
        self.ip_address_label = None                        # Ip地址标签
        self.device_hash = 0 # When list widget is looking for devices it checks the device_has # 设备hash值

        self.layout = QtWidgets.QHBoxLayout()               # 定义一个布局 水平布局的盒子
        self.layout.setContentsMargins(0, 6, 17, 6)         # 设置边距
        self.setLayout(self.layout)                         # 设置布局
        
        # 定义本地函数标签
        def __label(label_text):                    
            label = QtWidgets.QLabel()                      # 定义个标签
            label.setText(label_text)                       # 设置标签文本
            label.setAlignment(QtCore.Qt.AlignCenter)       # 设置对齐方式
            label.setStyleSheet("font-weight: bold")        # 设置样式表
            return label

        self.name_label = __label(self.name + " Devices")                                   # 名称标签
        self.ip_address_label = __label('IP Address')                                       # ip地址
        self.changelist_label = __label('Changelist') if show_changelist else None          # 更改列表（必须得有这个选项）
        self.layout.addWidget(self.name_label)                                              # 添加部件
        self.layout.addWidget(self.ip_address_label)                                        # 添加部件
        # 添加分割符
        spacer = QtWidgets.QSpacerItem(0, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        # 分割符添加到布局
        self.layout.addItem(spacer)
        # 如果有更改列表
        if self.changelist_label:
            #添加 更改列表布局
            self.layout.addWidget(self.changelist_label)
            spacer = QtWidgets.QSpacerItem(0, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            # 分割符添加到布局
            self.layout.addItem(spacer)
        
        # 打开按钮
        self.open_button = None
        # 如果显示打开按键
        if show_open_button:
            # 定义打开时的图片
            self.open_button = sb_widgets.ControlQPushButton.create(':/icons/images/icon_open.png',
                                                        icon_hover=':/icons/images/icon_open_hover.png',
                                                        icon_disabled=':/icons/images/icon_open_disabled.png',
                                                        icon_on=':/icons/images/icon_close.png',
                                                        icon_hover_on=':/icons/images/icon_close_hover.png',
                                                        icon_disabled_on=':/icons/images/icon_close_disabled.png',
                                                        tool_tip=f'Start all connected {self.name} devices')
            self.layout.setAlignment(self.open_button, QtCore.Qt.AlignVCenter)                          # 居中对齐
            self.open_button.clicked.connect(self.on_open_button_clicked)                               # 按键连接事件
            self.open_button.setEnabled(False)                                                          # 启用？
            self.layout.addWidget(self.open_button)                                                     # 向布局中添加

        # 连接按键
        self.connect_button = None
        # 如果显示连接按键
        if show_connect_button:
            # 设置连接按键的图片
            self.connect_button = sb_widgets.ControlQPushButton.create(':/icons/images/icon_connect.png',
                                                            icon_hover=':/icons/images/icon_connect_hover.png',
                                                            icon_disabled=':/icons/images/icon_connect_disabled.png',
                                                            icon_on=':/icons/images/icon_connected.png',
                                                            icon_hover_on=':/icons/images/icon_connected_hover.png',
                                                            icon_disabled_on=':/icons/images/icon_connected_disabled.png',
                                                            tool_tip=f'Connect all {self.name} devices')
            self.layout.setAlignment(self.connect_button, QtCore.Qt.AlignVCenter)                       # 居中对齐
            self.connect_button.clicked.connect(self.on_connect_button_clicked)                         # 按键连接事件
            self.layout.addWidget(self.connect_button)                                                  # 向布局中添加

        self.name_label.setMinimumSize(QtCore.QSize(235, 0))                                            # 设置名字标签最小尺寸是（长235，0）
        self.ip_address_label.setMinimumSize(QtCore.QSize(100, 0))                                      # 设置Ip地址标签最小尺寸（长100，0）

    # 显示事件
    def showEvent(self, event):
        super().showEvent(event)
        # 查找ip地址标签
        self.find_ip_address_label()

    # 查找ip地址标签
    def find_ip_address_label(self):
        labels = self.findChildren(QtWidgets.QLabel)            #查找子标签
        for label in labels:                                    # 遍历标签
            if label.text() == 'IP Address':                    # 如果文本是 IP Address
                self.ip_address_label = label
                return
    # 缩放事件
    def resizeEvent(self, event):
        super().resizeEvent(event)
        # 如果不是IP地址标签 就返回
        if not self.ip_address_label:
            return
        # 更改宽尺寸
        width = event.size().width()
        # 宽小于 sb部件的设备宽度隐藏IP地址
        if width < sb_widgets.DEVICE_WIDGET_HIDE_IP_ADDRESS_WIDTH:
            self.ip_address_label.hide()        # 隐藏
        else:
            self.ip_address_label.show()        #显示

    # 绘制事件
    def paintEvent(self, event):
        opt = QtWidgets.QStyleOption()                                                  #样式
        opt.initFrom(self)                                                              # 
        painter = QtGui.QPainter(self)                                                  # 绘制器
        self.style().drawPrimitive(QtWidgets.QStyle.PE_Widget, opt, painter, self)      # 

    # 打开按键点击
    def on_open_button_clicked(self, checked):
        button_state = checked                                                          # 按键状态 = 勾选状态
        plugin_name = self.name                                                         # 插件名 = 自己的名字
        self.signal_open_all_toggled.emit(plugin_name, button_state)                    # 打开所有的信号 ：发送

    # 连接按键点击
    def on_connect_button_clicked(self, checked):
        button_state = checked                                                          # 按键状态 = 勾选状态
        plugin_name = self.name                                                         # 插件名 = 自己的名字
        self.signal_connect_all_toggled.emit(plugin_name, button_state)                 # 连接所有的信号 ：发送

    # 更新连接状态
    def update_connection_state(self, any_devices_connected):
        # 连接状态为空 就返回
        if self.connect_button is None:
            return
        # 连接按键：设置复选（任意设备的连接）
        self.connect_button.setChecked(any_devices_connected)
        # 如果有任意设备连接
        if any_devices_connected:
            # 设置连接按键的提示文本（）
            self.connect_button.setToolTip(f"Disconnect all connected {self.name} devices")
        else:
            # 设置连接按键的提示文本（）
            self.connect_button.setToolTip(f"Connect all {self.name} devices")

    # 更新打开状态（任意设备的连接状态，任意设备打开状态）
    def update_opened_state(self, any_devices_connected, any_devices_opened):
        # 如果打开按键不存在 就直接返回
        if self.open_button is None:
            return
        # 打开按键 设置启用（任意设备连接了）
        self.open_button.setEnabled(any_devices_connected)
        # 打开按键 设置复选（任意设备打开了）
        self.open_button.setChecked(any_devices_opened)
        # 如果 任意设备打开了
        if any_devices_opened:
            # 打开按键的提示文本
            self.open_button.setToolTip(f"Stop all running {self.name} devices")
        else:
            # 打开按键的提示文本
            self.open_button.setToolTip(f"Start all connected {self.name} devices")
