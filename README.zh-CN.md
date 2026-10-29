# 巫师 3：AMD FSR 帧生成启动失效修复

[English](README.md)

针对《巫师 3》重制版 DX12：设置显示帧生成已开启，但每次启动都需要手动关闭再开启才生效的问题。本模组在读档后自动重新初始化已开启的 FSR 帧生成。

## 下载和安装

1. 退出游戏。
2. 到 [Releases 发布页](https://github.com/AlphaBoom/witcher3-amd-fsr-framegen-fix/releases/latest)，在 **Assets** 中下载 **`witcher3-amd-fsr-framegen-fix-v1.0.0.zip`**。
3. 将 ZIP **直接解压到游戏安装根目录**，也就是包含 `bin`、`content` 的 `The Witcher 3` 文件夹。
4. 使用 **DX12** 启动游戏，在设置中保留 **AMD FSR 帧生成：开启**，读档后约两秒自动生效。

解压后应得到：

```text
The Witcher 3/
└── mods/
    └── modFSRStartupReinit/
        ├── README.txt
        └── content/scripts/game/
            ├── r4game.ws
            └── player/player.ws
```

## 已验证范围

- 游戏：重制版 **5.01c**，DX12，EXE 文件版本 `5.0.0.1090142`。
- 显卡：**AMD Radeon RX 9060 XT**，Windows。
- 修复前：冷启动约 **118–119 FPS**，手动重新切换后约 **218 FPS**。
- 安装后：两次完整退出、重新启动并直接读档，分别为 **223 FPS** 和 **222 FPS**。

帧率会随场景和硬件变化。

## 实现方式

读档完成后延迟两秒，检查 FSR 帧生成是否受支持且用户已经开启。满足条件时，调用游戏原生设置接口关闭，再隔半秒重新开启，让两次设置发生在不同帧。

通过这次自动重新初始化，绕过启动时帧生成未生效的问题。

## 兼容性

覆盖 `game/r4game.ws` 和 `game/player/player.ws`。其他模组若也修改这两个文件，需要合并冲突，例如使用 Script Merger。

发布包以 **5.01c** 游戏脚本为基础。游戏更新后应先检查兼容性，旧脚本覆盖可能与新版游戏冲突。

## 卸载

退出游戏，将 `mods/modFSRStartupReinit` 文件夹删除或移到 `mods` 目录之外。

开发者可运行 `python tools/build_release.py` 构建并验证 ZIP。版权说明见 [NOTICE.md](NOTICE.md)。
