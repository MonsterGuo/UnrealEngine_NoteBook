// Copyright Epic Games, Inc. All Rights Reserved.

#pragma once

#include "CoreMinimal.h"
// 这里导入命令的头文件
#include "Framework/Commands/Commands.h"
// 导入自己定义的类
#include "StandaloneWinStyle.h"

// 继承自TCommands模板
class FStandaloneWinCommands : public TCommands<FStandaloneWinCommands>
{
public:
	// 构造模板命令
	// 通过模板实现一个FFStandaloneWinCommands对象（名称，关联描述，父类的关联菜单，样式名字）
	FStandaloneWinCommands()
		: TCommands<FStandaloneWinCommands>(TEXT("StandaloneWin"), NSLOCTEXT("Contexts", "StandaloneWin", "StandaloneWin Plugin"), NAME_None, FStandaloneWinStyle::GetStyleSetName())
	{
	}

	// TCommands<> interface
	// 模板的实现
	virtual void RegisterCommands() override;

public:
	// 创建一个OpenPluginWindow的共享指针
	TSharedPtr< FUICommandInfo > OpenPluginWindow;
};