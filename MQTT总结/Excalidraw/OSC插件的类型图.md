---

excalidraw-plugin: parsed
tags: [excalidraw]

---
==⚠  Switch to EXCALIDRAW VIEW in the MORE OPTIONS menu of this document. ⚠==


# Text Elements
OSC插件的总结 ^TWZoyd6i

OSCTypes.h（没有继承关系）
用于虚幻数据类型转OSC类型 ^0ubceCbZ

OSCStream.h（没有继承关系）
类似C++的Iostream流的输入输出：
提供OSC流的读写的相关函数 ^xYkjRTGU

OSCPacket.h（没有继承关系）接口类
用于读写OSC流
包含是否为消息或者束，
获取Ip地址
获取端口
创建包的工作
包含两个数据:
IP地址
端口 ^b2bN0p9q

OSCMessage.h（没有继承关系）接口类
OSC消息构造（）

设置包（IOS包 输入包）;
获取包（）；

设置地址（OSC地址 输入地址）；
获取地址（）；

私有变量
包： ^azVNO8vh

OSCLog.h
这里主要是声明一个日志类别的拓展：
后面的类型就可以用这个日志输出 ^ctWYDGax

OSCAddress.h
OSC地址类
OSC的命名空间：束标签，路径分割符

OSC地址：
私有数据：
容器，方式，是否是值类型，是否是值路径，Hash值

函数：
是否有效的方式
是否有效的路径
匹配
推入容器
弹出容器
移除容器
清理容器
获取方式
设置方式
获取容器路径
获取容器
获取完整路径

外加一些，操作符重构 ^pysivLmU

OSC客户端

OS客户端代理的接口类
获取发送IP地址（纯虚函数）
设置发送IP地址（纯虚函数）
是否激活（） （纯虚函数）
发送消息（）（纯虚函数）
发送束（）（纯虚函数）
停止（）（纯虚函数）


UOSCClient::继承自UObject类 ^zmdOCC8j

UClient类的实现

连接（）
激活（）

蓝图函数（）
获取发送的Ip地址（）
设置发送的Ip地址（）
发送OSC消息（）
发送OSC束（）

数据：
客户端代理指针 ^hstWKaTG

OSCServer服务器
申明了很多代理以备调用

OSC服务器代理的接口类
获取Ip地址（纯虚函数）
获取端口（纯虚函数）
获取多播循环回调（纯虚函数）

是否激活（纯虚函数）
监听（纯虚函数）
设置地址（纯虚函数）
设置多播循环回调（纯虚函数）
编辑器下能否tick（纯虚函数）
停止（纯虚函数）
添加百名单客户端（纯虚函数）
删除白名单客户端（纯虚函数）
清理白名单客户端（纯虚函数）
获取白名单客户端（纯虚函数）
设置白名单客户端启用（纯虚函数）
 ^qj4d8Eko

UOSCServer类继承自UObject类

提供以下函数：
获取多播循环（蓝图函数）
是否激活（蓝图函数）
监听（蓝图函数）
设置多播循环回调（蓝图函数）

OSC接收消息事件 OnOscMessageReceived（蓝图参数）
OSC接收消息原生事件 OnOscMessageReceivedNative

OSC接收束事件 OnOscBundleReceived （蓝图参数）
OSC接受束原生事件 OnOscBundleReceivedNative;

设置白名单客户端（蓝图函数）
添加白名单客户端（蓝图函数）
移除白名单客户端（蓝图函数）
清理白名单客户端（蓝图函数）
获取Ip地址（蓝图函数）
获取端口（蓝图函数）
获取白名单客户端（蓝图函数）

绑定事件到OSC地址形式匹配路径（蓝图函数）
解绑事件到OSC地址形式匹配路径（蓝图函数）
解绑所有事件到OSC地址形式匹配路径（蓝图函数）

获取绑定OSC地址形式（蓝图函数）
设置编辑器下可tick （蓝图函数）

清理包
处理包
弹出包列队

私有函数：
开始摧毁
调度束
调度消息

数据：
服务器代理
OSC包
地址形式
 ^uUezRGmj

OSC管理器
UOSCManager 继承自：蓝图函数库
创建OSC服务器（蓝图函数）
创建OSC客户端（蓝图函数）

添加消息到束 （蓝图函数）
添加束到束 （蓝图函数）

从束中获取束 （蓝图函数）
从束中获取消息（蓝图函数）

清理消息（蓝图函数）
清理束（蓝图函数）

添加浮点值到OSC消息（蓝图函数）
添加整数值到OSC消息（蓝图函数）
添加64位整数值到OSC消息（蓝图函数）
添加地址到OSC消息(蓝图函数）
添加Blob到OSC消息（蓝图函数）
添加bool到OSC消息（蓝图函数）

获取OSC消息地址在index处（蓝图函数）
获取OSC消息地址s（蓝图函数）

获取OSC消息浮点值在index（蓝图函数）
获取OSC消息浮点数组（蓝图函数）

获取OSC消息整形值在index（蓝图函数）
获取OSC消息整形数组（蓝图函数）

获取OSC消息字符串在index（蓝图函数）
获取OSC消息字符串组（蓝图函数）

获取OSC消息bool在index（蓝图函数）
获取OSC消息bool组（蓝图函数）

OSC地址是否有值路径（蓝图函数）
OSC地址是否有值形式（蓝图函数）

转换字符串成OSC地址（蓝图函数）
其他函数 ^rMha2SWO


# Embedded files
8830a2d047dff260ef62420a79e1b9a3dff70495: [[Image/Pasted Image 20220604101849_191.png]]

%%
# Drawing
```json
{
	"type": "excalidraw",
	"version": 2,
	"source": "https://excalidraw.com",
	"elements": [
		{
			"type": "rectangle",
			"version": 385,
			"versionNonce": 1399196764,
			"isDeleted": false,
			"id": "eMI9Zw_26NLXosFKWIN3M",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -778.3789950284092,
			"y": 71.91667325568915,
			"strokeColor": "#000000",
			"backgroundColor": "#fa5252",
			"width": 145,
			"height": 1128,
			"seed": 2037540324,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [
				{
					"type": "text",
					"id": "TWZoyd6i"
				},
				{
					"id": "0EKdcY6G030KLmbUFGTmu",
					"type": "arrow"
				},
				{
					"id": "-pEEfNEz5ocM6ObkCAV5Q",
					"type": "arrow"
				},
				{
					"id": "3yTwwMFqzpTWNncJVRgRj",
					"type": "arrow"
				},
				{
					"id": "4ixVXiW63ZQdhNm4AhwHz",
					"type": "arrow"
				},
				{
					"id": "0sV2lX6PE8pr8XgBCy1ar",
					"type": "arrow"
				},
				{
					"id": "ypJxu82Oy_mrVz5DYxdXl",
					"type": "arrow"
				},
				{
					"id": "z4eV7VK760TpRMIYlOaTy",
					"type": "arrow"
				},
				{
					"id": "Z_Lu7wkZ5awWSJnIub2An",
					"type": "arrow"
				},
				{
					"id": "lrN2mr_PsmrApsoCsSOQd",
					"type": "arrow"
				}
			],
			"updated": 1654325357455,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 399,
			"versionNonce": 1677050716,
			"isDeleted": false,
			"id": "TWZoyd6i",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -773.3789950284092,
			"y": 610.9166732556891,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 135,
			"height": 50,
			"seed": 1194605404,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [],
			"updated": 1654312166702,
			"link": null,
			"locked": false,
			"fontSize": 20.015860721982758,
			"fontFamily": 1,
			"text": "OSC插件的总\n结",
			"rawText": "OSC插件的总结",
			"baseline": 42,
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "eMI9Zw_26NLXosFKWIN3M",
			"originalText": "OSC插件的总结"
		},
		{
			"type": "rectangle",
			"version": 512,
			"versionNonce": 2013026780,
			"isDeleted": false,
			"id": "lseB9zr6zv7A1ZY-Qt3ta",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -2410.7546437581364,
			"y": -916.2209396362313,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 292,
			"height": 150,
			"seed": 455730396,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [
				{
					"id": "3yTwwMFqzpTWNncJVRgRj",
					"type": "arrow"
				},
				{
					"type": "text",
					"id": "0ubceCbZ"
				}
			],
			"updated": 1654312828739,
			"link": null,
			"locked": false
		},
		{
			"type": "arrow",
			"version": 1667,
			"versionNonce": 571932508,
			"isDeleted": false,
			"id": "3yTwwMFqzpTWNncJVRgRj",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -808.4476536250066,
			"y": 190.9816304139477,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 1280.0371925769277,
			"height": 976.1221963509056,
			"seed": 1684891876,
			"groupIds": [],
			"strokeSharpness": "round",
			"boundElements": [],
			"updated": 1654325520166,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "eMI9Zw_26NLXosFKWIN3M",
				"gap": 30.068658596597402,
				"focus": 0.5921635352354573
			},
			"endBinding": {
				"elementId": "lseB9zr6zv7A1ZY-Qt3ta",
				"gap": 30.269797556201866,
				"focus": -0.4204147014224959
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					-1280.0371925769277,
					-976.1221963509056
				]
			]
		},
		{
			"type": "text",
			"version": 522,
			"versionNonce": 1475592676,
			"isDeleted": false,
			"id": "0ubceCbZ",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -2405.7546437581364,
			"y": -911.2209396362313,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 282,
			"height": 140,
			"seed": 2097112164,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [],
			"updated": 1654312828739,
			"link": null,
			"locked": false,
			"fontSize": 28,
			"fontFamily": 1,
			"text": "OSCTypes.h（没有继\n承关系）\n用于虚幻数据类型转O\nSC类型",
			"rawText": "OSCTypes.h（没有继承关系）\n用于虚幻数据类型转OSC类型",
			"baseline": 129,
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": "lseB9zr6zv7A1ZY-Qt3ta",
			"originalText": "OSCTypes.h（没有继承关系）\n用于虚幻数据类型转OSC类型"
		},
		{
			"type": "rectangle",
			"version": 547,
			"versionNonce": 668278756,
			"isDeleted": false,
			"id": "yO6x6HwOVBClm3GnGgay1",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -2449.191670735676,
			"y": -415.0058917999278,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 346,
			"height": 220,
			"seed": 474381668,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [
				{
					"id": "3yTwwMFqzpTWNncJVRgRj",
					"type": "arrow"
				},
				{
					"id": "xYkjRTGU",
					"type": "text"
				},
				{
					"id": "0EKdcY6G030KLmbUFGTmu",
					"type": "arrow"
				}
			],
			"updated": 1654312829942,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 650,
			"versionNonce": 1131954268,
			"isDeleted": false,
			"id": "xYkjRTGU",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -2444.191670735676,
			"y": -410.0058917999278,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 336,
			"height": 210,
			"seed": 259357404,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [],
			"updated": 1654312829942,
			"link": null,
			"locked": false,
			"fontSize": 28,
			"fontFamily": 1,
			"text": "OSCStream.h（没有继承\n关系）\n类似C++的Iostream流的\n输入输出：\n提供OSC流的读写的相关函\n数",
			"rawText": "OSCStream.h（没有继承关系）\n类似C++的Iostream流的输入输出：\n提供OSC流的读写的相关函数",
			"baseline": 199,
			"textAlign": "left",
			"verticalAlign": "middle",
			"containerId": "yO6x6HwOVBClm3GnGgay1",
			"originalText": "OSCStream.h（没有继承关系）\n类似C++的Iostream流的输入输出：\n提供OSC流的读写的相关函数"
		},
		{
			"type": "arrow",
			"version": 1395,
			"versionNonce": 1312207836,
			"isDeleted": false,
			"id": "0EKdcY6G030KLmbUFGTmu",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -804.487204342729,
			"y": 368.4682422916105,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 1273.6050508678977,
			"height": 653.0662086007477,
			"seed": 1996913764,
			"groupIds": [],
			"strokeSharpness": "round",
			"boundElements": [],
			"updated": 1654325520168,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "eMI9Zw_26NLXosFKWIN3M",
				"gap": 26.108209314319765,
				"focus": 0.36076820669021975
			},
			"endBinding": {
				"elementId": "yO6x6HwOVBClm3GnGgay1",
				"gap": 25.099415525049153,
				"focus": -0.4084938310654575
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					-1273.6050508678977,
					-653.0662086007477
				]
			]
		},
		{
			"type": "arrow",
			"version": 1497,
			"versionNonce": 896260188,
			"isDeleted": false,
			"id": "-pEEfNEz5ocM6ObkCAV5Q",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -808.6966383322259,
			"y": 510.9770905407464,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 1128.343203094399,
			"height": 129.5518489176552,
			"seed": 2140589532,
			"groupIds": [],
			"strokeSharpness": "round",
			"boundElements": [],
			"updated": 1654325520170,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "eMI9Zw_26NLXosFKWIN3M",
				"gap": 30.317643303816567,
				"focus": 0.19767551421672558
			},
			"endBinding": {
				"elementId": "49SgMKaFc1IZqW36MIrgY",
				"gap": 24.53447872365018,
				"focus": 0.8066151192270414
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					-1128.343203094399,
					-129.5518489176552
				]
			]
		},
		{
			"type": "rectangle",
			"version": 1073,
			"versionNonce": 250057572,
			"isDeleted": false,
			"id": "49SgMKaFc1IZqW36MIrgY",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -2476.503306070963,
			"y": 31.89514079238336,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 539,
			"height": 325,
			"seed": 1185582308,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [
				{
					"id": "3yTwwMFqzpTWNncJVRgRj",
					"type": "arrow"
				},
				{
					"id": "b2bN0p9q",
					"type": "text"
				},
				{
					"id": "0EKdcY6G030KLmbUFGTmu",
					"type": "arrow"
				},
				{
					"id": "-pEEfNEz5ocM6ObkCAV5Q",
					"type": "arrow"
				}
			],
			"updated": 1654312731262,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 1039,
			"versionNonce": 1670956252,
			"isDeleted": false,
			"id": "b2bN0p9q",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -2471.503306070963,
			"y": 36.89514079238336,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 529,
			"height": 315,
			"seed": 951853916,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [],
			"updated": 1654312731262,
			"link": null,
			"locked": false,
			"fontSize": 28,
			"fontFamily": 1,
			"text": "OSCPacket.h（没有继承关系）接口类\n用于读写OSC流\n包含是否为消息或者束，\n获取Ip地址\n获取端口\n创建包的工作\n包含两个数据:\nIP地址\n端口",
			"rawText": "OSCPacket.h（没有继承关系）接口类\n用于读写OSC流\n包含是否为消息或者束，\n获取Ip地址\n获取端口\n创建包的工作\n包含两个数据:\nIP地址\n端口",
			"baseline": 304,
			"textAlign": "left",
			"verticalAlign": "middle",
			"containerId": "49SgMKaFc1IZqW36MIrgY",
			"originalText": "OSCPacket.h（没有继承关系）接口类\n用于读写OSC流\n包含是否为消息或者束，\n获取Ip地址\n获取端口\n创建包的工作\n包含两个数据:\nIP地址\n端口"
		},
		{
			"type": "rectangle",
			"version": 1273,
			"versionNonce": 1180142044,
			"isDeleted": false,
			"id": "j0uWC1nOnJI5l_O-lNsMu",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -2439.5156943581314,
			"y": 536.6398834459704,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 539,
			"height": 395,
			"seed": 1674113636,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [
				{
					"id": "3yTwwMFqzpTWNncJVRgRj",
					"type": "arrow"
				},
				{
					"id": "azVNO8vh",
					"type": "text"
				},
				{
					"id": "0EKdcY6G030KLmbUFGTmu",
					"type": "arrow"
				},
				{
					"id": "-pEEfNEz5ocM6ObkCAV5Q",
					"type": "arrow"
				},
				{
					"id": "4ixVXiW63ZQdhNm4AhwHz",
					"type": "arrow"
				}
			],
			"updated": 1654312733110,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 1428,
			"versionNonce": 337875428,
			"isDeleted": false,
			"id": "azVNO8vh",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -2434.5156943581314,
			"y": 541.6398834459704,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 529,
			"height": 385,
			"seed": 1329649116,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [],
			"updated": 1654312733110,
			"link": null,
			"locked": false,
			"fontSize": 28,
			"fontFamily": 1,
			"text": "OSCMessage.h（没有继承关系）接口类\nOSC消息构造（）\n\n设置包（IOS包 输入包）;\n获取包（）；\n\n设置地址（OSC地址 输入地址）；\n获取地址（）；\n\n私有变量\n包：",
			"rawText": "OSCMessage.h（没有继承关系）接口类\nOSC消息构造（）\n\n设置包（IOS包 输入包）;\n获取包（）；\n\n设置地址（OSC地址 输入地址）；\n获取地址（）；\n\n私有变量\n包：",
			"baseline": 373,
			"textAlign": "left",
			"verticalAlign": "middle",
			"containerId": "j0uWC1nOnJI5l_O-lNsMu",
			"originalText": "OSCMessage.h（没有继承关系）接口类\nOSC消息构造（）\n\n设置包（IOS包 输入包）;\n获取包（）；\n\n设置地址（OSC地址 输入地址）；\n获取地址（）；\n\n私有变量\n包："
		},
		{
			"type": "arrow",
			"version": 1529,
			"versionNonce": 864578780,
			"isDeleted": false,
			"id": "4ixVXiW63ZQdhNm4AhwHz",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -798.5317631603482,
			"y": 629.9444690734297,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 1074.528309896008,
			"height": 155.30581584571564,
			"seed": 158599644,
			"groupIds": [],
			"strokeSharpness": "round",
			"boundElements": [],
			"updated": 1654325520173,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "eMI9Zw_26NLXosFKWIN3M",
				"gap": 20.152768131938956,
				"focus": 0.033706513263810044
			},
			"endBinding": {
				"elementId": "j0uWC1nOnJI5l_O-lNsMu",
				"gap": 27.45562130177518,
				"focus": 0.39767314058516506
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					-1074.528309896008,
					155.30581584571564
				]
			]
		},
		{
			"type": "rectangle",
			"version": 212,
			"versionNonce": 1287769828,
			"isDeleted": false,
			"id": "s50Kda8zkxVWP5WPeTJCO",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -2452.8942417953954,
			"y": 1010.2563267332127,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 551,
			"height": 247.13238525390665,
			"seed": 1579335644,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [
				{
					"id": "0sV2lX6PE8pr8XgBCy1ar",
					"type": "arrow"
				},
				{
					"type": "text",
					"id": "ctWYDGax"
				}
			],
			"updated": 1654312940114,
			"link": null,
			"locked": false
		},
		{
			"type": "arrow",
			"version": 989,
			"versionNonce": 1511944540,
			"isDeleted": false,
			"id": "0sV2lX6PE8pr8XgBCy1ar",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -805.8346163301845,
			"y": 764.3985601245901,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 1083.7537521310187,
			"height": 221.2191834336329,
			"seed": 1030578660,
			"groupIds": [],
			"strokeSharpness": "round",
			"boundElements": [],
			"updated": 1654325520175,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "eMI9Zw_26NLXosFKWIN3M",
				"gap": 27.45562130177518,
				"focus": -0.18672915607863635
			},
			"endBinding": {
				"elementId": "s50Kda8zkxVWP5WPeTJCO",
				"gap": 27.540775214000007,
				"focus": -0.49753001947665865
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					-1083.7537521310187,
					221.2191834336329
				]
			]
		},
		{
			"type": "text",
			"version": 292,
			"versionNonce": 350279524,
			"isDeleted": false,
			"id": "ctWYDGax",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -2447.8942417953954,
			"y": 1015.2563267332127,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 541,
			"height": 105,
			"seed": 1694768860,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [],
			"updated": 1654312736319,
			"link": null,
			"locked": false,
			"fontSize": 28,
			"fontFamily": 1,
			"text": "OSCLog.h\n这里主要是声明一个日志类别的拓展：\n后面的类型就可以用这个日志输出",
			"rawText": "OSCLog.h\n这里主要是声明一个日志类别的拓展：\n后面的类型就可以用这个日志输出",
			"baseline": 94,
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": "s50Kda8zkxVWP5WPeTJCO",
			"originalText": "OSCLog.h\n这里主要是声明一个日志类别的拓展：\n后面的类型就可以用这个日志输出"
		},
		{
			"type": "image",
			"version": 182,
			"versionNonce": 1921213276,
			"isDeleted": false,
			"id": "11Gi8_I2bNoNFZiSDo_DE",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -2425.5538029526215,
			"y": 1131.8468711159444,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"width": 501,
			"height": 75,
			"seed": 653234916,
			"groupIds": [],
			"strokeSharpness": "round",
			"boundElements": [],
			"updated": 1654312742214,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "8830a2d047dff260ef62420a79e1b9a3dff70495",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "rectangle",
			"version": 458,
			"versionNonce": 845921372,
			"isDeleted": false,
			"id": "UT3SL_U-ZUpGMJi5vjdw_",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -109.93803035851647,
			"y": -873.4211517680789,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 887,
			"height": 815,
			"seed": 898610908,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [
				{
					"id": "ypJxu82Oy_mrVz5DYxdXl",
					"type": "arrow"
				},
				{
					"type": "text",
					"id": "pysivLmU"
				}
			],
			"updated": 1654312751938,
			"link": null,
			"locked": false
		},
		{
			"type": "arrow",
			"version": 1002,
			"versionNonce": 947906012,
			"isDeleted": false,
			"id": "ypJxu82Oy_mrVz5DYxdXl",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -607.2998274973005,
			"y": 228.50573577015055,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 474.6082380407975,
			"height": 800.5286789642685,
			"seed": 970064100,
			"groupIds": [],
			"strokeSharpness": "round",
			"boundElements": [],
			"updated": 1654325520178,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "eMI9Zw_26NLXosFKWIN3M",
				"gap": 26.079167531108737,
				"focus": -0.3513633138940141
			},
			"endBinding": {
				"elementId": "UT3SL_U-ZUpGMJi5vjdw_",
				"gap": 22.753559097986567,
				"focus": 0.7723874904793373
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					474.6082380407975,
					-800.5286789642685
				]
			]
		},
		{
			"type": "text",
			"version": 806,
			"versionNonce": 1216464740,
			"isDeleted": false,
			"id": "pysivLmU",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -104.93803035851647,
			"y": -868.4211517680789,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 877,
			"height": 805,
			"seed": 1965133148,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [],
			"updated": 1654312751939,
			"link": null,
			"locked": false,
			"fontSize": 28,
			"fontFamily": 1,
			"text": "OSCAddress.h\nOSC地址类\nOSC的命名空间：束标签，路径分割符\n\nOSC地址：\n私有数据：\n容器，方式，是否是值类型，是否是值路径，Hash值\n\n函数：\n是否有效的方式\n是否有效的路径\n匹配\n推入容器\n弹出容器\n移除容器\n清理容器\n获取方式\n设置方式\n获取容器路径\n获取容器\n获取完整路径\n\n外加一些，操作符重构",
			"rawText": "OSCAddress.h\nOSC地址类\nOSC的命名空间：束标签，路径分割符\n\nOSC地址：\n私有数据：\n容器，方式，是否是值类型，是否是值路径，Hash值\n\n函数：\n是否有效的方式\n是否有效的路径\n匹配\n推入容器\n弹出容器\n移除容器\n清理容器\n获取方式\n设置方式\n获取容器路径\n获取容器\n获取完整路径\n\n外加一些，操作符重构",
			"baseline": 794,
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": "UT3SL_U-ZUpGMJi5vjdw_",
			"originalText": "OSCAddress.h\nOSC地址类\nOSC的命名空间：束标签，路径分割符\n\nOSC地址：\n私有数据：\n容器，方式，是否是值类型，是否是值路径，Hash值\n\n函数：\n是否有效的方式\n是否有效的路径\n匹配\n推入容器\n弹出容器\n移除容器\n清理容器\n获取方式\n设置方式\n获取容器路径\n获取容器\n获取完整路径\n\n外加一些，操作符重构"
		},
		{
			"type": "rectangle",
			"version": 316,
			"versionNonce": 765462364,
			"isDeleted": false,
			"id": "Zv0LHPn0yqlDFSnwrVlEH",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -106.84803702614454,
			"y": 61.441511814340515,
			"strokeColor": "#000000",
			"backgroundColor": "#228be6",
			"width": 850.1736450195312,
			"height": 457.8960418701171,
			"seed": 497442404,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [
				{
					"id": "z4eV7VK760TpRMIYlOaTy",
					"type": "arrow"
				},
				{
					"type": "text",
					"id": "zmdOCC8j"
				},
				{
					"id": "JVi5HtaKOLEio2L4ny_xw",
					"type": "arrow"
				}
			],
			"updated": 1654312764574,
			"link": null,
			"locked": false
		},
		{
			"type": "arrow",
			"version": 696,
			"versionNonce": 599706204,
			"isDeleted": false,
			"id": "z4eV7VK760TpRMIYlOaTy",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -619.9561068279771,
			"y": 331.8037485369406,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 498.9292067670596,
			"height": 79.09542349343587,
			"seed": 231328996,
			"groupIds": [],
			"strokeSharpness": "round",
			"boundElements": [],
			"updated": 1654325520180,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "eMI9Zw_26NLXosFKWIN3M",
				"gap": 13.422888200432112,
				"focus": -0.5047694957567379
			},
			"endBinding": {
				"elementId": "Zv0LHPn0yqlDFSnwrVlEH",
				"gap": 14.178863034772974,
				"focus": 0.36214878681767193
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					498.9292067670596,
					-79.09542349343587
				]
			]
		},
		{
			"type": "text",
			"version": 520,
			"versionNonce": 30125156,
			"isDeleted": false,
			"id": "zmdOCC8j",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -101.84803702614454,
			"y": 66.44151181434052,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 840.1736450195312,
			"height": 420,
			"seed": 2032306404,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [],
			"updated": 1654312764574,
			"link": null,
			"locked": false,
			"fontSize": 28.011577531166875,
			"fontFamily": 1,
			"text": "OSC客户端\n\nOS客户端代理的接口类\n获取发送IP地址（纯虚函数）\n设置发送IP地址（纯虚函数）\n是否激活（） （纯虚函数）\n发送消息（）（纯虚函数）\n发送束（）（纯虚函数）\n停止（）（纯虚函数）\n\n\nUOSCClient::继承自UObject类",
			"rawText": "OSC客户端\n\nOS客户端代理的接口类\n获取发送IP地址（纯虚函数）\n设置发送IP地址（纯虚函数）\n是否激活（） （纯虚函数）\n发送消息（）（纯虚函数）\n发送束（）（纯虚函数）\n停止（）（纯虚函数）\n\n\nUOSCClient::继承自UObject类",
			"baseline": 409,
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": "Zv0LHPn0yqlDFSnwrVlEH",
			"originalText": "OSC客户端\n\nOS客户端代理的接口类\n获取发送IP地址（纯虚函数）\n设置发送IP地址（纯虚函数）\n是否激活（） （纯虚函数）\n发送消息（）（纯虚函数）\n发送束（）（纯虚函数）\n停止（）（纯虚函数）\n\n\nUOSCClient::继承自UObject类"
		},
		{
			"type": "rectangle",
			"version": 270,
			"versionNonce": 603268580,
			"isDeleted": false,
			"id": "1fdAvNBrVip92LBg59bVv",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 1212.7980099302354,
			"y": 44.711559320037395,
			"strokeColor": "#000000",
			"backgroundColor": "#228be6",
			"width": 912,
			"height": 465,
			"seed": 2020881892,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [
				{
					"id": "JVi5HtaKOLEio2L4ny_xw",
					"type": "arrow"
				},
				{
					"type": "text",
					"id": "hstWKaTG"
				}
			],
			"updated": 1654312765671,
			"link": null,
			"locked": false
		},
		{
			"type": "arrow",
			"version": 652,
			"versionNonce": 31253340,
			"isDeleted": false,
			"id": "JVi5HtaKOLEio2L4ny_xw",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 752.1237136754153,
			"y": 308.2489037592628,
			"strokeColor": "#000000",
			"backgroundColor": "#228be6",
			"width": 449.5390459151249,
			"height": 0.9911361110378607,
			"seed": 312161116,
			"groupIds": [],
			"strokeSharpness": "round",
			"boundElements": [],
			"updated": 1654325520182,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "Zv0LHPn0yqlDFSnwrVlEH",
				"gap": 8.798105682028563,
				"focus": 0.08184662865073113
			},
			"endBinding": {
				"elementId": "1fdAvNBrVip92LBg59bVv",
				"gap": 11.135250339695176,
				"focus": -0.12426384464393155
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					449.5390459151249,
					-0.9911361110378607
				]
			]
		},
		{
			"type": "text",
			"version": 438,
			"versionNonce": 499358300,
			"isDeleted": false,
			"id": "hstWKaTG",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 1217.7980099302354,
			"y": 49.711559320037395,
			"strokeColor": "#000000",
			"backgroundColor": "#228be6",
			"width": 902,
			"height": 455,
			"seed": 928878692,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [],
			"updated": 1654312765671,
			"link": null,
			"locked": false,
			"fontSize": 28,
			"fontFamily": 1,
			"text": "UClient类的实现\n\n连接（）\n激活（）\n\n蓝图函数（）\n获取发送的Ip地址（）\n设置发送的Ip地址（）\n发送OSC消息（）\n发送OSC束（）\n\n数据：\n客户端代理指针",
			"rawText": "UClient类的实现\n\n连接（）\n激活（）\n\n蓝图函数（）\n获取发送的Ip地址（）\n设置发送的Ip地址（）\n发送OSC消息（）\n发送OSC束（）\n\n数据：\n客户端代理指针",
			"baseline": 444,
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": "1fdAvNBrVip92LBg59bVv",
			"originalText": "UClient类的实现\n\n连接（）\n激活（）\n\n蓝图函数（）\n获取发送的Ip地址（）\n设置发送的Ip地址（）\n发送OSC消息（）\n发送OSC束（）\n\n数据：\n客户端代理指针"
		},
		{
			"id": "zzgaiCuRc9qlSJRSgwz2f",
			"type": "rectangle",
			"x": -113.43513569687002,
			"y": 627.6674620432368,
			"width": 760,
			"height": 710,
			"angle": 0,
			"strokeColor": "#000000",
			"backgroundColor": "#7950f2",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"seed": 1887174628,
			"version": 586,
			"versionNonce": 2133518428,
			"isDeleted": false,
			"boundElements": [
				{
					"id": "Z_Lu7wkZ5awWSJnIub2An",
					"type": "arrow"
				},
				{
					"type": "text",
					"id": "qj4d8Eko"
				},
				{
					"id": "oY7H-xvw47tVOI6ghL3wI",
					"type": "arrow"
				}
			],
			"updated": 1654325307099,
			"link": null,
			"locked": false
		},
		{
			"id": "Z_Lu7wkZ5awWSJnIub2An",
			"type": "arrow",
			"x": -617.1191663289874,
			"y": 673.7633341634235,
			"width": 494.7997864470234,
			"height": 292.1245932676312,
			"angle": 0,
			"strokeColor": "#000000",
			"backgroundColor": "#7950f2",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"strokeSharpness": "round",
			"seed": 411176028,
			"version": 487,
			"versionNonce": 60823516,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1654325520184,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					494.7997864470234,
					292.1245932676312
				]
			],
			"lastCommittedPoint": null,
			"startBinding": {
				"elementId": "eMI9Zw_26NLXosFKWIN3M",
				"gap": 16.259828699421803,
				"focus": -0.023989045875051532
			},
			"endBinding": {
				"elementId": "zzgaiCuRc9qlSJRSgwz2f",
				"gap": 8.884244185093854,
				"focus": -0.36733299079342396
			},
			"startArrowhead": null,
			"endArrowhead": "arrow"
		},
		{
			"id": "qj4d8Eko",
			"type": "text",
			"x": -108.43513569687002,
			"y": 632.6674620432368,
			"width": 750,
			"height": 700,
			"angle": 0,
			"strokeColor": "#000000",
			"backgroundColor": "#7950f2",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"seed": 761460196,
			"version": 770,
			"versionNonce": 194730852,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1654325307099,
			"link": null,
			"locked": false,
			"text": "OSCServer服务器\n申明了很多代理以备调用\n\nOSC服务器代理的接口类\n获取Ip地址（纯虚函数）\n获取端口（纯虚函数）\n获取多播循环回调（纯虚函数）\n\n是否激活（纯虚函数）\n监听（纯虚函数）\n设置地址（纯虚函数）\n设置多播循环回调（纯虚函数）\n编辑器下能否tick（纯虚函数）\n停止（纯虚函数）\n添加百名单客户端（纯虚函数）\n删除白名单客户端（纯虚函数）\n清理白名单客户端（纯虚函数）\n获取白名单客户端（纯虚函数）\n设置白名单客户端启用（纯虚函数）\n",
			"rawText": "OSCServer服务器\n申明了很多代理以备调用\n\nOSC服务器代理的接口类\n获取Ip地址（纯虚函数）\n获取端口（纯虚函数）\n获取多播循环回调（纯虚函数）\n\n是否激活（纯虚函数）\n监听（纯虚函数）\n设置地址（纯虚函数）\n设置多播循环回调（纯虚函数）\n编辑器下能否tick（纯虚函数）\n停止（纯虚函数）\n添加百名单客户端（纯虚函数）\n删除白名单客户端（纯虚函数）\n清理白名单客户端（纯虚函数）\n获取白名单客户端（纯虚函数）\n设置白名单客户端启用（纯虚函数）\n",
			"fontSize": 28,
			"fontFamily": 1,
			"textAlign": "left",
			"verticalAlign": "top",
			"baseline": 689,
			"containerId": "zzgaiCuRc9qlSJRSgwz2f",
			"originalText": "OSCServer服务器\n申明了很多代理以备调用\n\nOSC服务器代理的接口类\n获取Ip地址（纯虚函数）\n获取端口（纯虚函数）\n获取多播循环回调（纯虚函数）\n\n是否激活（纯虚函数）\n监听（纯虚函数）\n设置地址（纯虚函数）\n设置多播循环回调（纯虚函数）\n编辑器下能否tick（纯虚函数）\n停止（纯虚函数）\n添加百名单客户端（纯虚函数）\n删除白名单客户端（纯虚函数）\n清理白名单客户端（纯虚函数）\n获取白名单客户端（纯虚函数）\n设置白名单客户端启用（纯虚函数）\n"
		},
		{
			"id": "f3WHsQcyk4_M7G7b1vTsi",
			"type": "rectangle",
			"x": 1241.478372400461,
			"y": 633.0518118662344,
			"width": 1033,
			"height": 1516,
			"angle": 0,
			"strokeColor": "#000000",
			"backgroundColor": "#7950f2",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"seed": 2055599076,
			"version": 331,
			"versionNonce": 1441946460,
			"isDeleted": false,
			"boundElements": [
				{
					"type": "text",
					"id": "uUezRGmj"
				},
				{
					"id": "oY7H-xvw47tVOI6ghL3wI",
					"type": "arrow"
				}
			],
			"updated": 1654324996157,
			"link": null,
			"locked": false
		},
		{
			"id": "uUezRGmj",
			"type": "text",
			"x": 1246.478372400461,
			"y": 638.0518118662344,
			"width": 1023,
			"height": 1505,
			"angle": 0,
			"strokeColor": "#000000",
			"backgroundColor": "#7950f2",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"seed": 904500324,
			"version": 1179,
			"versionNonce": 1519300836,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1654325003416,
			"link": null,
			"locked": false,
			"text": "UOSCServer类继承自UObject类\n\n提供以下函数：\n获取多播循环（蓝图函数）\n是否激活（蓝图函数）\n监听（蓝图函数）\n设置多播循环回调（蓝图函数）\n\nOSC接收消息事件 OnOscMessageReceived（蓝图参数）\nOSC接收消息原生事件 OnOscMessageReceivedNative\n\nOSC接收束事件 OnOscBundleReceived （蓝图参数）\nOSC接受束原生事件 OnOscBundleReceivedNative;\n\n设置白名单客户端（蓝图函数）\n添加白名单客户端（蓝图函数）\n移除白名单客户端（蓝图函数）\n清理白名单客户端（蓝图函数）\n获取Ip地址（蓝图函数）\n获取端口（蓝图函数）\n获取白名单客户端（蓝图函数）\n\n绑定事件到OSC地址形式匹配路径（蓝图函数）\n解绑事件到OSC地址形式匹配路径（蓝图函数）\n解绑所有事件到OSC地址形式匹配路径（蓝图函数）\n\n获取绑定OSC地址形式（蓝图函数）\n设置编辑器下可tick （蓝图函数）\n\n清理包\n处理包\n弹出包列队\n\n私有函数：\n开始摧毁\n调度束\n调度消息\n\n数据：\n服务器代理\nOSC包\n地址形式\n",
			"rawText": "UOSCServer类继承自UObject类\n\n提供以下函数：\n获取多播循环（蓝图函数）\n是否激活（蓝图函数）\n监听（蓝图函数）\n设置多播循环回调（蓝图函数）\n\nOSC接收消息事件 OnOscMessageReceived（蓝图参数）\nOSC接收消息原生事件 OnOscMessageReceivedNative\n\nOSC接收束事件 OnOscBundleReceived （蓝图参数）\nOSC接受束原生事件 OnOscBundleReceivedNative;\n\n设置白名单客户端（蓝图函数）\n添加白名单客户端（蓝图函数）\n移除白名单客户端（蓝图函数）\n清理白名单客户端（蓝图函数）\n获取Ip地址（蓝图函数）\n获取端口（蓝图函数）\n获取白名单客户端（蓝图函数）\n\n绑定事件到OSC地址形式匹配路径（蓝图函数）\n解绑事件到OSC地址形式匹配路径（蓝图函数）\n解绑所有事件到OSC地址形式匹配路径（蓝图函数）\n\n获取绑定OSC地址形式（蓝图函数）\n设置编辑器下可tick （蓝图函数）\n\n清理包\n处理包\n弹出包列队\n\n私有函数：\n开始摧毁\n调度束\n调度消息\n\n数据：\n服务器代理\nOSC包\n地址形式\n",
			"fontSize": 28,
			"fontFamily": 1,
			"textAlign": "left",
			"verticalAlign": "top",
			"baseline": 1493,
			"containerId": "f3WHsQcyk4_M7G7b1vTsi",
			"originalText": "UOSCServer类继承自UObject类\n\n提供以下函数：\n获取多播循环（蓝图函数）\n是否激活（蓝图函数）\n监听（蓝图函数）\n设置多播循环回调（蓝图函数）\n\nOSC接收消息事件 OnOscMessageReceived（蓝图参数）\nOSC接收消息原生事件 OnOscMessageReceivedNative\n\nOSC接收束事件 OnOscBundleReceived （蓝图参数）\nOSC接受束原生事件 OnOscBundleReceivedNative;\n\n设置白名单客户端（蓝图函数）\n添加白名单客户端（蓝图函数）\n移除白名单客户端（蓝图函数）\n清理白名单客户端（蓝图函数）\n获取Ip地址（蓝图函数）\n获取端口（蓝图函数）\n获取白名单客户端（蓝图函数）\n\n绑定事件到OSC地址形式匹配路径（蓝图函数）\n解绑事件到OSC地址形式匹配路径（蓝图函数）\n解绑所有事件到OSC地址形式匹配路径（蓝图函数）\n\n获取绑定OSC地址形式（蓝图函数）\n设置编辑器下可tick （蓝图函数）\n\n清理包\n处理包\n弹出包列队\n\n私有函数：\n开始摧毁\n调度束\n调度消息\n\n数据：\n服务器代理\nOSC包\n地址形式\n"
		},
		{
			"id": "oY7H-xvw47tVOI6ghL3wI",
			"type": "arrow",
			"x": 662.4663263477134,
			"y": 984.2454695963684,
			"width": 574.9170843759684,
			"height": 5.122308564489458,
			"angle": 0,
			"strokeColor": "#000000",
			"backgroundColor": "#7950f2",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"strokeSharpness": "round",
			"seed": 807770844,
			"version": 404,
			"versionNonce": 552128732,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1654325520186,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					574.9170843759684,
					-5.122308564489458
				]
			],
			"lastCommittedPoint": null,
			"startBinding": {
				"elementId": "zzgaiCuRc9qlSJRSgwz2f",
				"gap": 15.901462044583468,
				"focus": 0.014245407975192909
			},
			"endBinding": {
				"elementId": "f3WHsQcyk4_M7G7b1vTsi",
				"gap": 4.094961676779121,
				"focus": 0.546244383954639
			},
			"startArrowhead": null,
			"endArrowhead": "arrow"
		},
		{
			"id": "eu8bBa2q1oX2tg4OJRu16",
			"type": "rectangle",
			"x": -121.17467834009494,
			"y": 1494.7548478566323,
			"width": 771,
			"height": 1445,
			"angle": 0,
			"strokeColor": "#000000",
			"backgroundColor": "#7950f2",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"seed": 173817948,
			"version": 300,
			"versionNonce": 354131548,
			"isDeleted": false,
			"boundElements": [
				{
					"id": "lrN2mr_PsmrApsoCsSOQd",
					"type": "arrow"
				},
				{
					"type": "text",
					"id": "rMha2SWO"
				}
			],
			"updated": 1654326797532,
			"link": null,
			"locked": false
		},
		{
			"id": "lrN2mr_PsmrApsoCsSOQd",
			"type": "arrow",
			"x": -623.8212082153353,
			"y": 1130.9927954797627,
			"width": 493.08874306216643,
			"height": 645.363086080145,
			"angle": 0,
			"strokeColor": "#000000",
			"backgroundColor": "#7950f2",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"strokeSharpness": "round",
			"seed": 202596444,
			"version": 373,
			"versionNonce": 2142943460,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1654326797532,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					493.08874306216643,
					645.363086080145
				]
			],
			"lastCommittedPoint": null,
			"startBinding": {
				"elementId": "eMI9Zw_26NLXosFKWIN3M",
				"gap": 9.557786813073937,
				"focus": 0.5877806959674472
			},
			"endBinding": {
				"elementId": "eu8bBa2q1oX2tg4OJRu16",
				"gap": 9.557786813073937,
				"focus": -0.06206720502530264
			},
			"startArrowhead": null,
			"endArrowhead": "arrow"
		},
		{
			"id": "rMha2SWO",
			"type": "text",
			"x": -116.17467834009494,
			"y": 1499.7548478566323,
			"width": 761,
			"height": 1435,
			"angle": 0,
			"strokeColor": "#000000",
			"backgroundColor": "#7950f2",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"seed": 775903076,
			"version": 1081,
			"versionNonce": 314115428,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1654326797532,
			"link": null,
			"locked": false,
			"text": "OSC管理器\nUOSCManager 继承自：蓝图函数库\n创建OSC服务器（蓝图函数）\n创建OSC客户端（蓝图函数）\n\n添加消息到束 （蓝图函数）\n添加束到束 （蓝图函数）\n\n从束中获取束 （蓝图函数）\n从束中获取消息（蓝图函数）\n\n清理消息（蓝图函数）\n清理束（蓝图函数）\n\n添加浮点值到OSC消息（蓝图函数）\n添加整数值到OSC消息（蓝图函数）\n添加64位整数值到OSC消息（蓝图函数）\n添加地址到OSC消息(蓝图函数）\n添加Blob到OSC消息（蓝图函数）\n添加bool到OSC消息（蓝图函数）\n\n获取OSC消息地址在index处（蓝图函数）\n获取OSC消息地址s（蓝图函数）\n\n获取OSC消息浮点值在index（蓝图函数）\n获取OSC消息浮点数组（蓝图函数）\n\n获取OSC消息整形值在index（蓝图函数）\n获取OSC消息整形数组（蓝图函数）\n\n获取OSC消息字符串在index（蓝图函数）\n获取OSC消息字符串组（蓝图函数）\n\n获取OSC消息bool在index（蓝图函数）\n获取OSC消息bool组（蓝图函数）\n\nOSC地址是否有值路径（蓝图函数）\nOSC地址是否有值形式（蓝图函数）\n\n转换字符串成OSC地址（蓝图函数）\n其他函数",
			"rawText": "OSC管理器\nUOSCManager 继承自：蓝图函数库\n创建OSC服务器（蓝图函数）\n创建OSC客户端（蓝图函数）\n\n添加消息到束 （蓝图函数）\n添加束到束 （蓝图函数）\n\n从束中获取束 （蓝图函数）\n从束中获取消息（蓝图函数）\n\n清理消息（蓝图函数）\n清理束（蓝图函数）\n\n添加浮点值到OSC消息（蓝图函数）\n添加整数值到OSC消息（蓝图函数）\n添加64位整数值到OSC消息（蓝图函数）\n添加地址到OSC消息(蓝图函数）\n添加Blob到OSC消息（蓝图函数）\n添加bool到OSC消息（蓝图函数）\n\n获取OSC消息地址在index处（蓝图函数）\n获取OSC消息地址s（蓝图函数）\n\n获取OSC消息浮点值在index（蓝图函数）\n获取OSC消息浮点数组（蓝图函数）\n\n获取OSC消息整形值在index（蓝图函数）\n获取OSC消息整形数组（蓝图函数）\n\n获取OSC消息字符串在index（蓝图函数）\n获取OSC消息字符串组（蓝图函数）\n\n获取OSC消息bool在index（蓝图函数）\n获取OSC消息bool组（蓝图函数）\n\nOSC地址是否有值路径（蓝图函数）\nOSC地址是否有值形式（蓝图函数）\n\n转换字符串成OSC地址（蓝图函数）\n其他函数",
			"fontSize": 28.006170253560988,
			"fontFamily": 1,
			"textAlign": "left",
			"verticalAlign": "top",
			"baseline": 1424,
			"containerId": "eu8bBa2q1oX2tg4OJRu16",
			"originalText": "OSC管理器\nUOSCManager 继承自：蓝图函数库\n创建OSC服务器（蓝图函数）\n创建OSC客户端（蓝图函数）\n\n添加消息到束 （蓝图函数）\n添加束到束 （蓝图函数）\n\n从束中获取束 （蓝图函数）\n从束中获取消息（蓝图函数）\n\n清理消息（蓝图函数）\n清理束（蓝图函数）\n\n添加浮点值到OSC消息（蓝图函数）\n添加整数值到OSC消息（蓝图函数）\n添加64位整数值到OSC消息（蓝图函数）\n添加地址到OSC消息(蓝图函数）\n添加Blob到OSC消息（蓝图函数）\n添加bool到OSC消息（蓝图函数）\n\n获取OSC消息地址在index处（蓝图函数）\n获取OSC消息地址s（蓝图函数）\n\n获取OSC消息浮点值在index（蓝图函数）\n获取OSC消息浮点数组（蓝图函数）\n\n获取OSC消息整形值在index（蓝图函数）\n获取OSC消息整形数组（蓝图函数）\n\n获取OSC消息字符串在index（蓝图函数）\n获取OSC消息字符串组（蓝图函数）\n\n获取OSC消息bool在index（蓝图函数）\n获取OSC消息bool组（蓝图函数）\n\nOSC地址是否有值路径（蓝图函数）\nOSC地址是否有值形式（蓝图函数）\n\n转换字符串成OSC地址（蓝图函数）\n其他函数"
		},
		{
			"id": "urCB6swQhVPwgwINpF47S",
			"type": "text",
			"x": 139.6292869105523,
			"y": 712.8462060414463,
			"width": 15,
			"height": 35,
			"angle": 0,
			"strokeColor": "#000000",
			"backgroundColor": "#7950f2",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"seed": 654374876,
			"version": 3,
			"versionNonce": 72195164,
			"isDeleted": true,
			"boundElements": null,
			"updated": 1654312914504,
			"link": null,
			"locked": false,
			"text": "",
			"rawText": "",
			"fontSize": 28,
			"fontFamily": 1,
			"textAlign": "left",
			"verticalAlign": "top",
			"baseline": 25,
			"containerId": null,
			"originalText": ""
		},
		{
			"id": "3zA2K7i6mlP3FE9IdSHNm",
			"type": "text",
			"x": 489.6292869105523,
			"y": 889.5128727081129,
			"width": 15,
			"height": 35,
			"angle": 0,
			"strokeColor": "#000000",
			"backgroundColor": "#7950f2",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"seed": 373512932,
			"version": 3,
			"versionNonce": 442392164,
			"isDeleted": true,
			"boundElements": null,
			"updated": 1654312915887,
			"link": null,
			"locked": false,
			"text": "",
			"rawText": "",
			"fontSize": 28,
			"fontFamily": 1,
			"textAlign": "left",
			"verticalAlign": "top",
			"baseline": 25,
			"containerId": null,
			"originalText": ""
		},
		{
			"id": "Ctl6Z9cN9LTXFplXHGo0L",
			"type": "text",
			"x": 596.2959535772188,
			"y": 702.8462060414463,
			"width": 15,
			"height": 35,
			"angle": 0,
			"strokeColor": "#000000",
			"backgroundColor": "#7950f2",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"seed": 1711551588,
			"version": 3,
			"versionNonce": 1070073828,
			"isDeleted": true,
			"boundElements": null,
			"updated": 1654312919304,
			"link": null,
			"locked": false,
			"text": "",
			"rawText": "",
			"fontSize": 28,
			"fontFamily": 1,
			"textAlign": "left",
			"verticalAlign": "top",
			"baseline": 25,
			"containerId": null,
			"originalText": ""
		},
		{
			"id": "PrfSbIlbzrwiOIPRdyk0P",
			"type": "text",
			"x": 539.6292869105523,
			"y": 702.8462060414463,
			"width": 15,
			"height": 35,
			"angle": 0,
			"strokeColor": "#000000",
			"backgroundColor": "#7950f2",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"seed": 19164380,
			"version": 3,
			"versionNonce": 339374428,
			"isDeleted": true,
			"boundElements": null,
			"updated": 1654312920449,
			"link": null,
			"locked": false,
			"text": "",
			"rawText": "",
			"fontSize": 28,
			"fontFamily": 1,
			"textAlign": "left",
			"verticalAlign": "top",
			"baseline": 25,
			"containerId": null,
			"originalText": ""
		},
		{
			"id": "VvBp3_EHSJ085QAsR8C-3",
			"type": "text",
			"x": 1199.3017061406954,
			"y": 829.3099371714103,
			"width": 15,
			"height": 35,
			"angle": 0,
			"strokeColor": "#000000",
			"backgroundColor": "#7950f2",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"seed": 631507428,
			"version": 3,
			"versionNonce": 2010197348,
			"isDeleted": true,
			"boundElements": null,
			"updated": 1654323628171,
			"link": null,
			"locked": false,
			"text": "",
			"rawText": "",
			"fontSize": 28,
			"fontFamily": 1,
			"textAlign": "left",
			"verticalAlign": "top",
			"baseline": 25,
			"containerId": null,
			"originalText": ""
		},
		{
			"id": "xLX5tb5u6fAB55QejCfuO",
			"type": "text",
			"x": 1166.8017061406954,
			"y": 779.3099371714103,
			"width": 15,
			"height": 35,
			"angle": 0,
			"strokeColor": "#000000",
			"backgroundColor": "#7950f2",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"seed": 292032348,
			"version": 3,
			"versionNonce": 1357235164,
			"isDeleted": true,
			"boundElements": null,
			"updated": 1654323629323,
			"link": null,
			"locked": false,
			"text": "",
			"rawText": "",
			"fontSize": 28,
			"fontFamily": 1,
			"textAlign": "left",
			"verticalAlign": "top",
			"baseline": 25,
			"containerId": null,
			"originalText": ""
		},
		{
			"id": "814IQ_x6cCKsh_As2r6Mp",
			"type": "text",
			"x": 1309.3017061406954,
			"y": 1176.8099371714102,
			"width": 15,
			"height": 35,
			"angle": 0,
			"strokeColor": "#000000",
			"backgroundColor": "#7950f2",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"seed": 1348960604,
			"version": 3,
			"versionNonce": 589755868,
			"isDeleted": true,
			"boundElements": null,
			"updated": 1654323629987,
			"link": null,
			"locked": false,
			"text": "",
			"rawText": "",
			"fontSize": 28,
			"fontFamily": 1,
			"textAlign": "left",
			"verticalAlign": "top",
			"baseline": 25,
			"containerId": null,
			"originalText": ""
		},
		{
			"id": "8GCjJJimQajTic6quVsIn",
			"type": "text",
			"x": 1615.3267915899141,
			"y": 776.9456641001212,
			"width": 15,
			"height": 35,
			"angle": 0,
			"strokeColor": "#000000",
			"backgroundColor": "#7950f2",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"seed": 1636337244,
			"version": 3,
			"versionNonce": 1407146716,
			"isDeleted": true,
			"boundElements": null,
			"updated": 1654323636972,
			"link": null,
			"locked": false,
			"text": "",
			"rawText": "",
			"fontSize": 28,
			"fontFamily": 1,
			"textAlign": "left",
			"verticalAlign": "top",
			"baseline": 25,
			"containerId": null,
			"originalText": ""
		}
	],
	"appState": {
		"theme": "light",
		"viewBackgroundColor": "#ffffff",
		"currentItemStrokeColor": "#000000",
		"currentItemBackgroundColor": "#7950f2",
		"currentItemFillStyle": "hachure",
		"currentItemStrokeWidth": 1,
		"currentItemStrokeStyle": "solid",
		"currentItemRoughness": 1,
		"currentItemOpacity": 100,
		"currentItemFontFamily": 1,
		"currentItemFontSize": 28,
		"currentItemTextAlign": "left",
		"currentItemStrokeSharpness": "sharp",
		"currentItemStartArrowhead": null,
		"currentItemEndArrowhead": "arrow",
		"currentItemLinearStrokeSharpness": "round",
		"gridSize": null,
		"colorPalette": {}
	},
	"files": {}
}
```
%%