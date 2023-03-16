```C++
/**自增操作*/
int32 n1=100;
int32 r1= FPlatformAtomics::InterlockedIncrement(&n1);  //n1=101 r1=101

/**自减操作*/
int32 n2 = 110;
int32 r2 = FPlatformAtomics::InterlockedDecrement(&n2); //n2 = 109 r2=109

// Fetch（获取） and Add操作
int32 n3 = 120;
//r3=n3 ; n3 = n3+5;
int32 r3 = FPlatformAtomics::InterlockedAdd(&n3,5);  //r3=120 n3=125

// 数值swap操作
int32 n4 =120;
// r4=n4; n4 =8;
int32 r4 = FPlatformAtomics::InterlockedExchange(&4,8); // r4=120 n4 =8

// 指针swap操作
int32 n51 = 140;
int32 n52 = 141;
int32* pn51 = &n51;
int32* pn52 = &n52;
// r5=pn51; pn51= pn52;
void* r5 = FPlatformAtomics::InterlockedExchangePtr((void**)&pn51,pn52);


//数值Compare And Swap
int32 n61 = 150;
int32 n62 = 151;
int32 n63 = 150;
// z6=n61; if(n61==n63) (n61=n62;)
int32 r6 = FPlatformAtomics::interlockedCompareExchange(&n61,n62,n63); //r6=150  n61=151  n62=151

int32 n71=160;
int32 n72=161;
int32 n73=60;
// r7=n71;if(n71==n73) (n71=n72)
int32 r7 = FPlatformAtomics::InterlockedCompareExchange(&n71,n72,n73); //r7=160  n71=160  n72=161

//数值与运算
int32 n81 = 8;
int32 n82 = 12;
int32 r8 = FPlatformAtomics::InterlockedAnd(&n81, n82);  //r8=8  n81=1000&1100=1000=8   n82=12

// 数值或运算
int32 n91 = 9;
int32 n92 = 12;
int32 r9 = FPlatformAtomics::InterlockedOr(&n91, n92);  //r9=9  n91=1001|1100=1101=13   n92=12

// 数值异或运算
int32 na1 = 9;
int32 na2 = 12;
int32 ra = FPlatformAtomics::InterlockedXor(&na1, na2);  // ra=9   na1=1001^1100=0101=5   na2=12
```

## FCriticalSection（用户模式下的临界区段）

> 当有线程进入临界区段时，其他线程必须等待。基于`原子操作`Interlocked函数实现。
优点：效率高（不需要昂贵的`用户态`切换到`内核态`的上下文切换）
缺点：不能用于进程间同步，只能用于进程内各线程间同步

| 平台                    | 实现类                                             |
| ----------------------- | -------------------------------------------------- |
| windows                 | typedef FWindowsCriticalSection FCriticalSection;  |
| Mac，Unix，Android，IOS | typedef FPThreadsCriticalSection FCriticalSection; |
| HoloLens                | typedef FHoloLensCriticalSection FCriticalSection; |
|                         |                                                    |

## FSystemWideCriticalSection（系统范围的临界区段）
> 当有线程进入临界区段时，其他线程必须等待。基于内核对象`Mutex（互斥体）`实现。
优点：可用于系统范围内`进程间同步`，也可以用于`进程内各线程间同步`
缺点：效率低（有昂贵的`用户态`切换到`内核态`的上下文切换）

| **平台**             | **实现类**                                                                           |
| -------------------- | ------------------------------------------------------------------------------------ |
| Windows              | typedef FWindowsSystemWideCriticalSection FSystemWideCriticalSection;                |
| Unix                 | typedef FUnixSystemWideCriticalSection FSystemWideCriticalSection;                   |
| Mac                  | typedef FMacSystemWideCriticalSection FSystemWideCriticalSection;                    |
| Android,IOS,HoloLens | // 未实现 typedef FSystemWideCriticalSectionNotImplemented FSystemWideCriticalSetion |


## FRWLock（读写锁）
由于读线程并不会破坏数据，因此读写锁将对锁操作的线程分成：`读线程和写线程`。以提高并发效率。
读线程以`共享模式（share）`来获取和释放锁，写线程以`独占模式（exclusive）`来获取和释放锁。
当没有写线程时，各个`读线程可并发运行`。`写线程与写线程是互斥的`；`写线程与读线程也是互斥的`。

| **平台**               | **实现类**                       |
| ---------------------- | -------------------------------- |
| Windows                | typedef FWindowsRWLock FRWLock;  |
| Mac/Unix/ Android/ IOS | typedef FPThreadsRWLock FRWLock; |
| HoloLens               | typedef FHoloLensRWLock FRWLock; |

## FEvent（事件对象）
基于操作系统内核对象实现。
ue4中通过`FEvent* FPlatformProcess::CreateSynchEvent(bool bIsManualReset)`来创建；
或者调用`FEvent* FPlatformProcess::GetSynchEventFromPool(bool bIsManualReset)`从缓存池里面获取一个。
注：bIsManualReset为`TRUE`表示为手动重置事件；为`FALSE`表示为自动重置事件。
操作系统将所有等待该Event线程切换到就绪后，会自动调用Reset将Event设置成未触发状态。因此，开发者自己不需要显示地调用Reset。
执行`Trigger函数`，可将Event设置成`触发状态`；执行`Reset函数`，可将Event设置成`未触发状态`。
调用`Wait函数`来`等待一个Event`。注：Event处于未触发状态时，会阻塞等待。


| **平台**             | **实现类**                     |
| -------------------- | ------------------------------ |
| Windows              | FEventWin : public FEvent      |
| Mac/Unix/Android/IOS | FPThreadEvent : public FEvent  |
| Hololens             | FEventHoloLens : public FEvent |

## FSemaphore（信号量）
仅在windows平台上实现，详见：FWindowsSemaphore
建议使用FEvent来替代

## 线程安全（Threadsafe）的容器
包括`TArray,、TMap、TSet`在内的容器都`不是线程安全的`，需要自己对同步进行管理。
| **类型**                                            | **解释说明**                                                                                                                                                                               |
| --------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| TArrayWithThreadsafeAdd                             | 从TArray上派生                                                                                                                                                                             |
|                                                     | 提供了AddThreadsafe函数来线程安全地往数组中添加元素                                                                                                                                        |
|                                                     | 注1：不会引发扩容时，AddThreadsafe才线程安全                                                                                                                                               |
|                                                     | 注2：其他的操作（Add、Remove、Empty等）都不是线程安全的                                                                                                                                    |
| TLockFreePointerListFIFO                            | 无锁队列（lock free queue），带内存空隙（pad），先进先出（FIFO）                                                                                                                           |
|                                                     | 基类FLockFreePointerFIFOBase                                                                                                                                                               |
|                                                     | [[#示例代码1]]                                                                                                                                                                             |
| TLockFreePointerListUnordered                       | 无锁栈（lock free stack），带内存空隙（pad），后进先出（LIFO）                                                                                                                             |
|                                                     | 基类FLockFreePointerListLIFOBase                                                                                                                                                           |
|                                                     | [[#示例代码2]]                                                                                                                                                                             |
| TLockFreePointerListLIFOPad                         | 无锁栈（lock free stack），带内存空隙（pad），后进先出（LIFO）                                                                                                                             |
|                                                     | 基类FLockFreePointerListLIFOBase                                                                                                                                                           |
| TClosableLockFreePointerListUnorderedSingleConsumer | 带close状态的无锁栈（lock free stack），后进先出（LIFO）·                                                                                                                                  |
|                                                     | 基类FLockFreePointerListLIFOBase                                                                                                                                                           |
|                                                     | 在TaskGraph的FGraphEvent类中使用该栈记录依赖该Event的所有FBaseGraphTask对象                                                                                                                |
| TLockFreePointerListLIFO                            | 内存空隙为0的无锁栈，后进先出（LIFO）                                                                                                                                                      |
|                                                     | 等价于TLockFreePointerListUnordered<T,TPaddingForCacheContention=0>                                                                                                                        |
|                                                     |                                                                                                                                                                                            |
| FStallingTaskQueue                                  | 无锁任务队列                                                                                                                                                                               |
|                                                     | 线程在while循环里不断的从队列里取任务然后执行，如果队列是空的，就会空跑while循环。虽然循环没有多少逻辑，也是会耗费系统资源的                                                               |
|                                                     | FStallingTaskQueue就是用来作此优化的类，stalling就是搁置线程的意思。另外它包含两个FLockFreePointerFIFOBase无锁队列，作为高优先级和低优先级队列                                             |
|                                                     | 虽然真正让线程Wait等待和Trigger唤醒的地方并不是在这个类里实现的，但它维护了各个线程的搁置状态                                                                                              |
|                                                     | 这些状态记录在一个TDoublePtr MasterState里，还是这个64位指针，不过这次它的低26位不是指针了，而是表示26个线程的搁置状态，1表示被搁置，可以被唤醒高于26位的部分仍然作为标记计数，防止ABA问题 |
| TQueue                                              | 基于链表（linked list）实现的不能插队（non-intrusive）的无锁队列（lock free queue），先进先出（FIFO）                                                                                      |
|                                                     | 其中Spsc模式是无竞争（contention free）的。                                                                                                                                                |
|                                                     | 有两种模式（EQueueMode）：Mpsc（多生产者单消费者）和Spsc（单生产者单消费者）。                                                                                                             |
| TCircularQueue                                      | 基于数组（TArray）实现的循环无锁队列，先进先出（FIFO）在仅有一个生产者和一个消费者时，线程安全                                                                                                                                     |
|                                                     |                                                                                                                                                                                            |
### TQueue
从Head处入队（Enqueue），从Tail处出队（Dequeue）。示意图如下：

	Tail                           Head
    |                               |
    V                               V
| Node C | --> | Node B | --> |  Node A | --> | nullptr |


### 示例代码1
```C++
template<class T, int TPaddingForCacheContention, uint64 TABAInc = 1> // TABAInc为解决无锁编程中ABA问题添加的参数值  
class FLockFreePointerFIFOBase  
{  
  // 内存空隙（pad），防止cpu读内存的高速缓存行（Cache Line）机制引发伪共享（False sharing）问题，导致急剧地性能下降  
  FPaddingForCacheContention<TPaddingForCacheContention> PadToAvoidContention1;  
  TDoublePtr Head; // 头指针 被pad包裹  
  FPaddingForCacheContention<TPaddingForCacheContention> PadToAvoidContention2;  
  TDoublePtr Tail; // 尾指针 被pad包裹  
  FPaddingForCacheContention<TPaddingForCacheContention> PadToAvoidContention3;  
};
```

### 示例代码2
```C++
template<class T, int TPaddingForCacheContention, uint64 TABAInc = 1> // TABAInc为解决无锁编程中ABA问题添加的参数值  
class FLockFreePointerListLIFOBase  
{  
  FLockFreePointerListLIFORoot<TPaddingForCacheContention, TABAInc> RootList;  
  {  
    // 内存空隙（pad），防止cpu读内存的高速缓存行（Cache Line）机制引发伪共享（False sharing）问题，导致急剧地性能下降  
    FPaddingForCacheContention<TPaddingForCacheContention> PadToAvoidContention1;  
    TDoublePtr Head; // 栈指针 被pad包裹  
    FPaddingForCacheContention<TPaddingForCacheContention> PadToAvoidContention2;  
  };  
};
```


# 线程安全的帮助工具
| **类型**                    | **解释说明**                                                               |
| --------------------------- | -------------------------------------------------------------------------- |
| FThreadSafeCounter          | 基于原子操作的FPlatformAtomics::Interlocked函数实现的线程安全的int32计数器 |
|                             | 如：FThreadSafeCounter OutstandingHeartbeats;                              |
| FThreadSafeCounter64        | 基于原子操作的FPlatformAtomics::Interlocked函数实现的线程安全的int64计数器 |
| FThreadSafeBool             | 从FThreadSafeCounter上派生实现的线程安全的Bool                             |
| TThreadSingleton            | 为每一个线程创建单例                                                       |
| FThreadIdleStats            | 从TThreadSingleton派生，用于计算各个线程的等待时间的统计逻辑               |
| FMemStack                   | 从TThreadSingleton派生，基于每个线程进行内存分配                           |
| TLockFreeFixedSizeAllocator | 固定大小的lockfree的内存分配器                                             |
| TLockFreeClassAllocator     | 从TLockFreeFixedSizeAllocator派生的对象内存分配器                          |
| FScopeLock                  | 基于作用域的自旋锁   [[#详解1]]                                                      |
| FScopedEvent                | 基于作用域的同步事件  [[#详解2]]                                                                         |


# 详解1
利用c++的[RAII](https://zh.wikipedia.org/wiki/RAII)（[Resource Acquisition is Initialization](https://en.wikipedia.org/wiki/Resource_acquisition_is_initialization)）特性（即：对象构造的时候其所需的资源便应该在构造函数中初始化，而对象析构的时候则释放这些资源），基于FCriticalSection实现的自旋锁（或旋转锁）。

{  
    // CritSection为一个FCriticalSection临界区段对象  
    FScopeLock ScopeLock(&CritSection); // 如果CritSection被其他线程持有，则当前线程会在此等待  
  
    // 临界段（critical section）  
  
  
    // 离开作用域，ScopeLock对象生命周期结束，会在其析构函数中释放对CritSection临界区段对象的占用  
}

# 详解2
利用c++的RAII（Resource Acquisition is Initialization）特性，基于FEvent实现的同步等待事件。

{  
    FScopedEvent MyEvent;  
    SendReferenceOrPointerToSomeOtherThread(&MyEvent); // 当其他线程中完成了任务时，调用MyEvent->Trigger()，将MyEvent变成触发态  
  
   // 离开作用域，会调用析构函数。MyEvent在析构函数中Wait任务的完成  
}

```C++
/****************************** UnrealEngine\Engine\Source\Runtime\Media\Private\MediaTicker.h ********************************/

#pragma once

#include "Containers/Array.h"
#include "HAL/CriticalSection.h"
#include "HAL/Runnable.h"
#include "Templates/Atomic.h"
#include "Templates/SharedPointer.h"

#include "IMediaTicker.h"

class FEvent;
class IMediaTickable;


/**
 * High frequency ticker thread.
 */
class FMediaTicker
    : public FRunnable
    , public IMediaTicker
{
public:

    /** Default constructor. */
    FMediaTicker();

    /** Virtual destructor. */
    virtual ~FMediaTicker();

public:

    //~ FRunnable interface

    virtual bool Init() override;
    virtual uint32 Run() override;
    virtual void Stop() override;
    virtual void Exit() override;

public:

    //~ IMediaTicker interface

    virtual void AddTickable(const TSharedRef<IMediaTickable, ESPMode::ThreadSafe>& Tickable) override;
    virtual void RemoveTickable(const TSharedRef<IMediaTickable, ESPMode::ThreadSafe>& Tickable) override;

protected:

    /** Tick all tickables. */
    void TickTickables();

private:

    /** Critical section for synchronizing access to high-frequency clock sinks. */
    FCriticalSection CriticalSection;

    /** Holds a flag indicating that the thread is stopping. */
    TAtomic<bool> Stopping;

    /** Collection of tickable objects. */
    TArray<TWeakPtr<IMediaTickable, ESPMode::ThreadSafe>> Tickables;

    /** Variable to avoid rellocating the Tickables array repeatedly. */
    TArray<TWeakPtr<IMediaTickable, ESPMode::ThreadSafe>> TickablesCopy;

    /** Holds an event signaling the thread to wake up. */
    FEvent* WakeupEvent;
};


/********************************************************************************************************************************/
/****************************** UnrealEngine\Engine\Source\Runtime\Media\Private\MediaTicker.cpp ********************************/
/********************************************************************************************************************************/
#include "HAL/Event.h"
#include "HAL/PlatformProcess.h"
#include "Misc/ScopeLock.h"

#include "IMediaTickable.h"


/* FMediaTicker structors
 *****************************************************************************/

FMediaTicker::FMediaTicker()
    : Stopping(false)
{
    WakeupEvent = FPlatformProcess::GetSynchEventFromPool(true);
}


FMediaTicker::~FMediaTicker()
{
    FPlatformProcess::ReturnSynchEventToPool(WakeupEvent);
    WakeupEvent = nullptr;
}


/* FRunnable interface
 *****************************************************************************/

bool FMediaTicker::Init()
{
    return true;
}


uint32 FMediaTicker::Run()
{
    while (!Stopping)
    {
        if (WakeupEvent->Wait() && !Stopping)
        {
            TickTickables();
            if (!Stopping)
            {
                FPlatformProcess::Sleep(0.005f);
            }
        }
    }

    return 0;
}


void FMediaTicker::Stop()
{
    Stopping = true;
    WakeupEvent->Trigger();
}


void FMediaTicker::Exit()
{
    // do nothing
}


/* IMediaTicker interface
 *****************************************************************************/

void FMediaTicker::AddTickable(const TSharedRef<IMediaTickable, ESPMode::ThreadSafe>& Tickable)
{
    FScopeLock Lock(&CriticalSection);
    Tickables.AddUnique(Tickable);
    WakeupEvent->Trigger();
}


void FMediaTicker::RemoveTickable(const TSharedRef<IMediaTickable, ESPMode::ThreadSafe>& Tickable)
{
    FScopeLock Lock(&CriticalSection);
    Tickables.Remove(Tickable);
}


/* FMediaTicker implementation
 *****************************************************************************/

void FMediaTicker::TickTickables()
{
    TickablesCopy.Reset();
    {
        FScopeLock Lock(&CriticalSection);

        for (int32 TickableIndex = Tickables.Num() - 1; TickableIndex >= 0; --TickableIndex)
        {
            TSharedPtr<IMediaTickable, ESPMode::ThreadSafe> Tickable = Tickables[TickableIndex].Pin();

            if (Tickable.IsValid())
            {
                TickablesCopy.Add(Tickable);
            }
            else
            {
                Tickables.RemoveAtSwap(TickableIndex);
            }
        }

        if (Tickables.Num() == 0)
        {
            WakeupEvent->Reset();
        }
    }

    for (int32 i=0; i < TickablesCopy.Num(); ++i)
    {
        TSharedPtr<IMediaTickable, ESPMode::ThreadSafe> Tickable = TickablesCopy[i].Pin();

        if (Tickable.IsValid())
        {
            Tickable->TickTickable();
        }
    }
}
```