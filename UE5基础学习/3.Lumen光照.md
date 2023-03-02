lumen光照的设计初衷：
![[Pasted image 20230227093416.png]]

# 软件光追
### 几何体限制（Geometry Limitations） ：

-   只有静态网格体、实例化静态网格体、分层实例化静态网格体和地形地貌能够在Lumen场景中呈现。
-   必须在`植被工具`设置中设置 **影响距离场光照（Affect Distance Field Lighting）** 才能启用植被。
###  材质限制（Material Limitations） ：

-   不支持世界位置偏移(WPO)。   
-   透明材质会被距离场忽略，蒙皮材质将被视为不透明。  
    -   蒙皮材质可能会导致植被上发生`严重的过度阴影`，从而使大片区域的叶子被屏蔽。
       
-   距离场是使用分配到静态网格体资产的材质属性构建的，而不是重载组件中的属性。
    -   重载具有`不同混合模式`或`启用了双面属性的的材质`将会导致三角形呈现和网格的距离场呈现不匹配。

### 工作流限制（Workflow Limitations）：

-   软件光线追踪要求关卡由模块化几何体组成。墙壁、地板和天花板等物体应该是单独的网格体。`大型的单个网格体`，例如山峰或多层大楼，将会具有较差的距离场呈现，可能会导致出现自遮蔽瑕疵。
    
-   `壁厚度不能少于10厘米`，以避免光线泄漏。
    
-   距离场不能呈现非常薄的特性，也不能呈现单面的网格体的后视效果。如果可以确保查看者看不到单侧网格体的`三角形背面`或仅`使用封闭的几何体`，就可以避免这些类型的瑕疵。
    
-   网格体距离场分辨率根据导入的静态`网格体缩放进行分配`。
    
    -   导入后非常小并随后在组件上放大的网格体将 **不会（will not）** 具有充足的距离场分辨率。如果在关卡中放置的实例上进行缩放，则应该根据静态网格体编辑器的构建设置来设置距离场分辨率。

# 硬件光追



## Lumen的平台支持

-   Lumen `**不（does not）** 支持前几代主机，例如PlayStation 4和Xbox One`(所以做游戏哪能这样子？)。
    
-   依赖动态光照的项目可以在这些平台和旧版PC硬件上组合使用[距离场环境光遮蔽](https://docs.unrealengine.com/5.1/zh-CN/distance-field-ambient-occlusion-in-unreal-engine)和[场景空间全局光照](https://docs.unrealengine.com/5.1/zh-CN/screen-space-global-illumination-in-unreal-engine)。
    
-   Lumen是面向次世代主机（PlayStation 5和Xbox Series S/X）和高端PC开发的。Lumen有两种光线追踪模式，每种都有不同的要求。
    
-   软件光线追踪要求：
    
-   显卡使用支持Shader Model 5 (SM5)的DirectX 11
    
    要求NVIDIA GeForce GTX-1070或更高级别的显卡。
    
-   硬件光线追踪要求：
    
    -   采用DirectX 12的Windows 10
        
    -   显卡必须是NVIDIA RTX-2000系列或更高，AMD RX-6000系列或更高。
        
- `  Lumen **不（does not）** 支持移动平台。我们目前没有计划开发适用于移动设备渲染器的动态全局光照。使用动态光照的游戏需要在移动设备上使用无阴影的[天空光照](https://docs.unrealengine.com/5.1/zh-CN/sky-lights-in-unreal-engine)。`(移动平台的限制)
    
-   Lumen 目前 **不（does not）** 支持虚拟现实(VR)系统。虽然支持VR，`但VR所要求的的高帧率和分辨率让全局光照无法适应`。(因为光锥的目标帧率是90fps，所以虚幻5目前是不能适应的)