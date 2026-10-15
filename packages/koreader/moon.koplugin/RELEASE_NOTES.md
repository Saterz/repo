# v0.2.5 · 2026-10-15

## 月读 v0.2.5

KOReader 插件包：`book.koplugin-v0.2.5.zip`

输入法词库（整库，手动 sideload）：`dictionary.sqlite3 dictionary-wubi.sqlite3 dictionary-cangjie.sqlite3 dictionary-zhuyin.sqlite3`

安装：解压后将 `book.koplugin` 复制到 KOReader 的 `plugins` 目录，然后重启。

拓展书源（可选，需同时安装月读）：`moonsource-kavita.koplugin-v0.2.5.zip`（Kavita）、
`moonsource-bookorbit.koplugin-v0.2.5.zip`（BookOrbit）。解压后同样放进 `plugins` 目录。

词库 sideload：下载对应布局的词库，直接放入 KOReader 数据目录下的
`.moon/`（与 `book.sqlite3` 同级）。附件已使用最终文件名，无需重命名。

### 更新内容

相对上一版本 `v0.2.4`：

#### 新功能

- :sparkles: (kavita): 请求超时与进度心跳间隔可在设置里调，慢设备不再 30s 拉不完书架 (5ca6ec29)

#### 修复

- :bug: (kavita): 卷行元数据只写真正变化的行、计入同步变更，开书取重读后的容器行 (56bfe0f2)
- :bug: (panel): 顶栏副标题取 book.authors，字段名写错成单数 author 一直读不到 (b4ea9673)
- :bug: (reader): 整本书冷打开按本地记录回落位置，sidecar 缺失不再停在开头 (e3ee1906)
- :bug: (cache): 清缓存保留 KOReader .sdr 边车，重下后位置/书签/标注还在 (81710d6b)
- :bug: (panel): 编辑态手势表不能为 nil，否则一点就崩 (139d90b2)
- :bug: (kavita): 页级进度按 spine 判，不再按百分比 (f978e057)
- :bug: (kavita): 阅读时间按服务器本地时间解析，刚读完的书不再排在旧书后面 (bcdfaee2)
- :bug: (library): 「最近阅读」只列读过的书，没读过的不再排在后头 (d68006cc)
- :bug: (kavita): 修复图书馆元数据/已读与首页继续阅读的高度、排序 (77c10241)

#### 变更

- fix: 业务代码不再静默吞错（锁屏预取、http 超时、诊断导出） (1ea6bfcd)
- fix: 审计修复（页级进度 nil 崩溃、最近阅读口径测试、封面预取吞错） (9d4b1a0f)
- fix(kavita): 心跳间隔与设置一致、清理过时注释、补 spineCmp 远端无 spine 测试 (348870ee)
- fix(bars): 微信读书页码模式按全书估算页码 (c37a4d0d)
- fix(remote): 上传默认覆盖同名文件 (2250e448)
- :feat: (kavita): 阅读期进度心跳，Kavita 阅读会话不再恒为 0 秒 (ff392961)
- :feat: (kavita): 最近阅读显示当前在读的卷；卷行继承容器（series 级）元数据 (42bd7207)

### 完整对比

https://github.com/AnkioTomas/moon/compare/v0.2.4...v0.2.5

# v0.2.4 · 2026-10-14

## 月读 v0.2.4

KOReader 插件包：`book.koplugin-v0.2.4.zip`

输入法词库（整库，手动 sideload）：`dictionary.sqlite3 dictionary-wubi.sqlite3 dictionary-cangjie.sqlite3 dictionary-zhuyin.sqlite3`

安装：解压后将 `book.koplugin` 复制到 KOReader 的 `plugins` 目录，然后重启。

拓展书源（可选，需同时安装月读）：`moonsource-kavita.koplugin-v0.2.4.zip`（Kavita）、
`moonsource-bookorbit.koplugin-v0.2.4.zip`（BookOrbit）。解压后同样放进 `plugins` 目录。

词库 sideload：下载对应布局的词库，直接放入 KOReader 数据目录下的
`.moon/`（与 `book.sqlite3` 同级）。附件已使用最终文件名，无需重命名。

### 更新内容

相对上一版本 `v0.2.3`：

#### 新功能

- :sparkles: (kindle): 新增 Kindle 书库源（对接 kindle.koplugin） (f3c1fde4)
- :sparkles: (local): 新增「按文件夹分类」开关，编辑分类时按开关决定是否移动文件 (dbe6d17c)
- :sparkles: (ui): 新增错误页“关闭月读”选项 (c3a60471)
- :sparkles: (ai): 添加 OCR 文字识别功能支持 (fb3ed540)
- :sparkles: (ai): 添加 OCR 文字识别功能支持 (b24f86b5)
- :sparkles: (desktop): add physical page-turn keys support (de382566)
- :sparkles: (ui): 支持顶栏独立字号与高度设置 (69be326f)
- :sparkles: (sync): 实现书架同步节流与并发登录重试机制 (c747a7e1)

#### 修复

- :bug: 海报锁屏：未打开过的网络书联网时预取封面 (653e38f6)
- :bug: (book): 修复书架刷新偶尔显示为空 (3c2eb376)
- :bug: (jdread): 修复京东扫码确认后仍停留在扫码页 (#36) (ff783987)
- :bug: (local): 修复系统 documents 目录扫不到：放开扫描深度、按 KOReader 格式表识别书籍、默认使用主目录 (84085ba8)
- :bug: (cache): 清理缓存后自动重新生成封面，复位本地扫盘封面标记并作废内存缓存 (37108a42)
- :bug: (desktop): fix exit hang by properly closing residual windows on exit (ce4ac42a)
- :bug: (copymanga): 修复并发请求时令牌过期重登逻辑 (d121fc54)
- :bug: (ui): 修复面板编辑手势事件未正确初始化的问题 (bde89f70)

#### 界面

- :lipstick: (ui): 重启后书架封面解码前留白，不再先闪色块封面 (b1cf5f8d)

#### 重构

- :recycle: (ai): 过滤 KOReader 的 .sdr 边车目录 (a9c3c784)
- :recycle: (local): 精简 documents 扫描修复 (df10019c)
- :recycle: (ui): 统一顶栏/底栏字体策略并规范水平留白 (ee42b04f)
- :recycle: (ai): 统一复用上传进度框实现通用操作进度反馈 (3bb5cfa6)
- :recycle: (ui): 重构远程管理页面结构与交互逻辑 (4aa90c2f)
- :recycle: (http): 统一超时管理，支持 AI/网络超时独立配置与倍率扩展 (bea815bf)
- :recycle: (desktop): 优化混合模式下书架同步节流逻辑 (cf98b31c)
- :recycle: (ui): 优化极窄屏下数字输入框宽度计算逻辑 (064d82d5)

#### 变更

- :green_heart: (tests): 每个 spec 独立进程运行，修复 CI 段错误 (486027c7)
- :green_heart: tests: 基线前预加载 ffi，避免卸载后重建 ctype 表导致段错误 (ed95deea)
- :speech_balloon: (local): 选择 Kindle documents 目录时提醒选子目录 (4d215a20)
- :lock: (local): 扫盘跳过带 DRM 的 mobi / azw / azw3 (fbf8693b)
- :adhesive_bandage: (book): 修复启动横幅加载失败导致插件崩溃的问题 (89d6c35b)

### 完整对比

https://github.com/AnkioTomas/moon/compare/v0.2.3...v0.2.4

# v0.2.3 · 2026-10-14

## 月读 v0.2.3

KOReader 插件包：`book.koplugin-v0.2.3.zip`

输入法词库（整库，手动 sideload）：`dictionary.sqlite3 dictionary-wubi.sqlite3 dictionary-cangjie.sqlite3 dictionary-zhuyin.sqlite3`

安装：解压后将 `book.koplugin` 复制到 KOReader 的 `plugins` 目录，然后重启。

拓展书源（可选，需同时安装月读）：`moonsource-kavita.koplugin-v0.2.3.zip`（Kavita）、
`moonsource-bookorbit.koplugin-v0.2.3.zip`（BookOrbit）。解压后同样放进 `plugins` 目录。

词库 sideload：下载对应布局的词库，直接放入 KOReader 数据目录下的
`.moon/`（与 `book.sqlite3` 同级）。附件已使用最终文件名，无需重命名。

### 更新内容

相对上一版本 `v0.2.2`：

#### 修复

- :bug: (copymanga): 令牌失效时用保存的账号自动重登重试，不再只报 HTTP 401 (#42) (11fd49f3)

### 完整对比

https://github.com/AnkioTomas/moon/compare/v0.2.2...v0.2.3

# v0.2.2 · 2026-10-14

## 月读 v0.2.2

KOReader 插件包：`book.koplugin-v0.2.2.zip`

输入法词库（整库，手动 sideload）：`dictionary.sqlite3 dictionary-wubi.sqlite3 dictionary-cangjie.sqlite3 dictionary-zhuyin.sqlite3`

安装：解压后将 `book.koplugin` 复制到 KOReader 的 `plugins` 目录，然后重启。

拓展书源（可选，需同时安装月读）：`moonsource-kavita.koplugin-v0.2.2.zip`（Kavita）、
`moonsource-bookorbit.koplugin-v0.2.2.zip`（BookOrbit）。解压后同样放进 `plugins` 目录。

词库 sideload：下载对应布局的词库，直接放入 KOReader 数据目录下的
`.moon/`（与 `book.sqlite3` 同级）。附件已使用最终文件名，无需重命名。

### 更新内容

相对上一版本 `v0.2.1`：

#### 修复

- :bug: (sync): 混合模式下同步全部已启用源的书架，不再只拉活跃源 (#42) (90ca523d)

### 完整对比

https://github.com/AnkioTomas/moon/compare/v0.2.1...v0.2.2

# v0.2.1 · 2026-10-13

## 月读 v0.2.1

KOReader 插件包：`book.koplugin-v0.2.1.zip`

输入法词库（整库，手动 sideload）：`dictionary.sqlite3 dictionary-wubi.sqlite3 dictionary-cangjie.sqlite3 dictionary-zhuyin.sqlite3`

安装：解压后将 `book.koplugin` 复制到 KOReader 的 `plugins` 目录，然后重启。

拓展书源（可选，需同时安装月读）：`moonsource-kavita.koplugin-v0.2.1.zip`（Kavita）、
`moonsource-bookorbit.koplugin-v0.2.1.zip`（BookOrbit）。解压后同样放进 `plugins` 目录。

词库 sideload：下载对应布局的词库，直接放入 KOReader 数据目录下的
`.moon/`（与 `book.sqlite3` 同级）。附件已使用最终文件名，无需重命名。

### 更新内容

相对上一版本 `v0.2.0`：

#### 新功能

- :sparkles: (insight): 统计页柱状图加纵坐标，按时长标刻度 (b74503c0)

#### 修复

- :bug: (lockscreen): 海报墙竖屏排版在高分屏不再挤成十列，无封面改用生成封面 (a43343fb)
- :bug: (home): 年份与新闻序号不再被截成省略号 (602112aa)

#### 界面

- :lipstick: (lockscreen): 美化阅读统计与当前阅读锁屏 (a87d6387)
- :lipstick: (store): 书城工具条搜索改为图标，去掉清除按钮 (0a5ea438)
- :lipstick: (library): 分组页返回按钮去掉边框和文字，只留图标 (e8f89dc7)

#### 变更

- :green_heart: (tests): 补 bottomcontainer 桩，柱状图测试在没有 KOReader 源码的 CI 上也能跑 (1fa06d32)
- :loud_sound: (log): 启动时在 book.log 写一行月读版本、KOReader 版本与设备型号 (44ed67b1)
- :ambulance: (lockscreen): 修复灰度 Kindle 上斜边海报墙导致启动崩溃 (d9c13aee)

### 完整对比

https://github.com/AnkioTomas/moon/compare/v0.2.0...v0.2.1
