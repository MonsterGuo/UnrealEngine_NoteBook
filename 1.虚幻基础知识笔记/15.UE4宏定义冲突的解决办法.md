># error C4668: 没有将“_WIN32_WINNT_WIN10_TH2”定义为预处理器宏，用“0”替换“#if/#elif”

一般为Windows中的宏和UE4冲突所致，需要用如下头文件包裹冲突的头文件：
```C++
#include "Windows/AllowWindowsPlatformTypes.h"
#include "Windows/PreWindowsApi.h"

#include "冲突的头文件"

#include "Windows/PostWindowsApi.h"
#include "Windows/HideWindowsPlatformTypes.h"

```