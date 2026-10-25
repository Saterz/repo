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

# v0.2.39 · 2026-10-25

## 月读 v0.2.39

KOReader 插件包：`book.koplugin-v0.2.39.zip`

输入法词库（整库，手动 sideload）：`dictionary.sqlite3 dictionary-wubi.sqlite3 dictionary-cangjie.sqlite3 dictionary-zhuyin.sqlite3`

安装：解压后将 `book.koplugin` 复制到 KOReader 的 `plugins` 目录，然后重启。

拓展书源（可选，需同时安装月读）：`moonsource-kavita.koplugin-v0.2.39.zip`（Kavita）、
`moonsource-bookorbit.koplugin-v0.2.39.zip`（BookOrbit）。解压后同样放进 `plugins` 目录。

词库 sideload：下载对应布局的词库，直接放入 KOReader 数据目录下的
`.moon/`（与 `book.sqlite3` 同级）。附件已使用最终文件名，无需重命名。

### 更新内容

相对上一版本 `v0.2.38`：

#### 新功能

- :sparkles: (wallpaper): 界面壁纸支持选文件夹，启动 / 唤醒随机换图 (eec139ca)
- :sparkles: (legado): 开源阅读支持 reader3 与轻阅读后端，可登录 (4583be57)
- :sparkles: (monitor): 设置页新增运行状态，按内存 / CPU 列出进程 (c8107dcf)

#### 修复

- :bug: (jjwxc): 修复设置页「晋江账号」点不动，登录入口回调引用了尚未声明的局部函数 (fa4fe256)
- :bug: Kindle 原生蓝牙按真实字段 bd_name / bd_address 读取，修复只显示 MAC (a93797ad)
- :bug: (utils): 模块加载器同名时目录模块压过残留的旧 .lua (e0b04d2d)
- :bug: (remote): 文件页快捷入口只高亮包含当前目录的最深一项 (1957a3db)

#### 性能

- :zap: online 任务最终失败后指数冷却，避免弱网下反复入队 (083d79d1)

#### 文档

- :memo: (readme): 补充翻页器 pageturner 联动插件的说明与安装 (54da1409)

### 完整对比

https://github.com/AnkioTomas/moon/compare/v0.2.38...v0.2.39

# v0.2.38 · 2026-10-24

## 月读 v0.2.38

KOReader 插件包：`book.koplugin-v0.2.38.zip`

输入法词库（整库，手动 sideload）：`dictionary.sqlite3 dictionary-wubi.sqlite3 dictionary-cangjie.sqlite3 dictionary-zhuyin.sqlite3`

安装：解压后将 `book.koplugin` 复制到 KOReader 的 `plugins` 目录，然后重启。

拓展书源（可选，需同时安装月读）：`moonsource-kavita.koplugin-v0.2.38.zip`（Kavita）、
`moonsource-bookorbit.koplugin-v0.2.38.zip`（BookOrbit）。解压后同样放进 `plugins` 目录。

词库 sideload：下载对应布局的词库，直接放入 KOReader 数据目录下的
`.moon/`（与 `book.sqlite3` 同级）。附件已使用最终文件名，无需重命名。

### 更新内容

相对上一版本 `v0.2.37`：

#### 新功能

- :sparkles: (source): 书架同步按远端进度自动标记已读 (7c9d1853)
- :sparkles: (panel): 快捷面板的 Wi-Fi 和蓝牙按钮显示当前连接的名字 (bb2a2a0c)
- :sparkles: (xray): 支持删除、按章识别与自动预取，标记默认关闭 (c28c8dfa)
- :sparkles: (desktop): 首次安装后桌面第一次打开时询问是否查看文档 (3360cb60)
- :sparkles: feat(subscribe): 缓存全部未读与文章内二三级目录 (68833c86)

#### 修复

- :bug: (bluetooth): 修复 Kindle 快捷面板关不掉蓝牙 (736e3ee4)
- :bug: (subscribe): 修复订阅正文中文名图片下不来，AVIF 图给出占位说明 (e5127d6d)

#### 性能

- :zap: (store): 书城榜单与搜索的匿名请求走 http 缓存 5 分钟 (02bb8d59)

#### 变更

- :children_crossing: (setting): 翻页动画、侧栏、X-Ray 等阅读功能提升到设置根页 (42b6529d)
- :children_crossing: (xray): 订阅文章不再提供 X-Ray (ec9dbaa5)
- :children_crossing: (reader): 边距调整默认直接重排不弹提示，设置里加开关可恢复 (21aad813)
- :children_crossing: (store): 书城下载时本地书库未配置，直接弹目录选择并接着下载 (6849396c)

### 完整对比

https://github.com/AnkioTomas/moon/compare/v0.2.37...v0.2.38
