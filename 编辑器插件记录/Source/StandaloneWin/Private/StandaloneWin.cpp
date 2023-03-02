// Copyright Epic Games, Inc. All Rights Reserved.

#include "StandaloneWin.h"
#include "StandaloneWinStyle.h"
#include "StandaloneWinCommands.h"
#include "LevelEditor.h"
#include "Widgets/Docking/SDockTab.h"
#include "Widgets/Layout/SBox.h"
#include "Widgets/Text/STextBlock.h"
#include "ToolMenus.h"
#include "Components/SizeBox.h"

//声明一个全局的标签名
static const FName StandaloneWinTabName("StandaloneWin");

//现在开始重新读这一段的代码 
// （1）定义一段命名空间：它的用途是防止别的模块有相同的模块名
#define LOCTEXT_NAMESPACE "FStandaloneWinModule"

// （2）启动模块
void FStandaloneWinModule::StartupModule()
{
	// 这个将会执行，在模块被载入内存的时候，这个事件在.uplugin文件中指定
	// This code will execute after your module is loaded into memory; the exact timing is specified in the .uplugin file per-module

	// （1）初始化
	FStandaloneWinStyle::Initialize();
	// （2）重新载入纹理
	FStandaloneWinStyle::ReloadTextures();
	// （3）独立窗口的注册工作（注册）  这个之前不理解
	FStandaloneWinCommands::Register();

	// 注册UI的命令
	PluginCommands = MakeShareable(new FUICommandList);

	// 插件命令-> 映射操作（OpenPluginWindow的指针，和操作绑定PluginButtonClicked，校验是否绑定成功（bool值））
	PluginCommands->MapAction(
		FStandaloneWinCommands::Get().OpenPluginWindow,
		FExecuteAction::CreateRaw(this, &FStandaloneWinModule::PluginButtonClicked),
		FCanExecuteAction());

	// 工具菜单上注册操作
	// 工具菜单:: 注册启动回调（注册菜单）
	UToolMenus::RegisterStartupCallback(FSimpleMulticastDelegate::FDelegate::CreateRaw(this, &FStandaloneWinModule::RegisterMenus));
	// 这是个运行时态的
	// 全局的Tab管理 ——> 注册通用的标签生成器（独立窗口的名称，生成Tab::创建委托（生成插件的Tab））
	FGlobalTabmanager::Get()->RegisterNomadTabSpawner(StandaloneWinTabName, FOnSpawnTab::CreateRaw(this, &FStandaloneWinModule::OnSpawnPluginTab))
		.SetDisplayName(LOCTEXT("FStandaloneWinTabTitle", "StandaloneWin"))  //设置默认的名字
		.SetMenuType(ETabSpawnerMenuType::Hidden);  //默认是隐藏的
}

// 注销模块::结束模块
void FStandaloneWinModule::ShutdownModule()
{
	// This function may be called during shutdown to clean up your module.  For modules that support dynamic reloading,
	// we call this function before unloading the module.
	// 注销菜单
	UToolMenus::UnRegisterStartupCallback(this);
	// 注销自己
	UToolMenus::UnregisterOwner(this);
	// 样式注销
	FStandaloneWinStyle::Shutdown();
	// UI命令注销
	FStandaloneWinCommands::Unregister();
	// 注销tab生成器
	FGlobalTabmanager::Get()->UnregisterNomadTabSpawner(StandaloneWinTabName);
}

// 启动生成插件的标签，它返回的是共享引用（这点需要注意）
TSharedRef<SDockTab> FStandaloneWinModule::OnSpawnPluginTab(const FSpawnTabArgs& SpawnTabArgs)
{
	// 设置部件的文本
	FText WidgetText = FText::Format(
		LOCTEXT("WindowWidgetText", "Add code to {0} in {1} to override this window's contents"),
		FText::FromString(TEXT("FStandaloneWinModule::OnSpawnPluginTab")),
		FText::FromString(TEXT("StandaloneWin.cpp"))
		);
	// 创建DockTab
	return SNew(SDockTab)
		.TabRole(ETabRole::NomadTab)
		[
			SNew(SBox)
			.HAlign(HAlign_Center)
			.VAlign(VAlign_Center)
			[
				SNew(STextBlock)
				.Text(WidgetText)
				.AutoWrapText(true)
			]
		];
}

// 点击插件的时候
void FStandaloneWinModule::PluginButtonClicked()
{
	// 尝试拿到Dock的共享指针
	TSharedPtr<SDockTab> MyDock=FGlobalTabmanager::Get()->TryInvokeTab(StandaloneWinTabName);
	// 从共享指针拿到父类的窗口，然后重新刷新尺寸
	MyDock->GetParentWindow()->Resize(FVector2D(500,800));
	
}

void FStandaloneWinModule::RegisterMenus()
{
	// Owner will be used for cleanup in call to UToolMenus::UnregisterOwner
	// Owner将用于在调用UToolMenus::UnregisterOwner时进行清理
	FToolMenuOwnerScoped OwnerScoped(this);

	{
		// 拿到了菜单指针
		UToolMenu* Menu = UToolMenus::Get()->ExtendMenu("LevelEditor.MainMenu.Window");
		{
			FToolMenuSection& Section = Menu->FindOrAddSection("WindowLayout");
			Section.AddMenuEntryWithCommandList(FStandaloneWinCommands::Get().OpenPluginWindow, PluginCommands);
		}
	}
	
	{
		UToolMenu* ToolbarMenu = UToolMenus::Get()->ExtendMenu("LevelEditor.LevelEditorToolBar");
		{
			FToolMenuSection& Section = ToolbarMenu->FindOrAddSection("Settings2");
			//ToolbarMenu.section
			//FToolMenuSection& Section = ToolbarMenu->AddSection("Monster");
			{
				FToolMenuEntry& Entry = Section.AddEntry(FToolMenuEntry::InitToolBarButton(FStandaloneWinCommands::Get().OpenPluginWindow));
				Entry.SetCommandList(PluginCommands);
			}
		}
	}
}

#undef LOCTEXT_NAMESPACE
	
IMPLEMENT_MODULE(FStandaloneWinModule, StandaloneWin)