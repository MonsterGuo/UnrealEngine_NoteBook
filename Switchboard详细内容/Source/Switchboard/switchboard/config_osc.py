# Copyright Epic Games, Inc. All Rights Reserved.
# UE4 启动
UE4_LAUNCH = '/UE4Launch'                                       # ue4启动器
UE4_LAUNCH_QUERY = '/UE4LaunchQuery'                            # ue4启动查询
UE4_LAUNCH_CONFIRM = '/UE4LaunchConfirm'                        # ue4启动确认

# Mobile 手机
BATTERY = '/Battery'                                            # 电池
BATTERY_QUERY = '/BatteryQuery'                                 # 电池查询
THERMALS = '/Thermals'                                          # 温度
THERMALS_QUERY = '/ThermalsQuery'                               # 温度查询
ARSESSION_START = '/ARSessionStart'                             # AR会话开始
ARSESSION_START_CONFIRM = '/ARSessionStartConfirm'              # AR会话开始确认
ARSESSION_STOP = '/ARSessionStop'                               # AR会话停止
ARSESSION_STOP_CONFIRM = '/ARSessionStopConfirm'                # AR会话停止确认

# LiveLink
LIVE_LINK_CONNECT = '/LiveLink'                                 # LiveLink连接
LIVE_LINK_SUBJECT = '/LiveLinkSubject'                          # LiveLink科目
ADD_LIVE_LINK_ADDRESS = '/AddLiveLinkAddress'                   # 添加LiveLink地址
CLEAR_LIVE_LINK_ADDRESSES = '/ClearAllLiveLinkAddresses'        # 清除LiveLink地址
LIVE_LINK_STREAM_START = '/LiveLinkStreamStart'                 # LiveLink流开始
LIVE_LINK_STREAM_STOP = '/LiveLinkStreamStop'                   # LiveLink流停止

# Master Recording commands
# 主要的记录命令 
RECORD_START = '/RecordStart'                                   # 记录开始
RECORD_START_CONFIRM = '/RecordStartConfirm'                    # 记录开始确认
RECORD_STOP = '/RecordStop'                                     # 记录停止
RECORD_STOP_CONFIRM = '/RecordStopConfirm'                      # 记录停止确认
RECORD_CANCEL = '/RecordCancel'                                 # 记录取消
RECORD_CANCEL_CONFIRM = '/RecordCancelConfirm'                  # 记录取消确认
RECORD_ADD_MARK = '/RecordAddMark'                              # 记录添加标记
RECORD_ADD_MARK_CONFIRM = '/RecordAddMarkConfirm'               # 记录添加标记确认
TAKE = '/Take'                                                  # 镜头编号
TAKE_CONFIRM = '/TakeConfirm'                                   # 镜头编号确认
TAKE_QUERY = '/TakeQuery'                                       # 镜头编号查询
SLATE = '/Slate'                                                # 场记板，比如记录一场戏的第几场
SLATE_CONFIRM = '/SlateConfirm'                                 # 场记板，确认
SLATE_QUERY = '/SlateQuery'                                     # 场记板，查询
SLATE_DESCRIPTION = '/SlateDescription'                         # 场记板，描述
DATA = '/Data'                                                  # 时间（数据）
DATA_QUERY = '/DataQuery'                                       # 时间（数据）查询

# OSC settings
OSC_ADD_SEND_TARGET = '/OSCAddSendTarget'                       # OSC添加发送目标
OSC_ADD_SEND_TARGET_CONFIRM = '/OSCAddSendTargetConfirm'        # OSC添加发送目标确认

# VPRC 虚拟堪景工具 https://docs.unrealengine.com/4.27/zh-CN/BuildingWorlds/VRMode/VirtualScouting/
VPRC_WILDCARD = '/VPRC*'                                        # 通配符
VPRC_RECIEVER_NAME = 'Record'                                   # VPRC接受名

# MONITOR 监视器
MONITOR_WILDCARD = '/Monitor*'                                  # 监视器通配符
MONITOR_RECIEVER_NAME = 'Monitor'                               # 监视器名