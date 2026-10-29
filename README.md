# The Witcher 3 — AMD FSR Frame Generation Startup Fix

[中文说明](README.zh-CN.md)

A local script mod for **The Witcher 3: Wild Hunt — Remastered (DX12)** that automatically reinitializes user-enabled AMD FSR Frame Generation after loading a save. It addresses the symptom where the setting shows **On**, but frame generation only starts working after manually turning it Off and On.

## Download and install

1. Close the game.
2. Open [Releases](https://github.com/AlphaBoom/witcher3-amd-fsr-framegen-fix/releases/latest) and download **`witcher3-amd-fsr-framegen-fix-v1.0.0.zip`** under **Assets**. GitHub's automatic “Source code” archives are for development; use the named mod ZIP for installation.
3. Extract the ZIP **directly into the game installation root** — the folder containing `bin`, `content`, and `mods` (create `mods` if absent).
4. Launch the game in **DirectX 12**, keep **AMD FSR Frame Generation enabled**, and load a save. The fix runs automatically about two seconds after loading completes.

Example Steam game root:

```text
D:\Program Files (x86)\Steam\steamapps\common\The Witcher 3\
```

After extraction, these paths must exist:

```text
The Witcher 3/
└── mods/
    └── modFSRStartupReinit/
        ├── README.txt
        └── content/scripts/game/
            ├── r4game.ws
            └── player/player.ws
```

No installer, Python, DLL loader, console command, or external automation is required to use the mod. Do not extract into `bin/x64_dx12`, Documents, or an extra ZIP-named subfolder.

## Compatibility and verification

**Tested:** Remastered **5.01c**, DX12 executable `5.0.0.1090142`, Windows, AMD Radeon **RX 9060 XT**. Other builds and GPUs are unverified. This is a fix for the game's native FSR frame generation; it does not configure driver-level AMD Fluid Motion Frames (AFMF).

Observed FPS at the test save:

| State | FPS |
|---|---:|
| Before the fix: cold start, saved setting On | 118–119 |
| Before the fix: after manual Off → On | 218 |
| With the mod: first full cold start and direct load | 223 |
| With the mod: second full cold start and direct load | 222 |

Both mod tests used a fresh game process and loaded directly without entering graphics settings or manually toggling frame generation. FPS depends on the scene and hardware; these results demonstrate activation, not a universal performance uplift.

## How it works

After `OnAfterLoadingScreenGameStart`, a two-second player timer checks whether FSR frame generation is supported and already enabled by the user. It calls the game's native graphics setting interface to turn FSR FG Off, then schedules another timer to turn it On **0.5 seconds later**, across separate frames. The user's disabled setting is respected. The hook runs after loading, rather than opening a menu or simulating input.

This is an automatic reinitialization workaround. The precise native-engine startup failure has not been identified. It does not replace DLLs or the executable, directly edit save files, or call `SaveUserSettings`.

## Other mods and game updates

This mod overrides `game/r4game.ws` and `game/player/player.ws`. Mods modifying either file require conflict resolution, for example with Script Merger. The local bilingual placeholder mod used during testing did not modify these files.

The release includes overrides based on 5.01c. After a game update, check compatibility before keeping this mod enabled; old script overrides can conflict with updated game scripts. Original game script hashes are recorded in `build-info.json`.

## Uninstall

Close the game and remove or move **`mods/modFSRStartupReinit`** out of `mods`. Reinstall by extracting the mod ZIP again. No restore of game binaries is required.

## Development

Run `python tools/build_release.py` with Python 3 to build and verify the distributable in `dist/`. This is a maintainer step only. The ZIP contains `mods/` at its root, and the builder checks script hashes and extraction paths. The `patches/` directory shows the changes relative to the tested game scripts.

See [NOTICE.md](NOTICE.md) for ownership and licensing. This is an unofficial community mod and is not affiliated with CD PROJEKT RED or AMD.
