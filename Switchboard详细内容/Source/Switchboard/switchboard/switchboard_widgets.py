# Copyright Epic Games, Inc. All Rights Reserved.
from PySide2 import QtCore, QtGui, QtWidgets
import time

DEVICE_LIST_WIDGET_HEIGHT = 54                      #设备列表部件高度
DEVICE_HEADER_LIST_WIDGET_HEIGHT = 40               #设备头部列表高度
DEVICE_WIDGET_HIDE_IP_ADDRESS_WIDTH = 500           #设备部件隐藏ip地址宽度

# 没有可滚动折叠盒子
class NonScrollableComboBox(QtWidgets.QComboBox):
    # 初始化
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.installEventFilter(self)
    # 事件筛选器
    def eventFilter(self, obj, event):
        # 如果 对象 = 自己 并且 事件类型 == 鼠标滚轮事件
        if obj == self and event.type() == QtCore.QEvent.Wheel:
            event.ignore() #事件忽略
            return True
        return False


# Each entry has a checkbox, the first element is a lineedit that will show all selected entries
# 每一个选项都有一个 checkbox ，第一个元素是一个文本编辑框 那个将会显示所有选项
class MultiSelectionComboBox(QtWidgets.QComboBox):
    #分割符
    separator = ' | '
    # 信号 选择 更改了
    signal_selection_changed = QtCore.Signal(list)
    # 初始化
    def __init__(self, parent=None):
        #超级初始化
        super().__init__(parent=parent)
        # 模块.元素更改.连接（状态更改）
        self.model().itemChanged.connect(self.on_stateChanged)
        # an editable combo has a lineedit at the first entry which we can use to show a list of all selected entries
        self.setEditable(True)
        super().addItem("")
        item = self.model().item(0, 0)
        item.setEnabled(False)
        # we only care about the editablilty as a means to get a lineedit, the user isn't allowed to change the text manually
        # 我们只关心可编辑性作为获得lineedit的一种方式，用户不允许手动更改文本
        self.lineEdit().installEventFilter(self)        #安装事件筛选器
        self.lineEdit().setReadOnly(True)               #设置为只读
        # disallow text selection
        # 禁用 文本选项
        # 可编辑文本.选择更改了.连接（文本编辑框，设置跳转的行前）
        self.lineEdit().selectionChanged.connect(lambda: self.lineEdit().setSelection(0, 0))
        
        # 弹出显示
        self.popup_is_showing = False
        # the combo calls show/hidePopup internally, to avoid messing up the state we only allow showing/hiding the popup
        # 组合调用show/hidePopup内部，为了避免搞乱状态，我们只允许显示/隐藏弹出
        # if it happened inside a time intervall that could have reasonably been triggered by a user.
        # 如果它发生在一个可能由用户合理触发的时间间隔内。
        # this is obviously a workaround but there seems to be no way to get better behavior w/o implementing a full-blown combobox.
        # 这显然是一个解决方案，但似乎没有办法得到更好的行为，没有实现一个成熟的组合框。
        # 最后 一次弹出 被 触发 = 当前时间
        self.last_time_popup_was_triggered = time.time()
    
    # 添加选项（选中选项，所有选项）
    def add_items(self, selected_entries, all_entries):
        # 所有选项中的选项
        for entry in all_entries:
            self.addItem(entry)                                                                 #添加选项
            item = self.model().item(self.count()-1, 0)                                         #元素 = 模块.选项（数目-1，0）
            item.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)              #设置标识（可复选，可启用）
            state = QtCore.Qt.Checked if entry in selected_entries else QtCore.Qt.Unchecked     #状态 = 选项在选中的里面就勾选启用
            item.setCheckState(state)                                                           #设置复选状态
        #无效条目 = 如果所有选中条目 不在 所有条目之中 就是无效条目
        invalid_entries = [entry for entry in selected_entries if entry not in all_entries]
        for entry in invalid_entries:
            self.addItem(entry)                                                                 #添加选项
            item = self.model().item(self.count()-1, 0)                                         #元素 = 模块.选项（数目-1，0）
            item.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)              #设置标识（可复选，可启用）
            state = QtCore.Qt.Checked                                                           #选中
            item.setCheckState(state)                                                           #设置复选状态

            brush = item.foreground()                                                           #刷用做前景
            brush.setColor(QtCore.Qt.red)                                                       #设置成红色
            item.setForeground(brush)                                                           #设置前景
    # 事件筛选
    def eventFilter(self, obj, event):
        # 文本编辑框 并且 鼠标按键按下
        if obj == self.lineEdit() and event.type() == QtCore.QEvent.MouseButtonPress:
            # if the lineedit is clicked we want the combo to open/close
            # 弹出显示？
            if self.popup_is_showing:
                self.hidePopup()        #隐藏
            else:
                self.showPopup()        #显示
            event.accept()              #事件接受
            return True
        # 如果对象是自己 并且 事件类型 鼠标滚轮
        elif obj == self and event.type() == QtCore.QEvent.Wheel:
            event.ignore()              #忽略
            return True
        return False
    # 滚轮事件
    def wheelEvent(self, event):
        event.ignore()                  #忽略
        return True

    # 显示弹出
    def showPopup(self):
        # 当前时间
        now = time.time()
        # 时间差 = （当前时间- 最后弹出时间的差值）
        diff = abs(now - self.last_time_popup_was_triggered)
        # 如果 时间差 大于 0.1
        if diff > 0.1:
            #调用父类的弹出
            super().showPopup()
            #弹出是否显示 改为真
            self.popup_is_showing = True
            #最后弹出时间为现在
            self.last_time_popup_was_triggered = now

    def hidePopup(self):
        # 当前时间
        now = time.time()
        # 时间差 = （当前时间- 最后弹出时间的差值）
        diff = abs(now - self.last_time_popup_was_triggered)
        # 如果 时间差 大于 0.1
        if diff > 0.1:
             #调用父类的隐藏
            super().hidePopup()
            #弹出是否显示 改为假
            self.popup_is_showing = False
            #最后弹出时间为现在
            self.last_time_popup_was_triggered = now
    # 状态更改
    def on_stateChanged(self, item):
        # 清理编辑文本
        self.clearEditText()
        # 选择选项
        selected_entries = []
        # 范围内（自己的数目）
        for i in range(self.count()):
            #选项 = 模块元素
            item = self.model().item(i, 0)
            # 如果 选项.复选状态 = 复选中了
            if item.checkState() == QtCore.Qt.Checked:
                #选择的选项.添加（元素文本）
                selected_entries.append(self.itemText(i))
        # 长度（选中选项）
        if len(selected_entries) > 0:
            #设置可编辑文本（自己的分割符，加入选中的选项）
            self.setEditText(self.separator.join(selected_entries))
        #信号选择更改.发送
        self.signal_selection_changed.emit(selected_entries)

# 控制弹出按键
class ControlQPushButton(QtWidgets.QPushButton):
    # 初始化
    def __init__(self, parent=None):
        # 继承自父类
        super().__init__(parent)
    # 聚焦事件
    def focusInEvent(self, e):
        # 继承自父类
        super().focusInEvent(e)
    # 进入事件
    def enterEvent(self, event):
        # 继承自父类
        super().enterEvent(event)
        # 聚焦
        self.setFocus() 
    # 离开事件
    def leaveEvent(self, event):
        # 继承自父类
        super().leaveEvent(event)
        # 清除聚焦
        self.clearFocus()
    # 类的方法 ：创建（图标关，图标开，图标覆盖,图标覆盖，图标禁用，图标禁用，图标尺寸，能否复选，复选值，工具提示）
    @classmethod
    def create(self, icon_off, icon_on=None,
                icon_hover_on=None, icon_hover=None,
                icon_disabled_on=None, icon_disabled=None,
                icon_size=None,
                checkable=True, checked=False,
                tool_tip=None, parent=True):
        # 按键 = 控制 pushbutton
        button = ControlQPushButton()
        # 设置参数（没有背景）
        button.setProperty("no_background", True)
        # 设置样式
        button.setStyle(button.style())
        # 图标
        icon = QtGui.QIcon()
        # 图标开
        if icon_on:
            pixmap = QtGui.QPixmap(icon_on)
            # 图标：正常 图标:开
            icon.addPixmap(pixmap, QtGui.QIcon.Normal, QtGui.QIcon.On)

        if icon_hover:
            pixmap = QtGui.QPixmap(icon_hover)
            # 图标：激活 图标:关
            icon.addPixmap(pixmap, QtGui.QIcon.Active, QtGui.QIcon.Off)

        if icon_hover_on:
            pixmap = QtGui.QPixmap(icon_hover_on)
            # 图标：激活 图标:开
            icon.addPixmap(pixmap, QtGui.QIcon.Active, QtGui.QIcon.On)

        if icon_disabled:
            pixmap = QtGui.QPixmap(icon_disabled)
            # 图标：禁用 图标:关
            icon.addPixmap(pixmap, QtGui.QIcon.Disabled, QtGui.QIcon.Off)

        if icon_disabled_on:
            pixmap = QtGui.QPixmap(icon_disabled)
            # 图标：禁用 图标:开
            icon.addPixmap(pixmap, QtGui.QIcon.Disabled, QtGui.QIcon.On)

        # 默认状态
        pixmap = QtGui.QPixmap(icon_off)
        # 图标:正常 图标:关
        icon.addPixmap(pixmap, QtGui.QIcon.Normal, QtGui.QIcon.Off)
        # 按键.设置图标
        button.setIcon(icon)
        # 如果没有 给 图标尺寸
        if not icon_size:
            # 图标尺寸 = 矩形尺寸
            icon_size = pixmap.rect().size()
        # 按键 设置图标尺寸
        button.setIconSize(icon_size)
        # 按键 设置最小尺寸
        button.setMinimumSize(QtCore.QSize(25, 35))
        # 如果没工作提示
        if tool_tip:
            # 按键设置工具提示
            button.setToolTip(tool_tip)
        # 复选
        if checkable:
            #按键 设置可否复选框
            button.setCheckable(checkable)
            # 按键 设置复选值
            button.setChecked(checked)

        return button

# 无边框 编辑文本
class FramelessQLineEdit(QtWidgets.QLineEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
        # 如果 不是只读
        if not self.isReadOnly():
            # 设置参数 （无边框）
            self.setProperty("frameless", True)
            self.setStyle(self.style())
        # 当前文本
        self.current_text = None
        # 是否有值
        self.is_valid = True
    #进入事件
    def enterEvent(self, event):
        super().enterEvent(event)
        # 如果 不是只读
        if not self.isReadOnly():
            # 设置qt参数（无边框 为假）
            set_qt_property(self, "frameless", False)
    
    # 离开事件
    def leaveEvent(self, event):
        super().leaveEvent(event)
        # 已经聚焦
        if self.hasFocus():
            return
        # 如果 不是只读
        if not self.isReadOnly():
            # 设置qt参数（无边框 为真）
            set_qt_property(self, "frameless", True)
    
    # 聚焦进入事件
    def focusInEvent(self, e):
        super().focusInEvent(e)
        # 存储当前值
        # Store the current value
        self.current_text = self.text()
        # 如果 不是只读
        if not self.isReadOnly():
            # 设置qt参数（无边框 为假）
            set_qt_property(self, "frameless", False)

    # 聚焦离开事件
    def focusOutEvent(self, e):
        super().focusOutEvent(e)
        # 如果 不是只读
        if not self.isReadOnly():
            # 设置qt参数（无边框 为真）
            set_qt_property(self, "frameless", True)
        # 如果 不是 是否有值
        if not self.is_valid:
            # 设置文本（当前文本）
            self.setText(self.current_text)
            # 是否有值设置成真
            self.is_valid = True
            # 设置qt参数（错误 假）
            set_qt_property(self, "error", False)
    # 键按下事件
    def keyPressEvent(self, e):
        super().keyPressEvent(e)
        # Key_Enter是小键盘的确认键，Key_Return是大键盘的回车键
        if e.key() == QtCore.Qt.Key_Return or e.key() == QtCore.Qt.Key_Enter:
            if self.is_valid:                   # 如果有值
                self.clearFocus()               # 清除聚焦
        # 如果按的是Esc键
        elif e.key() == QtCore.Qt.Key_Escape:   
            self.setText(self.current_text)     #设置文本（当前文本）
            self.clearFocus()                   #清除聚焦

# 设置Qt参数（部件名，参数，值）
def set_qt_property(widget, prop, value):
    widget.setProperty(prop, value)             #设置参数
    widget.setStyle(widget.style())             #设置样式
