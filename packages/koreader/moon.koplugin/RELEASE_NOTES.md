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

# v0.2.40 · 2026-10-25

## 月读 v0.2.40

KOReader 插件包：`book.koplugin-v0.2.40.zip`

输入法词库（整库，手动 sideload）：`dictionary.sqlite3 dictionary-wubi.sqlite3 dictionary-cangjie.sqlite3 dictionary-zhuyin.sqlite3`

安装：解压后将 `book.koplugin` 复制到 KOReader 的 `plugins` 目录，然后重启。

拓展书源（可选，需同时安装月读）：`moonsource-kavita.koplugin-v0.2.40.zip`（Kavita）、
`moonsource-bookorbit.koplugin-v0.2.40.zip`（BookOrbit）。解压后同样放进 `plugins` 目录。

词库 sideload：下载对应布局的词库，直接放入 KOReader 数据目录下的
`.moon/`（与 `book.sqlite3` 同级）。附件已使用最终文件名，无需重命名。

### 更新内容

相对上一版本 `v0.2.39`：

#### 新功能

- :sparkles: feat(subscribe): 远程管理支持从在线订阅源批量选择订阅 (1cda779e)
- :sparkles: feat(remote): 远程管理支持清除全部配置，文件浏览器新增预览视图 (e7a3724c)
- :sparkles: feat(subscribe): 超过 180 天的文章自动淘汰，并清理已淘汰文章的缓存与图片（收藏保留） (623ad4fc)
- :sparkles: feat(subscribe): 收藏星标改实心字符，订阅页筛选条件重启后保留 (82c97d04)
- :sparkles: feat(subscribe): 文章行右侧加星标按钮收藏，去掉长按 (ca001932)
- :sparkles: feat(subscribe): 订阅页顶栏加全部已读（按当前来源/分组） (ca49fa12)
- :sparkles: feat(monitor): 运行状态显示 KOReader 内存构成与 Lua 堆按模块估算 (d74cacdf)

#### 修复

- :bug: (jjwxc): 账号密码登录读 VIP 章节报 2016 浏览器标识异常，正文请求改用 App UA (750d8add)
- :bug: (reader): 反转翻页、划线样式、文本语言、词典偏好等每本书设置跨章保留 (7a1b913e)
- :bug: fix(subscribe): 范围书章节里的图片路径指回订阅目录 (5434e8df)
- :bug: fix(subscribe): 按图片内容识别 AVIF/HEIC 并转 JPEG，不再依赖地址后缀 (f76c9edd)
- :bug: fix(subscribe): 阅读中切章不再重排章号，章节文件每次按现行目录重渲 (439f56c1)
- :bug: fix(reader): 重新下载本章同时作废订阅文章缓存 (98d89e73)
- :bug: fix(subscribe): 本地化图片去掉 srcset，含 AVIF 链接的旧缓存联网重做 (b22c5bf9)
- :bug: fix(subscribe): AVIF 图片经 wsrv.nl 转 JPEG 后落地 (08975a2f)
- :bug: (xray): 本章 / 全书分析每段缩到 12000 字节，超长无换行段落在句末断开 (a8d50b79)
- Revert ":bug: fix(subscribe): 超大图换成原图链接，残缺的文章缓存联网时重做" (af4b2ed6)
- :bug: fix(subscribe): 超大图换成原图链接，残缺的文章缓存联网时重做 (1eca54dd)
- :bug: fix(subscribe): 放宽文章图片大小上限到 8MB，爱范儿大 GIF 不再丢图 (5e104ab7)
- :bug: (wechat): 跨章注释链接里的「注」图标也固定 0.8 字高，不再显示成大方块 (0d0d7e36)
- :bug: fix(subscribe): 全部选项未读数改为各源之和 (61de0df4)
- :bug: 运行状态页 infoRow 声明顺序导致分析 Lua 占用报错 (47abbeda)

#### 性能

- Revert ":zap: perf(source): 列源只读元信息，不再加载全部源模块" (4eee5ff7)
- :zap: perf(source): 列源只读元信息，不再加载全部源模块 (d1fdfa6a)

#### 重构

- :recycle: refactor(subscribe): 淘汰规则统一为 180 天或 600 条（收藏保留） (4eca4f80)
- :recycle: refactor(subscribe): 去掉文章图片大小上限，残缺缓存联网时重做 (fd4e3478)

#### 变更

- :white_check_mark: fix: 修复发布前离线测试失败（英文翻译引号语法错、远程页元素 id、翻译键缺失与残留） (c9cf9f7d)
- :fire: refactor(wechat): 去掉公众号文章页 8MB 与 30 张图的上限 (6dcaaadc)

### 完整对比

https://github.com/AnkioTomas/moon/compare/v0.2.39...v0.2.40
