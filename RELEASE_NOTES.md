# v1.0.0 — AMD FSR Frame Generation Startup Fix

[中文安装说明](https://github.com/AlphaBoom/witcher3-amd-fsr-framegen-fix/blob/main/README.zh-CN.md)

Download **witcher3-amd-fsr-framegen-fix-v1.0.0.zip** below and extract directly into **The Witcher 3 game root**, so it creates `mods/modFSRStartupReinit`. Close the game before installation. Use DX12 and leave AMD FSR Frame Generation enabled.

下载下方模组 ZIP，退出游戏后直接解压到包含 `bin`、`content` 的游戏根目录，即可安装。无需运行脚本或安装器；保持 FSR 帧生成开启，读档后自动生效。不要下载自动生成的 Source code 压缩包来直接安装。

- Reinitializes user-enabled FSR FG after loading: waits 2 seconds, turns FG Off, then On 0.5 seconds later.
- Respects the user's disabled setting; no simulated input or external process is required.
- Tested on Remastered **5.01c / DX12 / RX 9060 XT**. Two complete cold starts reached **223 / 222 FPS**, compared with **118–119 FPS** before the fix in the test scene.
- Other game versions and GPUs are unverified. This is a native FSR FG initialization workaround, not a driver AFMF tool.
- Overrides `game/r4game.ws` and `game/player/player.ws`; merge conflicts with other mods affecting those scripts, and recheck compatibility after game updates.
- To uninstall, close the game and move `mods/modFSRStartupReinit` out of `mods`.

SHA256SUMS.txt provides the downloadable mod ZIP checksum. Original game code retains CD PROJEKT ownership; see NOTICE.md and LICENSE-MOD in the repository.
