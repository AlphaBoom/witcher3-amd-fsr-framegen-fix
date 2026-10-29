The Witcher 3 AMD FSR Frame Generation Startup Fix v1.0.0
Tested: Remastered 5.01c / DX12 / RX 9060 XT.

Install: extract the ZIP into the game root containing bin and content.
Expected: The Witcher 3/mods/modFSRStartupReinit/content/scripts/game/...
Keep FSR frame generation enabled. Load a save; reinitialization runs automatically after about 2 seconds.
Uninstall: close the game and move modFSRStartupReinit out of mods.
Conflicts: game/r4game.ws and game/player/player.ws. Recheck after game updates.

安装：退出游戏，将ZIP直接解压到包含bin、content的游戏根目录。
保持FSR帧生成开启，读档后约两秒自动重新初始化，无需手动切换。
卸载：退出游戏，将modFSRStartupReinit移出mods目录。
已验证5.01c版本，游戏更新后需检查兼容性。

https://github.com/AlphaBoom/witcher3-amd-fsr-framegen-fix

Original game scripts: CD PROJEKT S.A. All rights reserved.
Original mod additions: Copyright (c) 2026 AlphaBoom, MIT; see repository LICENSE-MOD.
Unofficial community mod.
