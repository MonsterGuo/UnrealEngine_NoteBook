> [(4) UE5 World Partition / Getting Started Tutorial - YouTube](https://www.youtube.com/watch?v=ZY62CoOkwHA)

关键命令台指令：`wp.runtime.ToggleDataLayerActivation`

### 转化已有的关卡来使用世界分区
命令行工具
![[Pasted image 20230225164553.png|1000|L]]

UnrealEditor.exe QAGame -run=WorldPartitionConvertCommandlet Playground.umap -AllowCommandletRendering

首先找到 `UnrealEditor.exe` 可执行文件的位置。比如在以上示例中： `c:\Builds\Home_UE5_Engine\Engine\Binaries\Win64`。（原来也是自己编译的版本。。。回头得看看）
![[Pasted image 20230225164441.jpg|L]]
**-SCCProvider=(None,Perforce...)**

指定使用源控制提供者。若要不带源控制运行，输入`-SCCProvider=None`。

**-Verbose**

显示详细日志记录

**-ConversionSuffix**

在转化后的地图名后面添加_WP后缀。这在测试时很有用，避免更改源关卡。

**-DeleteSourceLevels**

在转化后删除源关卡。

**-ReportOnly**

只显示转化时会发生的事情，而不实际执行转化。

**-GenerateIni**

针对此地图生成一个默认 `.ini` 转化文件，而不实际执行转化。

**-SkipStableGUIDValidation**

跳过不稳定Actor GUIDs的验证过程。带有不稳定Actor GUIDs的关卡在多次转化时会产生不同的输出结果。重新保存关卡可以解决该问题。

**-OnlyMergeSubLevels**

不使用世界分区转化合并关卡和子关卡至一Actor一文件。转化后的关卡可以在使用世界分区的关卡中作为关卡实例。

**-FoliageTypePath=[Path]**

将植被类型作为资产提取到指定路径。若关卡包含嵌入的植被类型，使用此参数。


### 世界分区中的Actor

编辑世界时，Actor可以加入到任何地点，并且会基于它们的 **是否空间加载（Is Spatially Loaded）** 设置被自动分配至一个网格单元。该选项位于Actor的 **细节（Details）** 面板中的 **世界分区（World Partition）** 部分。

[![world-partition-actor-options.png|L](https://docs.unrealengine.com/5.1/Images/building-virtual-worlds/world-partition/world-partition-actor-options.jpg)


设置

描述
| 名称                       | 详情                                                                                |
| -------------------------- | ----------------------------------------------------------------------------------- |
| 运行时网格（Runtime Grid） | 判定Actor被放置在哪一个分区网格。如果选为 **无（None）** ，网格将会由分区系统决定。 |
| 是否空间加载（Is Spatially Loaded）                           |                                                                                     |

判定Actor是否为空间加载：

-   若启用，该Actor将会在进入任何流送源的范围内，并且没有被分配至禁用的数据层时加载。
    
-   若禁用，该Actor只要在没有被分配至禁用的数据层时就会加载。

由于一Actor一文件系统中，Actor都储存在各自独立的文件中，你不必从源控制中打开关卡文件来更改世界中的Actor。这样你在编辑Actor时，团队的其他成员仍然可以使用关卡文件。

更多有关一Actor一文件系统和虚幻引擎的集成源控制，参考 [一Actor一文件](https://docs.unrealengine.com/5.1/zh-CN/one-file-per-actor-in-unreal-engine) 文档.


### 流送源 (当数据准备好后玩家才会被传送过去)
运行时网格中单元的流送由两个因素判定：
-   流送源  
-   运行时网格设定
前者为关卡中流送源的位置。
流送源组件在世界中确定一个位置并且触发其周围网格单元的加载。玩家的控制器便是一种流送源。使用 `**世界分区流送源（World Partition Streaming Source）**` 组件也可以添加其他的流送源。比如，如果玩家要`传送至某个位置`，此处的流送源组件`便会启动`，这样可以加载其周围的网格单元。`当网格单元加载完毕，玩家到达此位置，`该流送源组件便会停用。玩家原本所在位置已经没有流送源，所以那里的网格单元会从内存中卸载。
![[Pasted image 20230225170832.png|L]]
