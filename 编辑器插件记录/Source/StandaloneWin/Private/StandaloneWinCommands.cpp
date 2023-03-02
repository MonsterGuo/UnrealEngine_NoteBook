// Copyright Epic Games, Inc. All Rights Reserved.

#include "StandaloneWinCommands.h"

#define LOCTEXT_NAMESPACE "FStandaloneWinModule"

void FStandaloneWinCommands::RegisterCommands()
{
	//注册命令（现在是拿到UI的共享指针，“名称”，“描述”，按键类型，“按键是否注册快捷键调用”（这里使用的是默认的））
	UI_COMMAND(OpenPluginWindow, "StandaloneWin", "Bring up StandaloneWin window", EUserInterfaceActionType::Button, FInputChord());
}

#undef LOCTEXT_NAMESPACE
