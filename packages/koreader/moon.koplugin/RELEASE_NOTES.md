# v0.4.6 · 2026-10-30

## 月读 v0.4.6

KOReader 插件包：`book.koplugin-v0.4.6.zip`

输入法词库（整库，手动 sideload）：`dictionary.sqlite3 dictionary-wubi.sqlite3 dictionary-cangjie.sqlite3 dictionary-zhuyin.sqlite3`

安装：解压后将 `book.koplugin` 复制到 KOReader 的 `plugins` 目录，然后重启。

拓展书源（可选，需同时安装月读）：`moonsource-kavita.koplugin-v0.4.6.zip`（Kavita）、
`moonsource-bookorbit.koplugin-v0.4.6.zip`（BookOrbit）。解压后同样放进 `plugins` 目录。

词库 sideload：下载对应布局的词库，直接放入 KOReader 数据目录下的
`.moon/`（与 `book.sqlite3` 同级）。附件已使用最终文件名，无需重命名。

### 更新内容

相对上一版本 `v0.4.5`：

#### 新功能

- :sparkles: (home): 最近阅读可隐藏已读完 (02643d53)

#### 修复

- :bug: (reader): 库外文件不再登记接管，不弹「本书已读完」 (623e5952)
- :bug: (bluetooth): 关 Wi-Fi 带崩后按 wanted 自动拉起 (480b5450)
- :bug: (passcode): 横屏解锁临时竖屏，避免底行被裁 (26242322)

#### 变更

- :globe_with_meridians: (l10n): 补「✓ 隐藏已读完」英文与繁体翻译，修 CI (e3206237)
- :white_check_mark: (home): 覆盖最近阅读隐藏已读完 (21bc23dd)

### 完整对比

https://github.com/AnkioTomas/moon/compare/v0.4.5...v0.4.6

# v0.4.5 · 2026-10-29

## 月读 v0.4.5

KOReader 插件包：`book.koplugin-v0.4.5.zip`

输入法词库（整库，手动 sideload）：`dictionary.sqlite3 dictionary-wubi.sqlite3 dictionary-cangjie.sqlite3 dictionary-zhuyin.sqlite3`

安装：解压后将 `book.koplugin` 复制到 KOReader 的 `plugins` 目录，然后重启。

拓展书源（可选，需同时安装月读）：`moonsource-kavita.koplugin-v0.4.5.zip`（Kavita）、
`moonsource-bookorbit.koplugin-v0.4.5.zip`（BookOrbit）。解压后同样放进 `plugins` 目录。

词库 sideload：下载对应布局的词库，直接放入 KOReader 数据目录下的
`.moon/`（与 `book.sqlite3` 同级）。附件已使用最终文件名，无需重命名。

### 更新内容

相对上一版本 `v0.4.4`：

#### 修复

- :bug: (remote): 日志脱敏注释去掉源名，通过 feature 边界检查 (8585375f)

### 完整对比

https://github.com/AnkioTomas/moon/compare/v0.4.4...v0.4.5

# v0.4.3 · 2026-10-29

## 月读 v0.4.3

KOReader 插件包：`book.koplugin-v0.4.3.zip`

输入法词库（整库，手动 sideload）：`dictionary.sqlite3 dictionary-wubi.sqlite3 dictionary-cangjie.sqlite3 dictionary-zhuyin.sqlite3`

安装：解压后将 `book.koplugin` 复制到 KOReader 的 `plugins` 目录，然后重启。

拓展书源（可选，需同时安装月读）：`moonsource-kavita.koplugin-v0.4.3.zip`（Kavita）、
`moonsource-bookorbit.koplugin-v0.4.3.zip`（BookOrbit）。解压后同样放进 `plugins` 目录。

词库 sideload：下载对应布局的词库，直接放入 KOReader 数据目录下的
`.moon/`（与 `book.sqlite3` 同级）。附件已使用最终文件名，无需重命名。

### 更新内容

相对上一版本 `v0.4.2`：

#### 修复

- :bug: (fonts): 坏界面字体不再写进 fontmap 导致 KO 冷启动崩溃 (13b9459e)

#### 变更

- :green_heart: (fonts): fontpicker 测试适配 set 的成功返回值 (cc89afdc)

### 完整对比

https://github.com/AnkioTomas/moon/compare/v0.4.2...v0.4.3

# v0.4.2 · 2026-10-29

## 月读 v0.4.2

KOReader 插件包：`book.koplugin-v0.4.2.zip`

输入法词库（整库，手动 sideload）：`dictionary.sqlite3 dictionary-wubi.sqlite3 dictionary-cangjie.sqlite3 dictionary-zhuyin.sqlite3`

安装：解压后将 `book.koplugin` 复制到 KOReader 的 `plugins` 目录，然后重启。

拓展书源（可选，需同时安装月读）：`moonsource-kavita.koplugin-v0.4.2.zip`（Kavita）、
`moonsource-bookorbit.koplugin-v0.4.2.zip`（BookOrbit）。解压后同样放进 `plugins` 目录。

词库 sideload：下载对应布局的词库，直接放入 KOReader 数据目录下的
`.moon/`（与 `book.sqlite3` 同级）。附件已使用最终文件名，无需重命名。

### 更新内容

相对上一版本 `v0.4.1`：

#### 修复

- :bug: (xray): 有进展的全书分析不再误报失败 (#77) (07b454af)
- :bug: (insight): 显隐配置缺失时不再崩溃 (fca11c3d)
- :bug: (xray): 显式重新生成时释放已删实体的墓碑 (693216ba)
- :bug: (kavita): 卷行不全时不按「缺行=未读」聚合，退回服务端比例 (de45eb95)
- :bug: (kavita): 起始页只把云端位置当提示，合并交给 kamare (2a94d5f4)
- :bug: (kavita): 漫画进度跨设备取更靠后，书架百分比与打开位置同源 (d5234162)

#### 重构

- :recycle: (toc): 目录不做保鲜，开书与临近章末静默刷新 (0e7726a8)

### 完整对比

https://github.com/AnkioTomas/moon/compare/v0.4.1...v0.4.2

# v0.4.1 · 2026-10-29

## 月读 v0.4.1

KOReader 插件包：`book.koplugin-v0.4.1.zip`

输入法词库（整库，手动 sideload）：`dictionary.sqlite3 dictionary-wubi.sqlite3 dictionary-cangjie.sqlite3 dictionary-zhuyin.sqlite3`

安装：解压后将 `book.koplugin` 复制到 KOReader 的 `plugins` 目录，然后重启。

拓展书源（可选，需同时安装月读）：`moonsource-kavita.koplugin-v0.4.1.zip`（Kavita）、
`moonsource-bookorbit.koplugin-v0.4.1.zip`（BookOrbit）。解压后同样放进 `plugins` 目录。

词库 sideload：下载对应布局的词库，直接放入 KOReader 数据目录下的
`.moon/`（与 `book.sqlite3` 同级）。附件已使用最终文件名，无需重命名。

### 更新内容

相对上一版本 `v0.4.0`：

#### 修复

- :bug: (wechat): 脚注弹窗与页底直显互斥，恢复 epub:type (cced23c3)

#### 变更

- :globe_with_meridians: (l10n): 删除已不用的脚注文案键 (d8c7d965)
- :construction_worker: ci: push main / PR 自动跑离线测试 (66bbf7af)
- :truck: test: 散落在 tests/ 根的 spec 归位到镜像目录 (718a1456)
- :white_check_mark: test: 离线测试只依赖系统 luajit + libsqlite3 (d1f90d30)
- :fire: chore: 删掉仓库里的代码审计报告 (5dc9adc4)

### 完整对比

https://github.com/AnkioTomas/moon/compare/v0.4.0...v0.4.1
