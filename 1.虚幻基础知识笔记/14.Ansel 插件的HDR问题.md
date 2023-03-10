 #  一．关于Raw格式的问题
 为了执行Raw捕获(EXR格式)，Ansel尝试使用某些启发式方法来检测哪个游戏缓冲区
包含HDR像素数据。这些启发式方法并不适用于所有游戏。例如，它们并不适用于游戏
使用多线程呈现的延迟上下文。==对于这些场景，可以使用提示API (查看 ansel/ hint .h)。除了HDR颜色缓冲区，Ansel还可以使用深度或HUDless缓冲区来应用需要这些类型的缓冲区的效果(如景深)。==

# 二．关于Raw格式的开启关闭

下面我们将概述如何使用提示API在这些情况下使捕获工作。
如果游戏开发者不想使用提示API使原始捕获工作，则应该在startSession回调期间将the ==ansel：：SessionConfiguration中的“isRawAllowed”设置设置为FALSE。这将禁用Ansel用户界面中的‘Raw’选项。==

```C++

// 在正确的设置HDR渲染目标前先调用这个

// bufferType是一个可选参数，指定this -是什么类型的缓冲区

// HDR颜色缓冲区，深度缓冲区或HUDless缓冲区。默认选项是HDR颜色缓冲区。

// hintType是一个可选参数，指定this -是什么类型的提示

// 它可以在此提示所标记的缓冲区的绑定之后或之前调用。

//默认选项是kHintTypePreBind，这意味着提示应该在//渲染目标被绑定。

// threadId是一个可选参数，允许Ansel匹配调用的线程

// SetRenderTarget(或类似的函数，因为它依赖于图形API)

//调用该提示的线程。knoomatching的默认值

//表示不会发生这样的匹配。特殊值0意味着

// Ansel SDK将自动匹配线程id。任何其他值都表示特定的线程id

// 已知在积分方面。

//函数一
ANSEL_SDK_API void markBufferBind(BufferType bufferType = kBufferTypeHDR,

HintType hintType = kHintTypePreBind,

uint64_t threadId = kThreadingBehaviourNoMatching);

//函数二
ANSEL_SDK_API void markBufferFinished(BufferType bufferType = kBufferTypeHDR,

uint64_t threadId = kThreadingBehaviourNoMatching);
```