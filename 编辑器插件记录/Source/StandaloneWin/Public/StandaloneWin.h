// Copyright Epic Games, Inc. All Rights Reserved.

#pragma once

#include "CoreMinimal.h"
#include "Modules/ModuleManager.h"

class FToolBarBuilder;
class FMenuBuilder;

class FStandaloneWinModule : public IModuleInterface
{
public:

	/** IModuleInterface implementation */
	// 模块接口的实现；包含了启动模块和关闭模块
	virtual void StartupModule() override;
	virtual void ShutdownModule() override;
	
	/** This function will be bound to Command (by default it will bring up plugin window) */
	//这个函数将会被绑定到命令（通过它将带来插件窗口）
	void PluginButtonClicked();
	
private:
	// 注册菜单
	void RegisterMenus();
	// 这里返回了<SDockTab>的共享指针，它会自动的管理插件标签的生成
	TSharedRef<class SDockTab> OnSpawnPluginTab(const class FSpawnTabArgs& SpawnTabArgs);

private:
	// 注册一系列的UI命令列表 插件命令：
	TSharedPtr<class FUICommandList> PluginCommands;
};
