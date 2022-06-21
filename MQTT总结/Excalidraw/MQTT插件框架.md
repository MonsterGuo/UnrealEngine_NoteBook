---

excalidraw-plugin: parsed
tags: [excalidraw]

---
==⚠  Switch to EXCALIDRAW VIEW in the MORE OPTIONS menu of this document. ⚠==


# Text Elements
 ^whMczjJq

MQTT插件 ^5EFIjP5t

一个客户端端有哪些必要元素 ^ppS2s0CN

1.服务端地址（必须的） ^UMv1bCTA

2.主题（topic）必须的 ^qhtBg88o

3.服务质量（QOS）必须的 ^inbNEOEl

链接选项：
mqtt的版本选择（）
清除会话（是否bool）
断连的时候是否发送消消息（bool,bool）
最大缓冲消息（最大缓冲消息数量）
删除最老的消息（）
保护链接的时间间隔（间隔）
自动重连（bool）
链接超时（超时）
用户名（字符串）
密码（数字也可以是字符串最终会转成二进制）
结束标识符（）
 ^VUKc1nYP

                     基础设置：
客户端名称：
客户端ID：
服务器地址：
端口：
用户名：
密码：
是否启用SSL/TLS：
        是使用CA证书/自定义证书

        自定义证书下：CA文件
                      客户端证书
                      客户端key文件
         ^d0hGTaSo

 ^d4DFyfuJ

                    高级设置
链接超时时长：秒
保持激活：秒
清除会话：bool
自动重连：bool
选择版本：复选（3.1，3.1.1，5.0） ^XTUdOmJC

                    遗嘱选项：
遗嘱消息的主题：topic
遗嘱消息的服务质量：QOS（复选框，0，1，2）
遗嘱消息保留标识：bool
遗嘱消息的消息体：消息体

 ^Dpe97lOP

消息的订阅 ^tFCFOs2n

消息的发送 ^Fxakm46Y

断开链接 ^0tdhP7uB

拿到客户端 ^AbpPY4jX

主题、消息体，服务质量 ^MsropNVn

创建一个主题对象：Topic设定（向哪个客户端客户端，主题，服务质量，返回值）
mqtt::topic top(cli, "test", QOS); ^TQWg8AiK

使用Topic.publish()发布消息
top.publish(std::move(payload)); ^sEr6mdFa

创建消息体：字符串形式的playload
string payload = to_string(++nsample) + "," +tmbuf + "," + to_string(x); ^20qK0Tir

通过主题对象发布消息 ^T69Px83M

使用cli客户端断开链接：cli.disconnect()->wait() ^Bpy2D2LP

遗嘱消息的创建：
message(主题，消息体，服务质量，返回值) ^vejOxQAt

客户端创建 ^FnKh0044

异步客户端创建：客户端cli创建形式
mqtt::async_client cli(SERVER_ADDRESS, CLIENT_ID); ^qgKZp42U

cli(服务端网址，客户端id，持久目录（可为空）) ^oU1CkRma

cli(服务端网址，客户端id，最大缓冲消息，持久目录（可为空）) ^YLeKeoP4

cli(服务端网址，客户端id，创建选项，持久目录（可为空）) ^L68uSPxO

创建选项：

获取发送当断连的时候（）查询用
设置发送当断连的时候（bool,bool）设置用

获取最大缓冲消息（）查询用
设置最大缓冲消息（int）设置用

mqtt版本（） 查询用
设置mqtt版本（int）设置用

删除最老消息（bool）设置用
保存持久消息（bool）设置用
持久内存的服务质量是否为0（bool）设置用
 ^lFnhDJyG

衍生产物：token令牌
用来检测消息是否发送完毕 ^8bfo06En

客户端开始消费：cli.start_consuming() ^YxqIa40V

客户端连接拿到令牌：tok=cli.connect(connOpts) ^7IGc8Gio

客户端的回复：rsp = tok—get_connect_response() ^DDz1wlX6

客户端是否已经注册了： 
 rsp.is_session_pressent() ^cpeH2TLr

客户端是否已经注册了： 
 cli.subscribe(Topic,Qos) ^PUBOuTKD

消息的获取：msg=cli.consume_message() ^wJgkMP1i

客户端是否连接：cli.is_connected() ^tcKueRbS

客户端取消订阅：cli.unsubscribe(TOPIC)->wait(); ^4ocBkhbI

客户端停止订阅：cli.stop_consuming(); ^U0cN4YIl

这里可以订阅多个主题，然后单独控制某个断连 ^k1ghZqul

异步客户端 ^kHRO2676

同步客户端 ^Qj9a5YrH

同步客户端创建
mqtt::client cli(SERVER_ADDRESS, CLIENT_ID); ^JivRfkwD

cli(服务端网址，客户端id，持久目录（可为空）) ^W2GyDGkS

cli(服务端网址，客户端id，最大缓冲消息，持久目录（可为空）) ^DOdxcSYA

cli(服务端网址，客户端id，创建选项，持久目录（可为空）) ^P6AKzMvb

创建选项：

获取发送当断连的时候（）查询用
设置发送当断连的时候（bool,bool）设置用

获取最大缓冲消息（）查询用
设置最大缓冲消息（int）设置用

mqtt版本（） 查询用
设置mqtt版本（int）设置用

删除最老消息（bool）设置用
保存持久消息（bool）设置用
持久内存的服务质量是否为0（bool）设置用
 ^FrbE6z4S

消息发布 ^FibcShlE

创建一个待发送的消息：
auto pubmsg = mqtt::make_message(Topic,payload) ^TmDl2q1Q

设置待发送消息的服务质量：QOS
pubmsg->set_qos(QOS); ^pnERv1Y3

通过客户端发布消息：
client.publish(pubmsg); ^txYWIx3N

通过创建消息发送 ^gb53u94V

创建一个消息指针：
mqtt::message_ptr pubmsg = mqtt::make_message(TOPIC, PAYLOAD1); ^7Tgk8UA0

设置消息的服务质量：
pubmsg->set_qos(QOS); ^Uug3Mo6O

客户端发布消息：
client.publish(pubmsg)->wait_for(TIMEOUT); ^9izVrYsD

创建一个Mqtt的消息指针 ^XVwCMPYY

创建一个消息令牌指针：
mqtt::delivery_token_ptr pubtok; ^zmeFs1Kb

通过客户端发布消息：
pubtok = client.publish(TOPIC, PAYLOAD2, strlen(PAYLOAD2), QOS, false);
pubtok->wait_for(TIMEOUT); ^oH0EzAic

通过一个发布令牌的指针： ^hwDmqf8v

定义一个action_listenter继承自iaction_listener ^UbabjnU3

创建一个动作监听器对象
action_listener listener; ^3W2uKtdb

创建发布消息的指针:
pubmsg = mqtt::make_message(TOPIC, PAYLOAD3); ^2f9CsroZ

通过客户端发布消息:
pubtok = client.publish(pubmsg, nullptr, listener);
                pubtok->wait(); ^EQ1p18EL

通过一个动作监听器 ^TZTolGjA

定义一个delivery_action_listener继承自action_listener ^lzvKw7tX

创建一个动作监听器对象
delivery_action_listener deliveryListener; ^y28nSWEv

创建发布消息的指针:
pubmsg = mqtt::make_message(TOPIC, PAYLOAD4); ^6RofVCT7

通过客户端发布消息:
client.publish(pubmsg, nullptr, deliveryListener);
while (!deliveryListener.is_done()) 
{                      
     this_thread::sleep_for(std::chrono::milliseconds(100));
} ^myDH7piu

通过一个动作监听器（基于原子操作拥有更好的多线程能力，拥有更好的内存调度能力，可以适度控制休眠时长） ^XtC6Pp7f

使用客户端接口发送：
client.publish(TOPIC, PAYLOAD2, strlen(PAYLOAD2)+1); ^pTjYWJUD

逐条的发送 ^0DkFlyID

使用客户端接口发送：
client.publish(mqtt::message(TOPIC, PAYLOAD3, QOS, false)); ^U0w7SUXg

通过一个监听器，没有token,没有“堆”的消息 ^lyCpVY9p

创建主题：
auto top = cli.get_topic("data/time", QOS); ^hJbvE6Af

通过主题发送：
top.publish(to_string(t)); ^bdlt7kNC

通过主题发送 ^qIfsi9Xh

消息订阅 ^xAb6Q5WT

客户端重连 ^8OuHSRRX

检测客户端链接状态
!cli.is_connected() ^35Zqspmw

客户端重连：
cli.reconnect(); ^56v5p5ID

客户端和链接选项设置
确定主题和服务质量QOS ^RlOz1F9g

设置链接回应 
mqtt::connect_response rsp = cli.connect(connOpts); ^0yWYDB1e

客户订阅设定：
cli.subscribe(TOPICS, QOS); ^FY2cEQRp

获取客户端消息：
auto msg = cli.consume_message(); ^NDrvLanB


# Embedded files
cfda0a84dac0978d1531272df5837e348fc25a20: [[Pasted Image 20220602225645_743.png]]
2afb138fffc8a31669f2b9490917a7fbba59847e: [[Pasted Image 20220602225753_309.png]]
3d865de549d64b089eb57a03bde0416ff08ab9fb: [[Pasted Image 20220602225816_878.png]]
b59e432443c35814b11a8de37a511f9fcba63549: [[Pasted Image 20220602230316_759.png]]
37b22e92ada111747b5678a89582cf4181a2b7e9: [[Pasted Image 20220602230723_671.png]]
6379942b0a6d661253a8e39dda33164911e81183: [[Image/Pasted Image 20220603073937_292.png]]

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
			"version": 652,
			"versionNonce": 98715740,
			"isDeleted": false,
			"id": "uUAFEbpVXYUeqfLtdzFbt",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -3367.025050314671,
			"y": 1299.5839929362369,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 770,
			"height": 225,
			"seed": 867684192,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [
				{
					"type": "text",
					"id": "5EFIjP5t"
				},
				{
					"id": "3ZYHc0ULg7f6QZ-qk8bO4",
					"type": "arrow"
				},
				{
					"id": "BWT3uZJqkWpsHh609M1vy",
					"type": "arrow"
				},
				{
					"id": "Qg-TGuMkrZRDOaiZ8grHc",
					"type": "arrow"
				},
				{
					"id": "9Xh8IsBqYvQoLdAqDRIQW",
					"type": "arrow"
				},
				{
					"id": "XcD6W0qWecTdEvGvGMyyE",
					"type": "arrow"
				},
				{
					"id": "vSGfYeepk2QgI7m7lnNlo",
					"type": "arrow"
				},
				{
					"id": "rMPbnJ4Dl_B8fGPLsIXcQ",
					"type": "arrow"
				}
			],
			"updated": 1654244965940,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 11,
			"versionNonce": 2141728348,
			"isDeleted": false,
			"id": "whMczjJq",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -294,
			"y": -195,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 11,
			"height": 25,
			"seed": 1778297696,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [],
			"updated": 1654242180964,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "",
			"rawText": "",
			"baseline": 18,
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": ""
		},
		{
			"type": "text",
			"version": 639,
			"versionNonce": 862866202,
			"isDeleted": false,
			"id": "5EFIjP5t",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -3362.025050314671,
			"y": 1389.0839929362369,
			"strokeColor": "#d9480f",
			"backgroundColor": "transparent",
			"width": 760,
			"height": 46,
			"seed": 377106272,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [],
			"updated": 1654494940363,
			"link": null,
			"locked": false,
			"fontSize": 36,
			"fontFamily": 1,
			"text": "MQTT插件",
			"rawText": "MQTT插件",
			"baseline": 32,
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "uUAFEbpVXYUeqfLtdzFbt",
			"originalText": "MQTT插件"
		},
		{
			"type": "arrow",
			"version": 2106,
			"versionNonce": 6936538,
			"isDeleted": false,
			"id": "3ZYHc0ULg7f6QZ-qk8bO4",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -2589.1303134725654,
			"y": 1432.4493816762595,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 2249.950165495655,
			"height": 1746.3797331851947,
			"seed": 1293546144,
			"groupIds": [],
			"strokeSharpness": "round",
			"boundElements": [],
			"updated": 1654494940364,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "uUAFEbpVXYUeqfLtdzFbt",
				"gap": 7.894736842105265,
				"focus": 0.7909063433587338
			},
			"endBinding": {
				"elementId": "k4Wfyyhj_3GNkvB6IOLXJ",
				"gap": 7.894736842105265,
				"focus": 0.7468785286591998
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
					2249.950165495655,
					-1746.3797331851947
				]
			]
		},
		{
			"type": "rectangle",
			"version": 151,
			"versionNonce": 1542531300,
			"isDeleted": false,
			"id": "k4Wfyyhj_3GNkvB6IOLXJ",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -331.2854111348056,
			"y": -362.5638959568844,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 368,
			"height": 50.2162324819962,
			"seed": 181841760,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [
				{
					"type": "text",
					"id": "ppS2s0CN"
				},
				{
					"id": "3ZYHc0ULg7f6QZ-qk8bO4",
					"type": "arrow"
				},
				{
					"id": "bZ1y17nEq7gOSGruWRIMs",
					"type": "arrow"
				},
				{
					"id": "OUD1_AyQh65-zG2rCmM8V",
					"type": "arrow"
				},
				{
					"id": "4Z1G1QJ18E64PfoI16Frl",
					"type": "arrow"
				},
				{
					"id": "-nIt49sTi6WvQG3QsoaQF",
					"type": "arrow"
				}
			],
			"updated": 1654242180964,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 160,
			"versionNonce": 479008710,
			"isDeleted": false,
			"id": "ppS2s0CN",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -326.2854111348056,
			"y": -349.95577971588625,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 358,
			"height": 25,
			"seed": 69107552,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [],
			"updated": 1654494940365,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "一个客户端端有哪些必要元素",
			"rawText": "一个客户端端有哪些必要元素",
			"baseline": 18,
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "k4Wfyyhj_3GNkvB6IOLXJ",
			"originalText": "一个客户端端有哪些必要元素"
		},
		{
			"type": "rectangle",
			"version": 71,
			"versionNonce": 1159883876,
			"isDeleted": false,
			"id": "2G2_Cbdau1EB8xZ4sKhzK",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 143.79541692168755,
			"y": -475.886957105519,
			"strokeColor": "#862e9c",
			"backgroundColor": "transparent",
			"width": 345.1959682633749,
			"height": 56,
			"seed": 1183204000,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [
				{
					"id": "bZ1y17nEq7gOSGruWRIMs",
					"type": "arrow"
				},
				{
					"type": "text",
					"id": "UMv1bCTA"
				}
			],
			"updated": 1654242180964,
			"link": null,
			"locked": false
		},
		{
			"type": "arrow",
			"version": 482,
			"versionNonce": 1138896646,
			"isDeleted": false,
			"id": "bZ1y17nEq7gOSGruWRIMs",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 40.129797035065735,
			"y": -345.5560278841606,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 101.52821636726131,
			"height": 102.74600060271382,
			"seed": 1780656992,
			"groupIds": [],
			"strokeSharpness": "round",
			"boundElements": [],
			"updated": 1654494940366,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "k4Wfyyhj_3GNkvB6IOLXJ",
				"gap": 3.4152081698713346,
				"focus": 0.8592046154774975
			},
			"endBinding": {
				"elementId": "2G2_Cbdau1EB8xZ4sKhzK",
				"gap": 2.1374035193605323,
				"focus": 0.8745640128592237
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
					101.52821636726131,
					-102.74600060271382
				]
			]
		},
		{
			"type": "text",
			"version": 102,
			"versionNonce": 98610266,
			"isDeleted": false,
			"id": "UMv1bCTA",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 148.79541692168755,
			"y": -460.386957105519,
			"strokeColor": "#862e9c",
			"backgroundColor": "transparent",
			"width": 335.1959682633749,
			"height": 25,
			"seed": 69596000,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [],
			"updated": 1654494940366,
			"link": null,
			"locked": false,
			"fontSize": 20.03511932953224,
			"fontFamily": 1,
			"text": "1.服务端地址（必须的）",
			"rawText": "1.服务端地址（必须的）",
			"baseline": 18,
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "2G2_Cbdau1EB8xZ4sKhzK",
			"originalText": "1.服务端地址（必须的）"
		},
		{
			"type": "rectangle",
			"version": 102,
			"versionNonce": 2048925788,
			"isDeleted": false,
			"id": "fD7_UjMxiuwScA0gYJYLp",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 141.65801340232701,
			"y": -394.6643595506953,
			"strokeColor": "#862e9c",
			"backgroundColor": "transparent",
			"width": 355,
			"height": 51.29847944765015,
			"seed": 1084076896,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [
				{
					"id": "OUD1_AyQh65-zG2rCmM8V",
					"type": "arrow"
				},
				{
					"type": "text",
					"id": "qhtBg88o"
				}
			],
			"updated": 1654242180964,
			"link": null,
			"locked": false
		},
		{
			"type": "arrow",
			"version": 619,
			"versionNonce": 813568282,
			"isDeleted": false,
			"id": "OUD1_AyQh65-zG2rCmM8V",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 43.061217502207626,
			"y": -332.7253900557215,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 96.18454449542438,
			"height": 21.535241875519546,
			"seed": 1429459616,
			"groupIds": [],
			"strokeSharpness": "round",
			"boundElements": [],
			"updated": 1654494940367,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "k4Wfyyhj_3GNkvB6IOLXJ",
				"gap": 6.3466286370133105,
				"focus": 0.7140969096807492
			},
			"endBinding": {
				"elementId": "fD7_UjMxiuwScA0gYJYLp",
				"gap": 2.412251404695013,
				"focus": 0.390376729122353
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
					96.18454449542438,
					-21.535241875519546
				]
			]
		},
		{
			"type": "text",
			"version": 82,
			"versionNonce": 721069446,
			"isDeleted": false,
			"id": "qhtBg88o",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 146.65801340232701,
			"y": -381.5151198268702,
			"strokeColor": "#862e9c",
			"backgroundColor": "transparent",
			"width": 345,
			"height": 25,
			"seed": 413301408,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [],
			"updated": 1654494940367,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "2.主题（topic）必须的",
			"rawText": "2.主题（topic）必须的",
			"baseline": 18,
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "fD7_UjMxiuwScA0gYJYLp",
			"originalText": "2.主题（topic）必须的"
		},
		{
			"type": "rectangle",
			"version": 145,
			"versionNonce": 1869846244,
			"isDeleted": false,
			"id": "GkqKovVFnVg84YeKWB2Z8",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 129.90221250912657,
			"y": -290.9986988957147,
			"strokeColor": "#862e9c",
			"backgroundColor": "transparent",
			"width": 355,
			"height": 43.817424440632294,
			"seed": 1103029088,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [
				{
					"id": "4Z1G1QJ18E64PfoI16Frl",
					"type": "arrow"
				},
				{
					"type": "text",
					"id": "inbNEOEl"
				}
			],
			"updated": 1654242180964,
			"link": null,
			"locked": false
		},
		{
			"type": "arrow",
			"version": 679,
			"versionNonce": 1356334278,
			"isDeleted": false,
			"id": "4Z1G1QJ18E64PfoI16Frl",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 43.335983850824476,
			"y": -316.58491728727086,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 82.29142161958112,
			"height": 39.87372430610992,
			"seed": 1257425760,
			"groupIds": [],
			"strokeSharpness": "round",
			"boundElements": [],
			"updated": 1654494940368,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "k4Wfyyhj_3GNkvB6IOLXJ",
				"gap": 6.621394985630104,
				"focus": -0.625685912911155
			},
			"endBinding": {
				"elementId": "GkqKovVFnVg84YeKWB2Z8",
				"gap": 4.274807038720951,
				"focus": -0.7455537098276913
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
					82.29142161958112,
					39.87372430610992
				]
			]
		},
		{
			"type": "text",
			"version": 121,
			"versionNonce": 1277956762,
			"isDeleted": false,
			"id": "inbNEOEl",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 134.90221250912657,
			"y": -281.58998667539856,
			"strokeColor": "#862e9c",
			"backgroundColor": "transparent",
			"width": 345,
			"height": 25,
			"seed": 149180256,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [],
			"updated": 1654494940368,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "3.服务质量（QOS）必须的",
			"rawText": "3.服务质量（QOS）必须的",
			"baseline": 18,
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "GkqKovVFnVg84YeKWB2Z8",
			"originalText": "3.服务质量（QOS）必须的"
		},
		{
			"type": "rectangle",
			"version": 385,
			"versionNonce": 322514396,
			"isDeleted": false,
			"id": "YQbgDJMINHxWvDWL7cERK",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 127.594725562382,
			"y": -175.92919882726233,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 738,
			"height": 467,
			"seed": 1916432032,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [
				{
					"id": "-nIt49sTi6WvQG3QsoaQF",
					"type": "arrow"
				},
				{
					"type": "text",
					"id": "VUKc1nYP"
				},
				{
					"id": "iwK2whagKYUQg2EBZAw_I",
					"type": "arrow"
				},
				{
					"id": "t0IERd3XYJofWcNKBAe2Q",
					"type": "arrow"
				},
				{
					"id": "KiCHatPnuMXvuiBUiFwCP",
					"type": "arrow"
				},
				{
					"id": "5-2ndW63UVS8MdqQvL4Le",
					"type": "arrow"
				}
			],
			"updated": 1654242180964,
			"link": null,
			"locked": false
		},
		{
			"type": "arrow",
			"version": 1144,
			"versionNonce": 1560457050,
			"isDeleted": false,
			"id": "-nIt49sTi6WvQG3QsoaQF",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 7.9274952923841795,
			"y": -296.3476634748881,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 103.66723026999782,
			"height": 498.5587092621306,
			"seed": 1588179616,
			"groupIds": [],
			"strokeSharpness": "round",
			"boundElements": [],
			"updated": 1654494940369,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "k4Wfyyhj_3GNkvB6IOLXJ",
				"gap": 16,
				"focus": -0.7751003938428374
			},
			"endBinding": {
				"elementId": "YQbgDJMINHxWvDWL7cERK",
				"gap": 16,
				"focus": -0.9940679305073734
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
					103.66723026999782,
					498.5587092621306
				]
			]
		},
		{
			"type": "text",
			"version": 810,
			"versionNonce": 163264582,
			"isDeleted": false,
			"id": "VUKc1nYP",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 132.594725562382,
			"y": -169.92919882726233,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 728,
			"height": 455,
			"seed": 936574624,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [],
			"updated": 1654494940371,
			"link": null,
			"locked": false,
			"fontSize": 28,
			"fontFamily": 1,
			"text": "链接选项：\nmqtt的版本选择（）\n清除会话（是否bool）\n断连的时候是否发送消消息（bool,bool）\n最大缓冲消息（最大缓冲消息数量）\n删除最老的消息（）\n保护链接的时间间隔（间隔）\n自动重连（bool）\n链接超时（超时）\n用户名（字符串）\n密码（数字也可以是字符串最终会转成二进制）\n结束标识符（）\n",
			"rawText": "链接选项：\nmqtt的版本选择（）\n清除会话（是否bool）\n断连的时候是否发送消消息（bool,bool）\n最大缓冲消息（最大缓冲消息数量）\n删除最老的消息（）\n保护链接的时间间隔（间隔）\n自动重连（bool）\n链接超时（超时）\n用户名（字符串）\n密码（数字也可以是字符串最终会转成二进制）\n结束标识符（）\n",
			"baseline": 444,
			"textAlign": "left",
			"verticalAlign": "middle",
			"containerId": "YQbgDJMINHxWvDWL7cERK",
			"originalText": "链接选项：\nmqtt的版本选择（）\n清除会话（是否bool）\n断连的时候是否发送消消息（bool,bool）\n最大缓冲消息（最大缓冲消息数量）\n删除最老的消息（）\n保护链接的时间间隔（间隔）\n自动重连（bool）\n链接超时（超时）\n用户名（字符串）\n密码（数字也可以是字符串最终会转成二进制）\n结束标识符（）\n"
		},
		{
			"type": "image",
			"version": 54,
			"versionNonce": 837210468,
			"isDeleted": false,
			"id": "gG9iQIU-vHPWbIPZ52mGy",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 1213.2611480884225,
			"y": -486.59584514887683,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"width": 819,
			"height": 477,
			"seed": 624159392,
			"groupIds": [],
			"strokeSharpness": "round",
			"boundElements": [
				{
					"id": "iwK2whagKYUQg2EBZAw_I",
					"type": "arrow"
				},
				{
					"id": "fqEwkd2oF1MTNceyU9DEY",
					"type": "arrow"
				}
			],
			"updated": 1654242180964,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "cfda0a84dac0978d1531272df5837e348fc25a20",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "arrow",
			"version": 244,
			"versionNonce": 2053616666,
			"isDeleted": false,
			"id": "iwK2whagKYUQg2EBZAw_I",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 892.7611480884227,
			"y": -90.09581463129882,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 312.0001220703123,
			"height": 151.99996948242176,
			"seed": 1280839520,
			"groupIds": [],
			"strokeSharpness": "round",
			"boundElements": [],
			"updated": 1654494940369,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "YQbgDJMINHxWvDWL7cERK",
				"gap": 27.16642252604072,
				"focus": 0.10970435928167521
			},
			"endBinding": {
				"elementId": "gG9iQIU-vHPWbIPZ52mGy",
				"gap": 8.4998779296875,
				"focus": 0.45123478965784625
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
					312.0001220703123,
					-151.99996948242176
				]
			]
		},
		{
			"type": "image",
			"version": 69,
			"versionNonce": 256836836,
			"isDeleted": false,
			"id": "YETT2lHWhNeom8PqYs-4U",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 1211.4607940845162,
			"y": 319.2041273853026,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"width": 833,
			"height": 377,
			"seed": 1430953824,
			"groupIds": [],
			"strokeSharpness": "round",
			"boundElements": [
				{
					"id": "t0IERd3XYJofWcNKBAe2Q",
					"type": "arrow"
				},
				{
					"id": "Ed6CpErONQfJuL2xZpiP5",
					"type": "arrow"
				}
			],
			"updated": 1654242180964,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "2afb138fffc8a31669f2b9490917a7fbba59847e",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "arrow",
			"version": 281,
			"versionNonce": 1447960794,
			"isDeleted": false,
			"id": "t0IERd3XYJofWcNKBAe2Q",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 882.7609955005323,
			"y": 96.04328950356779,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 311.1998596191404,
			"height": 297.76784124048794,
			"seed": 1390030496,
			"groupIds": [],
			"strokeSharpness": "round",
			"boundElements": [],
			"updated": 1654494940370,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "YQbgDJMINHxWvDWL7cERK",
				"gap": 17.16626993815032,
				"focus": -0.5643388666747904
			},
			"endBinding": {
				"elementId": "YETT2lHWhNeom8PqYs-4U",
				"gap": 17.499938964843523,
				"focus": -0.5133949027460685
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
					311.1998596191404,
					297.76784124048794
				]
			]
		},
		{
			"type": "image",
			"version": 76,
			"versionNonce": 856678236,
			"isDeleted": false,
			"id": "a3HDqFKD5yeNNxzRyYv3t",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 1214.5772938297264,
			"y": 788.0041456958495,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"width": 663.767366720517,
			"height": 506,
			"seed": 54157152,
			"groupIds": [],
			"strokeSharpness": "round",
			"boundElements": [
				{
					"id": "KiCHatPnuMXvuiBUiFwCP",
					"type": "arrow"
				},
				{
					"id": "-o4fmKHaP0iLcrgNPBpPG",
					"type": "arrow"
				}
			],
			"updated": 1654312149994,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "3d865de549d64b089eb57a03bde0416ff08ab9fb",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "arrow",
			"version": 266,
			"versionNonce": 1816720794,
			"isDeleted": false,
			"id": "KiCHatPnuMXvuiBUiFwCP",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 874.7609649829542,
			"y": 270.86854423383005,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 325.2000732421873,
			"height": 669.7936412801778,
			"seed": 1789081440,
			"groupIds": [],
			"strokeSharpness": "round",
			"boundElements": [],
			"updated": 1654494940370,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "YQbgDJMINHxWvDWL7cERK",
				"gap": 9.166239420572197,
				"focus": -0.5692840977593915
			},
			"endBinding": {
				"elementId": "a3HDqFKD5yeNNxzRyYv3t",
				"gap": 14.616255604585035,
				"focus": -0.6548667543777493
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
					325.2000732421873,
					669.7936412801778
				]
			]
		},
		{
			"type": "rectangle",
			"version": 114,
			"versionNonce": 1895177188,
			"isDeleted": false,
			"id": "MsI0FIvOpX7HDLGxAlEe4",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 2450.1181251808202,
			"y": -472.9623943228679,
			"strokeColor": "#1864ab",
			"backgroundColor": "transparent",
			"width": 747,
			"height": 504,
			"seed": 1820957536,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [
				{
					"id": "fqEwkd2oF1MTNceyU9DEY",
					"type": "arrow"
				},
				{
					"type": "text",
					"id": "d0hGTaSo"
				}
			],
			"updated": 1654242180964,
			"link": null,
			"locked": false
		},
		{
			"type": "arrow",
			"version": 396,
			"versionNonce": 393756550,
			"isDeleted": false,
			"id": "fqEwkd2oF1MTNceyU9DEY",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 2046.0160834294377,
			"y": -206.34357795121826,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 390.1820135763171,
			"height": 16.609047695895242,
			"seed": 905106272,
			"groupIds": [],
			"strokeSharpness": "round",
			"boundElements": [],
			"updated": 1654494940372,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "gG9iQIU-vHPWbIPZ52mGy",
				"gap": 13.754935341015246,
				"focus": 0.2335358325292454
			},
			"endBinding": {
				"elementId": "MsI0FIvOpX7HDLGxAlEe4",
				"gap": 13.920028175065184,
				"focus": 0.06898761369013896
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
					390.1820135763171,
					-16.609047695895242
				]
			]
		},
		{
			"type": "text",
			"version": 444,
			"versionNonce": 1792140250,
			"isDeleted": false,
			"id": "d0hGTaSo",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 2455.1181251808202,
			"y": -467.9623943228679,
			"strokeColor": "#1864ab",
			"backgroundColor": "transparent",
			"width": 737,
			"height": 490,
			"seed": 1905325728,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [],
			"updated": 1654494940373,
			"link": null,
			"locked": false,
			"fontSize": 28,
			"fontFamily": 1,
			"text": "                     基础设置：\n客户端名称：\n客户端ID：\n服务器地址：\n端口：\n用户名：\n密码：\n是否启用SSL/TLS：\n        是使用CA证书/自定义证书\n\n        自定义证书下：CA文件\n                      客户端证书\n                      客户端key文件\n        ",
			"rawText": "                     基础设置：\n客户端名称：\n客户端ID：\n服务器地址：\n端口：\n用户名：\n密码：\n是否启用SSL/TLS：\n        是使用CA证书/自定义证书\n\n        自定义证书下：CA文件\n                      客户端证书\n                      客户端key文件\n        ",
			"baseline": 479,
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": "MsI0FIvOpX7HDLGxAlEe4",
			"originalText": "                     基础设置：\n客户端名称：\n客户端ID：\n服务器地址：\n端口：\n用户名：\n密码：\n是否启用SSL/TLS：\n        是使用CA证书/自定义证书\n\n        自定义证书下：CA文件\n                      客户端证书\n                      客户端key文件\n        "
		},
		{
			"type": "image",
			"version": 170,
			"versionNonce": 1108089052,
			"isDeleted": false,
			"id": "aI6SIiO3DKMzaRSscr3Ry",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 1199.9847430193622,
			"y": 49.27093290694961,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"width": 792,
			"height": 175,
			"seed": 316706656,
			"groupIds": [],
			"strokeSharpness": "round",
			"boundElements": [
				{
					"id": "5-2ndW63UVS8MdqQvL4Le",
					"type": "arrow"
				},
				{
					"id": "Ij5p31ta_1hxVyUdpi-g-",
					"type": "arrow"
				}
			],
			"updated": 1654242180964,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "b59e432443c35814b11a8de37a511f9fcba63549",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "arrow",
			"version": 441,
			"versionNonce": 1300968026,
			"isDeleted": false,
			"id": "5-2ndW63UVS8MdqQvL4Le",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 875.1846941912373,
			"y": -4.222017426286783,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 315.1999511718749,
			"height": 154.73995705796372,
			"seed": 1588137632,
			"groupIds": [],
			"strokeSharpness": "round",
			"boundElements": [],
			"updated": 1654494940370,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "YQbgDJMINHxWvDWL7cERK",
				"gap": 9.589968628855218,
				"focus": -0.59725435646019
			},
			"endBinding": {
				"elementId": "aI6SIiO3DKMzaRSscr3Ry",
				"gap": 9.60009765625,
				"focus": -0.7550962040710846
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
					315.1999511718749,
					154.73995705796372
				]
			]
		},
		{
			"type": "image",
			"version": 77,
			"versionNonce": 860659036,
			"isDeleted": false,
			"id": "OZPUfZwG4jUYyK9IGzrI_",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 2456.5847186052997,
			"y": 91.97094511398086,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"width": 818,
			"height": 244,
			"seed": 476071584,
			"groupIds": [],
			"strokeSharpness": "round",
			"boundElements": [
				{
					"id": "Ij5p31ta_1hxVyUdpi-g-",
					"type": "arrow"
				}
			],
			"updated": 1654242180964,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "37b22e92ada111747b5678a89582cf4181a2b7e9",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "arrow",
			"version": 287,
			"versionNonce": 1801156196,
			"isDeleted": false,
			"id": "Ij5p31ta_1hxVyUdpi-g-",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 2019.1545267468236,
			"y": 164.15820498753186,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 422.43019185847606,
			"height": 68.46942580560636,
			"seed": 1281380000,
			"groupIds": [],
			"strokeSharpness": "round",
			"boundElements": [],
			"updated": 1654242180964,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "aI6SIiO3DKMzaRSscr3Ry",
				"focus": -0.2788331554789979,
				"gap": 27.169783727461436
			},
			"endBinding": {
				"elementId": "OZPUfZwG4jUYyK9IGzrI_",
				"focus": -0.46406791259186736,
				"gap": 15
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
					422.43019185847606,
					68.46942580560636
				]
			]
		},
		{
			"type": "rectangle",
			"version": 247,
			"versionNonce": 587764188,
			"isDeleted": false,
			"id": "twtKwslo8fG6CkYjGe4Cc",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 2460.7846697771747,
			"y": 416.3709084928871,
			"strokeColor": "#1864ab",
			"backgroundColor": "transparent",
			"width": 785.599853515625,
			"height": 388.79998779296875,
			"seed": 1377009312,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [
				{
					"id": "Ed6CpErONQfJuL2xZpiP5",
					"type": "arrow"
				},
				{
					"type": "text",
					"id": "XTUdOmJC"
				}
			],
			"updated": 1654242180964,
			"link": null,
			"locked": false
		},
		{
			"type": "arrow",
			"version": 612,
			"versionNonce": 1633441946,
			"isDeleted": false,
			"id": "Ed6CpErONQfJuL2xZpiP5",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 2059.1848162615497,
			"y": 510.27712203002443,
			"strokeColor": "#1864ab",
			"backgroundColor": "transparent",
			"width": 400.599853515625,
			"height": 100.13309575771723,
			"seed": 1771379552,
			"groupIds": [],
			"strokeSharpness": "round",
			"boundElements": [],
			"updated": 1654494940374,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "YETT2lHWhNeom8PqYs-4U",
				"gap": 14.724022177033476,
				"focus": -0.35957679541447696
			},
			"endBinding": {
				"elementId": "twtKwslo8fG6CkYjGe4Cc",
				"gap": 1,
				"focus": -0.3351957205593829
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
					400.599853515625,
					100.13309575771723
				]
			]
		},
		{
			"type": "text",
			"version": 11,
			"versionNonce": 273806940,
			"isDeleted": false,
			"id": "d4DFyfuJ",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 2614.3847674334247,
			"y": 425.0709817350746,
			"strokeColor": "#1864ab",
			"backgroundColor": "transparent",
			"width": 15,
			"height": 35,
			"seed": 715468640,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [],
			"updated": 1654242180964,
			"link": null,
			"locked": false,
			"fontSize": 28,
			"fontFamily": 1,
			"text": "",
			"rawText": "",
			"baseline": 25,
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": ""
		},
		{
			"type": "text",
			"version": 334,
			"versionNonce": 866555398,
			"isDeleted": false,
			"id": "XTUdOmJC",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 2465.7846697771747,
			"y": 421.3709084928871,
			"strokeColor": "#1864ab",
			"backgroundColor": "transparent",
			"width": 775.599853515625,
			"height": 210,
			"seed": 1438680928,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [],
			"updated": 1654494940374,
			"link": null,
			"locked": false,
			"fontSize": 28.15205760470095,
			"fontFamily": 1,
			"text": "                    高级设置\n链接超时时长：秒\n保持激活：秒\n清除会话：bool\n自动重连：bool\n选择版本：复选（3.1，3.1.1，5.0）",
			"rawText": "                    高级设置\n链接超时时长：秒\n保持激活：秒\n清除会话：bool\n自动重连：bool\n选择版本：复选（3.1，3.1.1，5.0）",
			"baseline": 199,
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": "twtKwslo8fG6CkYjGe4Cc",
			"originalText": "                    高级设置\n链接超时时长：秒\n保持激活：秒\n清除会话：bool\n自动重连：bool\n选择版本：复选（3.1，3.1.1，5.0）"
		},
		{
			"type": "rectangle",
			"version": 82,
			"versionNonce": 1207618268,
			"isDeleted": false,
			"id": "lHhTlR9xXNGpB0RbCkm80",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 2471.9851092302997,
			"y": 903.1709573210121,
			"strokeColor": "#1864ab",
			"backgroundColor": "transparent",
			"width": 768,
			"height": 304,
			"seed": 1076926304,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [
				{
					"id": "-o4fmKHaP0iLcrgNPBpPG",
					"type": "arrow"
				},
				{
					"type": "text",
					"id": "Dpe97lOP"
				},
				{
					"id": "flHQ6_BUaUxmEBKfYakXI",
					"type": "arrow"
				}
			],
			"updated": 1654242180964,
			"link": null,
			"locked": false
		},
		{
			"type": "arrow",
			"version": 235,
			"versionNonce": 800187718,
			"isDeleted": false,
			"id": "-o4fmKHaP0iLcrgNPBpPG",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 1889.5848406756127,
			"y": 1047.5854789832404,
			"strokeColor": "#1864ab",
			"backgroundColor": "transparent",
			"width": 566.400268554687,
			"height": 2.47625655053389,
			"seed": 1345414816,
			"groupIds": [],
			"strokeSharpness": "round",
			"boundElements": [],
			"updated": 1654494940375,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "a3HDqFKD5yeNNxzRyYv3t",
				"gap": 11.240180125368738,
				"focus": 0.031760316487124796
			},
			"endBinding": {
				"elementId": "lHhTlR9xXNGpB0RbCkm80",
				"gap": 16,
				"focus": 0.07685185911998924
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
					566.400268554687,
					-2.47625655053389
				]
			]
		},
		{
			"type": "text",
			"version": 304,
			"versionNonce": 2044471002,
			"isDeleted": false,
			"id": "Dpe97lOP",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 2476.9851092302997,
			"y": 908.1709573210121,
			"strokeColor": "#1864ab",
			"backgroundColor": "transparent",
			"width": 758,
			"height": 245,
			"seed": 2035308384,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [],
			"updated": 1654494940376,
			"link": null,
			"locked": false,
			"fontSize": 28,
			"fontFamily": 1,
			"text": "                    遗嘱选项：\n遗嘱消息的主题：topic\n遗嘱消息的服务质量：QOS（复选框，0，1，2）\n遗嘱消息保留标识：bool\n遗嘱消息的消息体：消息体\n\n",
			"rawText": "                    遗嘱选项：\n遗嘱消息的主题：topic\n遗嘱消息的服务质量：QOS（复选框，0，1，2）\n遗嘱消息保留标识：bool\n遗嘱消息的消息体：消息体\n\n",
			"baseline": 235,
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": "lHhTlR9xXNGpB0RbCkm80",
			"originalText": "                    遗嘱选项：\n遗嘱消息的主题：topic\n遗嘱消息的服务质量：QOS（复选框，0，1，2）\n遗嘱消息保留标识：bool\n遗嘱消息的消息体：消息体\n\n"
		},
		{
			"type": "rectangle",
			"version": 469,
			"versionNonce": 1586177124,
			"isDeleted": false,
			"id": "MRiydNpb-CXQiejwi0ni4",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -102.54806337712171,
			"y": 4907.837262863004,
			"strokeColor": "#e67700",
			"backgroundColor": "transparent",
			"width": 616.0000610351562,
			"height": 207.9998779296875,
			"seed": 757895008,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [
				{
					"id": "BWT3uZJqkWpsHh609M1vy",
					"type": "arrow"
				},
				{
					"type": "text",
					"id": "tFCFOs2n"
				},
				{
					"id": "in63DlygZ2DKeLyRmwRs7",
					"type": "arrow"
				}
			],
			"updated": 1654242180964,
			"link": null,
			"locked": false
		},
		{
			"type": "arrow",
			"version": 1973,
			"versionNonce": 1359557382,
			"isDeleted": false,
			"id": "BWT3uZJqkWpsHh609M1vy",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1332.2103879092408,
			"y": 1932.3352077586608,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 1216.5080371078657,
			"height": 2946.3418765784063,
			"seed": 344445600,
			"groupIds": [],
			"strokeSharpness": "round",
			"boundElements": [],
			"updated": 1654494940408,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "m-xpFu4AdPvg479-leXh1",
				"gap": 11.464320882391121,
				"focus": -0.6887355868133548
			},
			"endBinding": {
				"elementId": "MRiydNpb-CXQiejwi0ni4",
				"gap": 31.9898622895505,
				"focus": -0.7584598973377541
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
					1216.5080371078657,
					2946.3418765784063
				]
			]
		},
		{
			"type": "text",
			"version": 451,
			"versionNonce": 1382683206,
			"isDeleted": false,
			"id": "tFCFOs2n",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -97.54806337712171,
			"y": 4988.837201827848,
			"strokeColor": "#e67700",
			"backgroundColor": "transparent",
			"width": 606.0000610351562,
			"height": 46,
			"seed": 1780177760,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [],
			"updated": 1654494940377,
			"link": null,
			"locked": false,
			"fontSize": 36.0000072517021,
			"fontFamily": 1,
			"text": "消息的订阅",
			"rawText": "消息的订阅",
			"baseline": 32,
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "MRiydNpb-CXQiejwi0ni4",
			"originalText": "消息的订阅"
		},
		{
			"type": "rectangle",
			"version": 294,
			"versionNonce": 683090566,
			"isDeleted": false,
			"id": "Oo7fZ1Osv6j7xfCZ9E1fo",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -173.88091860173148,
			"y": 2705.837191655323,
			"strokeColor": "#e67700",
			"backgroundColor": "transparent",
			"width": 672,
			"height": 183.99993896484375,
			"seed": 591021920,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [
				{
					"id": "Qg-TGuMkrZRDOaiZ8grHc",
					"type": "arrow"
				},
				{
					"type": "text",
					"id": "Fxakm46Y"
				},
				{
					"id": "X00OV73xWVzaIt3qG2fwQ",
					"type": "arrow"
				}
			],
			"updated": 1654495224278,
			"link": null,
			"locked": false
		},
		{
			"type": "arrow",
			"version": 1573,
			"versionNonce": 940541338,
			"isDeleted": false,
			"id": "Qg-TGuMkrZRDOaiZ8grHc",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1297.48278631897,
			"y": 1859.7456094268127,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 1094.5963071297222,
			"height": 909.5959481239488,
			"seed": 614281056,
			"groupIds": [],
			"strokeSharpness": "round",
			"boundElements": [],
			"updated": 1654495224278,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "m-xpFu4AdPvg479-leXh1",
				"gap": 14.462427643729598,
				"focus": -0.7003646571073038
			},
			"endBinding": {
				"elementId": "Oo7fZ1Osv6j7xfCZ9E1fo",
				"gap": 29.005560587516356,
				"focus": -0.7403306894793689
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
					1094.5963071297222,
					909.5959481239488
				]
			]
		},
		{
			"type": "text",
			"version": 313,
			"versionNonce": 1000779994,
			"isDeleted": false,
			"id": "Fxakm46Y",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -168.88091860173148,
			"y": 2774.8371611377447,
			"strokeColor": "#e67700",
			"backgroundColor": "transparent",
			"width": 662,
			"height": 46,
			"seed": 876266336,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [],
			"updated": 1654495224278,
			"link": null,
			"locked": false,
			"fontSize": 36,
			"fontFamily": 1,
			"text": "消息的发送",
			"rawText": "消息的发送",
			"baseline": 32,
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "Oo7fZ1Osv6j7xfCZ9E1fo",
			"originalText": "消息的发送"
		},
		{
			"type": "rectangle",
			"version": 513,
			"versionNonce": 1434742748,
			"isDeleted": false,
			"id": "N4lOwtxP9gyC4NQ9g_NTg",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1513.5473106101945,
			"y": 10114.338346237028,
			"strokeColor": "#e67700",
			"backgroundColor": "transparent",
			"width": 694.0000915527344,
			"height": 173.99993896484375,
			"seed": 1857552224,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [
				{
					"id": "9Xh8IsBqYvQoLdAqDRIQW",
					"type": "arrow"
				},
				{
					"type": "text",
					"id": "0tdhP7uB"
				},
				{
					"id": "VId7fjOJBPONK_GPdxvCp",
					"type": "arrow"
				}
			],
			"updated": 1654244851672,
			"link": null,
			"locked": false
		},
		{
			"type": "arrow",
			"version": 1874,
			"versionNonce": 1326168922,
			"isDeleted": false,
			"id": "9Xh8IsBqYvQoLdAqDRIQW",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -2817.3261276698377,
			"y": 1547.7396997006063,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 1341.9399440934524,
			"height": 8560.598585501266,
			"seed": 1240407712,
			"groupIds": [],
			"strokeSharpness": "round",
			"boundElements": [],
			"updated": 1654494940379,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "uUAFEbpVXYUeqfLtdzFbt",
				"gap": 23.155706764369597,
				"focus": -0.3562376743922029
			},
			"endBinding": {
				"elementId": "N4lOwtxP9gyC4NQ9g_NTg",
				"gap": 6.00006103515625,
				"focus": -0.8159441765765417
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
					1341.9399440934524,
					8560.598585501266
				]
			]
		},
		{
			"type": "text",
			"version": 463,
			"versionNonce": 37217926,
			"isDeleted": false,
			"id": "0tdhP7uB",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1508.5473106101945,
			"y": 10178.33831571945,
			"strokeColor": "#e67700",
			"backgroundColor": "transparent",
			"width": 684.0000915527344,
			"height": 46,
			"seed": 1409829536,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [],
			"updated": 1654494940379,
			"link": null,
			"locked": false,
			"fontSize": 36.000004818564975,
			"fontFamily": 1,
			"text": "断开链接",
			"rawText": "断开链接",
			"baseline": 32,
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "N4lOwtxP9gyC4NQ9g_NTg",
			"originalText": "断开链接"
		},
		{
			"type": "rectangle",
			"version": 473,
			"versionNonce": 573830620,
			"isDeleted": false,
			"id": "xalqx3Solpn8KKQWo_zWx",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 1136.4525876645453,
			"y": 4925.337949508512,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 495,
			"height": 102,
			"seed": 534453920,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [
				{
					"id": "in63DlygZ2DKeLyRmwRs7",
					"type": "arrow"
				},
				{
					"type": "text",
					"id": "AbpPY4jX"
				},
				{
					"id": "aFPFlZt89gLLxWb0c8FMR",
					"type": "arrow"
				}
			],
			"updated": 1654242180965,
			"link": null,
			"locked": false
		},
		{
			"type": "arrow",
			"version": 1708,
			"versionNonce": 818226630,
			"isDeleted": false,
			"id": "in63DlygZ2DKeLyRmwRs7",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 524.86028378448,
			"y": 4980.646291173362,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 609.6848574259087,
			"height": 9.621961042465045,
			"seed": 1522253664,
			"groupIds": [],
			"strokeSharpness": "round",
			"boundElements": [],
			"updated": 1654494940380,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "MRiydNpb-CXQiejwi0ni4",
				"gap": 11.408286126445319,
				"focus": -0.24021562200725852
			},
			"endBinding": {
				"elementId": "xalqx3Solpn8KKQWo_zWx",
				"gap": 1.9074464541565703,
				"focus": 0.16846484955301685
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
					609.6848574259087,
					-9.621961042465045
				]
			]
		},
		{
			"type": "text",
			"version": 501,
			"versionNonce": 1554923098,
			"isDeleted": false,
			"id": "AbpPY4jX",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 1141.4525876645453,
			"y": 4953.337949508512,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 485,
			"height": 46,
			"seed": 1863012192,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [],
			"updated": 1654494940380,
			"link": null,
			"locked": false,
			"fontSize": 36.00002683957182,
			"fontFamily": 1,
			"text": "拿到客户端",
			"rawText": "拿到客户端",
			"baseline": 32,
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "xalqx3Solpn8KKQWo_zWx",
			"originalText": "拿到客户端"
		},
		{
			"type": "rectangle",
			"version": 350,
			"versionNonce": 1673855204,
			"isDeleted": false,
			"id": "eftFqsimzRQCq6eMyspRY",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 1027.7855700457292,
			"y": 2744.6710641325362,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 624.0000915527344,
			"height": 151.99996948242188,
			"seed": 113369760,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [
				{
					"id": "in63DlygZ2DKeLyRmwRs7",
					"type": "arrow"
				},
				{
					"id": "MsropNVn",
					"type": "text"
				},
				{
					"id": "X00OV73xWVzaIt3qG2fwQ",
					"type": "arrow"
				},
				{
					"id": "okJynwLY_m0k9WM74SQ2q",
					"type": "arrow"
				},
				{
					"id": "1zoIhTevPe2muR0LdpmjL",
					"type": "arrow"
				},
				{
					"id": "AFMObxe1Svj-XMn1Ond7p",
					"type": "arrow"
				},
				{
					"id": "7O6DevAemKiVtBsQSGyeS",
					"type": "arrow"
				},
				{
					"id": "z1NJYXC0IbotS1aRvxjYp",
					"type": "arrow"
				}
			],
			"updated": 1654242746070,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 349,
			"versionNonce": 110002118,
			"isDeleted": false,
			"id": "MsropNVn",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 1032.7855700457292,
			"y": 2797.671048873747,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 614.0000915527344,
			"height": 46,
			"seed": 683349856,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [],
			"updated": 1654494940382,
			"link": null,
			"locked": false,
			"fontSize": 36.00001073582633,
			"fontFamily": 1,
			"text": "主题、消息体，服务质量",
			"rawText": "主题、消息体，服务质量",
			"baseline": 32,
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "eftFqsimzRQCq6eMyspRY",
			"originalText": "主题、消息体，服务质量"
		},
		{
			"type": "arrow",
			"version": 825,
			"versionNonce": 33538650,
			"isDeleted": false,
			"id": "X00OV73xWVzaIt3qG2fwQ",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 523.1185931170182,
			"y": 2813.212838498458,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 486.6544313549996,
			"height": 3.4565603616460976,
			"seed": 2108470944,
			"groupIds": [],
			"strokeSharpness": "round",
			"boundElements": [],
			"updated": 1654495224278,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "Oo7fZ1Osv6j7xfCZ9E1fo",
				"gap": 24.999511718749773,
				"focus": 0.1862488747056345
			},
			"endBinding": {
				"elementId": "eftFqsimzRQCq6eMyspRY",
				"gap": 18.01254557371135,
				"focus": 0.16951450438382368
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
					486.6544313549996,
					-3.4565603616460976
				]
			]
		},
		{
			"type": "rectangle",
			"version": 457,
			"versionNonce": 288943580,
			"isDeleted": false,
			"id": "Pvx5T7iaLR2xb41V4scM8",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 2271.1135896384776,
			"y": 4197.204354995573,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 876,
			"height": 194,
			"seed": 1120894629,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [
				{
					"id": "okJynwLY_m0k9WM74SQ2q",
					"type": "arrow"
				},
				{
					"type": "text",
					"id": "TQWg8AiK"
				},
				{
					"id": "f5strhgKL5CTflUTfJSOC",
					"type": "arrow"
				}
			],
			"updated": 1654243472169,
			"link": null,
			"locked": false
		},
		{
			"type": "arrow",
			"version": 1715,
			"versionNonce": 2107764698,
			"isDeleted": false,
			"id": "okJynwLY_m0k9WM74SQ2q",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 1632.9574999259053,
			"y": 2921.078997030657,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 500.247085741461,
			"height": 1317.42737649217,
			"seed": 656066981,
			"groupIds": [],
			"strokeSharpness": "round",
			"boundElements": [],
			"updated": 1654494940381,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "eftFqsimzRQCq6eMyspRY",
				"gap": 24.40796341569876,
				"focus": -0.7482446587877828
			},
			"endBinding": {
				"elementId": "AyinSuFD9jNitDqpIxeZr",
				"gap": 27.40897345353369,
				"focus": -0.9832687633387751
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
					500.247085741461,
					1317.42737649217
				]
			]
		},
		{
			"type": "text",
			"version": 590,
			"versionNonce": 807847002,
			"isDeleted": false,
			"id": "TQWg8AiK",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 2276.1135896384776,
			"y": 4225.204354995573,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 866,
			"height": 138,
			"seed": 534852645,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [],
			"updated": 1654494940384,
			"link": null,
			"locked": false,
			"fontSize": 36,
			"fontFamily": 1,
			"text": "创建一个主题对象：Topic设定（向哪个客户端客户端\n，主题，服务质量，返回值）\nmqtt::topic top(cli, \"test\", QOS);",
			"rawText": "创建一个主题对象：Topic设定（向哪个客户端客户端，主题，服务质量，返回值）\nmqtt::topic top(cli, \"test\", QOS);",
			"baseline": 124,
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "Pvx5T7iaLR2xb41V4scM8",
			"originalText": "创建一个主题对象：Topic设定（向哪个客户端客户端，主题，服务质量，返回值）\nmqtt::topic top(cli, \"test\", QOS);"
		},
		{
			"type": "rectangle",
			"version": 487,
			"versionNonce": 1422764252,
			"isDeleted": false,
			"id": "Hg-Q_bB9U73qe6aCOXCQ9",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 4915.78023596009,
			"y": 4213.204619481251,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 924.0000915527339,
			"height": 102,
			"seed": 166605707,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [
				{
					"type": "text",
					"id": "sEr6mdFa"
				},
				{
					"id": "ewAWsBPETy7zJog20jgKg",
					"type": "arrow"
				},
				{
					"id": "f9TlkUKHeOYPiv1slxK70",
					"type": "arrow"
				}
			],
			"updated": 1654243875168,
			"link": null,
			"locked": false
		},
		{
			"type": "arrow",
			"version": 1858,
			"versionNonce": 1583866886,
			"isDeleted": false,
			"id": "f5strhgKL5CTflUTfJSOC",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 3148.1135896384776,
			"y": 4281.566235611192,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 207.99950154622456,
			"height": 0.0015397617999042268,
			"seed": 753081899,
			"groupIds": [],
			"strokeSharpness": "round",
			"boundElements": [],
			"updated": 1654494940386,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "Pvx5T7iaLR2xb41V4scM8",
				"gap": 1,
				"focus": -0.13025203363791618
			},
			"endBinding": {
				"elementId": "Q8NrnSPvTsYZT3KfFG1gG",
				"gap": 1,
				"focus": -0.08307996387246303
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
					207.99950154622456,
					-0.0015397617999042268
				]
			]
		},
		{
			"type": "text",
			"version": 500,
			"versionNonce": 451243206,
			"isDeleted": false,
			"id": "sEr6mdFa",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 4920.78023596009,
			"y": 4218.204619481251,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 914.0000915527339,
			"height": 92,
			"seed": 759949355,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [],
			"updated": 1654494940385,
			"link": null,
			"locked": false,
			"fontSize": 36.00001081804843,
			"fontFamily": 1,
			"text": "使用Topic.publish()发布消息\ntop.publish(std::move(payload));",
			"rawText": "使用Topic.publish()发布消息\ntop.publish(std::move(payload));",
			"baseline": 79,
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "Hg-Q_bB9U73qe6aCOXCQ9",
			"originalText": "使用Topic.publish()发布消息\ntop.publish(std::move(payload));"
		},
		{
			"type": "rectangle",
			"version": 582,
			"versionNonce": 139484772,
			"isDeleted": false,
			"id": "Q8NrnSPvTsYZT3KfFG1gG",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 3357.113091184702,
			"y": 4196.537647638802,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 1313,
			"height": 157,
			"seed": 1199620779,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [
				{
					"type": "text",
					"id": "20qK0Tir"
				},
				{
					"id": "f5strhgKL5CTflUTfJSOC",
					"type": "arrow"
				},
				{
					"id": "ewAWsBPETy7zJog20jgKg",
					"type": "arrow"
				}
			],
			"updated": 1654243582271,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 578,
			"versionNonce": 2111753242,
			"isDeleted": false,
			"id": "20qK0Tir",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 3362.113091184702,
			"y": 4229.037647638802,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 1303,
			"height": 92,
			"seed": 872156747,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [],
			"updated": 1654494940386,
			"link": null,
			"locked": false,
			"fontSize": 36.00000653948103,
			"fontFamily": 1,
			"text": "创建消息体：字符串形式的playload\nstring payload = to_string(++nsample) + \",\" +tmbuf + \",\" + to_string(x);",
			"rawText": "创建消息体：字符串形式的playload\nstring payload = to_string(++nsample) + \",\" +tmbuf + \",\" + to_string(x);",
			"baseline": 79,
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "Q8NrnSPvTsYZT3KfFG1gG",
			"originalText": "创建消息体：字符串形式的playload\nstring payload = to_string(++nsample) + \",\" +tmbuf + \",\" + to_string(x);"
		},
		{
			"type": "arrow",
			"version": 1505,
			"versionNonce": 1360622406,
			"isDeleted": false,
			"id": "ewAWsBPETy7zJog20jgKg",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 4671.113091184702,
			"y": 4268.219484164366,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 243.6671447753879,
			"height": 2.0853671708091497,
			"seed": 1975584037,
			"groupIds": [],
			"strokeSharpness": "round",
			"boundElements": [],
			"updated": 1654494940386,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "Q8NrnSPvTsYZT3KfFG1gG",
				"gap": 1,
				"focus": -0.14794867560088132
			},
			"endBinding": {
				"elementId": "Hg-Q_bB9U73qe6aCOXCQ9",
				"gap": 1,
				"focus": -0.183111739321727
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
					243.6671447753879,
					2.0853671708091497
				]
			]
		},
		{
			"type": "rectangle",
			"version": 528,
			"versionNonce": 1624771428,
			"isDeleted": false,
			"id": "AyinSuFD9jNitDqpIxeZr",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 2160.6135591209004,
			"y": 4049.3709504545573,
			"strokeColor": "#5c940d",
			"backgroundColor": "transparent",
			"width": 5302.666931152342,
			"height": 381.33316040038966,
			"seed": 1356357611,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [
				{
					"id": "okJynwLY_m0k9WM74SQ2q",
					"type": "arrow"
				}
			],
			"updated": 1654243683852,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 356,
			"versionNonce": 2005947612,
			"isDeleted": false,
			"id": "T69Px83M",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 2215.7798799216816,
			"y": 4075.204115941211,
			"strokeColor": "#364fc7",
			"backgroundColor": "transparent",
			"width": 361,
			"height": 52,
			"seed": 977709413,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [],
			"updated": 1654243024206,
			"link": null,
			"locked": false,
			"fontSize": 36,
			"fontFamily": 1,
			"text": "通过主题对象发布消息",
			"rawText": "通过主题对象发布消息",
			"baseline": 39,
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "通过主题对象发布消息"
		},
		{
			"type": "rectangle",
			"version": 580,
			"versionNonce": 1869701860,
			"isDeleted": false,
			"id": "pFeQMKNcbtySdNzaIy4xR",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -579.7180652280583,
			"y": 10138.70453555791,
			"strokeColor": "#d9480f",
			"backgroundColor": "transparent",
			"width": 722,
			"height": 113.99993896484375,
			"seed": 2084047333,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [
				{
					"id": "VId7fjOJBPONK_GPdxvCp",
					"type": "arrow"
				},
				{
					"type": "text",
					"id": "Bpy2D2LP"
				}
			],
			"updated": 1654244851672,
			"link": null,
			"locked": false
		},
		{
			"type": "arrow",
			"version": 1861,
			"versionNonce": 186792154,
			"isDeleted": false,
			"id": "VId7fjOJBPONK_GPdxvCp",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -800.2408714946284,
			"y": 10189.796474150657,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 202.5229283368824,
			"height": 3.4776211739790597,
			"seed": 1813719781,
			"groupIds": [],
			"strokeSharpness": "round",
			"boundElements": [],
			"updated": 1654494940387,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "N4lOwtxP9gyC4NQ9g_NTg",
				"gap": 19.30634756283166,
				"focus": -0.19182617600256274
			},
			"endBinding": {
				"elementId": "pFeQMKNcbtySdNzaIy4xR",
				"gap": 17.999877929687614,
				"focus": -0.06451988324991316
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
					202.5229283368824,
					3.4776211739790597
				]
			]
		},
		{
			"type": "text",
			"version": 586,
			"versionNonce": 1507711430,
			"isDeleted": false,
			"id": "Bpy2D2LP",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -574.7180652280583,
			"y": 10149.704505040332,
			"strokeColor": "#d9480f",
			"backgroundColor": "transparent",
			"width": 712,
			"height": 92,
			"seed": 893603051,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [],
			"updated": 1654494940387,
			"link": null,
			"locked": false,
			"fontSize": 36,
			"fontFamily": 1,
			"text": "使用cli客户端断开链接：cli.disconnect()->w\nait()",
			"rawText": "使用cli客户端断开链接：cli.disconnect()->wait()",
			"baseline": 79,
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "pFeQMKNcbtySdNzaIy4xR",
			"originalText": "使用cli客户端断开链接：cli.disconnect()->wait()"
		},
		{
			"type": "arrow",
			"version": 366,
			"versionNonce": 1573564678,
			"isDeleted": false,
			"id": "flHQ6_BUaUxmEBKfYakXI",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 3264.1280861902233,
			"y": 1053.0377390445253,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 541.9999694824219,
			"height": 3.999938763317232,
			"seed": 1269752939,
			"groupIds": [],
			"strokeSharpness": "round",
			"boundElements": [],
			"updated": 1654494940388,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "lHhTlR9xXNGpB0RbCkm80",
				"gap": 24.142976959923544,
				"focus": -0.03323107829892804
			},
			"endBinding": {
				"elementId": "danfNXXTWO-vC6MoFXh5H",
				"gap": 26.000213623046875,
				"focus": 0.020209882157385475
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
					541.9999694824219,
					3.999938763317232
				]
			]
		},
		{
			"type": "rectangle",
			"version": 96,
			"versionNonce": 1438685412,
			"isDeleted": false,
			"id": "danfNXXTWO-vC6MoFXh5H",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 3832.128269295692,
			"y": 891.0376552681964,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 1140,
			"height": 348.0000305175781,
			"seed": 1165372939,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [
				{
					"id": "vejOxQAt",
					"type": "text"
				},
				{
					"id": "flHQ6_BUaUxmEBKfYakXI",
					"type": "arrow"
				}
			],
			"updated": 1654242180965,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 193,
			"versionNonce": 1043941978,
			"isDeleted": false,
			"id": "vejOxQAt",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 3837.128269295692,
			"y": 896.0376552681964,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 1130,
			"height": 92,
			"seed": 580644453,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [],
			"updated": 1654494940388,
			"link": null,
			"locked": false,
			"fontSize": 36,
			"fontFamily": 1,
			"text": "遗嘱消息的创建：\nmessage(主题，消息体，服务质量，返回值)",
			"rawText": "遗嘱消息的创建：\nmessage(主题，消息体，服务质量，返回值)",
			"baseline": 79,
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": "danfNXXTWO-vC6MoFXh5H",
			"originalText": "遗嘱消息的创建：\nmessage(主题，消息体，服务质量，返回值)"
		},
		{
			"type": "rectangle",
			"version": 303,
			"versionNonce": 864279652,
			"isDeleted": false,
			"id": "EUsZYiTTEH5Z5eSusSeJB",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -149.2052471431101,
			"y": 1720.2042583565753,
			"strokeColor": "#e67700",
			"backgroundColor": "transparent",
			"width": 696.0000610351562,
			"height": 140,
			"seed": 695074053,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [
				{
					"id": "XcD6W0qWecTdEvGvGMyyE",
					"type": "arrow"
				},
				{
					"type": "text",
					"id": "FnKh0044"
				}
			],
			"updated": 1654242180965,
			"link": null,
			"locked": false
		},
		{
			"type": "arrow",
			"version": 985,
			"versionNonce": 548987462,
			"isDeleted": false,
			"id": "XcD6W0qWecTdEvGvGMyyE",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1291.7641950631644,
			"y": 1790.6557197705083,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 1129.520326685533,
			"height": 69.2134277102623,
			"seed": 1825278565,
			"groupIds": [],
			"strokeSharpness": "round",
			"boundElements": [],
			"updated": 1654494940409,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "m-xpFu4AdPvg479-leXh1",
				"gap": 20.181018899535275,
				"focus": -0.3137336461310793
			},
			"endBinding": {
				"elementId": "EUsZYiTTEH5Z5eSusSeJB",
				"gap": 13.038621234521202,
				"focus": 0.995192209456219
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
					1129.520326685533,
					-69.2134277102623
				]
			]
		},
		{
			"type": "text",
			"version": 104,
			"versionNonce": 573220742,
			"isDeleted": false,
			"id": "FnKh0044",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -144.2052471431101,
			"y": 1767.2042583565753,
			"strokeColor": "#e67700",
			"backgroundColor": "transparent",
			"width": 686.0000610351562,
			"height": 46,
			"seed": 1156963173,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [],
			"updated": 1654494940390,
			"link": null,
			"locked": false,
			"fontSize": 36.00000320301111,
			"fontFamily": 1,
			"text": "客户端创建",
			"rawText": "客户端创建",
			"baseline": 32,
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "EUsZYiTTEH5Z5eSusSeJB",
			"originalText": "客户端创建"
		},
		{
			"type": "rectangle",
			"version": 370,
			"versionNonce": 614183004,
			"isDeleted": false,
			"id": "5nfvIwl0YFI26AvyV6i5H",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 760.1289508549405,
			"y": 1668.2044185738634,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 1080,
			"height": 204,
			"seed": 376732645,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [
				{
					"id": "q5rSrhXMigqXSvhgWfmtQ",
					"type": "arrow"
				},
				{
					"type": "text",
					"id": "qgKZp42U"
				},
				{
					"id": "ZsLOVI6tjAzt-Fni5b4Ur",
					"type": "arrow"
				},
				{
					"id": "DjXDHrV9GIpQ-PFlcwy29",
					"type": "arrow"
				},
				{
					"id": "cQSQ2QVxNUYpuujLgqT6d",
					"type": "arrow"
				}
			],
			"updated": 1654242180965,
			"link": null,
			"locked": false
		},
		{
			"type": "arrow",
			"version": 710,
			"versionNonce": 1759116250,
			"isDeleted": false,
			"id": "q5rSrhXMigqXSvhgWfmtQ",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 545.1279844649629,
			"y": 1785.0581603365033,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 201.78946528925508,
			"height": 3.758114853959569,
			"seed": 1029313931,
			"groupIds": [],
			"strokeSharpness": "round",
			"boundElements": [],
			"updated": 1654494940390,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": {
				"elementId": "5nfvIwl0YFI26AvyV6i5H",
				"gap": 13.211501100722389,
				"focus": -0.2580370081279849
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
					201.78946528925508,
					3.758114853959569
				]
			]
		},
		{
			"type": "text",
			"version": 318,
			"versionNonce": 240104582,
			"isDeleted": false,
			"id": "qgKZp42U",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 765.1289508549405,
			"y": 1724.2044185738634,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 1070,
			"height": 92,
			"seed": 2050004971,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [],
			"updated": 1654494940391,
			"link": null,
			"locked": false,
			"fontSize": 36.000008459156255,
			"fontFamily": 1,
			"text": "异步客户端创建：客户端cli创建形式\nmqtt::async_client cli(SERVER_ADDRESS, CLIENT_ID);",
			"rawText": "异步客户端创建：客户端cli创建形式\nmqtt::async_client cli(SERVER_ADDRESS, CLIENT_ID);",
			"baseline": 79,
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "5nfvIwl0YFI26AvyV6i5H",
			"originalText": "异步客户端创建：客户端cli创建形式\nmqtt::async_client cli(SERVER_ADDRESS, CLIENT_ID);"
		},
		{
			"type": "rectangle",
			"version": 29,
			"versionNonce": 235603684,
			"isDeleted": false,
			"id": "tzJp4KOf_XEp1Hjje9GPZ",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 2211.7957802820233,
			"y": 1478.8712378284208,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 883,
			"height": 72.00002034505201,
			"seed": 508232811,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [
				{
					"type": "text",
					"id": "oU1CkRma"
				},
				{
					"id": "ZsLOVI6tjAzt-Fni5b4Ur",
					"type": "arrow"
				}
			],
			"updated": 1654242180965,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 116,
			"versionNonce": 2048873370,
			"isDeleted": false,
			"id": "oU1CkRma",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 2216.7957802820233,
			"y": 1491.8712480009467,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 873,
			"height": 46,
			"seed": 145071877,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [],
			"updated": 1654494940392,
			"link": null,
			"locked": false,
			"fontSize": 36,
			"fontFamily": 1,
			"text": "cli(服务端网址，客户端id，持久目录（可为空）)",
			"rawText": "cli(服务端网址，客户端id，持久目录（可为空）)",
			"baseline": 32,
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "tzJp4KOf_XEp1Hjje9GPZ",
			"originalText": "cli(服务端网址，客户端id，持久目录（可为空）)"
		},
		{
			"type": "arrow",
			"version": 446,
			"versionNonce": 1152594886,
			"isDeleted": false,
			"id": "ZsLOVI6tjAzt-Fni5b4Ur",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 1851.9335585704218,
			"y": 1771.1763067077454,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 355.365558300143,
			"height": 244.94141946262016,
			"seed": 497316107,
			"groupIds": [],
			"strokeSharpness": "round",
			"boundElements": [],
			"updated": 1654494940392,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "5nfvIwl0YFI26AvyV6i5H",
				"gap": 11.804607715481007,
				"focus": 0.8041103403143609
			},
			"endBinding": {
				"elementId": "tzJp4KOf_XEp1Hjje9GPZ",
				"gap": 4.496663411458333,
				"focus": 0.8699299908183952
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
					355.365558300143,
					-244.94141946262016
				]
			]
		},
		{
			"type": "rectangle",
			"version": 181,
			"versionNonce": 2124332508,
			"isDeleted": false,
			"id": "E40FJF4fkZQzAr6fRxsbP",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 2210.295983732544,
			"y": 1606.871268345999,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 876,
			"height": 102,
			"seed": 355663403,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [
				{
					"id": "YLeKeoP4",
					"type": "text"
				},
				{
					"id": "ZsLOVI6tjAzt-Fni5b4Ur",
					"type": "arrow"
				},
				{
					"id": "DjXDHrV9GIpQ-PFlcwy29",
					"type": "arrow"
				},
				{
					"id": "wUYsfS8tk2KiBjdMd8Wdt",
					"type": "arrow"
				}
			],
			"updated": 1654242180965,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 294,
			"versionNonce": 1023820166,
			"isDeleted": false,
			"id": "YLeKeoP4",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 2215.295983732544,
			"y": 1611.871268345999,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 866,
			"height": 92,
			"seed": 1243844101,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [],
			"updated": 1654494940393,
			"link": null,
			"locked": false,
			"fontSize": 36,
			"fontFamily": 1,
			"text": "cli(服务端网址，客户端id，最大缓冲消息，持久目录\n（可为空）)",
			"rawText": "cli(服务端网址，客户端id，最大缓冲消息，持久目录（可为空）)",
			"baseline": 79,
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "E40FJF4fkZQzAr6fRxsbP",
			"originalText": "cli(服务端网址，客户端id，最大缓冲消息，持久目录（可为空）)"
		},
		{
			"type": "arrow",
			"version": 606,
			"versionNonce": 1290129498,
			"isDeleted": false,
			"id": "DjXDHrV9GIpQ-PFlcwy29",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 1858.5847659201768,
			"y": 1809.875317942506,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 345.8116369367285,
			"height": 124.3552002682934,
			"seed": 155292869,
			"groupIds": [],
			"strokeSharpness": "round",
			"boundElements": [],
			"updated": 1654494940393,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "5nfvIwl0YFI26AvyV6i5H",
				"gap": 18.455815065236358,
				"focus": 0.8119684855143199
			},
			"endBinding": {
				"elementId": "E40FJF4fkZQzAr6fRxsbP",
				"gap": 5.899580875638894,
				"focus": 0.6329738386501139
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
					345.8116369367285,
					-124.3552002682934
				]
			]
		},
		{
			"type": "rectangle",
			"version": 194,
			"versionNonce": 611598692,
			"isDeleted": false,
			"id": "e1JW95e1kynGWCOjxHr_B",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 2201.129276375773,
			"y": 1782.8713293811545,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 1092,
			"height": 95,
			"seed": 2089747429,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [
				{
					"id": "cQSQ2QVxNUYpuujLgqT6d",
					"type": "arrow"
				},
				{
					"type": "text",
					"id": "L68uSPxO"
				},
				{
					"id": "RCyQ-oaZl5M5ju9_M_DzS",
					"type": "arrow"
				}
			],
			"updated": 1654242180965,
			"link": null,
			"locked": false
		},
		{
			"type": "arrow",
			"version": 692,
			"versionNonce": 1460674758,
			"isDeleted": false,
			"id": "cQSQ2QVxNUYpuujLgqT6d",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 1863.8789508549407,
			"y": 1815.3964032928247,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 316.3096616735943,
			"height": 9.26730900639177,
			"seed": 1838642629,
			"groupIds": [],
			"strokeSharpness": "round",
			"boundElements": [],
			"updated": 1654494940394,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "5nfvIwl0YFI26AvyV6i5H",
				"gap": 23.75,
				"focus": 0.24337856627689322
			},
			"endBinding": {
				"elementId": "e1JW95e1kynGWCOjxHr_B",
				"gap": 20.940663847238124,
				"focus": -0.17170516964814675
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
					316.3096616735943,
					9.26730900639177
				]
			]
		},
		{
			"type": "text",
			"version": 151,
			"versionNonce": 911594330,
			"isDeleted": false,
			"id": "L68uSPxO",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 2206.129276375773,
			"y": 1807.3713293811545,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 1082,
			"height": 46,
			"seed": 659481227,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [],
			"updated": 1654494940394,
			"link": null,
			"locked": false,
			"fontSize": 36.00000509806407,
			"fontFamily": 1,
			"text": "cli(服务端网址，客户端id，创建选项，持久目录（可为空）)",
			"rawText": "cli(服务端网址，客户端id，创建选项，持久目录（可为空）)",
			"baseline": 32,
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "e1JW95e1kynGWCOjxHr_B",
			"originalText": "cli(服务端网址，客户端id，创建选项，持久目录（可为空）)"
		},
		{
			"type": "rectangle",
			"version": 245,
			"versionNonce": 826981212,
			"isDeleted": false,
			"id": "0ZJnpEZzwABn5sKvY01kw",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 3878.46244694869,
			"y": 1358.8712886910498,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 741.333618164062,
			"height": 829.3332417805984,
			"seed": 82199051,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [
				{
					"id": "RCyQ-oaZl5M5ju9_M_DzS",
					"type": "arrow"
				},
				{
					"type": "text",
					"id": "lFnhDJyG"
				},
				{
					"id": "Vgp0fQ04jaEOknjMV6Bxm",
					"type": "arrow"
				},
				{
					"id": "wUYsfS8tk2KiBjdMd8Wdt",
					"type": "arrow"
				}
			],
			"updated": 1654242180965,
			"link": null,
			"locked": false
		},
		{
			"type": "arrow",
			"version": 587,
			"versionNonce": 95836186,
			"isDeleted": false,
			"id": "RCyQ-oaZl5M5ju9_M_DzS",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 3312.6966146904256,
			"y": 1825.232125394347,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 549.7539019544756,
			"height": 89.52187652979069,
			"seed": 2097262789,
			"groupIds": [],
			"strokeSharpness": "round",
			"boundElements": [],
			"updated": 1654494940395,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "e1JW95e1kynGWCOjxHr_B",
				"gap": 19.567338314652716,
				"focus": 0.6374705232031127
			},
			"endBinding": {
				"elementId": "0ZJnpEZzwABn5sKvY01kw",
				"gap": 16.01193030378886,
				"focus": 0.21218711900727882
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
					549.7539019544756,
					-89.52187652979069
				]
			]
		},
		{
			"type": "text",
			"version": 675,
			"versionNonce": 1732155802,
			"isDeleted": false,
			"id": "lFnhDJyG",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 3883.46244694869,
			"y": 1363.8712886910498,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 731.333618164062,
			"height": 690,
			"seed": 1347636837,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [],
			"updated": 1654494940396,
			"link": null,
			"locked": false,
			"fontSize": 36.13164931347046,
			"fontFamily": 1,
			"text": "创建选项：\n\n获取发送当断连的时候（）查询用\n设置发送当断连的时候（bool,bool）设置用\n\n获取最大缓冲消息（）查询用\n设置最大缓冲消息（int）设置用\n\nmqtt版本（） 查询用\n设置mqtt版本（int）设置用\n\n删除最老消息（bool）设置用\n保存持久消息（bool）设置用\n持久内存的服务质量是否为0（bool）设置用\n",
			"rawText": "创建选项：\n\n获取发送当断连的时候（）查询用\n设置发送当断连的时候（bool,bool）设置用\n\n获取最大缓冲消息（）查询用\n设置最大缓冲消息（int）设置用\n\nmqtt版本（） 查询用\n设置mqtt版本（int）设置用\n\n删除最老消息（bool）设置用\n保存持久消息（bool）设置用\n持久内存的服务质量是否为0（bool）设置用\n",
			"baseline": 676,
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": "0ZJnpEZzwABn5sKvY01kw",
			"originalText": "创建选项：\n\n获取发送当断连的时候（）查询用\n设置发送当断连的时候（bool,bool）设置用\n\n获取最大缓冲消息（）查询用\n设置最大缓冲消息（int）设置用\n\nmqtt版本（） 查询用\n设置mqtt版本（int）设置用\n\n删除最老消息（bool）设置用\n保存持久消息（bool）设置用\n持久内存的服务质量是否为0（bool）设置用\n"
		},
		{
			"type": "arrow",
			"version": 120,
			"versionNonce": 428756614,
			"isDeleted": false,
			"id": "Vgp0fQ04jaEOknjMV6Bxm",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "dashed",
			"roughness": 2,
			"opacity": 100,
			"angle": 0,
			"x": 3867.796146492961,
			"y": 1529.5378943225608,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 744.0000406901049,
			"height": 2.6666768391926325,
			"seed": 831356171,
			"groupIds": [],
			"strokeSharpness": "round",
			"boundElements": [],
			"updated": 1654494940395,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "0ZJnpEZzwABn5sKvY01kw",
				"gap": 10.66630045572947,
				"focus": 0.5832597010843548
			},
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					-744.0000406901049,
					-2.6666768391926325
				]
			]
		},
		{
			"type": "arrow",
			"version": 322,
			"versionNonce": 1628343750,
			"isDeleted": false,
			"id": "wUYsfS8tk2KiBjdMd8Wdt",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "dashed",
			"roughness": 2,
			"opacity": 100,
			"angle": 0,
			"x": 3867.7961464929604,
			"y": 1620.2045508167012,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 768.000081380208,
			"height": 37.333323160807595,
			"seed": 1927266347,
			"groupIds": [],
			"strokeSharpness": "round",
			"boundElements": [],
			"updated": 1654494940395,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "0ZJnpEZzwABn5sKvY01kw",
				"gap": 10.66630045572947,
				"focus": 0.3972181205507991
			},
			"endBinding": {
				"elementId": "E40FJF4fkZQzAr6fRxsbP",
				"gap": 13.500081380208485,
				"focus": 0.29899048332872297
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
					-768.000081380208,
					37.333323160807595
				]
			]
		},
		{
			"type": "image",
			"version": 126,
			"versionNonce": 996568932,
			"isDeleted": false,
			"id": "MFf0XcJ6t4zj48Egpa-XK",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "dashed",
			"roughness": 2,
			"opacity": 100,
			"angle": 0,
			"x": 5173.293989917438,
			"y": 1685.2044389189125,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"width": 590,
			"height": 308,
			"seed": 667388907,
			"groupIds": [],
			"strokeSharpness": "round",
			"boundElements": [
				{
					"id": "t_IWXHTcUdm2VV6MhSulF",
					"type": "arrow"
				}
			],
			"updated": 1654242180965,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "6379942b0a6d661253a8e39dda33164911e81183",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "arrow",
			"version": 276,
			"versionNonce": 1745201372,
			"isDeleted": false,
			"id": "t_IWXHTcUdm2VV6MhSulF",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "dashed",
			"roughness": 2,
			"opacity": 100,
			"angle": 0,
			"x": 4592.296704958924,
			"y": 1806.8438888263847,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 579.49734599367,
			"height": 38.47732103842577,
			"seed": 1607785483,
			"groupIds": [],
			"strokeSharpness": "round",
			"boundElements": [],
			"updated": 1654242180965,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": {
				"elementId": "MFf0XcJ6t4zj48Egpa-XK",
				"focus": 0.5214942644319343,
				"gap": 1.49993896484375
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
					579.49734599367,
					-38.47732103842577
				]
			]
		},
		{
			"type": "rectangle",
			"version": 354,
			"versionNonce": 687187812,
			"isDeleted": false,
			"id": "tQW85a2vZdqvwGwMDRNnb",
			"fillStyle": "hachure",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"angle": 0,
			"x": 6262.134561354118,
			"y": 4178.871085240529,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 969,
			"height": 163,
			"seed": 1463392683,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [
				{
					"type": "text",
					"id": "8bfo06En"
				},
				{
					"id": "f9TlkUKHeOYPiv1slxK70",
					"type": "arrow"
				}
			],
			"updated": 1654243622221,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 405,
			"versionNonce": 640570438,
			"isDeleted": false,
			"id": "8bfo06En",
			"fillStyle": "hachure",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"angle": 0,
			"x": 6267.134561354118,
			"y": 4214.371085240529,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 959,
			"height": 92,
			"seed": 1904717285,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [],
			"updated": 1654494940397,
			"link": null,
			"locked": false,
			"fontSize": 36,
			"fontFamily": 1,
			"text": "衍生产物：token令牌\n用来检测消息是否发送完毕",
			"rawText": "衍生产物：token令牌\n用来检测消息是否发送完毕",
			"baseline": 79,
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "tQW85a2vZdqvwGwMDRNnb",
			"originalText": "衍生产物：token令牌\n用来检测消息是否发送完毕"
		},
		{
			"type": "rectangle",
			"version": 504,
			"versionNonce": 601760220,
			"isDeleted": false,
			"id": "q3-wzo9H1ywCoFfhr1vFG",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 1902.6345155777512,
			"y": 4925.370894505664,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 495,
			"height": 102,
			"seed": 1598148316,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [
				{
					"id": "in63DlygZ2DKeLyRmwRs7",
					"type": "arrow"
				},
				{
					"id": "YxqIa40V",
					"type": "text"
				},
				{
					"id": "aFPFlZt89gLLxWb0c8FMR",
					"type": "arrow"
				},
				{
					"id": "qjPmt7P_pS6o2SijKjimu",
					"type": "arrow"
				}
			],
			"updated": 1654242180965,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 599,
			"versionNonce": 845151386,
			"isDeleted": false,
			"id": "YxqIa40V",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 1907.6345155777512,
			"y": 4930.370894505664,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 485,
			"height": 92,
			"seed": 162274532,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [],
			"updated": 1654494940398,
			"link": null,
			"locked": false,
			"fontSize": 36.00002683957182,
			"fontFamily": 1,
			"text": "客户端开始消费：cli.start_c\nonsuming()",
			"rawText": "客户端开始消费：cli.start_consuming()",
			"baseline": 79,
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "q3-wzo9H1ywCoFfhr1vFG",
			"originalText": "客户端开始消费：cli.start_consuming()"
		},
		{
			"type": "arrow",
			"version": 434,
			"versionNonce": 1864883078,
			"isDeleted": false,
			"id": "aFPFlZt89gLLxWb0c8FMR",
			"fillStyle": "hachure",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"angle": 0,
			"x": 1649.134607130486,
			"y": 4974.055816283132,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 241.99996948242188,
			"height": 8.700507945203753,
			"seed": 685349724,
			"groupIds": [],
			"strokeSharpness": "round",
			"boundElements": [],
			"updated": 1654494940398,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "xalqx3Solpn8KKQWo_zWx",
				"gap": 17.682019465940584,
				"focus": -0.19726944655682896
			},
			"endBinding": {
				"elementId": "q3-wzo9H1ywCoFfhr1vFG",
				"gap": 11.499938964843295,
				"focus": -0.2620632474090287
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
					241.99996948242188,
					8.700507945203753
				]
			]
		},
		{
			"type": "rectangle",
			"version": 580,
			"versionNonce": 1221696868,
			"isDeleted": false,
			"id": "r5WRaFqzTFlcs5gzGMPUI",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 2691.6343019547044,
			"y": 4561.3708410999025,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 495,
			"height": 148,
			"seed": 1556148188,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [
				{
					"id": "in63DlygZ2DKeLyRmwRs7",
					"type": "arrow"
				},
				{
					"id": "7IGc8Gio",
					"type": "text"
				},
				{
					"id": "aFPFlZt89gLLxWb0c8FMR",
					"type": "arrow"
				},
				{
					"id": "qjPmt7P_pS6o2SijKjimu",
					"type": "arrow"
				}
			],
			"updated": 1654242180965,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 788,
			"versionNonce": 464978246,
			"isDeleted": false,
			"id": "7IGc8Gio",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 2696.6343019547044,
			"y": 4589.3708410999025,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 485,
			"height": 92,
			"seed": 2146143204,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [],
			"updated": 1654494940399,
			"link": null,
			"locked": false,
			"fontSize": 36.00002683957182,
			"fontFamily": 1,
			"text": "客户端连接拿到令牌：tok=cli\n.connect(connOpts)",
			"rawText": "客户端连接拿到令牌：tok=cli.connect(connOpts)",
			"baseline": 79,
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "r5WRaFqzTFlcs5gzGMPUI",
			"originalText": "客户端连接拿到令牌：tok=cli.connect(connOpts)"
		},
		{
			"type": "arrow",
			"version": 445,
			"versionNonce": 1764317530,
			"isDeleted": false,
			"id": "qjPmt7P_pS6o2SijKjimu",
			"fillStyle": "hachure",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"angle": 0,
			"x": 2403.1345460953303,
			"y": 4973.454600217427,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 275.99990844726517,
			"height": 319.8144005883951,
			"seed": 150186332,
			"groupIds": [],
			"strokeSharpness": "round",
			"boundElements": [],
			"updated": 1654494940399,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "q3-wzo9H1ywCoFfhr1vFG",
				"gap": 5.5000305175790345,
				"focus": 0.8592524407056908
			},
			"endBinding": {
				"elementId": "r5WRaFqzTFlcs5gzGMPUI",
				"gap": 12.49984741210892,
				"focus": 0.7844032725096224
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
					275.99990844726517,
					-319.8144005883951
				]
			]
		},
		{
			"type": "rectangle",
			"version": 704,
			"versionNonce": 345284444,
			"isDeleted": false,
			"id": "2MILh1TaawmbikdO7pCvr",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 2710.634240919548,
			"y": 4854.370787694141,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 495,
			"height": 148,
			"seed": 1645803108,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [
				{
					"id": "in63DlygZ2DKeLyRmwRs7",
					"type": "arrow"
				},
				{
					"id": "DDz1wlX6",
					"type": "text"
				},
				{
					"id": "aFPFlZt89gLLxWb0c8FMR",
					"type": "arrow"
				},
				{
					"id": "qjPmt7P_pS6o2SijKjimu",
					"type": "arrow"
				},
				{
					"id": "D1wF2ZpgHYCuEtOXLG3kA",
					"type": "arrow"
				},
				{
					"id": "DhaKtcVddhaGCZbeB9nnf",
					"type": "arrow"
				}
			],
			"updated": 1654242180966,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 975,
			"versionNonce": 1223681990,
			"isDeleted": false,
			"id": "DDz1wlX6",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 2715.634240919548,
			"y": 4859.370787694141,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 485,
			"height": 138,
			"seed": 551752156,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [],
			"updated": 1654494940401,
			"link": null,
			"locked": false,
			"fontSize": 36.00002683957182,
			"fontFamily": 1,
			"text": "客户端的回复：rsp = \ntok—get_connect_respons\ne()",
			"rawText": "客户端的回复：rsp = tok—get_connect_response()",
			"baseline": 124,
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "2MILh1TaawmbikdO7pCvr",
			"originalText": "客户端的回复：rsp = tok—get_connect_response()"
		},
		{
			"type": "arrow",
			"version": 371,
			"versionNonce": 1613307418,
			"isDeleted": false,
			"id": "D1wF2ZpgHYCuEtOXLG3kA",
			"fillStyle": "hachure",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"angle": 0,
			"x": 2947.9983273093117,
			"y": 4750.127511624083,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 119.18757131760731,
			"height": 94.74345917552728,
			"seed": 1346574428,
			"groupIds": [],
			"strokeSharpness": "round",
			"boundElements": [],
			"updated": 1654494940400,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": {
				"elementId": "2MILh1TaawmbikdO7pCvr",
				"gap": 9.49981689453034,
				"focus": -0.6881146874559816
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
					-119.18757131760731,
					94.74345917552728
				]
			]
		},
		{
			"type": "rectangle",
			"version": 748,
			"versionNonce": 1573152740,
			"isDeleted": false,
			"id": "9T-_aRlX7TO9FGyRHK7N6",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 2697.6345155777512,
			"y": 5091.870825841113,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 497,
			"height": 140,
			"seed": 836361820,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [
				{
					"id": "in63DlygZ2DKeLyRmwRs7",
					"type": "arrow"
				},
				{
					"id": "cpeH2TLr",
					"type": "text"
				},
				{
					"id": "aFPFlZt89gLLxWb0c8FMR",
					"type": "arrow"
				},
				{
					"id": "qjPmt7P_pS6o2SijKjimu",
					"type": "arrow"
				},
				{
					"id": "D1wF2ZpgHYCuEtOXLG3kA",
					"type": "arrow"
				},
				{
					"id": "DhaKtcVddhaGCZbeB9nnf",
					"type": "arrow"
				},
				{
					"id": "QnZ7RbIp-oGTbtqxiX3Zd",
					"type": "arrow"
				}
			],
			"updated": 1654242180966,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 1081,
			"versionNonce": 2040807706,
			"isDeleted": false,
			"id": "cpeH2TLr",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 2702.6345155777512,
			"y": 5115.870825841113,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 487,
			"height": 92,
			"seed": 1476314468,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [],
			"updated": 1654494940402,
			"link": null,
			"locked": false,
			"fontSize": 36.00002683957182,
			"fontFamily": 1,
			"text": "客户端是否已经注册了： \n rsp.is_session_pressent()",
			"rawText": "客户端是否已经注册了： \n rsp.is_session_pressent()",
			"baseline": 79,
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "9T-_aRlX7TO9FGyRHK7N6",
			"originalText": "客户端是否已经注册了： \n rsp.is_session_pressent()"
		},
		{
			"type": "arrow",
			"version": 463,
			"versionNonce": 2070609670,
			"isDeleted": false,
			"id": "DhaKtcVddhaGCZbeB9nnf",
			"fillStyle": "hachure",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"angle": 0,
			"x": 3053.4986102647927,
			"y": 5008.865627549218,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 276.9403149562113,
			"height": 72.5412367201343,
			"seed": 2141848548,
			"groupIds": [],
			"strokeSharpness": "round",
			"boundElements": [],
			"updated": 1654494940401,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "2MILh1TaawmbikdO7pCvr",
				"gap": 6.494839855076862,
				"focus": -0.7597395321729907
			},
			"endBinding": {
				"elementId": "9T-_aRlX7TO9FGyRHK7N6",
				"gap": 10.463961571761502,
				"focus": -0.9244276799087446
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
					-276.9403149562113,
					72.5412367201343
				]
			]
		},
		{
			"type": "rectangle",
			"version": 800,
			"versionNonce": 1466567900,
			"isDeleted": false,
			"id": "xgy4jLcYPVelNRWAvoLn7",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 2702.6345766129075,
			"y": 5317.370688512012,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 497,
			"height": 148,
			"seed": 1046166756,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [
				{
					"id": "in63DlygZ2DKeLyRmwRs7",
					"type": "arrow"
				},
				{
					"id": "PUBOuTKD",
					"type": "text"
				},
				{
					"id": "aFPFlZt89gLLxWb0c8FMR",
					"type": "arrow"
				},
				{
					"id": "qjPmt7P_pS6o2SijKjimu",
					"type": "arrow"
				},
				{
					"id": "D1wF2ZpgHYCuEtOXLG3kA",
					"type": "arrow"
				},
				{
					"id": "DhaKtcVddhaGCZbeB9nnf",
					"type": "arrow"
				},
				{
					"id": "QnZ7RbIp-oGTbtqxiX3Zd",
					"type": "arrow"
				}
			],
			"updated": 1654242180966,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 1170,
			"versionNonce": 223532230,
			"isDeleted": false,
			"id": "PUBOuTKD",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 2707.6345766129075,
			"y": 5345.370688512012,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 487,
			"height": 92,
			"seed": 1437496156,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [],
			"updated": 1654494940403,
			"link": null,
			"locked": false,
			"fontSize": 36.00002683957182,
			"fontFamily": 1,
			"text": "客户端是否已经注册了： \n cli.subscribe(Topic,Qos)",
			"rawText": "客户端是否已经注册了： \n cli.subscribe(Topic,Qos)",
			"baseline": 79,
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "xgy4jLcYPVelNRWAvoLn7",
			"originalText": "客户端是否已经注册了： \n cli.subscribe(Topic,Qos)"
		},
		{
			"type": "arrow",
			"version": 488,
			"versionNonce": 946933210,
			"isDeleted": false,
			"id": "QnZ7RbIp-oGTbtqxiX3Zd",
			"fillStyle": "hachure",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"angle": 0,
			"x": 3050.749408706671,
			"y": 5258.379642491288,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 291.76456909238914,
			"height": 48.491053650118374,
			"seed": 161534556,
			"groupIds": [],
			"strokeSharpness": "round",
			"boundElements": [],
			"updated": 1654494940402,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "9T-_aRlX7TO9FGyRHK7N6",
				"gap": 26.508816650174595,
				"focus": -1.023317226112622
			},
			"endBinding": {
				"elementId": "xgy4jLcYPVelNRWAvoLn7",
				"gap": 10.499992370605469,
				"focus": -1.0098405520241804
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
					-291.76456909238914,
					48.491053650118374
				]
			]
		},
		{
			"type": "rectangle",
			"version": 147,
			"versionNonce": 1417366236,
			"isDeleted": false,
			"id": "ptWvDF3ZEKchYYnQyvAs1",
			"fillStyle": "hachure",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"angle": 0,
			"x": 2580.054633449411,
			"y": 4473.871008946582,
			"strokeColor": "#364fc7",
			"backgroundColor": "transparent",
			"width": 824.000244140625,
			"height": 1136.0000610351562,
			"seed": 1357938148,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [],
			"updated": 1654263828419,
			"link": null,
			"locked": false
		},
		{
			"type": "rectangle",
			"version": 190,
			"versionNonce": 1215923676,
			"isDeleted": false,
			"id": "vPoLqsftBm3_gmG2QIU-K",
			"fillStyle": "hachure",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"angle": 0,
			"x": 3524.054877590037,
			"y": 4865.871131016895,
			"strokeColor": "#364fc7",
			"backgroundColor": "transparent",
			"width": 912,
			"height": 143.99993896484375,
			"seed": 1609781084,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [
				{
					"id": "gABVFyFdTQduUxiNYSAw2",
					"type": "arrow"
				},
				{
					"type": "text",
					"id": "wJgkMP1i"
				},
				{
					"id": "jYIxcuPt2fwxF7fEtndYW",
					"type": "arrow"
				}
			],
			"updated": 1654242180966,
			"link": null,
			"locked": false
		},
		{
			"type": "arrow",
			"version": 420,
			"versionNonce": 1166426778,
			"isDeleted": false,
			"id": "gABVFyFdTQduUxiNYSAw2",
			"fillStyle": "hachure",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"angle": 0,
			"x": 3377.7691242750493,
			"y": 4948.279259288576,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 144.00007459850394,
			"height": 7.962173154319316,
			"seed": 2130086236,
			"groupIds": [],
			"strokeSharpness": "round",
			"boundElements": [],
			"updated": 1654494940403,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": {
				"elementId": "vPoLqsftBm3_gmG2QIU-K",
				"gap": 2.285678716483517,
				"focus": -0.4496314476903586
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
					144.00007459850394,
					7.962173154319316
				]
			]
		},
		{
			"type": "text",
			"version": 128,
			"versionNonce": 1162664774,
			"isDeleted": false,
			"id": "wJgkMP1i",
			"fillStyle": "hachure",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"angle": 0,
			"x": 3529.054877590037,
			"y": 4914.8711004993165,
			"strokeColor": "#364fc7",
			"backgroundColor": "transparent",
			"width": 902,
			"height": 46,
			"seed": 1750003036,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [],
			"updated": 1654494940404,
			"link": null,
			"locked": false,
			"fontSize": 36,
			"fontFamily": 1,
			"text": "消息的获取：msg=cli.consume_message()",
			"rawText": "消息的获取：msg=cli.consume_message()",
			"baseline": 32,
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "vPoLqsftBm3_gmG2QIU-K",
			"originalText": "消息的获取：msg=cli.consume_message()"
		},
		{
			"type": "rectangle",
			"version": 667,
			"versionNonce": 2127920604,
			"isDeleted": false,
			"id": "wu66dy-hEplWzcORcQven",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 4730.949307114776,
			"y": 4514.870932652637,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 728,
			"height": 137,
			"seed": 1110015964,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [
				{
					"id": "in63DlygZ2DKeLyRmwRs7",
					"type": "arrow"
				},
				{
					"id": "tcKueRbS",
					"type": "text"
				},
				{
					"id": "aFPFlZt89gLLxWb0c8FMR",
					"type": "arrow"
				},
				{
					"id": "qjPmt7P_pS6o2SijKjimu",
					"type": "arrow"
				},
				{
					"id": "jYIxcuPt2fwxF7fEtndYW",
					"type": "arrow"
				},
				{
					"id": "U4JCdBPSXC4nO6UNIOoRD",
					"type": "arrow"
				}
			],
			"updated": 1654263837907,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 889,
			"versionNonce": 252388762,
			"isDeleted": false,
			"id": "tcKueRbS",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 4735.949307114776,
			"y": 4560.370932652637,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 718,
			"height": 46,
			"seed": 1863580644,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [],
			"updated": 1654494940405,
			"link": null,
			"locked": false,
			"fontSize": 36.00002683957182,
			"fontFamily": 1,
			"text": "客户端是否连接：cli.is_connected()",
			"rawText": "客户端是否连接：cli.is_connected()",
			"baseline": 32,
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "wu66dy-hEplWzcORcQven",
			"originalText": "客户端是否连接：cli.is_connected()"
		},
		{
			"type": "arrow",
			"version": 520,
			"versionNonce": 1457357446,
			"isDeleted": false,
			"id": "jYIxcuPt2fwxF7fEtndYW",
			"fillStyle": "hachure",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"angle": 0,
			"x": 4450.866140390923,
			"y": 4935.923880360364,
			"strokeColor": "#364fc7",
			"backgroundColor": "transparent",
			"width": 260.18119619558547,
			"height": 314.7686259344482,
			"seed": 1673395932,
			"groupIds": [],
			"strokeSharpness": "round",
			"boundElements": [],
			"updated": 1654494940404,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "vPoLqsftBm3_gmG2QIU-K",
				"gap": 14.811262800885515,
				"focus": 0.9101634953671952
			},
			"endBinding": {
				"elementId": "wu66dy-hEplWzcORcQven",
				"gap": 19.901970528268066,
				"focus": 0.8384519775402008
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
					260.18119619558547,
					-314.7686259344482
				]
			]
		},
		{
			"type": "rectangle",
			"version": 754,
			"versionNonce": 964273252,
			"isDeleted": false,
			"id": "fiOSYEF-SveLUD1vF_4TO",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 4671.237637192902,
			"y": 4798.3439678292325,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 898,
			"height": 150,
			"seed": 702054876,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [
				{
					"id": "in63DlygZ2DKeLyRmwRs7",
					"type": "arrow"
				},
				{
					"id": "4ocBkhbI",
					"type": "text"
				},
				{
					"id": "aFPFlZt89gLLxWb0c8FMR",
					"type": "arrow"
				},
				{
					"id": "qjPmt7P_pS6o2SijKjimu",
					"type": "arrow"
				},
				{
					"id": "jYIxcuPt2fwxF7fEtndYW",
					"type": "arrow"
				},
				{
					"id": "9dFq03DRylUdtdmmhI3PH",
					"type": "arrow"
				},
				{
					"id": "r3UXv7KBmFKbCVtWc14IX",
					"type": "arrow"
				},
				{
					"id": "U4JCdBPSXC4nO6UNIOoRD",
					"type": "arrow"
				}
			],
			"updated": 1654263877002,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 982,
			"versionNonce": 1195192006,
			"isDeleted": false,
			"id": "4ocBkhbI",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 4676.237637192902,
			"y": 4850.3439678292325,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 888,
			"height": 46,
			"seed": 1598953956,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [],
			"updated": 1654494940406,
			"link": null,
			"locked": false,
			"fontSize": 36.00002683957182,
			"fontFamily": 1,
			"text": "客户端取消订阅：cli.unsubscribe(TOPIC)->wait();",
			"rawText": "客户端取消订阅：cli.unsubscribe(TOPIC)->wait();",
			"baseline": 32,
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "fiOSYEF-SveLUD1vF_4TO",
			"originalText": "客户端取消订阅：cli.unsubscribe(TOPIC)->wait();"
		},
		{
			"type": "arrow",
			"version": 705,
			"versionNonce": 142742490,
			"isDeleted": false,
			"id": "U4JCdBPSXC4nO6UNIOoRD",
			"fillStyle": "hachure",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"angle": 0,
			"x": 5192.193579857247,
			"y": 4664.697252537144,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 356.0555667824792,
			"height": 109.57758972029114,
			"seed": 570725724,
			"groupIds": [],
			"strokeSharpness": "round",
			"boundElements": [],
			"updated": 1654494940405,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "wu66dy-hEplWzcORcQven",
				"gap": 12.826319884506589,
				"focus": -0.6162866919910369
			},
			"endBinding": {
				"elementId": "fiOSYEF-SveLUD1vF_4TO",
				"gap": 24.069125571798157,
				"focus": -0.8748501218867215
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
					-356.0555667824792,
					109.57758972029114
				]
			]
		},
		{
			"type": "rectangle",
			"version": 746,
			"versionNonce": 1353490020,
			"isDeleted": false,
			"id": "CI14esbzzbf_vnTqSOcNP",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 4709.634162258006,
			"y": 5169.457299941862,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 877,
			"height": 102,
			"seed": 768035300,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [
				{
					"id": "in63DlygZ2DKeLyRmwRs7",
					"type": "arrow"
				},
				{
					"id": "U0cN4YIl",
					"type": "text"
				},
				{
					"id": "aFPFlZt89gLLxWb0c8FMR",
					"type": "arrow"
				},
				{
					"id": "qjPmt7P_pS6o2SijKjimu",
					"type": "arrow"
				},
				{
					"id": "jYIxcuPt2fwxF7fEtndYW",
					"type": "arrow"
				},
				{
					"id": "U4JCdBPSXC4nO6UNIOoRD",
					"type": "arrow"
				},
				{
					"id": "9dFq03DRylUdtdmmhI3PH",
					"type": "arrow"
				}
			],
			"updated": 1654263870802,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 991,
			"versionNonce": 1671325018,
			"isDeleted": false,
			"id": "U0cN4YIl",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 4714.634162258006,
			"y": 5197.457299941862,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 867,
			"height": 46,
			"seed": 1821750876,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [],
			"updated": 1654494940407,
			"link": null,
			"locked": false,
			"fontSize": 36.00002683957182,
			"fontFamily": 1,
			"text": "客户端停止订阅：cli.stop_consuming();",
			"rawText": "客户端停止订阅：cli.stop_consuming();",
			"baseline": 32,
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "CI14esbzzbf_vnTqSOcNP",
			"originalText": "客户端停止订阅：cli.stop_consuming();"
		},
		{
			"type": "arrow",
			"version": 754,
			"versionNonce": 1853318662,
			"isDeleted": false,
			"id": "9dFq03DRylUdtdmmhI3PH",
			"fillStyle": "hachure",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"angle": 0,
			"x": 5277.990816965089,
			"y": 4973.8439678292325,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 458.2838184825041,
			"height": 170.1133321126299,
			"seed": 195655268,
			"groupIds": [],
			"strokeSharpness": "round",
			"boundElements": [],
			"updated": 1654494940406,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "fiOSYEF-SveLUD1vF_4TO",
				"gap": 25.5,
				"focus": -0.6581671566569888
			},
			"endBinding": {
				"elementId": "CI14esbzzbf_vnTqSOcNP",
				"gap": 25.5,
				"focus": -0.9281532832769033
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
					-458.2838184825041,
					170.1133321126299
				]
			]
		},
		{
			"type": "rectangle",
			"version": 85,
			"versionNonce": 287994076,
			"isDeleted": false,
			"id": "NBrg5KQvbVlrzH8cGrERg",
			"fillStyle": "hachure",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"angle": 0,
			"x": 4588.055121730662,
			"y": 4474.870993687793,
			"strokeColor": "#364fc7",
			"backgroundColor": "transparent",
			"width": 1103.9999389648438,
			"height": 936.0000610351562,
			"seed": 1543758436,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [],
			"updated": 1654242180966,
			"link": null,
			"locked": false
		},
		{
			"type": "rectangle",
			"version": 148,
			"versionNonce": 1100389092,
			"isDeleted": false,
			"id": "fjJZF1szWiaB08naZxtF2",
			"fillStyle": "hachure",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"angle": 0,
			"x": 6012.054450343941,
			"y": 4770.870978429004,
			"strokeColor": "#364fc7",
			"backgroundColor": "transparent",
			"width": 1044,
			"height": 108.00003051757812,
			"seed": 156427492,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [
				{
					"id": "r3UXv7KBmFKbCVtWc14IX",
					"type": "arrow"
				},
				{
					"type": "text",
					"id": "k1ghZqul"
				}
			],
			"updated": 1654242180966,
			"link": null,
			"locked": false
		},
		{
			"type": "arrow",
			"version": 635,
			"versionNonce": 1612491290,
			"isDeleted": false,
			"id": "r3UXv7KBmFKbCVtWc14IX",
			"fillStyle": "hachure",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"angle": 0,
			"x": 5582.988814895051,
			"y": 4849.33175213575,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 402.0656278194956,
			"height": 5.0482343666271845,
			"seed": 455814884,
			"groupIds": [],
			"strokeSharpness": "round",
			"boundElements": [],
			"updated": 1654494940407,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "fiOSYEF-SveLUD1vF_4TO",
				"gap": 13.751177702149487,
				"focus": -0.22642641264950195
			},
			"endBinding": {
				"elementId": "fjJZF1szWiaB08naZxtF2",
				"gap": 27.00000762939453,
				"focus": -0.20674761301199526
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
					402.0656278194956,
					-5.0482343666271845
				]
			]
		},
		{
			"type": "text",
			"version": 109,
			"versionNonce": 1022237830,
			"isDeleted": false,
			"id": "k1ghZqul",
			"fillStyle": "hachure",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"angle": 0,
			"x": 6017.054450343941,
			"y": 4801.870993687793,
			"strokeColor": "#364fc7",
			"backgroundColor": "transparent",
			"width": 1034,
			"height": 46,
			"seed": 1447379428,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [],
			"updated": 1654494940408,
			"link": null,
			"locked": false,
			"fontSize": 36,
			"fontFamily": 1,
			"text": "这里可以订阅多个主题，然后单独控制某个断连",
			"rawText": "这里可以订阅多个主题，然后单独控制某个断连",
			"baseline": 32,
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "fjJZF1szWiaB08naZxtF2",
			"originalText": "这里可以订阅多个主题，然后单独控制某个断连"
		},
		{
			"type": "rectangle",
			"version": 152,
			"versionNonce": 1349577180,
			"isDeleted": false,
			"id": "m-xpFu4AdPvg479-leXh1",
			"fillStyle": "hachure",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"angle": 0,
			"x": -1839.9452139626997,
			"y": 1756.8708868762697,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 528,
			"height": 164,
			"seed": 393020380,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [
				{
					"type": "text",
					"id": "kHRO2676"
				},
				{
					"id": "Qg-TGuMkrZRDOaiZ8grHc",
					"type": "arrow"
				},
				{
					"id": "BWT3uZJqkWpsHh609M1vy",
					"type": "arrow"
				},
				{
					"id": "XcD6W0qWecTdEvGvGMyyE",
					"type": "arrow"
				},
				{
					"id": "vSGfYeepk2QgI7m7lnNlo",
					"type": "arrow"
				}
			],
			"updated": 1654242180966,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 115,
			"versionNonce": 313334234,
			"isDeleted": false,
			"id": "kHRO2676",
			"fillStyle": "hachure",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"angle": 0,
			"x": -1834.9452139626997,
			"y": 1815.8708868762697,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 518,
			"height": 46,
			"seed": 281134812,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [],
			"updated": 1654494940409,
			"link": null,
			"locked": false,
			"fontSize": 36.000007065162784,
			"fontFamily": 1,
			"text": "异步客户端",
			"rawText": "异步客户端",
			"baseline": 32,
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "m-xpFu4AdPvg479-leXh1",
			"originalText": "异步客户端"
		},
		{
			"type": "arrow",
			"version": 230,
			"versionNonce": 355510662,
			"isDeleted": false,
			"id": "vSGfYeepk2QgI7m7lnNlo",
			"fillStyle": "hachure",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"angle": 0,
			"x": -2591.9450308572304,
			"y": 1452.8708716174806,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 743.9999389648433,
			"height": 380.0000000000002,
			"seed": 123549276,
			"groupIds": [],
			"strokeSharpness": "round",
			"boundElements": [],
			"updated": 1654494940409,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "uUAFEbpVXYUeqfLtdzFbt",
				"gap": 5.080019457440358,
				"focus": -0.512543372451181
			},
			"endBinding": {
				"elementId": "m-xpFu4AdPvg479-leXh1",
				"gap": 7.9998779296875,
				"focus": -0.6130116637843748
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
					743.9999389648433,
					380.0000000000002
				]
			]
		},
		{
			"type": "rectangle",
			"version": 322,
			"versionNonce": 203140700,
			"isDeleted": false,
			"id": "cc25eEaYz8T-81nUqQ1Gg",
			"fillStyle": "hachure",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"angle": 0,
			"x": -1492.6122061501985,
			"y": 6019.870823297981,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 528,
			"height": 164,
			"seed": 45022300,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [
				{
					"id": "Qj9a5YrH",
					"type": "text"
				},
				{
					"id": "Qg-TGuMkrZRDOaiZ8grHc",
					"type": "arrow"
				},
				{
					"id": "BWT3uZJqkWpsHh609M1vy",
					"type": "arrow"
				},
				{
					"id": "XcD6W0qWecTdEvGvGMyyE",
					"type": "arrow"
				},
				{
					"id": "vSGfYeepk2QgI7m7lnNlo",
					"type": "arrow"
				},
				{
					"id": "rMPbnJ4Dl_B8fGPLsIXcQ",
					"type": "arrow"
				},
				{
					"id": "SmmcJXlGhB7bTOODGxO64",
					"type": "arrow"
				},
				{
					"id": "VLN42MiSWKpf35WgfwX_n",
					"type": "arrow"
				},
				{
					"id": "keQGqqp-0wC2OFUe9XWwR",
					"type": "arrow"
				},
				{
					"id": "ZV7LPImdCvAU-pQh6DE85",
					"type": "arrow"
				}
			],
			"updated": 1654244970700,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 284,
			"versionNonce": 67194118,
			"isDeleted": false,
			"id": "Qj9a5YrH",
			"fillStyle": "hachure",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"angle": 0,
			"x": -1487.6122061501985,
			"y": 6078.870823297981,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 518,
			"height": 46,
			"seed": 17991524,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [],
			"updated": 1654494940411,
			"link": null,
			"locked": false,
			"fontSize": 36.000007065162784,
			"fontFamily": 1,
			"text": "同步客户端",
			"rawText": "同步客户端",
			"baseline": 32,
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "cc25eEaYz8T-81nUqQ1Gg",
			"originalText": "同步客户端"
		},
		{
			"type": "arrow",
			"version": 459,
			"versionNonce": 341888666,
			"isDeleted": false,
			"id": "rMPbnJ4Dl_B8fGPLsIXcQ",
			"fillStyle": "hachure",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"angle": 0,
			"x": -2647.486033034455,
			"y": 1531.8709250232419,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 1186.8488330965577,
			"height": 4479.999898274738,
			"seed": 1569687908,
			"groupIds": [],
			"strokeSharpness": "round",
			"boundElements": [],
			"updated": 1654494940410,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "uUAFEbpVXYUeqfLtdzFbt",
				"gap": 7.2869320870049705,
				"focus": -0.7299956148512863
			},
			"endBinding": {
				"elementId": "cc25eEaYz8T-81nUqQ1Gg",
				"gap": 8,
				"focus": -0.7286134841332306
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
					1186.8488330965577,
					4479.999898274738
				]
			]
		},
		{
			"type": "rectangle",
			"version": 370,
			"versionNonce": 781190982,
			"isDeleted": false,
			"id": "GioDGPHjEwhS6EvxBSc1f",
			"fillStyle": "hachure",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"angle": 0,
			"x": -617.9459056944668,
			"y": 6040.537446731412,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 1353,
			"height": 156,
			"seed": 55837028,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [
				{
					"type": "text",
					"id": "JivRfkwD"
				},
				{
					"id": "SmmcJXlGhB7bTOODGxO64",
					"type": "arrow"
				},
				{
					"id": "rUa7m-iwIZ_m6s1wSjD6V",
					"type": "arrow"
				},
				{
					"id": "Gv1Osxl_RiNa2NhYsmPIL",
					"type": "arrow"
				},
				{
					"id": "X0Y8XaqGrn4CmsK355bP7",
					"type": "arrow"
				}
			],
			"updated": 1654495744883,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 371,
			"versionNonce": 1204516890,
			"isDeleted": false,
			"id": "JivRfkwD",
			"fillStyle": "hachure",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"angle": 0,
			"x": -612.9459056944668,
			"y": 6072.537446731412,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 1343,
			"height": 92,
			"seed": 175865948,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [],
			"updated": 1654495744883,
			"link": null,
			"locked": false,
			"fontSize": 36,
			"fontFamily": 1,
			"text": "同步客户端创建\nmqtt::client cli(SERVER_ADDRESS, CLIENT_ID);",
			"rawText": "同步客户端创建\nmqtt::client cli(SERVER_ADDRESS, CLIENT_ID);",
			"baseline": 79,
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "GioDGPHjEwhS6EvxBSc1f",
			"originalText": "同步客户端创建\nmqtt::client cli(SERVER_ADDRESS, CLIENT_ID);"
		},
		{
			"type": "arrow",
			"version": 868,
			"versionNonce": 1251566810,
			"isDeleted": false,
			"id": "SmmcJXlGhB7bTOODGxO64",
			"fillStyle": "hachure",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"angle": 0,
			"x": -942.0455171090757,
			"y": 6133.340852644329,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 302.4439484788643,
			"height": 7.231076220807154,
			"seed": 1242786268,
			"groupIds": [],
			"strokeSharpness": "round",
			"boundElements": [],
			"updated": 1654495744883,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "cc25eEaYz8T-81nUqQ1Gg",
				"focus": 0.25731166053346977,
				"gap": 22.5666890411228
			},
			"endBinding": {
				"elementId": "GioDGPHjEwhS6EvxBSc1f",
				"focus": -0.4112220740235558,
				"gap": 21.655662935744658
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
					302.4439484788643,
					7.231076220807154
				]
			]
		},
		{
			"type": "rectangle",
			"version": 191,
			"versionNonce": 906371044,
			"isDeleted": false,
			"id": "MWU5lJoB7yMwcP108Zjyc",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 1294.7206795919915,
			"y": 5860.370490147756,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 883,
			"height": 72.00002034505201,
			"seed": 845776740,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [
				{
					"id": "W2GyDGkS",
					"type": "text"
				},
				{
					"id": "ZsLOVI6tjAzt-Fni5b4Ur",
					"type": "arrow"
				},
				{
					"id": "X0Y8XaqGrn4CmsK355bP7",
					"type": "arrow"
				},
				{
					"id": "GISclLutp1SYL9YDNqLVl",
					"type": "arrow"
				}
			],
			"updated": 1654242180966,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 273,
			"versionNonce": 1672564678,
			"isDeleted": false,
			"id": "W2GyDGkS",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 1299.7206795919915,
			"y": 5873.370500320282,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 873,
			"height": 46,
			"seed": 677384412,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [],
			"updated": 1654494940414,
			"link": null,
			"locked": false,
			"fontSize": 36,
			"fontFamily": 1,
			"text": "cli(服务端网址，客户端id，持久目录（可为空）)",
			"rawText": "cli(服务端网址，客户端id，持久目录（可为空）)",
			"baseline": 32,
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "MWU5lJoB7yMwcP108Zjyc",
			"originalText": "cli(服务端网址，客户端id，持久目录（可为空）)"
		},
		{
			"type": "rectangle",
			"version": 341,
			"versionNonce": 528515940,
			"isDeleted": false,
			"id": "vU-_McMhJxl6MDuj1nPXK",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 1293.220883042512,
			"y": 5988.370520665334,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 876,
			"height": 102,
			"seed": 436927204,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [
				{
					"id": "DOdxcSYA",
					"type": "text"
				},
				{
					"id": "ZsLOVI6tjAzt-Fni5b4Ur",
					"type": "arrow"
				},
				{
					"id": "DjXDHrV9GIpQ-PFlcwy29",
					"type": "arrow"
				},
				{
					"id": "wUYsfS8tk2KiBjdMd8Wdt",
					"type": "arrow"
				},
				{
					"id": "rUa7m-iwIZ_m6s1wSjD6V",
					"type": "arrow"
				},
				{
					"id": "sxyZk7FAeyxSg4_l92oUe",
					"type": "arrow"
				}
			],
			"updated": 1654242180966,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 451,
			"versionNonce": 245848346,
			"isDeleted": false,
			"id": "DOdxcSYA",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 1298.220883042512,
			"y": 5993.370520665334,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 866,
			"height": 92,
			"seed": 476157276,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [],
			"updated": 1654494940416,
			"link": null,
			"locked": false,
			"fontSize": 36,
			"fontFamily": 1,
			"text": "cli(服务端网址，客户端id，最大缓冲消息，持久目录\n（可为空）)",
			"rawText": "cli(服务端网址，客户端id，最大缓冲消息，持久目录（可为空）)",
			"baseline": 79,
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "vU-_McMhJxl6MDuj1nPXK",
			"originalText": "cli(服务端网址，客户端id，最大缓冲消息，持久目录（可为空）)"
		},
		{
			"type": "rectangle",
			"version": 354,
			"versionNonce": 1122137828,
			"isDeleted": false,
			"id": "Wml3IpE4oTuW_G3f-91su",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 1284.054175685741,
			"y": 6164.370581700488,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 1092,
			"height": 95,
			"seed": 70385252,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [
				{
					"id": "cQSQ2QVxNUYpuujLgqT6d",
					"type": "arrow"
				},
				{
					"id": "P6AKzMvb",
					"type": "text"
				},
				{
					"id": "RCyQ-oaZl5M5ju9_M_DzS",
					"type": "arrow"
				},
				{
					"id": "Gv1Osxl_RiNa2NhYsmPIL",
					"type": "arrow"
				},
				{
					"id": "OLGnefuesK4365i0HUPVe",
					"type": "arrow"
				}
			],
			"updated": 1654242180966,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 308,
			"versionNonce": 466138118,
			"isDeleted": false,
			"id": "P6AKzMvb",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 1289.054175685741,
			"y": 6188.870581700488,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 1082,
			"height": 46,
			"seed": 247368156,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [],
			"updated": 1654494940417,
			"link": null,
			"locked": false,
			"fontSize": 36.00000509806407,
			"fontFamily": 1,
			"text": "cli(服务端网址，客户端id，创建选项，持久目录（可为空）)",
			"rawText": "cli(服务端网址，客户端id，创建选项，持久目录（可为空）)",
			"baseline": 32,
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "Wml3IpE4oTuW_G3f-91su",
			"originalText": "cli(服务端网址，客户端id，创建选项，持久目录（可为空）)"
		},
		{
			"type": "arrow",
			"version": 1042,
			"versionNonce": 1481218842,
			"isDeleted": false,
			"id": "X0Y8XaqGrn4CmsK355bP7",
			"fillStyle": "hachure",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"angle": 0,
			"x": 753.0540993917962,
			"y": 6066.829048034866,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 806.4306049831571,
			"height": 131.0393839710223,
			"seed": 1947511004,
			"groupIds": [],
			"strokeSharpness": "round",
			"boundElements": [],
			"updated": 1654495744884,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "GioDGPHjEwhS6EvxBSc1f",
				"gap": 18.000005086262945,
				"focus": 0.32414637972983107
			},
			"endBinding": {
				"elementId": "MWU5lJoB7yMwcP108Zjyc",
				"gap": 3.4191535710365315,
				"focus": -0.0993198736005414
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
					806.4306049831571,
					-131.0393839710223
				]
			]
		},
		{
			"type": "arrow",
			"version": 1017,
			"versionNonce": 1049344410,
			"isDeleted": false,
			"id": "rUa7m-iwIZ_m6s1wSjD6V",
			"fillStyle": "hachure",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"angle": 0,
			"x": 747.9619516807745,
			"y": 6135.482861269119,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 552.8884372779962,
			"height": 34.798981523753355,
			"seed": 1374047332,
			"groupIds": [],
			"strokeSharpness": "round",
			"boundElements": [],
			"updated": 1654495744884,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "GioDGPHjEwhS6EvxBSc1f",
				"gap": 12.907857375241292,
				"focus": 0.49501587127071506
			},
			"endBinding": {
				"elementId": "vU-_McMhJxl6MDuj1nPXK",
				"gap": 10.31335908003166,
				"focus": -0.435619542798246
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
					552.8884372779962,
					-34.798981523753355
				]
			]
		},
		{
			"type": "arrow",
			"version": 1035,
			"versionNonce": 1389721178,
			"isDeleted": false,
			"id": "Gv1Osxl_RiNa2NhYsmPIL",
			"fillStyle": "hachure",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"angle": 0,
			"x": 686.4872024910262,
			"y": 6212.674535682607,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 591.4122964233734,
			"height": 29.85627612195094,
			"seed": 758123876,
			"groupIds": [],
			"strokeSharpness": "round",
			"boundElements": [],
			"updated": 1654495744884,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "GioDGPHjEwhS6EvxBSc1f",
				"gap": 16.137088951194528,
				"focus": 0.5537270586156494
			},
			"endBinding": {
				"elementId": "Wml3IpE4oTuW_G3f-91su",
				"gap": 6.154676771341428,
				"focus": -0.7797995911865345
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
					591.4122964233734,
					29.85627612195094
				]
			]
		},
		{
			"type": "rectangle",
			"version": 379,
			"versionNonce": 1983263324,
			"isDeleted": false,
			"id": "xH-ufr1sAxrLNJ03uMiyH",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 2676.972307196159,
			"y": 5862.537219121148,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 741.333618164062,
			"height": 829.3332417805984,
			"seed": 1819514980,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [
				{
					"id": "RCyQ-oaZl5M5ju9_M_DzS",
					"type": "arrow"
				},
				{
					"id": "FrbE6z4S",
					"type": "text"
				},
				{
					"id": "Vgp0fQ04jaEOknjMV6Bxm",
					"type": "arrow"
				},
				{
					"id": "wUYsfS8tk2KiBjdMd8Wdt",
					"type": "arrow"
				},
				{
					"id": "OLGnefuesK4365i0HUPVe",
					"type": "arrow"
				},
				{
					"id": "GISclLutp1SYL9YDNqLVl",
					"type": "arrow"
				},
				{
					"id": "sxyZk7FAeyxSg4_l92oUe",
					"type": "arrow"
				}
			],
			"updated": 1654242180966,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 803,
			"versionNonce": 1021066650,
			"isDeleted": false,
			"id": "FrbE6z4S",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 2681.972307196159,
			"y": 5867.537219121148,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 731.333618164062,
			"height": 690,
			"seed": 2021363676,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [],
			"updated": 1654494940419,
			"link": null,
			"locked": false,
			"fontSize": 36.13164931347046,
			"fontFamily": 1,
			"text": "创建选项：\n\n获取发送当断连的时候（）查询用\n设置发送当断连的时候（bool,bool）设置用\n\n获取最大缓冲消息（）查询用\n设置最大缓冲消息（int）设置用\n\nmqtt版本（） 查询用\n设置mqtt版本（int）设置用\n\n删除最老消息（bool）设置用\n保存持久消息（bool）设置用\n持久内存的服务质量是否为0（bool）设置用\n",
			"rawText": "创建选项：\n\n获取发送当断连的时候（）查询用\n设置发送当断连的时候（bool,bool）设置用\n\n获取最大缓冲消息（）查询用\n设置最大缓冲消息（int）设置用\n\nmqtt版本（） 查询用\n设置mqtt版本（int）设置用\n\n删除最老消息（bool）设置用\n保存持久消息（bool）设置用\n持久内存的服务质量是否为0（bool）设置用\n",
			"baseline": 676,
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": "xH-ufr1sAxrLNJ03uMiyH",
			"originalText": "创建选项：\n\n获取发送当断连的时候（）查询用\n设置发送当断连的时候（bool,bool）设置用\n\n获取最大缓冲消息（）查询用\n设置最大缓冲消息（int）设置用\n\nmqtt版本（） 查询用\n设置mqtt版本（int）设置用\n\n删除最老消息（bool）设置用\n保存持久消息（bool）设置用\n持久内存的服务质量是否为0（bool）设置用\n"
		},
		{
			"type": "image",
			"version": 203,
			"versionNonce": 1576503004,
			"isDeleted": false,
			"id": "fhMkOc0jr2wUlJT_Pkrsh",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "dashed",
			"roughness": 2,
			"opacity": 100,
			"angle": 0,
			"x": 4225.1367765972,
			"y": 6127.5370563607285,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"width": 590,
			"height": 308,
			"seed": 178973668,
			"groupIds": [],
			"strokeSharpness": "round",
			"boundElements": [
				{
					"id": "RchxLY0FOyxlbAbbT7YXx",
					"type": "arrow"
				}
			],
			"updated": 1654242180966,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "6379942b0a6d661253a8e39dda33164911e81183",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "arrow",
			"version": 427,
			"versionNonce": 1145955556,
			"isDeleted": false,
			"id": "RchxLY0FOyxlbAbbT7YXx",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "dashed",
			"roughness": 2,
			"opacity": 100,
			"angle": 0,
			"x": 3606.806321065769,
			"y": 6206.509880291638,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 616.8305165665865,
			"height": 4.290616762015816,
			"seed": 2058695772,
			"groupIds": [],
			"strokeSharpness": "round",
			"boundElements": [],
			"updated": 1654242180966,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": {
				"elementId": "fhMkOc0jr2wUlJT_Pkrsh",
				"focus": 0.5214942644319304,
				"gap": 1.4999389648446595
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
					616.8305165665865,
					-4.290616762015816
				]
			]
		},
		{
			"type": "arrow",
			"version": 465,
			"versionNonce": 1239434054,
			"isDeleted": false,
			"id": "OLGnefuesK4365i0HUPVe",
			"fillStyle": "hachure",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"angle": 0,
			"x": 2382.0545012065763,
			"y": 6222.6468130110015,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 282.66703287760356,
			"height": 43.0171837855587,
			"seed": 1467406172,
			"groupIds": [],
			"strokeSharpness": "round",
			"boundElements": [],
			"updated": 1654494940418,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "Wml3IpE4oTuW_G3f-91su",
				"gap": 6.000325520835304,
				"focus": 0.7257825373722742
			},
			"endBinding": {
				"elementId": "xH-ufr1sAxrLNJ03uMiyH",
				"gap": 12.250773111979242,
				"focus": 0.3308338403784952
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
					282.66703287760356,
					-43.0171837855587
				]
			]
		},
		{
			"type": "arrow",
			"version": 475,
			"versionNonce": 1153690246,
			"isDeleted": false,
			"id": "GISclLutp1SYL9YDNqLVl",
			"fillStyle": "hachure",
			"strokeWidth": 0.5,
			"strokeStyle": "dashed",
			"roughness": 2,
			"opacity": 100,
			"angle": 0,
			"x": 2658.9723021098966,
			"y": 5937.524014364228,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 466.2510935465498,
			"height": 16.191648692969466,
			"seed": 881220316,
			"groupIds": [],
			"strokeSharpness": "round",
			"boundElements": [],
			"updated": 1654494940418,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "xH-ufr1sAxrLNJ03uMiyH",
				"gap": 18.00000508626249,
				"focus": 0.7629305377377588
			},
			"endBinding": {
				"elementId": "MWU5lJoB7yMwcP108Zjyc",
				"gap": 15.00052897135538,
				"focus": 0.17744888806898662
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
					-466.2510935465498,
					-16.191648692969466
				]
			]
		},
		{
			"type": "arrow",
			"version": 474,
			"versionNonce": 1261480390,
			"isDeleted": false,
			"id": "sxyZk7FAeyxSg4_l92oUe",
			"fillStyle": "hachure",
			"strokeWidth": 0.5,
			"strokeStyle": "dashed",
			"roughness": 2,
			"opacity": 100,
			"angle": 0,
			"x": 2654.0548267274094,
			"y": 6033.529822097456,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 474.666951497396,
			"height": 13.440029287443394,
			"seed": 1319663332,
			"groupIds": [],
			"strokeSharpness": "round",
			"boundElements": [],
			"updated": 1654494940418,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "xH-ufr1sAxrLNJ03uMiyH",
				"gap": 22.917480468750227,
				"focus": 0.5993439357283213
			},
			"endBinding": {
				"elementId": "vU-_McMhJxl6MDuj1nPXK",
				"gap": 10.166992187501364,
				"focus": 0.3200069611276092
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
					-474.666951497396,
					13.440029287443394
				]
			]
		},
		{
			"type": "rectangle",
			"version": 255,
			"versionNonce": 1539111908,
			"isDeleted": false,
			"id": "HjS-IRFFZ14OfsrZiWncp",
			"fillStyle": "hachure",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"angle": 0,
			"x": 2592.7212085633455,
			"y": 5721.203829838918,
			"strokeColor": "#364fc7",
			"backgroundColor": "transparent",
			"width": 890.6667073567711,
			"height": 1058.6667887369795,
			"seed": 1927641316,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [
				{
					"id": "gABVFyFdTQduUxiNYSAw2",
					"type": "arrow"
				}
			],
			"updated": 1654242180966,
			"link": null,
			"locked": false
		},
		{
			"type": "rectangle",
			"version": 288,
			"versionNonce": 466882140,
			"isDeleted": false,
			"id": "gbEYacF1HLVBsHvZfFSKh",
			"fillStyle": "hachure",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"angle": 0,
			"x": -559.2795238585293,
			"y": 7007.870496505588,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 913,
			"height": 195,
			"seed": 799689316,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [
				{
					"id": "VLN42MiSWKpf35WgfwX_n",
					"type": "arrow"
				},
				{
					"type": "text",
					"id": "FibcShlE"
				},
				{
					"id": "gZ4oA8UHynu4kqt6u9giv",
					"type": "arrow"
				},
				{
					"id": "YJoLfpcnSj3swkhaoTAyL",
					"type": "arrow"
				},
				{
					"id": "MnpBtp_73OM3dvppnuvyE",
					"type": "arrow"
				},
				{
					"id": "mI6BgLVzwKwQvhsihzJaw",
					"type": "arrow"
				}
			],
			"updated": 1654244365797,
			"link": null,
			"locked": false
		},
		{
			"type": "arrow",
			"version": 719,
			"versionNonce": 1014331994,
			"isDeleted": false,
			"id": "VLN42MiSWKpf35WgfwX_n",
			"fillStyle": "hachure",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"angle": 0,
			"x": -980.8292293377166,
			"y": 6186.578536456093,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 410.716745226739,
			"height": 894.7398728856688,
			"seed": 602019172,
			"groupIds": [],
			"strokeSharpness": "round",
			"boundElements": [],
			"updated": 1654494940420,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "cc25eEaYz8T-81nUqQ1Gg",
				"gap": 2.707713158111801,
				"focus": -0.692542754417053
			},
			"endBinding": {
				"elementId": "gbEYacF1HLVBsHvZfFSKh",
				"gap": 10.832960252448288,
				"focus": -0.9102979551332765
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
					410.716745226739,
					894.7398728856688
				]
			]
		},
		{
			"type": "text",
			"version": 211,
			"versionNonce": 613686598,
			"isDeleted": false,
			"id": "FibcShlE",
			"fillStyle": "hachure",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"angle": 0,
			"x": -554.2795238585293,
			"y": 7082.370496505588,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 903,
			"height": 46,
			"seed": 2030206300,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [],
			"updated": 1654494940421,
			"link": null,
			"locked": false,
			"fontSize": 36,
			"fontFamily": 1,
			"text": "消息发布",
			"rawText": "消息发布",
			"baseline": 32,
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "gbEYacF1HLVBsHvZfFSKh",
			"originalText": "消息发布"
		},
		{
			"type": "rectangle",
			"version": 206,
			"versionNonce": 996373860,
			"isDeleted": false,
			"id": "cMS14cXqkLsuBgwb5WptB",
			"fillStyle": "hachure",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"angle": 0,
			"x": 884.7203133810519,
			"y": 7019.870644007224,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 1065,
			"height": 148,
			"seed": 1071990364,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [
				{
					"id": "gZ4oA8UHynu4kqt6u9giv",
					"type": "arrow"
				},
				{
					"type": "text",
					"id": "TmDl2q1Q"
				},
				{
					"id": "JSbo9b8EgL_C_5UrvG8q3",
					"type": "arrow"
				}
			],
			"updated": 1654244190973,
			"link": null,
			"locked": false
		},
		{
			"type": "arrow",
			"version": 569,
			"versionNonce": 267158662,
			"isDeleted": false,
			"id": "gZ4oA8UHynu4kqt6u9giv",
			"fillStyle": "hachure",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"angle": 0,
			"x": 366.8454559553657,
			"y": 7096.015256578099,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 501.54142024783465,
			"height": 0.6748255969596357,
			"seed": 446101724,
			"groupIds": [],
			"strokeSharpness": "round",
			"boundElements": [],
			"updated": 1654494940421,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "gbEYacF1HLVBsHvZfFSKh",
				"gap": 13.124979813894925,
				"focus": -0.10179076615949159
			},
			"endBinding": {
				"elementId": "cMS14cXqkLsuBgwb5WptB",
				"gap": 16.33343717785158,
				"focus": -0.047618615113757354
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
					501.54142024783465,
					0.6748255969596357
				]
			]
		},
		{
			"type": "text",
			"version": 257,
			"versionNonce": 1324450714,
			"isDeleted": false,
			"id": "TmDl2q1Q",
			"fillStyle": "hachure",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"angle": 0,
			"x": 889.7203133810519,
			"y": 7047.870644007224,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 1055,
			"height": 92,
			"seed": 304730972,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [],
			"updated": 1654494940422,
			"link": null,
			"locked": false,
			"fontSize": 36,
			"fontFamily": 1,
			"text": "创建一个待发送的消息：\nauto pubmsg = mqtt::make_message(Topic,payload)",
			"rawText": "创建一个待发送的消息：\nauto pubmsg = mqtt::make_message(Topic,payload)",
			"baseline": 79,
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "cMS14cXqkLsuBgwb5WptB",
			"originalText": "创建一个待发送的消息：\nauto pubmsg = mqtt::make_message(Topic,payload)"
		},
		{
			"type": "rectangle",
			"version": 251,
			"versionNonce": 443789788,
			"isDeleted": false,
			"id": "3PU-tjGsQQxl6A0RFgk2b",
			"fillStyle": "hachure",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"angle": 0,
			"x": 2275.387122463081,
			"y": 7041.204084152081,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 1013.3331298828122,
			"height": 106.66666666666606,
			"seed": 278014044,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [
				{
					"id": "JSbo9b8EgL_C_5UrvG8q3",
					"type": "arrow"
				},
				{
					"type": "text",
					"id": "pnERv1Y3"
				},
				{
					"id": "lD-kEUOxyfMUs5s68uwz1",
					"type": "arrow"
				}
			],
			"updated": 1654242180967,
			"link": null,
			"locked": false
		},
		{
			"type": "arrow",
			"version": 664,
			"versionNonce": 670171226,
			"isDeleted": false,
			"id": "JSbo9b8EgL_C_5UrvG8q3",
			"fillStyle": "hachure",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"angle": 0,
			"x": 1956.3869088400384,
			"y": 7096.073521748984,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 308.3335062662718,
			"height": 0.2750736027628591,
			"seed": 41337692,
			"groupIds": [],
			"strokeSharpness": "round",
			"boundElements": [],
			"updated": 1654494940422,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "cMS14cXqkLsuBgwb5WptB",
				"gap": 6.666595458986649,
				"focus": 0.036037359596019086
			},
			"endBinding": {
				"elementId": "3PU-tjGsQQxl6A0RFgk2b",
				"gap": 10.666707356771212,
				"focus": -0.01486468224562817
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
					308.3335062662718,
					-0.2750736027628591
				]
			]
		},
		{
			"type": "text",
			"version": 267,
			"versionNonce": 1639649670,
			"isDeleted": false,
			"id": "pnERv1Y3",
			"fillStyle": "hachure",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"angle": 0,
			"x": 2280.387122463081,
			"y": 7048.537417485414,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 1003.3331298828122,
			"height": 92,
			"seed": 536363876,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [],
			"updated": 1654494940423,
			"link": null,
			"locked": false,
			"fontSize": 36.03588233118063,
			"fontFamily": 1,
			"text": "设置待发送消息的服务质量：QOS\npubmsg->set_qos(QOS);",
			"rawText": "设置待发送消息的服务质量：QOS\npubmsg->set_qos(QOS);",
			"baseline": 79,
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "3PU-tjGsQQxl6A0RFgk2b",
			"originalText": "设置待发送消息的服务质量：QOS\npubmsg->set_qos(QOS);"
		},
		{
			"type": "rectangle",
			"version": 341,
			"versionNonce": 1093602660,
			"isDeleted": false,
			"id": "cuj5087SHlg9oPWqXaACZ",
			"fillStyle": "hachure",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"angle": 0,
			"x": 3508.0538501649044,
			"y": 7011.203931564192,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 1013.3331298828122,
			"height": 106.66666666666606,
			"seed": 835986268,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [
				{
					"id": "JSbo9b8EgL_C_5UrvG8q3",
					"type": "arrow"
				},
				{
					"id": "txYWIx3N",
					"type": "text"
				},
				{
					"id": "lD-kEUOxyfMUs5s68uwz1",
					"type": "arrow"
				}
			],
			"updated": 1654242180967,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 405,
			"versionNonce": 2085480090,
			"isDeleted": false,
			"id": "txYWIx3N",
			"fillStyle": "hachure",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"angle": 0,
			"x": 3513.0538501649044,
			"y": 7018.537264897525,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 1003.3331298828122,
			"height": 92,
			"seed": 527913060,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [],
			"updated": 1654494940424,
			"link": null,
			"locked": false,
			"fontSize": 36.05982375257182,
			"fontFamily": 1,
			"text": "通过客户端发布消息：\nclient.publish(pubmsg);",
			"rawText": "通过客户端发布消息：\nclient.publish(pubmsg);",
			"baseline": 79,
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "cuj5087SHlg9oPWqXaACZ",
			"originalText": "通过客户端发布消息：\nclient.publish(pubmsg);"
		},
		{
			"type": "arrow",
			"version": 774,
			"versionNonce": 749400262,
			"isDeleted": false,
			"id": "lD-kEUOxyfMUs5s68uwz1",
			"fillStyle": "hachure",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"angle": 0,
			"x": 3302.720140448109,
			"y": 7081.9324360114715,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 202.66698201497366,
			"height": 4.926850555228157,
			"seed": 1527517020,
			"groupIds": [],
			"strokeSharpness": "round",
			"boundElements": [],
			"updated": 1654494940424,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "3PU-tjGsQQxl6A0RFgk2b",
				"gap": 13.999888102215436,
				"focus": 0.0007991062624619482
			},
			"endBinding": {
				"elementId": "cuj5087SHlg9oPWqXaACZ",
				"gap": 2.666727701822083,
				"focus": -0.0013158700472782766
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
					202.66698201497366,
					-4.926850555228157
				]
			]
		},
		{
			"type": "rectangle",
			"version": 295,
			"versionNonce": 1743021028,
			"isDeleted": false,
			"id": "oRdYLQiJsctKGcjMHdHKH",
			"fillStyle": "hachure",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"angle": 0,
			"x": 815.386715562041,
			"y": 6894.203885787823,
			"strokeColor": "#e67700",
			"backgroundColor": "transparent",
			"width": 4075.999450683593,
			"height": 330.00007629394537,
			"seed": 1123915876,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [],
			"updated": 1654243864088,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 212,
			"versionNonce": 1767058532,
			"isDeleted": false,
			"id": "gb53u94V",
			"fillStyle": "hachure",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"angle": 0,
			"x": 881.3869291850881,
			"y": 6940.203702682355,
			"strokeColor": "#364fc7",
			"backgroundColor": "transparent",
			"width": 289,
			"height": 52,
			"seed": 1650655708,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [],
			"updated": 1654244757927,
			"link": null,
			"locked": false,
			"fontSize": 36,
			"fontFamily": 1,
			"text": "通过创建消息发送",
			"rawText": "通过创建消息发送",
			"baseline": 39,
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "通过创建消息发送"
		},
		{
			"type": "rectangle",
			"version": 438,
			"versionNonce": 1464722396,
			"isDeleted": false,
			"id": "AQYvcvOScCarOEhCK1hNn",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 2199.847728172186,
			"y": 2488.5377798816417,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 1263,
			"height": 146,
			"seed": 89638492,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [
				{
					"id": "okJynwLY_m0k9WM74SQ2q",
					"type": "arrow"
				},
				{
					"id": "7Tgk8UA0",
					"type": "text"
				},
				{
					"id": "f5strhgKL5CTflUTfJSOC",
					"type": "arrow"
				},
				{
					"id": "1zoIhTevPe2muR0LdpmjL",
					"type": "arrow"
				},
				{
					"id": "tiY3bfLCxpvhNVfQ2VsP7",
					"type": "arrow"
				}
			],
			"updated": 1654242180967,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 604,
			"versionNonce": 358293126,
			"isDeleted": false,
			"id": "7Tgk8UA0",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 2204.847728172186,
			"y": 2515.5377798816417,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 1253,
			"height": 92,
			"seed": 1907580260,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [],
			"updated": 1654494940426,
			"link": null,
			"locked": false,
			"fontSize": 36,
			"fontFamily": 1,
			"text": "创建一个消息指针：\nmqtt::message_ptr pubmsg = mqtt::make_message(TOPIC, PAYLOAD1);",
			"rawText": "创建一个消息指针：\nmqtt::message_ptr pubmsg = mqtt::make_message(TOPIC, PAYLOAD1);",
			"baseline": 79,
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "AQYvcvOScCarOEhCK1hNn",
			"originalText": "创建一个消息指针：\nmqtt::message_ptr pubmsg = mqtt::make_message(TOPIC, PAYLOAD1);"
		},
		{
			"type": "arrow",
			"version": 351,
			"versionNonce": 1372193626,
			"isDeleted": false,
			"id": "1zoIhTevPe2muR0LdpmjL",
			"fillStyle": "hachure",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"angle": 0,
			"x": 1662.3692915365136,
			"y": 2792.6914198078907,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 529.586785585208,
			"height": 204.49139127066655,
			"seed": 1134962908,
			"groupIds": [],
			"strokeSharpness": "round",
			"boundElements": [],
			"updated": 1654494940425,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "eftFqsimzRQCq6eMyspRY",
				"gap": 10.583629938050155,
				"focus": 0.49157123064944513
			},
			"endBinding": {
				"elementId": "AQYvcvOScCarOEhCK1hNn",
				"gap": 7.891651050464526,
				"focus": 0.6950702651301767
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
					529.586785585208,
					-204.49139127066655
				]
			]
		},
		{
			"type": "rectangle",
			"version": 509,
			"versionNonce": 777730916,
			"isDeleted": false,
			"id": "alMQNTr1iYs33Z4RTD80J",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 3611.0143744938005,
			"y": 2495.2040091296903,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 554,
			"height": 146,
			"seed": 796193372,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [
				{
					"id": "okJynwLY_m0k9WM74SQ2q",
					"type": "arrow"
				},
				{
					"id": "Uug3Mo6O",
					"type": "text"
				},
				{
					"id": "f5strhgKL5CTflUTfJSOC",
					"type": "arrow"
				},
				{
					"id": "1zoIhTevPe2muR0LdpmjL",
					"type": "arrow"
				},
				{
					"id": "tiY3bfLCxpvhNVfQ2VsP7",
					"type": "arrow"
				},
				{
					"id": "YV0JCQW-bIA1s6ARLHFrD",
					"type": "arrow"
				}
			],
			"updated": 1654242180967,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 705,
			"versionNonce": 168330842,
			"isDeleted": false,
			"id": "Uug3Mo6O",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 3616.0143744938005,
			"y": 2522.2040091296903,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 544,
			"height": 92,
			"seed": 1682895204,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [],
			"updated": 1654494940427,
			"link": null,
			"locked": false,
			"fontSize": 36,
			"fontFamily": 1,
			"text": "设置消息的服务质量：\npubmsg->set_qos(QOS);",
			"rawText": "设置消息的服务质量：\npubmsg->set_qos(QOS);",
			"baseline": 79,
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "alMQNTr1iYs33Z4RTD80J",
			"originalText": "设置消息的服务质量：\npubmsg->set_qos(QOS);"
		},
		{
			"type": "arrow",
			"version": 316,
			"versionNonce": 1791057350,
			"isDeleted": false,
			"id": "tiY3bfLCxpvhNVfQ2VsP7",
			"fillStyle": "hachure",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"angle": 0,
			"x": 3467.1811225406755,
			"y": 2573.8530567553394,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 138.66678873697902,
			"height": 6.464821027407652,
			"seed": 2013632604,
			"groupIds": [],
			"strokeSharpness": "round",
			"boundElements": [],
			"updated": 1654494940427,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "AQYvcvOScCarOEhCK1hNn",
				"gap": 4.33339436848928,
				"focus": 0.4095869734511648
			},
			"endBinding": {
				"elementId": "alMQNTr1iYs33Z4RTD80J",
				"gap": 5.166463216145985,
				"focus": 0.16261279913393847
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
					138.66678873697902,
					-6.464821027407652
				]
			]
		},
		{
			"type": "rectangle",
			"version": 565,
			"versionNonce": 574857564,
			"isDeleted": false,
			"id": "ndjrXdVxx9ANLBHk1oJhi",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 4448.847707827135,
			"y": 2512.537383153128,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 944,
			"height": 108,
			"seed": 1525140836,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [
				{
					"id": "okJynwLY_m0k9WM74SQ2q",
					"type": "arrow"
				},
				{
					"id": "9izVrYsD",
					"type": "text"
				},
				{
					"id": "f5strhgKL5CTflUTfJSOC",
					"type": "arrow"
				},
				{
					"id": "1zoIhTevPe2muR0LdpmjL",
					"type": "arrow"
				},
				{
					"id": "tiY3bfLCxpvhNVfQ2VsP7",
					"type": "arrow"
				},
				{
					"id": "YV0JCQW-bIA1s6ARLHFrD",
					"type": "arrow"
				}
			],
			"updated": 1654242180967,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 779,
			"versionNonce": 1980541830,
			"isDeleted": false,
			"id": "9izVrYsD",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 4453.847707827135,
			"y": 2520.537383153128,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 934,
			"height": 92,
			"seed": 38873820,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [],
			"updated": 1654494940428,
			"link": null,
			"locked": false,
			"fontSize": 36,
			"fontFamily": 1,
			"text": "客户端发布消息：\nclient.publish(pubmsg)->wait_for(TIMEOUT);",
			"rawText": "客户端发布消息：\nclient.publish(pubmsg)->wait_for(TIMEOUT);",
			"baseline": 79,
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "ndjrXdVxx9ANLBHk1oJhi",
			"originalText": "客户端发布消息：\nclient.publish(pubmsg)->wait_for(TIMEOUT);"
		},
		{
			"type": "arrow",
			"version": 257,
			"versionNonce": 1452976922,
			"isDeleted": false,
			"id": "YV0JCQW-bIA1s6ARLHFrD",
			"fillStyle": "hachure",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"angle": 0,
			"x": 4171.18116323078,
			"y": 2571.4746973897213,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 271.9999186197929,
			"height": 6.620683999115954,
			"seed": 1929709404,
			"groupIds": [],
			"strokeSharpness": "round",
			"boundElements": [],
			"updated": 1654494940428,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "alMQNTr1iYs33Z4RTD80J",
				"gap": 6.16678873697947,
				"focus": -0.04541882711049677
			},
			"endBinding": {
				"elementId": "ndjrXdVxx9ANLBHk1oJhi",
				"gap": 5.6666259765625,
				"focus": -0.3540262210601632
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
					271.9999186197929,
					6.620683999115954
				]
			]
		},
		{
			"type": "rectangle",
			"version": 102,
			"versionNonce": 1887870812,
			"isDeleted": false,
			"id": "bqYfsD_pkgaxTFu1ZHwWt",
			"fillStyle": "hachure",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"angle": 0,
			"x": 2131.1812649560416,
			"y": 2326.204039647265,
			"strokeColor": "#c92a2a",
			"backgroundColor": "transparent",
			"width": 3455.999959309896,
			"height": 365.33325195312545,
			"seed": 1512710756,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [],
			"updated": 1654242431626,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 46,
			"versionNonce": 707993180,
			"isDeleted": false,
			"id": "XVwCMPYY",
			"fillStyle": "hachure",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"angle": 0,
			"x": 2258.8478909326054,
			"y": 2390.5378002266903,
			"strokeColor": "#364fc7",
			"backgroundColor": "transparent",
			"width": 413,
			"height": 52,
			"seed": 1623217636,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [],
			"updated": 1654242648521,
			"link": null,
			"locked": false,
			"fontSize": 36,
			"fontFamily": 1,
			"text": "创建一个Mqtt的消息指针",
			"rawText": "创建一个Mqtt的消息指针",
			"baseline": 39,
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "创建一个Mqtt的消息指针"
		},
		{
			"type": "rectangle",
			"version": 518,
			"versionNonce": 620783972,
			"isDeleted": false,
			"id": "AzF14LfbA4oM4R1YEOMWu",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 2163.3480536930224,
			"y": 2846.8710318347635,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 1013,
			"height": 163,
			"seed": 2054076508,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [
				{
					"id": "okJynwLY_m0k9WM74SQ2q",
					"type": "arrow"
				},
				{
					"id": "zmeFs1Kb",
					"type": "text"
				},
				{
					"id": "f5strhgKL5CTflUTfJSOC",
					"type": "arrow"
				},
				{
					"id": "1zoIhTevPe2muR0LdpmjL",
					"type": "arrow"
				},
				{
					"id": "tiY3bfLCxpvhNVfQ2VsP7",
					"type": "arrow"
				},
				{
					"id": "AFMObxe1Svj-XMn1Ond7p",
					"type": "arrow"
				},
				{
					"id": "frANsdcHEFlElmTbSxajr",
					"type": "arrow"
				}
			],
			"updated": 1654242180967,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 693,
			"versionNonce": 695044442,
			"isDeleted": false,
			"id": "zmeFs1Kb",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 2168.3480536930224,
			"y": 2882.3710318347635,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 1003,
			"height": 92,
			"seed": 859605860,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [],
			"updated": 1654494940429,
			"link": null,
			"locked": false,
			"fontSize": 36,
			"fontFamily": 1,
			"text": "创建一个消息令牌指针：\nmqtt::delivery_token_ptr pubtok;",
			"rawText": "创建一个消息令牌指针：\nmqtt::delivery_token_ptr pubtok;",
			"baseline": 79,
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "AzF14LfbA4oM4R1YEOMWu",
			"originalText": "创建一个消息令牌指针：\nmqtt::delivery_token_ptr pubtok;"
		},
		{
			"type": "arrow",
			"version": 303,
			"versionNonce": 934890182,
			"isDeleted": false,
			"id": "AFMObxe1Svj-XMn1Ond7p",
			"fillStyle": "hachure",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"angle": 0,
			"x": 1669.3463678178314,
			"y": 2853.927480434626,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 491.210771696753,
			"height": 30.93160535321158,
			"seed": 598908900,
			"groupIds": [],
			"strokeSharpness": "round",
			"boundElements": [],
			"updated": 1654494940429,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "eftFqsimzRQCq6eMyspRY",
				"gap": 17.560706219367553,
				"focus": 0.1307306255811172
			},
			"endBinding": {
				"elementId": "AzF14LfbA4oM4R1YEOMWu",
				"gap": 2.7909141784380815,
				"focus": 0.10090299719775034
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
					491.210771696753,
					30.93160535321158
				]
			]
		},
		{
			"type": "rectangle",
			"version": 108,
			"versionNonce": 904532828,
			"isDeleted": false,
			"id": "35VfoTlZvHFrU8GT0lPp3",
			"fillStyle": "hachure",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"angle": 0,
			"x": 3403.5150458805247,
			"y": 2859.8710318347617,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 1435,
			"height": 150,
			"seed": 1025849700,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [
				{
					"id": "frANsdcHEFlElmTbSxajr",
					"type": "arrow"
				},
				{
					"type": "text",
					"id": "oH0EzAic"
				}
			],
			"updated": 1654242180967,
			"link": null,
			"locked": false
		},
		{
			"type": "arrow",
			"version": 275,
			"versionNonce": 1751600666,
			"isDeleted": false,
			"id": "frANsdcHEFlElmTbSxajr",
			"fillStyle": "hachure",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"angle": 0,
			"x": 3179.1756884449105,
			"y": 2943.825947065957,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 207.67276645737184,
			"height": 11.820321713649719,
			"seed": 1933181156,
			"groupIds": [],
			"strokeSharpness": "round",
			"boundElements": [],
			"updated": 1654494940430,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "AzF14LfbA4oM4R1YEOMWu",
				"gap": 2.8276347518881266,
				"focus": 0.40283917675976944
			},
			"endBinding": {
				"elementId": "35VfoTlZvHFrU8GT0lPp3",
				"gap": 16.66659097824231,
				"focus": 0.38547325750001854
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
					207.67276645737184,
					-11.820321713649719
				]
			]
		},
		{
			"type": "text",
			"version": 125,
			"versionNonce": 789559430,
			"isDeleted": false,
			"id": "oH0EzAic",
			"fillStyle": "hachure",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"angle": 0,
			"x": 3408.5150458805247,
			"y": 2865.8710318347617,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 1425,
			"height": 138,
			"seed": 1349866724,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [],
			"updated": 1654494940430,
			"link": null,
			"locked": false,
			"fontSize": 36,
			"fontFamily": 1,
			"text": "通过客户端发布消息：\npubtok = client.publish(TOPIC, PAYLOAD2, strlen(PAYLOAD2), QOS, false);\npubtok->wait_for(TIMEOUT);",
			"rawText": "通过客户端发布消息：\npubtok = client.publish(TOPIC, PAYLOAD2, strlen(PAYLOAD2), QOS, false);\npubtok->wait_for(TIMEOUT);",
			"baseline": 124,
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "35VfoTlZvHFrU8GT0lPp3",
			"originalText": "通过客户端发布消息：\npubtok = client.publish(TOPIC, PAYLOAD2, strlen(PAYLOAD2), QOS, false);\npubtok->wait_for(TIMEOUT);"
		},
		{
			"type": "rectangle",
			"version": 109,
			"versionNonce": 1887411556,
			"isDeleted": false,
			"id": "TBiM0SWl6euCo7wtgXFdd",
			"fillStyle": "hachure",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"angle": 0,
			"x": 2136.848379213856,
			"y": 2733.204517755986,
			"strokeColor": "#c92a2a",
			"backgroundColor": "transparent",
			"width": 3063.9998372395835,
			"height": 341.33336385091167,
			"seed": 1489456220,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [],
			"updated": 1654242427610,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 47,
			"versionNonce": 1987497572,
			"isDeleted": false,
			"id": "hwDmqf8v",
			"fillStyle": "hachure",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"angle": 0,
			"x": 2254.181956687813,
			"y": 2750.5379528145804,
			"strokeColor": "#364fc7",
			"backgroundColor": "transparent",
			"width": 433,
			"height": 52,
			"seed": 375803364,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [],
			"updated": 1654242645352,
			"link": null,
			"locked": false,
			"fontSize": 36,
			"fontFamily": 1,
			"text": "通过一个发布令牌的指针：",
			"rawText": "通过一个发布令牌的指针：",
			"baseline": 39,
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "通过一个发布令牌的指针："
		},
		{
			"type": "rectangle",
			"version": 584,
			"versionNonce": 168346212,
			"isDeleted": false,
			"id": "3TAu-tkGtlwcUpycFzs2p",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 2171.016917625313,
			"y": 3266.371342096807,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 952,
			"height": 133.33333333333303,
			"seed": 2011166300,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [
				{
					"id": "okJynwLY_m0k9WM74SQ2q",
					"type": "arrow"
				},
				{
					"id": "f5strhgKL5CTflUTfJSOC",
					"type": "arrow"
				},
				{
					"id": "1zoIhTevPe2muR0LdpmjL",
					"type": "arrow"
				},
				{
					"id": "tiY3bfLCxpvhNVfQ2VsP7",
					"type": "arrow"
				},
				{
					"id": "AFMObxe1Svj-XMn1Ond7p",
					"type": "arrow"
				},
				{
					"id": "frANsdcHEFlElmTbSxajr",
					"type": "arrow"
				},
				{
					"id": "7O6DevAemKiVtBsQSGyeS",
					"type": "arrow"
				},
				{
					"type": "text",
					"id": "UbabjnU3"
				},
				{
					"id": "f0lDk88qJwmuAzhP7ZKPm",
					"type": "arrow"
				}
			],
			"updated": 1654242213367,
			"link": null,
			"locked": false
		},
		{
			"type": "arrow",
			"version": 266,
			"versionNonce": 1456650182,
			"isDeleted": false,
			"id": "7O6DevAemKiVtBsQSGyeS",
			"fillStyle": "hachure",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"angle": 0,
			"x": 1653.1359830239255,
			"y": 2879.5809400288285,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 515.175545062303,
			"height": 457.00957814012827,
			"seed": 2131042524,
			"groupIds": [],
			"strokeSharpness": "round",
			"boundElements": [],
			"updated": 1654494940431,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "eftFqsimzRQCq6eMyspRY",
				"gap": 1.3503214254620137,
				"focus": -0.6209693569478774
			},
			"endBinding": {
				"elementId": "3TAu-tkGtlwcUpycFzs2p",
				"gap": 2.7053895390844236,
				"focus": -0.8758206951558745
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
					515.175545062303,
					457.00957814012827
				]
			]
		},
		{
			"type": "text",
			"version": 107,
			"versionNonce": 683215962,
			"isDeleted": false,
			"id": "UbabjnU3",
			"fillStyle": "hachure",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"angle": 0,
			"x": 2176.016917625313,
			"y": 3310.0380087634735,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 942,
			"height": 46,
			"seed": 1528932060,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [],
			"updated": 1654494940432,
			"link": null,
			"locked": false,
			"fontSize": 36,
			"fontFamily": 1,
			"text": "定义一个action_listenter继承自iaction_listener",
			"rawText": "定义一个action_listenter继承自iaction_listener",
			"baseline": 32,
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "3TAu-tkGtlwcUpycFzs2p",
			"originalText": "定义一个action_listenter继承自iaction_listener"
		},
		{
			"type": "rectangle",
			"version": 681,
			"versionNonce": 185557092,
			"isDeleted": false,
			"id": "WECoR_ITzQv9rDsEIm1By",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 3298.850902000312,
			"y": 3263.8714031319632,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 662,
			"height": 113,
			"seed": 1152980700,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [
				{
					"id": "okJynwLY_m0k9WM74SQ2q",
					"type": "arrow"
				},
				{
					"id": "f5strhgKL5CTflUTfJSOC",
					"type": "arrow"
				},
				{
					"id": "1zoIhTevPe2muR0LdpmjL",
					"type": "arrow"
				},
				{
					"id": "tiY3bfLCxpvhNVfQ2VsP7",
					"type": "arrow"
				},
				{
					"id": "AFMObxe1Svj-XMn1Ond7p",
					"type": "arrow"
				},
				{
					"id": "frANsdcHEFlElmTbSxajr",
					"type": "arrow"
				},
				{
					"id": "7O6DevAemKiVtBsQSGyeS",
					"type": "arrow"
				},
				{
					"id": "3W2uKtdb",
					"type": "text"
				},
				{
					"id": "f0lDk88qJwmuAzhP7ZKPm",
					"type": "arrow"
				},
				{
					"id": "4Gne7lM1Sy-ZXDhQNw0om",
					"type": "arrow"
				}
			],
			"updated": 1654242250799,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 250,
			"versionNonce": 1800250566,
			"isDeleted": false,
			"id": "3W2uKtdb",
			"fillStyle": "hachure",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"angle": 0,
			"x": 3303.850902000312,
			"y": 3274.3714031319632,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 652,
			"height": 92,
			"seed": 1345148132,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [],
			"updated": 1654494940433,
			"link": null,
			"locked": false,
			"fontSize": 36,
			"fontFamily": 1,
			"text": "创建一个动作监听器对象\naction_listener listener;",
			"rawText": "创建一个动作监听器对象\naction_listener listener;",
			"baseline": 79,
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "WECoR_ITzQv9rDsEIm1By",
			"originalText": "创建一个动作监听器对象\naction_listener listener;"
		},
		{
			"type": "arrow",
			"version": 249,
			"versionNonce": 424309018,
			"isDeleted": false,
			"id": "f0lDk88qJwmuAzhP7ZKPm",
			"fillStyle": "hachure",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"angle": 0,
			"x": 3132.4808400496286,
			"y": 3323.853408323832,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 160.15540679931655,
			"height": 6.21368670713764,
			"seed": 1716849636,
			"groupIds": [],
			"strokeSharpness": "round",
			"boundElements": [],
			"updated": 1654494940432,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "3TAu-tkGtlwcUpycFzs2p",
				"gap": 9.463922424315657,
				"focus": -0.32912130964518127
			},
			"endBinding": {
				"elementId": "WECoR_ITzQv9rDsEIm1By",
				"gap": 6.214655151366688,
				"focus": -0.32850030685979115
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
					160.15540679931655,
					6.21368670713764
				]
			]
		},
		{
			"type": "rectangle",
			"version": 749,
			"versionNonce": 2043146076,
			"isDeleted": false,
			"id": "vW4Cnwe7JzudG7KZhX3_y",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 4103.85049509927,
			"y": 3266.038141006312,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 958,
			"height": 102,
			"seed": 2107495524,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [
				{
					"id": "okJynwLY_m0k9WM74SQ2q",
					"type": "arrow"
				},
				{
					"id": "f5strhgKL5CTflUTfJSOC",
					"type": "arrow"
				},
				{
					"id": "1zoIhTevPe2muR0LdpmjL",
					"type": "arrow"
				},
				{
					"id": "tiY3bfLCxpvhNVfQ2VsP7",
					"type": "arrow"
				},
				{
					"id": "AFMObxe1Svj-XMn1Ond7p",
					"type": "arrow"
				},
				{
					"id": "frANsdcHEFlElmTbSxajr",
					"type": "arrow"
				},
				{
					"id": "7O6DevAemKiVtBsQSGyeS",
					"type": "arrow"
				},
				{
					"id": "2f9CsroZ",
					"type": "text"
				},
				{
					"id": "f0lDk88qJwmuAzhP7ZKPm",
					"type": "arrow"
				},
				{
					"id": "4Gne7lM1Sy-ZXDhQNw0om",
					"type": "arrow"
				},
				{
					"id": "ur_Cs-rJdSi-J4ufR4TqN",
					"type": "arrow"
				}
			],
			"updated": 1654242380487,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 328,
			"versionNonce": 1778652186,
			"isDeleted": false,
			"id": "2f9CsroZ",
			"fillStyle": "hachure",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"angle": 0,
			"x": 4108.85049509927,
			"y": 3271.038141006312,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 948,
			"height": 92,
			"seed": 321065948,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [],
			"updated": 1654494940434,
			"link": null,
			"locked": false,
			"fontSize": 36,
			"fontFamily": 1,
			"text": "创建发布消息的指针:\npubmsg = mqtt::make_message(TOPIC, PAYLOAD3);",
			"rawText": "创建发布消息的指针:\npubmsg = mqtt::make_message(TOPIC, PAYLOAD3);",
			"baseline": 79,
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "vW4Cnwe7JzudG7KZhX3_y",
			"originalText": "创建发布消息的指针:\npubmsg = mqtt::make_message(TOPIC, PAYLOAD3);"
		},
		{
			"type": "arrow",
			"version": 182,
			"versionNonce": 1695095814,
			"isDeleted": false,
			"id": "4Gne7lM1Sy-ZXDhQNw0om",
			"fillStyle": "hachure",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"angle": 0,
			"x": 3961.850902000312,
			"y": 3318.049155142121,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 140.99959309895803,
			"height": 0.2629274733321836,
			"seed": 741796572,
			"groupIds": [],
			"strokeSharpness": "round",
			"boundElements": [],
			"updated": 1654494940433,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "WECoR_ITzQv9rDsEIm1By",
				"gap": 1,
				"focus": -0.05149657088416894
			},
			"endBinding": {
				"elementId": "vW4Cnwe7JzudG7KZhX3_y",
				"gap": 1,
				"focus": -0.041797692567193165
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
					140.99959309895803,
					0.2629274733321836
				]
			]
		},
		{
			"type": "arrow",
			"version": 364,
			"versionNonce": 1398702298,
			"isDeleted": false,
			"id": "ur_Cs-rJdSi-J4ufR4TqN",
			"fillStyle": "hachure",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"angle": 0,
			"x": 5087.35049509927,
			"y": 3303.4725514191114,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 359.3548719380815,
			"height": 8.488945743820295,
			"seed": 1788744164,
			"groupIds": [],
			"strokeSharpness": "round",
			"boundElements": [],
			"updated": 1654494940435,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "vW4Cnwe7JzudG7KZhX3_y",
				"gap": 25.5,
				"focus": -0.40894072840816714
			},
			"endBinding": {
				"elementId": "wJO-WvISj_34fGUzcLByt",
				"gap": 19.812038869214465,
				"focus": -0.3352377437935165
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
					359.3548719380815,
					8.488945743820295
				]
			]
		},
		{
			"type": "rectangle",
			"version": 790,
			"versionNonce": 20085980,
			"isDeleted": false,
			"id": "wJO-WvISj_34fGUzcLByt",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 5466.517405906567,
			"y": 3195.537947728311,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 1268,
			"height": 190,
			"seed": 1668691812,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [
				{
					"id": "okJynwLY_m0k9WM74SQ2q",
					"type": "arrow"
				},
				{
					"id": "f5strhgKL5CTflUTfJSOC",
					"type": "arrow"
				},
				{
					"id": "1zoIhTevPe2muR0LdpmjL",
					"type": "arrow"
				},
				{
					"id": "tiY3bfLCxpvhNVfQ2VsP7",
					"type": "arrow"
				},
				{
					"id": "AFMObxe1Svj-XMn1Ond7p",
					"type": "arrow"
				},
				{
					"id": "frANsdcHEFlElmTbSxajr",
					"type": "arrow"
				},
				{
					"id": "7O6DevAemKiVtBsQSGyeS",
					"type": "arrow"
				},
				{
					"id": "EQ1p18EL",
					"type": "text"
				},
				{
					"id": "f0lDk88qJwmuAzhP7ZKPm",
					"type": "arrow"
				},
				{
					"id": "4Gne7lM1Sy-ZXDhQNw0om",
					"type": "arrow"
				},
				{
					"id": "ur_Cs-rJdSi-J4ufR4TqN",
					"type": "arrow"
				}
			],
			"updated": 1654242389258,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 410,
			"versionNonce": 2020217286,
			"isDeleted": false,
			"id": "EQ1p18EL",
			"fillStyle": "hachure",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"angle": 0,
			"x": 5471.517405906567,
			"y": 3221.537947728311,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 1258,
			"height": 138,
			"seed": 1605787868,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [],
			"updated": 1654494940435,
			"link": null,
			"locked": false,
			"fontSize": 36,
			"fontFamily": 1,
			"text": "通过客户端发布消息:\npubtok = client.publish(pubmsg, nullptr, listener);\n                pubtok->wait();",
			"rawText": "通过客户端发布消息:\npubtok = client.publish(pubmsg, nullptr, listener);\n                pubtok->wait();",
			"baseline": 124,
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "wJO-WvISj_34fGUzcLByt",
			"originalText": "通过客户端发布消息:\npubtok = client.publish(pubmsg, nullptr, listener);\n                pubtok->wait();"
		},
		{
			"type": "rectangle",
			"version": 75,
			"versionNonce": 112093540,
			"isDeleted": false,
			"id": "84i7Olld5r1FJoNVAv_B1",
			"fillStyle": "hachure",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"angle": 0,
			"x": 2144.8505968245354,
			"y": 3125.8712454578044,
			"strokeColor": "#c92a2a",
			"backgroundColor": "transparent",
			"width": 4668.000183105469,
			"height": 335.9999847412109,
			"seed": 1840403420,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [],
			"updated": 1654242440631,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 35,
			"versionNonce": 1621251940,
			"isDeleted": false,
			"id": "TZTolGjA",
			"fillStyle": "hachure",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"angle": 0,
			"x": 2262.514883120104,
			"y": 3169.8715252022785,
			"strokeColor": "#364fc7",
			"backgroundColor": "transparent",
			"width": 325,
			"height": 52,
			"seed": 994875236,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [],
			"updated": 1654242640977,
			"link": null,
			"locked": false,
			"fontSize": 36,
			"fontFamily": 1,
			"text": "通过一个动作监听器",
			"rawText": "通过一个动作监听器",
			"baseline": 39,
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "通过一个动作监听器"
		},
		{
			"type": "rectangle",
			"version": 636,
			"versionNonce": 148484060,
			"isDeleted": false,
			"id": "uLr3XE8sutvoya1iks4FM",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 2180.680563051741,
			"y": 3739.3716142118865,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 952,
			"height": 133.33333333333303,
			"seed": 1461444828,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [
				{
					"id": "okJynwLY_m0k9WM74SQ2q",
					"type": "arrow"
				},
				{
					"id": "f5strhgKL5CTflUTfJSOC",
					"type": "arrow"
				},
				{
					"id": "1zoIhTevPe2muR0LdpmjL",
					"type": "arrow"
				},
				{
					"id": "tiY3bfLCxpvhNVfQ2VsP7",
					"type": "arrow"
				},
				{
					"id": "AFMObxe1Svj-XMn1Ond7p",
					"type": "arrow"
				},
				{
					"id": "frANsdcHEFlElmTbSxajr",
					"type": "arrow"
				},
				{
					"id": "7O6DevAemKiVtBsQSGyeS",
					"type": "arrow"
				},
				{
					"id": "lzvKw7tX",
					"type": "text"
				},
				{
					"id": "uKVJ3_9mIjLlsuWRijK7R",
					"type": "arrow"
				}
			],
			"updated": 1654242738711,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 163,
			"versionNonce": 1241748058,
			"isDeleted": false,
			"id": "lzvKw7tX",
			"fillStyle": "hachure",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"angle": 0,
			"x": 2185.680563051741,
			"y": 3783.038280878553,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 942,
			"height": 46,
			"seed": 565455588,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [],
			"updated": 1654494940436,
			"link": null,
			"locked": false,
			"fontSize": 36,
			"fontFamily": 1,
			"text": "定义一个delivery_action_listener继承自action_listener",
			"rawText": "定义一个delivery_action_listener继承自action_listener",
			"baseline": 32,
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "uLr3XE8sutvoya1iks4FM",
			"originalText": "定义一个delivery_action_listener继承自action_listener"
		},
		{
			"type": "rectangle",
			"version": 761,
			"versionNonce": 642768476,
			"isDeleted": false,
			"id": "ahv-Xoyh28z6k_HJxiLsZ",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 3308.51454742674,
			"y": 3736.8716752470427,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 761,
			"height": 102,
			"seed": 589522268,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [
				{
					"id": "okJynwLY_m0k9WM74SQ2q",
					"type": "arrow"
				},
				{
					"id": "f5strhgKL5CTflUTfJSOC",
					"type": "arrow"
				},
				{
					"id": "1zoIhTevPe2muR0LdpmjL",
					"type": "arrow"
				},
				{
					"id": "tiY3bfLCxpvhNVfQ2VsP7",
					"type": "arrow"
				},
				{
					"id": "AFMObxe1Svj-XMn1Ond7p",
					"type": "arrow"
				},
				{
					"id": "frANsdcHEFlElmTbSxajr",
					"type": "arrow"
				},
				{
					"id": "7O6DevAemKiVtBsQSGyeS",
					"type": "arrow"
				},
				{
					"id": "y28nSWEv",
					"type": "text"
				},
				{
					"id": "uKVJ3_9mIjLlsuWRijK7R",
					"type": "arrow"
				},
				{
					"id": "MehLZBhd8lY2cIKuk35ka",
					"type": "arrow"
				}
			],
			"updated": 1654242871169,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 322,
			"versionNonce": 1634205382,
			"isDeleted": false,
			"id": "y28nSWEv",
			"fillStyle": "hachure",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"angle": 0,
			"x": 3313.51454742674,
			"y": 3741.8716752470427,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 751,
			"height": 92,
			"seed": 523578980,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [],
			"updated": 1654494940437,
			"link": null,
			"locked": false,
			"fontSize": 36,
			"fontFamily": 1,
			"text": "创建一个动作监听器对象\ndelivery_action_listener deliveryListener;",
			"rawText": "创建一个动作监听器对象\ndelivery_action_listener deliveryListener;",
			"baseline": 79,
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "ahv-Xoyh28z6k_HJxiLsZ",
			"originalText": "创建一个动作监听器对象\ndelivery_action_listener deliveryListener;"
		},
		{
			"type": "arrow",
			"version": 440,
			"versionNonce": 2069116698,
			"isDeleted": false,
			"id": "uKVJ3_9mIjLlsuWRijK7R",
			"fillStyle": "hachure",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"angle": 0,
			"x": 3134.6269688011107,
			"y": 3792.8830329817424,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 172.60943622603736,
			"height": 4.720166043160589,
			"seed": 2093373916,
			"groupIds": [],
			"strokeSharpness": "round",
			"boundElements": [],
			"updated": 1654494940437,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "uLr3XE8sutvoya1iks4FM",
				"gap": 1.9464057493692473,
				"focus": -0.3291169930503527
			},
			"endBinding": {
				"elementId": "ahv-Xoyh28z6k_HJxiLsZ",
				"gap": 1.2781423995920675,
				"focus": -0.3285003068597803
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
					172.60943622603736,
					4.720166043160589
				]
			]
		},
		{
			"type": "rectangle",
			"version": 819,
			"versionNonce": 1956927204,
			"isDeleted": false,
			"id": "bpVcmo1dHedqJPMutq5g7",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 4241.514018455386,
			"y": 3731.0383826038133,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 958,
			"height": 102,
			"seed": 1556726244,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [
				{
					"id": "okJynwLY_m0k9WM74SQ2q",
					"type": "arrow"
				},
				{
					"id": "f5strhgKL5CTflUTfJSOC",
					"type": "arrow"
				},
				{
					"id": "1zoIhTevPe2muR0LdpmjL",
					"type": "arrow"
				},
				{
					"id": "tiY3bfLCxpvhNVfQ2VsP7",
					"type": "arrow"
				},
				{
					"id": "AFMObxe1Svj-XMn1Ond7p",
					"type": "arrow"
				},
				{
					"id": "frANsdcHEFlElmTbSxajr",
					"type": "arrow"
				},
				{
					"id": "7O6DevAemKiVtBsQSGyeS",
					"type": "arrow"
				},
				{
					"id": "6RofVCT7",
					"type": "text"
				},
				{
					"id": "uKVJ3_9mIjLlsuWRijK7R",
					"type": "arrow"
				},
				{
					"id": "MehLZBhd8lY2cIKuk35ka",
					"type": "arrow"
				}
			],
			"updated": 1654242884302,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 398,
			"versionNonce": 2105709914,
			"isDeleted": false,
			"id": "6RofVCT7",
			"fillStyle": "hachure",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"angle": 0,
			"x": 4246.514018455386,
			"y": 3736.0383826038133,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 948,
			"height": 92,
			"seed": 2132196956,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [],
			"updated": 1654494940438,
			"link": null,
			"locked": false,
			"fontSize": 36,
			"fontFamily": 1,
			"text": "创建发布消息的指针:\npubmsg = mqtt::make_message(TOPIC, PAYLOAD4);",
			"rawText": "创建发布消息的指针:\npubmsg = mqtt::make_message(TOPIC, PAYLOAD4);",
			"baseline": 79,
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "bpVcmo1dHedqJPMutq5g7",
			"originalText": "创建发布消息的指针:\npubmsg = mqtt::make_message(TOPIC, PAYLOAD4);"
		},
		{
			"type": "arrow",
			"version": 407,
			"versionNonce": 449328646,
			"isDeleted": false,
			"id": "MehLZBhd8lY2cIKuk35ka",
			"fillStyle": "hachure",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"angle": 0,
			"x": 4070.51454742674,
			"y": 3784.8889245376495,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 169.99947102864553,
			"height": 0.18239104914391646,
			"seed": 830465380,
			"groupIds": [],
			"strokeSharpness": "round",
			"boundElements": [],
			"updated": 1654494940438,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "ahv-Xoyh28z6k_HJxiLsZ",
				"gap": 1,
				"focus": -0.05005895351263999
			},
			"endBinding": {
				"elementId": "bpVcmo1dHedqJPMutq5g7",
				"gap": 1,
				"focus": -0.04179769256720859
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
					169.99947102864553,
					-0.18239104914391646
				]
			]
		},
		{
			"type": "arrow",
			"version": 462,
			"versionNonce": 27231558,
			"isDeleted": false,
			"id": "fdnm3Q43Fowcu7xz6Lh44",
			"fillStyle": "hachure",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"angle": 0,
			"x": 5234.111866419503,
			"y": 3790.4806096351044,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 222.25714604427776,
			"height": 7.289565380972817,
			"seed": 317100764,
			"groupIds": [],
			"strokeSharpness": "round",
			"boundElements": [],
			"updated": 1654494940439,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": {
				"elementId": "CoaB8Uyyw_w2crzI5Eha1",
				"gap": 19.81203886921412,
				"focus": -0.04686140412802145
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
					222.25714604427776,
					7.289565380972817
				]
			]
		},
		{
			"type": "rectangle",
			"version": 845,
			"versionNonce": 187934044,
			"isDeleted": false,
			"id": "CoaB8Uyyw_w2crzI5Eha1",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 5476.181051332995,
			"y": 3668.53821984339,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 1268,
			"height": 286,
			"seed": 1655019748,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [
				{
					"id": "okJynwLY_m0k9WM74SQ2q",
					"type": "arrow"
				},
				{
					"id": "f5strhgKL5CTflUTfJSOC",
					"type": "arrow"
				},
				{
					"id": "1zoIhTevPe2muR0LdpmjL",
					"type": "arrow"
				},
				{
					"id": "tiY3bfLCxpvhNVfQ2VsP7",
					"type": "arrow"
				},
				{
					"id": "AFMObxe1Svj-XMn1Ond7p",
					"type": "arrow"
				},
				{
					"id": "frANsdcHEFlElmTbSxajr",
					"type": "arrow"
				},
				{
					"id": "7O6DevAemKiVtBsQSGyeS",
					"type": "arrow"
				},
				{
					"id": "myDH7piu",
					"type": "text"
				},
				{
					"id": "uKVJ3_9mIjLlsuWRijK7R",
					"type": "arrow"
				},
				{
					"id": "MehLZBhd8lY2cIKuk35ka",
					"type": "arrow"
				},
				{
					"id": "fdnm3Q43Fowcu7xz6Lh44",
					"type": "arrow"
				}
			],
			"updated": 1654242941420,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 500,
			"versionNonce": 234543642,
			"isDeleted": false,
			"id": "myDH7piu",
			"fillStyle": "hachure",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"angle": 0,
			"x": 5481.181051332995,
			"y": 3673.53821984339,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 1258,
			"height": 276,
			"seed": 919066460,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [],
			"updated": 1654494940440,
			"link": null,
			"locked": false,
			"fontSize": 36,
			"fontFamily": 1,
			"text": "通过客户端发布消息:\nclient.publish(pubmsg, nullptr, deliveryListener);\nwhile (!deliveryListener.is_done()) \n{                      \n     this_thread::sleep_for(std::chrono::milliseconds(100));\n}",
			"rawText": "通过客户端发布消息:\nclient.publish(pubmsg, nullptr, deliveryListener);\nwhile (!deliveryListener.is_done()) \n{                      \n     this_thread::sleep_for(std::chrono::milliseconds(100));\n}",
			"baseline": 263,
			"textAlign": "left",
			"verticalAlign": "middle",
			"containerId": "CoaB8Uyyw_w2crzI5Eha1",
			"originalText": "通过客户端发布消息:\nclient.publish(pubmsg, nullptr, deliveryListener);\nwhile (!deliveryListener.is_done()) \n{                      \n     this_thread::sleep_for(std::chrono::milliseconds(100));\n}"
		},
		{
			"type": "rectangle",
			"version": 154,
			"versionNonce": 1368453604,
			"isDeleted": false,
			"id": "MZw2feZRlocWR-M9xYkPU",
			"fillStyle": "hachure",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"angle": 0,
			"x": 2154.513937075182,
			"y": 3590.871563349251,
			"strokeColor": "#c92a2a",
			"backgroundColor": "transparent",
			"width": 4708.000183105469,
			"height": 400.0000254313148,
			"seed": 1539890276,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [
				{
					"id": "z1NJYXC0IbotS1aRvxjYp",
					"type": "arrow"
				}
			],
			"updated": 1654242973999,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 262,
			"versionNonce": 466955356,
			"isDeleted": false,
			"id": "XtC6Pp7f",
			"fillStyle": "hachure",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"angle": 0,
			"x": 2272.178528546532,
			"y": 3642.871797317358,
			"strokeColor": "#364fc7",
			"backgroundColor": "transparent",
			"width": 1801,
			"height": 52,
			"seed": 1192004572,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [],
			"updated": 1654242998717,
			"link": null,
			"locked": false,
			"fontSize": 36,
			"fontFamily": 1,
			"text": "通过一个动作监听器（基于原子操作拥有更好的多线程能力，拥有更好的内存调度能力，可以适度控制休眠时长）",
			"rawText": "通过一个动作监听器（基于原子操作拥有更好的多线程能力，拥有更好的内存调度能力，可以适度控制休眠时长）",
			"baseline": 39,
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "通过一个动作监听器（基于原子操作拥有更好的多线程能力，拥有更好的内存调度能力，可以适度控制休眠时长）"
		},
		{
			"type": "arrow",
			"version": 132,
			"versionNonce": 239481562,
			"isDeleted": false,
			"id": "z1NJYXC0IbotS1aRvxjYp",
			"fillStyle": "hachure",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"angle": 0,
			"x": 1651.1964226129703,
			"y": 2907.623910157983,
			"strokeColor": "#364fc7",
			"backgroundColor": "transparent",
			"width": 480.7612209497238,
			"height": 812.5120573620711,
			"seed": 2107655644,
			"groupIds": [],
			"strokeSharpness": "round",
			"boundElements": [],
			"updated": 1654494940382,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "eftFqsimzRQCq6eMyspRY",
				"gap": 10.95287654302473,
				"focus": -0.7282453245089409
			},
			"endBinding": {
				"elementId": "MZw2feZRlocWR-M9xYkPU",
				"gap": 22.55629351248823,
				"focus": -0.9443291469385776
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
					480.7612209497238,
					812.5120573620711
				]
			]
		},
		{
			"type": "arrow",
			"version": 158,
			"versionNonce": 573331034,
			"isDeleted": false,
			"id": "f9TlkUKHeOYPiv1slxK70",
			"fillStyle": "hachure",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"angle": 0,
			"x": 5849.848867495105,
			"y": 4264.1296745378495,
			"strokeColor": "#364fc7",
			"backgroundColor": "transparent",
			"width": 402.66642252604197,
			"height": 4.982768544212377,
			"seed": 371174748,
			"groupIds": [],
			"strokeSharpness": "round",
			"boundElements": [],
			"updated": 1654494940397,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "Hg-Q_bB9U73qe6aCOXCQ9",
				"gap": 10.068539982280527,
				"focus": 0.10167387504221108
			},
			"endBinding": {
				"elementId": "tQW85a2vZdqvwGwMDRNnb",
				"gap": 9.619271332971039,
				"focus": 0.08387439629070796
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
					402.66642252604197,
					-4.982768544212377
				]
			]
		},
		{
			"type": "rectangle",
			"version": 222,
			"versionNonce": 1304033500,
			"isDeleted": false,
			"id": "sOGlgwjkC5-jhEikr1z6g",
			"fillStyle": "hachure",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"angle": 0,
			"x": 868.6818244449728,
			"y": 7414.03792992639,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 1065,
			"height": 148,
			"seed": 570380508,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [
				{
					"id": "gZ4oA8UHynu4kqt6u9giv",
					"type": "arrow"
				},
				{
					"id": "pTjYWJUD",
					"type": "text"
				},
				{
					"id": "JSbo9b8EgL_C_5UrvG8q3",
					"type": "arrow"
				},
				{
					"id": "YJoLfpcnSj3swkhaoTAyL",
					"type": "arrow"
				}
			],
			"updated": 1654244004798,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 304,
			"versionNonce": 1770482630,
			"isDeleted": false,
			"id": "pTjYWJUD",
			"fillStyle": "hachure",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"angle": 0,
			"x": 873.6818244449728,
			"y": 7442.03792992639,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 1055,
			"height": 92,
			"seed": 2097134308,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [],
			"updated": 1654494940441,
			"link": null,
			"locked": false,
			"fontSize": 36,
			"fontFamily": 1,
			"text": "使用客户端接口发送：\nclient.publish(TOPIC, PAYLOAD2, strlen(PAYLOAD2)+1);",
			"rawText": "使用客户端接口发送：\nclient.publish(TOPIC, PAYLOAD2, strlen(PAYLOAD2)+1);",
			"baseline": 79,
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "sOGlgwjkC5-jhEikr1z6g",
			"originalText": "使用客户端接口发送：\nclient.publish(TOPIC, PAYLOAD2, strlen(PAYLOAD2)+1);"
		},
		{
			"type": "arrow",
			"version": 145,
			"versionNonce": 411862746,
			"isDeleted": false,
			"id": "YJoLfpcnSj3swkhaoTAyL",
			"fillStyle": "hachure",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"angle": 0,
			"x": 363.6821296207541,
			"y": 7157.279387093236,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 481.9999694824218,
			"height": 310.4085998582359,
			"seed": 570060124,
			"groupIds": [],
			"strokeSharpness": "round",
			"boundElements": [],
			"updated": 1654494940440,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "gbEYacF1HLVBsHvZfFSKh",
				"gap": 9.961653479283314,
				"focus": -0.6347420887767341
			},
			"endBinding": {
				"elementId": "sOGlgwjkC5-jhEikr1z6g",
				"gap": 22.999725341796875,
				"focus": -0.8092294636355478
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
					481.9999694824218,
					310.4085998582359
				]
			]
		},
		{
			"type": "rectangle",
			"version": 155,
			"versionNonce": 86094820,
			"isDeleted": false,
			"id": "_6B2bQ7Wdu1XmvZhAtQ9v",
			"fillStyle": "hachure",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"angle": 0,
			"x": 817.6822211734884,
			"y": 7297.038021479124,
			"strokeColor": "#e67700",
			"backgroundColor": "transparent",
			"width": 1274.6666971842437,
			"height": 311.9999694824219,
			"seed": 1020150628,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [],
			"updated": 1654244547139,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 242,
			"versionNonce": 1853358052,
			"isDeleted": false,
			"id": "0DkFlyID",
			"fillStyle": "hachure",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"angle": 0,
			"x": 876.1820991031759,
			"y": 7339.53808251428,
			"strokeColor": "#364fc7",
			"backgroundColor": "transparent",
			"width": 181,
			"height": 52,
			"seed": 1006633564,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [],
			"updated": 1654244760503,
			"link": null,
			"locked": false,
			"fontSize": 36,
			"fontFamily": 1,
			"text": "逐条的发送",
			"rawText": "逐条的发送",
			"baseline": 39,
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "逐条的发送"
		},
		{
			"type": "rectangle",
			"version": 290,
			"versionNonce": 106829540,
			"isDeleted": false,
			"id": "Nt8dRTdzEfzYkT881cDIy",
			"fillStyle": "hachure",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"angle": 0,
			"x": 851.182129620754,
			"y": 7747.038036737913,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 1362,
			"height": 157,
			"seed": 1078711900,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [
				{
					"id": "gZ4oA8UHynu4kqt6u9giv",
					"type": "arrow"
				},
				{
					"id": "U0w7SUXg",
					"type": "text"
				},
				{
					"id": "JSbo9b8EgL_C_5UrvG8q3",
					"type": "arrow"
				},
				{
					"id": "YJoLfpcnSj3swkhaoTAyL",
					"type": "arrow"
				}
			],
			"updated": 1654244069334,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 375,
			"versionNonce": 1707776922,
			"isDeleted": false,
			"id": "U0w7SUXg",
			"fillStyle": "hachure",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"angle": 0,
			"x": 856.182129620754,
			"y": 7779.538036737913,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 1352,
			"height": 92,
			"seed": 466111844,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [],
			"updated": 1654494940442,
			"link": null,
			"locked": false,
			"fontSize": 36,
			"fontFamily": 1,
			"text": "使用客户端接口发送：\nclient.publish(mqtt::message(TOPIC, PAYLOAD3, QOS, false));",
			"rawText": "使用客户端接口发送：\nclient.publish(mqtt::message(TOPIC, PAYLOAD3, QOS, false));",
			"baseline": 79,
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "Nt8dRTdzEfzYkT881cDIy",
			"originalText": "使用客户端接口发送：\nclient.publish(mqtt::message(TOPIC, PAYLOAD3, QOS, false));"
		},
		{
			"type": "rectangle",
			"version": 194,
			"versionNonce": 2111128284,
			"isDeleted": false,
			"id": "fHrjMijbsYyTctIekViSG",
			"fillStyle": "hachure",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"angle": 0,
			"x": 828.3483690413268,
			"y": 7647.704550816689,
			"strokeColor": "#e67700",
			"backgroundColor": "transparent",
			"width": 1605.3334045410156,
			"height": 276.0000610351562,
			"seed": 483786204,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [
				{
					"id": "MnpBtp_73OM3dvppnuvyE",
					"type": "arrow"
				}
			],
			"updated": 1654244550301,
			"link": null,
			"locked": false
		},
		{
			"type": "arrow",
			"version": 133,
			"versionNonce": 1242275994,
			"isDeleted": false,
			"id": "MnpBtp_73OM3dvppnuvyE",
			"fillStyle": "hachure",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"angle": 0,
			"x": 360.8017312694021,
			"y": 7215.141380324161,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 453.54685139497155,
			"height": 578.6454094717992,
			"seed": 2028514788,
			"groupIds": [],
			"strokeSharpness": "round",
			"boundElements": [],
			"updated": 1654494940420,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "gbEYacF1HLVBsHvZfFSKh",
				"gap": 14.167524973536274,
				"focus": -0.7084385400946845
			},
			"endBinding": {
				"elementId": "fHrjMijbsYyTctIekViSG",
				"gap": 13.999786376953125,
				"focus": -0.9035707905763587
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
					453.54685139497155,
					578.6454094717992
				]
			]
		},
		{
			"type": "text",
			"version": 106,
			"versionNonce": 783704932,
			"isDeleted": false,
			"id": "lyCpVY9p",
			"fillStyle": "hachure",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"angle": 0,
			"x": 882.1820380680197,
			"y": 7684.038051996702,
			"strokeColor": "#364fc7",
			"backgroundColor": "transparent",
			"width": 717,
			"height": 52,
			"seed": 720973916,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [],
			"updated": 1654244763463,
			"link": null,
			"locked": false,
			"fontSize": 36,
			"fontFamily": 1,
			"text": "通过一个监听器，没有token,没有“堆”的消息",
			"rawText": "通过一个监听器，没有token,没有“堆”的消息",
			"baseline": 39,
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "通过一个监听器，没有token,没有“堆”的消息"
		},
		{
			"type": "rectangle",
			"version": 352,
			"versionNonce": 1059840988,
			"isDeleted": false,
			"id": "TebHoweR2TOGLvU5jQILf",
			"fillStyle": "hachure",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"angle": 0,
			"x": 850.3493659488795,
			"y": 8081.038059626095,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 1362,
			"height": 157,
			"seed": 1651555300,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [
				{
					"id": "gZ4oA8UHynu4kqt6u9giv",
					"type": "arrow"
				},
				{
					"id": "hJbvE6Af",
					"type": "text"
				},
				{
					"id": "JSbo9b8EgL_C_5UrvG8q3",
					"type": "arrow"
				},
				{
					"id": "YJoLfpcnSj3swkhaoTAyL",
					"type": "arrow"
				},
				{
					"id": "mI6BgLVzwKwQvhsihzJaw",
					"type": "arrow"
				},
				{
					"id": "DTCUrDmkHWVYa38U3mMLe",
					"type": "arrow"
				}
			],
			"updated": 1654244898553,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 456,
			"versionNonce": 581269894,
			"isDeleted": false,
			"id": "hJbvE6Af",
			"fillStyle": "hachure",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"angle": 0,
			"x": 855.3493659488795,
			"y": 8113.538059626095,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 1352,
			"height": 92,
			"seed": 1190421596,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [],
			"updated": 1654494940443,
			"link": null,
			"locked": false,
			"fontSize": 36,
			"fontFamily": 1,
			"text": "创建主题：\nauto top = cli.get_topic(\"data/time\", QOS);",
			"rawText": "创建主题：\nauto top = cli.get_topic(\"data/time\", QOS);",
			"baseline": 79,
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "TebHoweR2TOGLvU5jQILf",
			"originalText": "创建主题：\nauto top = cli.get_topic(\"data/time\", QOS);"
		},
		{
			"type": "arrow",
			"version": 243,
			"versionNonce": 870848602,
			"isDeleted": false,
			"id": "mI6BgLVzwKwQvhsihzJaw",
			"fillStyle": "hachure",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"angle": 0,
			"x": 306.23333103154147,
			"y": 7212.038174067015,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 523.3162643937303,
			"height": 907.7936633876507,
			"seed": 1644515804,
			"groupIds": [],
			"strokeSharpness": "round",
			"boundElements": [],
			"updated": 1654494940442,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "gbEYacF1HLVBsHvZfFSKh",
				"gap": 9.167677561426899,
				"focus": -0.6778195916349541
			},
			"endBinding": {
				"elementId": "TebHoweR2TOGLvU5jQILf",
				"gap": 20.799770523607776,
				"focus": -0.934812477976209
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
					523.3162643937303,
					907.7936633876507
				]
			]
		},
		{
			"type": "rectangle",
			"version": 364,
			"versionNonce": 1701240676,
			"isDeleted": false,
			"id": "6I3UeYgXN6uKg8jQBmvWI",
			"fillStyle": "hachure",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"angle": 0,
			"x": 2345.348908185208,
			"y": 8066.5380519967,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 1362,
			"height": 157,
			"seed": 1052359900,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [
				{
					"id": "gZ4oA8UHynu4kqt6u9giv",
					"type": "arrow"
				},
				{
					"id": "bdlt7kNC",
					"type": "text"
				},
				{
					"id": "JSbo9b8EgL_C_5UrvG8q3",
					"type": "arrow"
				},
				{
					"id": "YJoLfpcnSj3swkhaoTAyL",
					"type": "arrow"
				},
				{
					"id": "mI6BgLVzwKwQvhsihzJaw",
					"type": "arrow"
				},
				{
					"id": "DTCUrDmkHWVYa38U3mMLe",
					"type": "arrow"
				}
			],
			"updated": 1654244539799,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 493,
			"versionNonce": 836435610,
			"isDeleted": false,
			"id": "bdlt7kNC",
			"fillStyle": "hachure",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"angle": 0,
			"x": 2350.348908185208,
			"y": 8099.0380519967,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 1352,
			"height": 92,
			"seed": 1886523108,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [],
			"updated": 1654494940444,
			"link": null,
			"locked": false,
			"fontSize": 36,
			"fontFamily": 1,
			"text": "通过主题发送：\ntop.publish(to_string(t));",
			"rawText": "通过主题发送：\ntop.publish(to_string(t));",
			"baseline": 79,
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "6I3UeYgXN6uKg8jQBmvWI",
			"originalText": "通过主题发送：\ntop.publish(to_string(t));"
		},
		{
			"type": "arrow",
			"version": 171,
			"versionNonce": 872962246,
			"isDeleted": false,
			"id": "DTCUrDmkHWVYa38U3mMLe",
			"fillStyle": "hachure",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"angle": 0,
			"x": 2228.3488776676304,
			"y": 8150.72957322322,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 113.9999389648433,
			"height": 7.716338969294156,
			"seed": 2076429788,
			"groupIds": [],
			"strokeSharpness": "round",
			"boundElements": [],
			"updated": 1654494940444,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "TebHoweR2TOGLvU5jQILf",
				"gap": 15.999511718750568,
				"focus": -0.4493474633174356
			},
			"endBinding": {
				"elementId": "6I3UeYgXN6uKg8jQBmvWI",
				"gap": 3.000091552734375,
				"focus": -0.47920001975383847
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
					113.9999389648433,
					7.716338969294156
				]
			]
		},
		{
			"type": "rectangle",
			"version": 115,
			"versionNonce": 1601855196,
			"isDeleted": false,
			"id": "xtFj6esEewtjLJQ01uGd6",
			"fillStyle": "hachure",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"angle": 0,
			"x": 836.1280048100161,
			"y": 7982.870706313931,
			"strokeColor": "#e67700",
			"backgroundColor": "transparent",
			"width": 2909.33349609375,
			"height": 314.66664632161337,
			"seed": 515652060,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [],
			"updated": 1654244496520,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 60,
			"versionNonce": 811357924,
			"isDeleted": false,
			"id": "qIfsi9Xh",
			"fillStyle": "hachure",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"angle": 0,
			"x": 918.1277199792871,
			"y": 8004.2040803373675,
			"strokeColor": "#364fc7",
			"backgroundColor": "transparent",
			"width": 217,
			"height": 52,
			"seed": 197763940,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [],
			"updated": 1654244767032,
			"link": null,
			"locked": false,
			"fontSize": 36,
			"fontFamily": 1,
			"text": "通过主题发送",
			"rawText": "通过主题发送",
			"baseline": 39,
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "通过主题发送"
		},
		{
			"type": "rectangle",
			"version": 120,
			"versionNonce": 794421724,
			"isDeleted": false,
			"id": "IhN5L1ODXAkRJnLsatyMM",
			"fillStyle": "hachure",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"angle": 0,
			"x": -379.87256485144565,
			"y": 8597.537606948703,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 867,
			"height": 213.33333333333394,
			"seed": 1459757916,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [
				{
					"id": "keQGqqp-0wC2OFUe9XWwR",
					"type": "arrow"
				},
				{
					"type": "text",
					"id": "xAb6Q5WT"
				},
				{
					"id": "pM6FTa5Erw4OVEJ0b57ug",
					"type": "arrow"
				}
			],
			"updated": 1654261262293,
			"link": null,
			"locked": false
		},
		{
			"type": "arrow",
			"version": 254,
			"versionNonce": 99883866,
			"isDeleted": false,
			"id": "keQGqqp-0wC2OFUe9XWwR",
			"fillStyle": "hachure",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"angle": 0,
			"x": -1045.2726232749633,
			"y": 6185.537332290504,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 646.7334731370581,
			"height": 2546.342166730804,
			"seed": 731856092,
			"groupIds": [],
			"strokeSharpness": "round",
			"boundElements": [],
			"updated": 1654494940445,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "cc25eEaYz8T-81nUqQ1Gg",
				"gap": 1.6665089925236316,
				"focus": -0.5690810094698644
			},
			"endBinding": {
				"elementId": "IhN5L1ODXAkRJnLsatyMM",
				"gap": 18.666585286459394,
				"focus": -0.9969689439980849
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
					646.7334731370581,
					2546.342166730804
				]
			]
		},
		{
			"type": "text",
			"version": 83,
			"versionNonce": 2043774598,
			"isDeleted": false,
			"id": "xAb6Q5WT",
			"fillStyle": "hachure",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"angle": 0,
			"x": -374.87256485144565,
			"y": 8681.20427361537,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 857,
			"height": 46,
			"seed": 273321060,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [],
			"updated": 1654494940445,
			"link": null,
			"locked": false,
			"fontSize": 36,
			"fontFamily": 1,
			"text": "消息订阅",
			"rawText": "消息订阅",
			"baseline": 32,
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "IhN5L1ODXAkRJnLsatyMM",
			"originalText": "消息订阅"
		},
		{
			"type": "rectangle",
			"version": 222,
			"versionNonce": 298681052,
			"isDeleted": false,
			"id": "rJg6daFa3pxsz5XK_0cz9",
			"fillStyle": "hachure",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"angle": 0,
			"x": -483.871842602098,
			"y": 9283.538062169255,
			"strokeColor": "#e67700",
			"backgroundColor": "transparent",
			"width": 1017,
			"height": 195,
			"seed": 591288292,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [
				{
					"type": "text",
					"id": "8OuHSRRX"
				},
				{
					"id": "4IXiGaPz9-mg_VA_FdzBH",
					"type": "arrow"
				},
				{
					"id": "ZV7LPImdCvAU-pQh6DE85",
					"type": "arrow"
				}
			],
			"updated": 1654244970701,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 179,
			"versionNonce": 744922714,
			"isDeleted": false,
			"id": "8OuHSRRX",
			"fillStyle": "hachure",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"angle": 0,
			"x": -478.871842602098,
			"y": 9358.038062169255,
			"strokeColor": "#e67700",
			"backgroundColor": "transparent",
			"width": 1007,
			"height": 46,
			"seed": 2107038684,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [],
			"updated": 1654494940446,
			"link": null,
			"locked": false,
			"fontSize": 36,
			"fontFamily": 1,
			"text": "客户端重连",
			"rawText": "客户端重连",
			"baseline": 32,
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "rJg6daFa3pxsz5XK_0cz9",
			"originalText": "客户端重连"
		},
		{
			"type": "rectangle",
			"version": 298,
			"versionNonce": 2100212422,
			"isDeleted": false,
			"id": "RmWlsg7Oyu2nkCEo8w3Tf",
			"fillStyle": "hachure",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"angle": 0,
			"x": 894.7957599369638,
			"y": 9257.537594233061,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 760.0002034505208,
			"height": 184.00004069010348,
			"seed": 1429929948,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [
				{
					"id": "4IXiGaPz9-mg_VA_FdzBH",
					"type": "arrow"
				},
				{
					"type": "text",
					"id": "35Zqspmw"
				},
				{
					"id": "zEcd5bIMZ0iPe5sFg8hlU",
					"type": "arrow"
				}
			],
			"updated": 1654494940447,
			"link": null,
			"locked": false
		},
		{
			"type": "arrow",
			"version": 596,
			"versionNonce": 896910106,
			"isDeleted": false,
			"id": "4IXiGaPz9-mg_VA_FdzBH",
			"fillStyle": "hachure",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"angle": 0,
			"x": 552.1755584970485,
			"y": 9365.226291518753,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 333.99489450580234,
			"height": 2.3842128652013344,
			"seed": 1488155492,
			"groupIds": [],
			"strokeSharpness": "round",
			"boundElements": [],
			"updated": 1654494940447,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "rJg6daFa3pxsz5XK_0cz9",
				"gap": 19.04740109914647,
				"focus": -0.19358913683782766
			},
			"endBinding": {
				"elementId": "RmWlsg7Oyu2nkCEo8w3Tf",
				"gap": 8.625306934112865,
				"focus": -0.22010875212710332
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
					333.99489450580234,
					2.3842128652013344
				]
			]
		},
		{
			"type": "arrow",
			"version": 135,
			"versionNonce": 1201282310,
			"isDeleted": false,
			"id": "ZV7LPImdCvAU-pQh6DE85",
			"fillStyle": "hachure",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"angle": 0,
			"x": -1179.8715984614716,
			"y": 6186.2042812447735,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 664.0000406901037,
			"height": 3216.6667683919286,
			"seed": 196140252,
			"groupIds": [],
			"strokeSharpness": "round",
			"boundElements": [],
			"updated": 1654494940446,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "cc25eEaYz8T-81nUqQ1Gg",
				"gap": 2.3334579467918957,
				"focus": -0.11153111626207801
			},
			"endBinding": {
				"elementId": "rJg6daFa3pxsz5XK_0cz9",
				"gap": 31.999715169269848,
				"focus": -1.0309862705614314
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
					664.0000406901037,
					3216.6667683919286
				]
			]
		},
		{
			"type": "text",
			"version": 44,
			"versionNonce": 945767578,
			"isDeleted": false,
			"id": "35Zqspmw",
			"fillStyle": "hachure",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"angle": 0,
			"x": 899.7957599369638,
			"y": 9303.537614578112,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 750.0002034505208,
			"height": 92,
			"seed": 446706532,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [],
			"updated": 1654494940448,
			"link": null,
			"locked": false,
			"fontSize": 36.000029296882936,
			"fontFamily": 1,
			"text": "检测客户端链接状态\n!cli.is_connected()",
			"rawText": "检测客户端链接状态\n!cli.is_connected()",
			"baseline": 79,
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "RmWlsg7Oyu2nkCEo8w3Tf",
			"originalText": "检测客户端链接状态\n!cli.is_connected()"
		},
		{
			"type": "rectangle",
			"version": 40,
			"versionNonce": 1259631196,
			"isDeleted": false,
			"id": "M61Ka8tK9YiZ4Ew5f4McR",
			"fillStyle": "hachure",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"angle": 0,
			"x": 2177.4608091719947,
			"y": 9267.537784967903,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 824,
			"height": 173.33333333333394,
			"seed": 25793124,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [
				{
					"id": "zEcd5bIMZ0iPe5sFg8hlU",
					"type": "arrow"
				},
				{
					"type": "text",
					"id": "56v5p5ID"
				}
			],
			"updated": 1654245059190,
			"link": null,
			"locked": false
		},
		{
			"type": "arrow",
			"version": 68,
			"versionNonce": 2147459418,
			"isDeleted": false,
			"id": "zEcd5bIMZ0iPe5sFg8hlU",
			"fillStyle": "hachure",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"angle": 0,
			"x": 1668.1273130782447,
			"y": 9355.537866466519,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 501.33341471354106,
			"height": 2.666625811953054,
			"seed": 1243362532,
			"groupIds": [],
			"strokeSharpness": "round",
			"boundElements": [],
			"updated": 1654494940448,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "RmWlsg7Oyu2nkCEo8w3Tf",
				"gap": 13.331349690760248,
				"focus": 0.08606997538905894
			},
			"endBinding": {
				"elementId": "M61Ka8tK9YiZ4Ew5f4McR",
				"gap": 8.000081380208712,
				"focus": 0.040145113271750174
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
					501.33341471354106,
					-2.666625811953054
				]
			]
		},
		{
			"type": "text",
			"version": 31,
			"versionNonce": 977877318,
			"isDeleted": false,
			"id": "56v5p5ID",
			"fillStyle": "hachure",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"angle": 0,
			"x": 2182.4608091719947,
			"y": 9308.20445163457,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 814,
			"height": 92,
			"seed": 551333988,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [],
			"updated": 1654494940449,
			"link": null,
			"locked": false,
			"fontSize": 36,
			"fontFamily": 1,
			"text": "客户端重连：\ncli.reconnect();",
			"rawText": "客户端重连：\ncli.reconnect();",
			"baseline": 79,
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "M61Ka8tK9YiZ4Ew5f4McR",
			"originalText": "客户端重连：\ncli.reconnect();"
		},
		{
			"type": "rectangle",
			"version": 135,
			"versionNonce": 1099232996,
			"isDeleted": false,
			"id": "ZPdVyyYp6g5uTsz_V9tgn",
			"fillStyle": "hachure",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"angle": 0,
			"x": 697.5123330163951,
			"y": 8595.191088114265,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 726,
			"height": 193,
			"seed": 1485131876,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [
				{
					"type": "text",
					"id": "RlOz1F9g"
				},
				{
					"id": "pM6FTa5Erw4OVEJ0b57ug",
					"type": "arrow"
				},
				{
					"id": "1YzuJplOEdcGRaLaVUIKi",
					"type": "arrow"
				}
			],
			"updated": 1654261373212,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 177,
			"versionNonce": 1951606682,
			"isDeleted": false,
			"id": "RlOz1F9g",
			"fillStyle": "hachure",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"angle": 0,
			"x": 702.5123330163951,
			"y": 8645.691088114265,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 716,
			"height": 92,
			"seed": 1512408028,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [],
			"updated": 1654494940450,
			"link": null,
			"locked": false,
			"fontSize": 36,
			"fontFamily": 1,
			"text": "客户端和链接选项设置\n确定主题和服务质量QOS",
			"rawText": "客户端和链接选项设置\n确定主题和服务质量QOS",
			"baseline": 79,
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "ZPdVyyYp6g5uTsz_V9tgn",
			"originalText": "客户端和链接选项设置\n确定主题和服务质量QOS"
		},
		{
			"type": "arrow",
			"version": 231,
			"versionNonce": 1755193478,
			"isDeleted": false,
			"id": "pM6FTa5Erw4OVEJ0b57ug",
			"fillStyle": "hachure",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"angle": 0,
			"x": 497.97747616572235,
			"y": 8692.139176592485,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 196.44690330546916,
			"height": 6.582871777944092,
			"seed": 1617069532,
			"groupIds": [],
			"strokeSharpness": "round",
			"boundElements": [],
			"updated": 1654494940449,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "IhN5L1ODXAkRJnLsatyMM",
				"gap": 10.850041017167865,
				"focus": -0.22241463568904055
			},
			"endBinding": {
				"elementId": "ZPdVyyYp6g5uTsz_V9tgn",
				"gap": 3.0879535452036655,
				"focus": -0.17759742234436945
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
					196.44690330546916,
					6.582871777944092
				]
			]
		},
		{
			"type": "rectangle",
			"version": 235,
			"versionNonce": 1340648164,
			"isDeleted": false,
			"id": "DxYRRe1M_fM_JZV2J1CE7",
			"fillStyle": "hachure",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"angle": 0,
			"x": 1556.3413735437389,
			"y": 8617.099886332038,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 982,
			"height": 124,
			"seed": 1444415844,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [
				{
					"id": "1YzuJplOEdcGRaLaVUIKi",
					"type": "arrow"
				},
				{
					"type": "text",
					"id": "0yWYDB1e"
				},
				{
					"id": "8EKu1RB3x3BBtj06l1RQ1",
					"type": "arrow"
				}
			],
			"updated": 1654261478244,
			"link": null,
			"locked": false
		},
		{
			"type": "arrow",
			"version": 327,
			"versionNonce": 2038375514,
			"isDeleted": false,
			"id": "1YzuJplOEdcGRaLaVUIKi",
			"fillStyle": "hachure",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"angle": 0,
			"x": 1428.859842830199,
			"y": 8676.938305514104,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 120.7272861830636,
			"height": 1.2032925318453636,
			"seed": 1511792228,
			"groupIds": [],
			"strokeSharpness": "round",
			"boundElements": [],
			"updated": 1654494940450,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "ZPdVyyYp6g5uTsz_V9tgn",
				"gap": 5.347509813803932,
				"focus": -0.11064566622260474
			},
			"endBinding": {
				"elementId": "DxYRRe1M_fM_JZV2J1CE7",
				"gap": 6.754244530476192,
				"focus": 0.12446599764960298
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
					120.7272861830636,
					-1.2032925318453636
				]
			]
		},
		{
			"type": "text",
			"version": 96,
			"versionNonce": 918465926,
			"isDeleted": false,
			"id": "0yWYDB1e",
			"fillStyle": "hachure",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"angle": 0,
			"x": 1561.3413735437389,
			"y": 8633.099886332038,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 972,
			"height": 92,
			"seed": 1439799012,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [],
			"updated": 1654494940452,
			"link": null,
			"locked": false,
			"fontSize": 36.0286557610571,
			"fontFamily": 1,
			"text": "设置链接回应 \nmqtt::connect_response rsp = cli.connect(connOpts);",
			"rawText": "设置链接回应 \nmqtt::connect_response rsp = cli.connect(connOpts);",
			"baseline": 79,
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "DxYRRe1M_fM_JZV2J1CE7",
			"originalText": "设置链接回应 \nmqtt::connect_response rsp = cli.connect(connOpts);"
		},
		{
			"type": "rectangle",
			"version": 101,
			"versionNonce": 158392164,
			"isDeleted": false,
			"id": "RjLeOoLUGVurQ5MRRaVRS",
			"fillStyle": "hachure",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"angle": 0,
			"x": 2741.6132851648326,
			"y": 8621.481638346198,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 774,
			"height": 121,
			"seed": 1378214884,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [
				{
					"id": "8EKu1RB3x3BBtj06l1RQ1",
					"type": "arrow"
				},
				{
					"type": "text",
					"id": "FY2cEQRp"
				},
				{
					"id": "Oho76AsVbH-HJikRZyZXY",
					"type": "arrow"
				}
			],
			"updated": 1654261611836,
			"link": null,
			"locked": false
		},
		{
			"type": "arrow",
			"version": 129,
			"versionNonce": 1457196230,
			"isDeleted": false,
			"id": "8EKu1RB3x3BBtj06l1RQ1",
			"fillStyle": "hachure",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"angle": 0,
			"x": 2557.2464350295113,
			"y": 8675.161563401614,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 165.07704285433192,
			"height": 0.3394789656249486,
			"seed": 1380804068,
			"groupIds": [],
			"strokeSharpness": "round",
			"boundElements": [],
			"updated": 1654494940452,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "DxYRRe1M_fM_JZV2J1CE7",
				"gap": 18.905061485772425,
				"focus": -0.04590237525201613
			},
			"endBinding": {
				"elementId": "RjLeOoLUGVurQ5MRRaVRS",
				"gap": 19.289807280989432,
				"focus": 0.13043432180935624
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
					165.07704285433192,
					-0.3394789656249486
				]
			]
		},
		{
			"type": "text",
			"version": 78,
			"versionNonce": 832907098,
			"isDeleted": false,
			"id": "FY2cEQRp",
			"fillStyle": "hachure",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"angle": 0,
			"x": 2746.6132851648326,
			"y": 8635.981638346198,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 764,
			"height": 92,
			"seed": 2145066340,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [],
			"updated": 1654494940453,
			"link": null,
			"locked": false,
			"fontSize": 36,
			"fontFamily": 1,
			"text": "客户订阅设定：\ncli.subscribe(TOPICS, QOS);",
			"rawText": "客户订阅设定：\ncli.subscribe(TOPICS, QOS);",
			"baseline": 79,
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "RjLeOoLUGVurQ5MRRaVRS",
			"originalText": "客户订阅设定：\ncli.subscribe(TOPICS, QOS);"
		},
		{
			"type": "rectangle",
			"version": 66,
			"versionNonce": 1702609124,
			"isDeleted": false,
			"id": "Gjbuiq_kxdQJScClIS_XN",
			"fillStyle": "hachure",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"angle": 0,
			"x": 3749.4233437585826,
			"y": 8628.054323587898,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 750,
			"height": 118.30806732177734,
			"seed": 993216860,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [
				{
					"id": "Oho76AsVbH-HJikRZyZXY",
					"type": "arrow"
				},
				{
					"type": "text",
					"id": "NDrvLanB"
				}
			],
			"updated": 1654261668723,
			"link": null,
			"locked": false
		},
		{
			"type": "arrow",
			"version": 88,
			"versionNonce": 66792474,
			"isDeleted": false,
			"id": "Oho76AsVbH-HJikRZyZXY",
			"fillStyle": "hachure",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"angle": 0,
			"x": 3525.9518166589733,
			"y": 8673.16257064408,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 214.70748901367188,
			"height": 10.296686876108652,
			"seed": 1171977564,
			"groupIds": [],
			"strokeSharpness": "round",
			"boundElements": [],
			"updated": 1654494940453,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "RjLeOoLUGVurQ5MRRaVRS",
				"gap": 10.338531494140625,
				"focus": -0.35257306054222526
			},
			"endBinding": {
				"elementId": "Gjbuiq_kxdQJScClIS_XN",
				"gap": 8.7640380859375,
				"focus": -0.18998458765398296
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
					214.70748901367188,
					10.296686876108652
				]
			]
		},
		{
			"type": "text",
			"version": 11,
			"versionNonce": 766556806,
			"isDeleted": false,
			"id": "NDrvLanB",
			"fillStyle": "hachure",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"angle": 0,
			"x": 3754.4233437585826,
			"y": 8641.208357248786,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 740,
			"height": 92,
			"seed": 633609308,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [],
			"updated": 1654494940454,
			"link": null,
			"locked": false,
			"fontSize": 36,
			"fontFamily": 1,
			"text": "获取客户端消息：\nauto msg = cli.consume_message();",
			"rawText": "获取客户端消息：\nauto msg = cli.consume_message();",
			"baseline": 79,
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "Gjbuiq_kxdQJScClIS_XN",
			"originalText": "获取客户端消息：\nauto msg = cli.consume_message();"
		}
	],
	"appState": {
		"theme": "light",
		"viewBackgroundColor": "#f1f3f5",
		"currentItemStrokeColor": "#000000",
		"currentItemBackgroundColor": "transparent",
		"currentItemFillStyle": "hachure",
		"currentItemStrokeWidth": 0.5,
		"currentItemStrokeStyle": "solid",
		"currentItemRoughness": 2,
		"currentItemOpacity": 100,
		"currentItemFontFamily": 1,
		"currentItemFontSize": 36,
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