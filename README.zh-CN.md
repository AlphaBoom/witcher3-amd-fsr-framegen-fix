# 巫师 3：AMD FSR 帧生成启动失效修复

[English](README.md)

针对《巫师 3》重制版 DX12：设置显示帧生成已开启，但每次启动都需要手动关闭再开启才生效的问题。本模组在读档后自动重新初始化已开启的 FSR 帧生成。

## 下载和安装

1. 退出游戏。
2. 到 [Releases 发布页](https://github.com/AlphaBoom/witcher3-amd-fsr-framegen-fix/releases/latest)，在 **Assets** 中下载 **`witcher3-amd-fsr-framegen-fix-v1.0.0.zip`**。请下载这个模组 ZIP；GitHub 自动生成的 `Source code` 压缩包用于开发，不是直接安装包。
3. 将 ZIP **直接解压到游戏安装根目录**，也就是包含 `bin`、`content` 的 `The Witcher 3` 文件夹。解压时不要再套一层压缩包同名目录。
4. 使用 **DX12** 启动游戏，在设置中保留 **AMD FSR 帧生成：开启**，读档后约两秒自动生效，无需再手动切换。

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

不需要安装器、Python、额外 DLL、控制台或外部按键脚本。不要解压到 `bin/x64_dx12` 或“文档”中的游戏配置目录。

## 已验证范围

- 游戏：重制版 **5.01c**，DX12，EXE 文件版本 `5.0.0.1090142`。
- 显卡：**AMD Radeon RX 9060 XT**，Windows。
- 修复前：冷启动约 **118–119 FPS**，手动重新切换后约 **218 FPS**。
- 安装后：两次完整退出、重新启动并直接读档，分别为 **223 FPS** 和 **222 FPS**，均未进入图像设置或手动切换。

其他版本、显卡尚未验证。以上是测试场景的读数，不代表固定增帧幅度。模组处理游戏原生 FSR 帧生成，不设置驱动级 AFMF。

## 实现方式

读档完成后延迟两秒，检查 FSR 帧生成是否受支持且用户已经开启。满足条件时，调用游戏原生设置接口关闭，再隔半秒重新开启，保证两次设置发生在不同帧。用户原本关闭时不会强制开启。整个过程在游戏脚本内部完成，不打开菜单、不模拟输入。

这是绕过启动初始化故障的自动重置补丁，尚未定位引擎底层的精确原因。不替换 EXE 或 DLL，不直接修改存档，也不主动保存用户设置。

## 兼容性

覆盖 `game/r4game.ws` 和 `game/player/player.ws`。其他模组若也修改这两个文件，需要合并冲突，例如使用 Script Merger。测试时的双语占位符模组未覆盖这两个文件。

发布包以 **5.01c** 游戏脚本为基础。游戏更新后应先检查兼容性，旧脚本覆盖可能与新版游戏冲突。

## 卸载

退出游戏，将 `mods/modFSRStartupReinit` 文件夹删除或移到 `mods` 目录之外。重新解压即可重新安装，无需恢复游戏二进制文件。

开发者可运行 `python tools/build_release.py` 重新构建并验证 ZIP；普通玩家只需下载并解压发布包。版权说明见 [NOTICE.md](NOTICE.md)。本项目是非官方社区模组，与 CD PROJEKT RED、AMD 无关联。
