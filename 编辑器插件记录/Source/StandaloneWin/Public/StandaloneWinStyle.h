// Copyright Epic Games, Inc. All Rights Reserved.

#pragma once

#include "CoreMinimal.h"
#include "Styling/SlateStyle.h"

/**  */
// 普通类型用来描述窗口样式，感觉这个东西有点像一个容器，主要作用就是承载函数
class FStandaloneWinStyle
{
public:

	//静态函数可以通过类型名调用 
	static void Initialize();
	//静态函数可以通过类型名调用
	static void Shutdown();

	/** reloads textures used by slate renderer */
	/** 重新载入纹理被用作slate渲染 **/
	static void ReloadTextures();

	/** @return The Slate style set for the Shooter game */
	/*** ？？？？？？***/
	static const ISlateStyle& Get();
	// 获取 样式的名称
	static FName GetStyleSetName();

private:
	// 静态的Create它返回的是一个共享指针 方便后面管理对象的实例。
	static TSharedRef< class FSlateStyleSet > Create();

private:
	// 是一个FSlateStyleset的共享指针，它指向的是样式的实例，这个是个全局的。所有的FStandaloneWinStyle就只有一个。
	static TSharedPtr< class FSlateStyleSet > StyleInstance;
};