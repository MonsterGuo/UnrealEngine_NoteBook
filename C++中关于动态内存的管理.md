```ad-note
title:几种基础的变量的生存周期
#### 先是三种基础对象的生存周期 

全局变量：在程序启动时分配，在程序结束时销毁

局部自动对象：在进入定义所在程序块时分配，离开块时销毁

static对象：在第一次使用时分配，在程序结束时销毁。

动态对象：C++支持动态内存分配。它的生存周期与在哪里创建是无关的，只有被主动释放时，才会销毁。
```
## C++为什么会定义两个智能指针
正是因为以上动态对象的这种特性，C++的标准库为我们提供以上两种智能指针来管理动态对象。当一个对象应该被释放时，指向它的智能指针能保证它被正确的释放。

##  动态内存内存的管理通过 new （创建）和delete（销毁）来管理。

## 带来的后果：
当忘记释放内存时，会导致内存泄漏。
当有指针引用内存的情况下，而却释放了它，这种情况下就会产生“引用非法指针”。

# 带来智能指针原由
智能指针与常规指针的区别，智能指针能负责自动释放所指的对象。
shared_ptr ： 允许多个指针指向同一个对象
unique_ptr ：这个指针独占这个对象

```C++ 
// 共享指针与独占指针.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <memory>
using namespace std;

class MyTest
{
public:
    MyTest(string name, int age) {
        _name = name;
        _age = age;
    };
    ~MyTest() = default;
    void sayHello() {
        cout << "Hello " << _name << "! You are " << _age << " years old." << endl;
    };

public:
    string _name;
    int _age;
};

void test_unique_ptr()
{
    //独占对象
    //保证指针所指对象生命周期与其一致
    unique_ptr<MyTest> unique_ptr_01(new MyTest("tom", 20));
    unique_ptr_01->sayHello();

    //不允许直接做右值
    //unique_ptr<int> unique_ptr_02 = unique_ptr_01;

    //需要通过move来处理
    unique_ptr<MyTest> unique_ptr_03 = move(unique_ptr_01);
    if (!unique_ptr_01)cout << "unique_ptr_01 is empty" << endl;
    unique_ptr_03->sayHello();

    //释放指针
    unique_ptr_03.reset();
    if (!unique_ptr_03)cout << "unique_ptr_03 is empty" << endl;
    cout << "***********************************" << endl;
}

void test_shared_ptr()
{
    shared_ptr<MyTest> shared_ptr_01(make_shared<MyTest>("tom", 20)); //这两个虽然是指向同一个对象
    shared_ptr<MyTest> shared_ptr_02 = shared_ptr_01;
    shared_ptr<MyTest> shared_ptr_03 = shared_ptr_01;
    shared_ptr_01->sayHello();
    shared_ptr_02->sayHello();
    cout << "shared_ptr_01:" << shared_ptr_01.use_count() << "***********" << endl;
    cout << "shared_ptr_02:" << shared_ptr_02.use_count() << "***********" << endl;
    cout << "shared_ptr_03:" << shared_ptr_03.use_count() << "***********" << endl;
    //这个就是相当于将自己的共享指针指向一个空的。
    shared_ptr_01.reset();
    cout << "shared_ptr_01:" << shared_ptr_01.use_count() << "***********" << endl;
    cout << "shared_ptr_02:" << shared_ptr_02.use_count() << "***********" << endl;
    cout << "shared_ptr_03:" << shared_ptr_03.use_count() << "***********" << endl;
    if (!shared_ptr_01)cout << "shared_ptr_01 is empty" << endl;
    shared_ptr_02->sayHello();

    shared_ptr_02.reset();
    if (!shared_ptr_02)cout << "shared_ptr_02 is empty" << endl;
    cout << "shared_ptr_01:" << shared_ptr_01.use_count() << "***********" << endl;
    cout << "shared_ptr_02:" << shared_ptr_02.use_count() << "***********" << endl;
    cout << "***********************************" << endl;
}

void test_weak_ptr()
{
    shared_ptr<MyTest> shared_ptr_01(make_shared<MyTest>("tom", 20));
    weak_ptr<MyTest> weak_ptr_01 = shared_ptr_01;
    shared_ptr_01->sayHello();
    weak_ptr_01.lock()->sayHello();

    weak_ptr_01.reset();
    if (!weak_ptr_01.lock())cout << "weak_ptr_01 is empty" << endl;
    shared_ptr_01->sayHello();

    weak_ptr<MyTest> weak_ptr_02 = shared_ptr_01;
    weak_ptr<MyTest> weak_ptr_03 = weak_ptr_02;
    if (weak_ptr_01.lock())weak_ptr_02.lock()->sayHello();
    shared_ptr_01.reset();
    if (!weak_ptr_01.lock())cout << "weak_ptr_02 is empty" << endl;
}

int main()
{
    test_unique_ptr();
    test_shared_ptr();
    test_weak_ptr();

    return 0;
}
```


智能指针能更方便的管理所创建的动态内存对象，它的计数器为0时代表了没有引用，所指向的对象就会释放。

## 直接的内存管理（对于非动态类型，他们的内存有较为完善的编译与释放原则，所以不需要特殊的人为干涉）
```C++
//使用new一个对象
int *pi = new int;  //pi 指向的是一个动态分配，未初始化的无名对象。
string *ps = new string; //初始化为空string

```

```C++
#include <iostream>
#include <string>
#include <memory>
using namespace std;

int main()
{
    int i;
    i = 10;
    int* p = new int();
    int* p1 = new int(1024);
    string* ps = new string(10, '9');
    auto p2 = new auto(i);  //并且会用i来初始化对象
    cout <<"p:" << *p << endl;
    cout <<"p1:" << *p1 << endl;
    cout <<"p2:" << *p2 << endl;
    cout <<"i:" << i << endl;  
    cout << *ps << endl;
    std::cout << "Hello World!\n";
}

```
