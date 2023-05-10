# 载入lib库
```C++
#pragma comment(lib, "mf")  
#pragma comment(lib, "mfplat")  
#pragma comment(lib, "mfplay")  
#pragma comment(lib, "mfuuid")  
#pragma comment(lib, "shlwapi")  
#pragma comment(lib, "d3d11")
```

我们经常用到的是#pragma comment（lib，"\*.lib"）这类的。  
#pragma comment(lib,“Ws2_32.lib”)表示链接Ws2_32.lib这个库。  和在工程设置里写上链入Ws2_32.lib的效果一样，不过这种方法写的程序别人在使用你的代码的时候就不用再设置工程settings了。


# 载入动态链接库
```C++
//载入dll  
if (LoadLibraryW(TEXT("shlwapi.dll")) == nullptr)  
{  
   UE_LOG(LogWmfMedia, Log, TEXT("Failed to load shlwapi.dll"));  
  
   return false;  
}
```