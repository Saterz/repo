# v0.2.48 · 2026-10-26

## 月读 v0.2.48

KOReader 插件包：`book.koplugin-v0.2.48.zip`

输入法词库（整库，手动 sideload）：`dictionary.sqlite3 dictionary-wubi.sqlite3 dictionary-cangjie.sqlite3 dictionary-zhuyin.sqlite3`

安装：解压后将 `book.koplugin` 复制到 KOReader 的 `plugins` 目录，然后重启。

拓展书源（可选，需同时安装月读）：`moonsource-kavita.koplugin-v0.2.48.zip`（Kavita）、
`moonsource-bookorbit.koplugin-v0.2.48.zip`（BookOrbit）。解压后同样放进 `plugins` 目录。

词库 sideload：下载对应布局的词库，直接放入 KOReader 数据目录下的
`.moon/`（与 `book.sqlite3` 同级）。附件已使用最终文件名，无需重命名。

### 更新内容

相对上一版本 `v0.2.47`：

#### 新功能

- :sparkles: (update): 长按检查更新可强制重装最新包 (ccdbc876)

#### 修复

- :bug: (note): 空串 note/drawer 不再把高亮判成笔记 (b34e50ff)
- :bug: (lockscreen): 票根粗体带色不再因 Color==nil 崩溃 (bc200b1f)

#### 变更

- :white_check_mark: (lockscreen): 补强 Color 判空回归覆盖统计柱标签 (8bf79ed2)

### 完整对比

https://github.com/AnkioTomas/moon/compare/v0.2.47...v0.2.48

# v0.2.47 · 2026-10-26

## 月读 v0.2.47

KOReader 插件包：`book.koplugin-v0.2.47.zip`

输入法词库（整库，手动 sideload）：`dictionary.sqlite3 dictionary-wubi.sqlite3 dictionary-cangjie.sqlite3 dictionary-zhuyin.sqlite3`

安装：解压后将 `book.koplugin` 复制到 KOReader 的 `plugins` 目录，然后重启。

拓展书源（可选，需同时安装月读）：`moonsource-kavita.koplugin-v0.2.47.zip`（Kavita）、
`moonsource-bookorbit.koplugin-v0.2.47.zip`（BookOrbit）。解压后同样放进 `plugins` 目录。

词库 sideload：下载对应布局的词库，直接放入 KOReader 数据目录下的
`.moon/`（与 `book.sqlite3` 同级）。附件已使用最终文件名，无需重命名。

### 更新内容

相对上一版本 `v0.2.46`：

#### 新功能

- :sparkles: (bars): 阅读页顶栏底栏组件支持居中对齐 (fa533f46)

#### 修复

- :bug: (jjwxc): App 章节整包解密失败时重试一次 (178a3b09)
- :bug: (images): 兼容 SVG 主题变量与透明填充 (5d554556)
- :bug: (tasks): keepalive 撑着时不清 pause_auto_suspend (6e674c61)
- :bug: (ui): 彩色主题文字改用透传代理画布 (0cccabdc)

#### 性能

- :zap: (reader): 保存为默认同步全书排版快照 (c97d6dc5)
- :zap: (kindle): 锁屏合成与 HTTP 写缓存移出热路径 (92d44a6b)
- :zap: (library): 书架对账少写、筛选少扫、段评 uid 去重 (e1b527a6)
- :zap: (kindle): 降低低端机休眠与绘制路径卡顿 (554a1f1a)

### 完整对比

https://github.com/AnkioTomas/moon/compare/v0.2.46...v0.2.47

# v0.2.46 · 2026-10-26

## 月读 v0.2.46

KOReader 插件包：`book.koplugin-v0.2.46.zip`

输入法词库（整库，手动 sideload）：`dictionary.sqlite3 dictionary-wubi.sqlite3 dictionary-cangjie.sqlite3 dictionary-zhuyin.sqlite3`

安装：解压后将 `book.koplugin` 复制到 KOReader 的 `plugins` 目录，然后重启。

拓展书源（可选，需同时安装月读）：`moonsource-kavita.koplugin-v0.2.46.zip`（Kavita）、
`moonsource-bookorbit.koplugin-v0.2.46.zip`（BookOrbit）。解压后同样放进 `plugins` 目录。

词库 sideload：下载对应布局的词库，直接放入 KOReader 数据目录下的
`.moon/`（与 `book.sqlite3` 同级）。附件已使用最终文件名，无需重命名。

### 更新内容

相对上一版本 `v0.2.45`：

#### 新功能

- :sparkles: (online): 请求携带月读版本与设备 UA (fb09b3a3)
- :sparkles: (reviews): 段评图片支持点击放大 (d6eadde7)
- :sparkles: (animation): 支持慢标准快三档翻页速度 (855c07dc)
- :sparkles: (desktop): 增加统计页显示开关 (c97d9eb7)
- :sparkles: (reader): 支持返回键关书回月读 (0be12365)
- :sparkles: (ui): 统一顶层窗口分页与关闭操作 (94132ef1)

#### 修复

- :bug: (remote): 修正网页翻译并保留用户原文 (5f86b35e)
- :bug: (ui): 修复容量查询失败并清零诊断 (76d7d06e)
- :bug: (subscribe): 重开文章时保留有效双语缓存 (9dcb9b1d)
- :bug: (subscribe): 修复已缓存文章无法离线打开 (40fb4b31)
- :bug: (metadata): 保留本地书籍资料并补齐番茄详情 (012de710)
- :bug: (progress): 修复多源阅读位置同步 (2efc910e)
- :bug: (extensions): 补齐动态回调插件入口 (4fe9f02c)
- :bug: fix(panel): 兼容 Kindle 空 Wi-Fi 网络名 (0ff81f59)
- :bug: (reviews): 在线刷新段评并移除失效标记 (c2c880c7)
- :bug: (remote): 手动开启远程管理时先连接 Wi-Fi (0da700af)
- :bug: (lockscreen): 补齐主题着色并保持灰度兼容 (26b4765e)

#### 界面

- :lipstick: (settings): 彩色显示移入外观并按需显示主题色 (6881ac7e)
- :lipstick: (ui): 支持单主题色并保留主题选中样式 (c47591ac)

#### 性能

- :zap: (subscribe): 限制并发加速文章缓存 (b1e23f93)

#### 其他

- :wrench: chore(types): 修正 LuaLS 类型契约并清零诊断 (58d68678)

#### 变更

- :white_check_mark: (tests): 修复无 KOReader 环境的发布测试 (52c495ff)

### 完整对比

https://github.com/AnkioTomas/moon/compare/v0.2.45...v0.2.46

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
