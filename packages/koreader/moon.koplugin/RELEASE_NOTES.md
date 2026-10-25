# v0.2.45 · 2026-10-25

## 月读 v0.2.45

KOReader 插件包：`book.koplugin-v0.2.45.zip`

输入法词库（整库，手动 sideload）：`dictionary.sqlite3 dictionary-wubi.sqlite3 dictionary-cangjie.sqlite3 dictionary-zhuyin.sqlite3`

安装：解压后将 `book.koplugin` 复制到 KOReader 的 `plugins` 目录，然后重启。

拓展书源（可选，需同时安装月读）：`moonsource-kavita.koplugin-v0.2.45.zip`（Kavita）、
`moonsource-bookorbit.koplugin-v0.2.45.zip`（BookOrbit）。解压后同样放进 `plugins` 目录。

词库 sideload：下载对应布局的词库，直接放入 KOReader 数据目录下的
`.moon/`（与 `book.sqlite3` 同级）。附件已使用最终文件名，无需重命名。

### 更新内容

相对上一版本 `v0.2.44`：

#### 新功能

- :sparkles: (panel): 新增默认隐藏的阅读书签按钮 (6bf2d399)

#### 修复

- :bug: (bars): 修复顶部状态栏遮挡书签标记 (fa129613)
- :bug: (reviews): 长段评支持点开全文分页查看 (7135ef77)

### 完整对比

https://github.com/AnkioTomas/moon/compare/v0.2.44...v0.2.45

# v0.2.44 · 2026-10-25

## 月读 v0.2.44

KOReader 插件包：`book.koplugin-v0.2.44.zip`

输入法词库（整库，手动 sideload）：`dictionary.sqlite3 dictionary-wubi.sqlite3 dictionary-cangjie.sqlite3 dictionary-zhuyin.sqlite3`

安装：解压后将 `book.koplugin` 复制到 KOReader 的 `plugins` 目录，然后重启。

拓展书源（可选，需同时安装月读）：`moonsource-kavita.koplugin-v0.2.44.zip`（Kavita）、
`moonsource-bookorbit.koplugin-v0.2.44.zip`（BookOrbit）。解压后同样放进 `plugins` 目录。

词库 sideload：下载对应布局的词库，直接放入 KOReader 数据目录下的
`.moon/`（与 `book.sqlite3` 同级）。附件已使用最终文件名，无需重命名。

### 更新内容

相对上一版本 `v0.2.43`：

#### 新功能

- :sparkles: (fontmap): 自动检测书内缺失字体并支持映射 (19ac382e)
- :sparkles: (passcode): 新增手势密码，与 PIN 互斥切换 (8eb14b85)
- :sparkles: (reflow): TXT 重新排版支持 GBK / UTF-16 转码，不再只认 UTF-8 (db6dd182)

#### 修复

- :bug: (fontmap): 增加默认关闭的字体映射开关 (9517bb03)
- :bug: (fonts): 异步修复缺失空格的微信字体 (bd70ed14)
- :bug: (ui): 状态列按文字宽度扩展，避免总内存被截断 (eabe181d)

#### 变更

- :white_check_mark: (fontmap): 补齐默认关闭开关的设置页回归 (477b2184)

### 完整对比

https://github.com/AnkioTomas/moon/compare/v0.2.43...v0.2.44

# v0.2.43 · 2026-10-25

## 月读 v0.2.43

KOReader 插件包：`book.koplugin-v0.2.43.zip`

输入法词库（整库，手动 sideload）：`dictionary.sqlite3 dictionary-wubi.sqlite3 dictionary-cangjie.sqlite3 dictionary-zhuyin.sqlite3`

安装：解压后将 `book.koplugin` 复制到 KOReader 的 `plugins` 目录，然后重启。

拓展书源（可选，需同时安装月读）：`moonsource-kavita.koplugin-v0.2.43.zip`（Kavita）、
`moonsource-bookorbit.koplugin-v0.2.43.zip`（BookOrbit）。解压后同样放进 `plugins` 目录。

词库 sideload：下载对应布局的词库，直接放入 KOReader 数据目录下的
`.moon/`（与 `book.sqlite3` 同级）。附件已使用最终文件名，无需重命名。

### 更新内容

相对上一版本 `v0.2.42`：

#### 修复

- :bug: (jjwxc): VIP 章节段评带上当前协议的登录态，修复 1004 登入验证失败 (43b2181d)
- :bug: (bluetooth): Kobo 已配对设备不再误报「无法控制系统蓝牙」，并记录命令日志 (e3965aa6)
- :bug: (bars): 底栏章节序号只显示图标，目录长度取自未定义变量 (4230cf00)

### 完整对比

https://github.com/AnkioTomas/moon/compare/v0.2.42...v0.2.43

# v0.2.42 · 2026-10-25

## 月读 v0.2.42

KOReader 插件包：`book.koplugin-v0.2.42.zip`

输入法词库（整库，手动 sideload）：`dictionary.sqlite3 dictionary-wubi.sqlite3 dictionary-cangjie.sqlite3 dictionary-zhuyin.sqlite3`

安装：解压后将 `book.koplugin` 复制到 KOReader 的 `plugins` 目录，然后重启。

拓展书源（可选，需同时安装月读）：`moonsource-kavita.koplugin-v0.2.42.zip`（Kavita）、
`moonsource-bookorbit.koplugin-v0.2.42.zip`（BookOrbit）。解压后同样放进 `plugins` 目录。

词库 sideload：下载对应布局的词库，直接放入 KOReader 数据目录下的
`.moon/`（与 `book.sqlite3` 同级）。附件已使用最终文件名，无需重命名。

### 更新内容

相对上一版本 `v0.2.41`：

#### 修复

- :bug: (insight): 当日阅读段落只显示最早 3 段，改为显示最近 3 段 (8bfb4442)

### 完整对比

https://github.com/AnkioTomas/moon/compare/v0.2.41...v0.2.42

# v0.2.41 · 2026-10-25

## 月读 v0.2.41

KOReader 插件包：`book.koplugin-v0.2.41.zip`

输入法词库（整库，手动 sideload）：`dictionary.sqlite3 dictionary-wubi.sqlite3 dictionary-cangjie.sqlite3 dictionary-zhuyin.sqlite3`

安装：解压后将 `book.koplugin` 复制到 KOReader 的 `plugins` 目录，然后重启。

拓展书源（可选，需同时安装月读）：`moonsource-kavita.koplugin-v0.2.41.zip`（Kavita）、
`moonsource-bookorbit.koplugin-v0.2.41.zip`（BookOrbit）。解压后同样放进 `plugins` 目录。

词库 sideload：下载对应布局的词库，直接放入 KOReader 数据目录下的
`.moon/`（与 `book.sqlite3` 同级）。附件已使用最终文件名，无需重命名。

### 更新内容

相对上一版本 `v0.2.40`：

#### 新功能

- :sparkles: feat(panel): 退出 / 重启 KOReader 先弹提示再执行 (9028ac73)

#### 修复

- :bug: (jjwxc): 已购 VIP 章报「响应无效」，登录协议拆成网页 / App 两套二选一 (84ca140a)

#### 变更

- :globe_with_meridians: (l10n): 晋江登录协议相关文案 (5f83e41a)

### 完整对比

https://github.com/AnkioTomas/moon/compare/v0.2.40...v0.2.41
