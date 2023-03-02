// Copyright Epic Games, Inc. All Rights Reserved.

#include "StandaloneWinStyle.h"
#include "Styling/SlateStyleRegistry.h"
#include "Framework/Application/SlateApplication.h"
#include "Slate/SlateGameResources.h"
#include "Interfaces/IPluginManager.h"
#include "Styling/SlateStyleMacros.h"

#define RootToContentDir Style->RootToContentDir

// （1） 先将样式它指向一个空指针
TSharedPtr<FSlateStyleSet> FStandaloneWinStyle::StyleInstance = nullptr;
// （2） 初始化函数
void FStandaloneWinStyle::Initialize()
{
	//如果这个样式的实例是空的，通过它来创建一个对象
	if (!StyleInstance.IsValid())
	{
		// 船舰样式的实例
		StyleInstance = Create();
		// 注册样式实例
		FSlateStyleRegistry::RegisterSlateStyle(*StyleInstance);
	}
}

// 结束样式
void FStandaloneWinStyle::Shutdown()
{
	// 注销Slate样式
	FSlateStyleRegistry::UnRegisterSlateStyle(*StyleInstance);
	// 再次确认 共享指针指向的对象是不是清理完成
	ensure(StyleInstance.IsUnique());
	// 将共享指针 指向空nullptr
	StyleInstance.Reset();
}

// 获取样式的名字，这个没啥好说的，这个是唯一的。
FName FStandaloneWinStyle::GetStyleSetName()
{
	static FName StyleSetName(TEXT("StandaloneWinStyle"));
	return StyleSetName;
}

// 定义两个 常量主要是用来指定图标的大小
const FVector2D Icon16x16(16.0f, 16.0f);
const FVector2D Icon20x20(20.0f, 20.0f);

TSharedRef< FSlateStyleSet > FStandaloneWinStyle::Create()
{
	// 创建一个slate样式的关联容器，（样式对象）
	TSharedRef< FSlateStyleSet > Style = MakeShareable(new FSlateStyleSet("StandaloneWinStyle"));
	// 设置样式的 图片资产的根目录
	Style->SetContentRoot(IPluginManager::Get().FindPlugin("StandaloneWin")->GetBaseDir() / TEXT("Resources"));
	// 设置样式图标（比如：StandaloneWin.OpenPluginWindow 用的就是 后面指定的图标）
	Style->Set("StandaloneWin.OpenPluginWindow", new IMAGE_BRUSH_SVG(TEXT("PlaceholderButtonIcon"), Icon20x20));

	// 返回样式的共享指针
	return Style;
}

// 重新载入纹理
void FStandaloneWinStyle::ReloadTextures()
{
	// 尝试初始化slate；
	if (FSlateApplication::IsInitialized())
	{
		//使用slate应用获取到渲染器，让它重新载入图片。
		FSlateApplication::Get().GetRenderer()->ReloadTextureResources();
	}
}

// 通过get函数能获取到实例，基础的接口部分函数。（控制了可调用的范围）
const ISlateStyle& FStandaloneWinStyle::Get()
{
	return *StyleInstance;
}
