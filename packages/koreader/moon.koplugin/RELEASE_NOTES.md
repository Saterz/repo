# v0.2.30 · 2026-10-22

## 月读 v0.2.30

KOReader 插件包：`book.koplugin-v0.2.30.zip`

输入法词库（整库，手动 sideload）：`dictionary.sqlite3 dictionary-wubi.sqlite3 dictionary-cangjie.sqlite3 dictionary-zhuyin.sqlite3`

安装：解压后将 `book.koplugin` 复制到 KOReader 的 `plugins` 目录，然后重启。

拓展书源（可选，需同时安装月读）：`moonsource-kavita.koplugin-v0.2.30.zip`（Kavita）、
`moonsource-bookorbit.koplugin-v0.2.30.zip`（BookOrbit）。解压后同样放进 `plugins` 目录。

词库 sideload：下载对应布局的词库，直接放入 KOReader 数据目录下的
`.moon/`（与 `book.sqlite3` 同级）。附件已使用最终文件名，无需重命名。

### 更新内容

相对上一版本 `v0.2.29`：

#### 新功能

- :sparkles: (panel): 下滑快捷面板增加电源菜单 (044f38b2)
- :sparkles: (bars): 阅读页上下栏新增「剩余运存」组件 (f7896445)
- :sparkles: (wechat): 微信读书全面迁移到 App 协议，正文改走 chapterdownload (20d954ef)
- :sparkles: (bluetooth): 支持 Kindle 原生与 Kobo 系统蓝牙，后端拆成 khp / kindle / kobo (07ab5ae1)
- :sparkles: (home): 新增阅读小卡，本月挑战与今年读完目标可在统计页自己设置 (cbc78f25)
- :sparkles: (insight): 统计页扩成六页（今日/本月/本年/榜单/趋势/进度），页面与数据卡片可在设置里多选显示 (9550805d)
- :sparkles: (home): 一言、书摘正文透明不铺底色，阅读统计卡片底色透明度可调 (288e48e2)
- :sparkles: (ime): 快捷面板新增简繁转换，整本书转成简体或繁体 (7ed17d82)

#### 修复

- :bug: (wake): 唤醒卡死防护与休眠/唤醒诊断日志 (122cbed3)
- :bug: (subscribe): 图片链接直接收图，添加菜单加上推荐源 (db87fa57)
- :bug: (fonts): WOFF 转换改分块解压，修复小内存设备字体解压失败 (9c8687f7)
- :bug: (subscribe): 修复公众号「加载更早的文章」翻不动 (2f6437be)

#### 界面

- :lipstick: (panel): 快捷面板编辑对齐首页组件风格 (c10ce3ac)

#### 性能

- :zap: (local): WebDAV 本地书扫描改为先入库、后台上传 (a2d99fcb)

#### 文档

- :memo: (docs): README 补充电源菜单与剩余运存组件 (3a5eaf4d)

#### 变更

- :green_heart: (ci): 修复 CI 离线测试三处失败 (802986cd)
- :globe_with_meridians: (subscribe): 补上添加菜单「推荐」的英繁文案 (68e986cb)
- :loud_sound: (reader): 关书与退回桌面各步耗时超 100ms 记日志，定位退出卡顿 (bca74119)
- :label: (insight): 修掉统计页新增代码的 LuaLS 类型警告 (c465e098)
- :children_crossing: (tasks): 只有缓存任务拦自动休眠，休眠与待机路径补日志 (f472ea75)
- :loud_sound: (source): 各书源解密失败时写日志，晋江 VIP 额外记录失败阶段与原始 contentvars (bf47e96c)

### 完整对比

https://github.com/AnkioTomas/moon/compare/v0.2.29...v0.2.30

# v0.2.29 · 2026-10-21

## 月读 v0.2.29

KOReader 插件包：`book.koplugin-v0.2.29.zip`

输入法词库（整库，手动 sideload）：`dictionary.sqlite3 dictionary-wubi.sqlite3 dictionary-cangjie.sqlite3 dictionary-zhuyin.sqlite3`

安装：解压后将 `book.koplugin` 复制到 KOReader 的 `plugins` 目录，然后重启。

拓展书源（可选，需同时安装月读）：`moonsource-kavita.koplugin-v0.2.29.zip`（Kavita）、
`moonsource-bookorbit.koplugin-v0.2.29.zip`（BookOrbit）。解压后同样放进 `plugins` 目录。

词库 sideload：下载对应布局的词库，直接放入 KOReader 数据目录下的
`.moon/`（与 `book.sqlite3` 同级）。附件已使用最终文件名，无需重命名。

### 更新内容

相对上一版本 `v0.2.28`：

#### 新功能

- :sparkles: (font): 已下载的在线字体可以删除 (2c24a8d6)

#### 修复

- :bug: (wechat): 带 BOM 的章节正文不再被误判成试读片段 (7312e1f2)

#### 文档

- :memo: (docs): README 补充长佩、潇湘等新数据源，同步设置分组与刮削、书库页签说明 (5cd17cc9)

#### 变更

- :children_crossing: (wechat): 章节取不到正文时进入临时提示页，不再挡在阅读器外 (ef98a2a8)

### 完整对比

https://github.com/AnkioTomas/moon/compare/v0.2.28...v0.2.29

# v0.2.28 · 2026-10-21

## 月读 v0.2.28

KOReader 插件包：`book.koplugin-v0.2.28.zip`

输入法词库（整库，手动 sideload）：`dictionary.sqlite3 dictionary-wubi.sqlite3 dictionary-cangjie.sqlite3 dictionary-zhuyin.sqlite3`

安装：解压后将 `book.koplugin` 复制到 KOReader 的 `plugins` 目录，然后重启。

拓展书源（可选，需同时安装月读）：`moonsource-kavita.koplugin-v0.2.28.zip`（Kavita）、
`moonsource-bookorbit.koplugin-v0.2.28.zip`（BookOrbit）。解压后同样放进 `plugins` 目录。

词库 sideload：下载对应布局的词库，直接放入 KOReader 数据目录下的
`.moon/`（与 `book.sqlite3` 同级）。附件已使用最终文件名，无需重命名。

### 更新内容

相对上一版本 `v0.2.27`：

#### 新功能

- :sparkles: (ui): 弹窗支持可配置的下滑/上滑关闭手势 (5574fedf)
- :sparkles: (scrape): 应用前弹修改预览，可逐行取消；去掉「自动」来源 (5fbe0616)
- :sparkles: (zlib): 新增 iread.ink、zh.per101.ru 候选镜像，清理登录失败的镜像 (c143a191)
- :sparkles: (library): 书库页签改为多选弹窗，新增本地文件夹页签 (7f8886fb)
- :sparkles: (home): 一言、书摘组件新增居中、竖线、引号三种样式 (6d5e9a57)
- :sparkles: (xiaoxiang): 新站接口、VIP 章节 Fock 解密与标点字形识别 (fdd64ce2)
- :sparkles: (changpei): token 过期时用 refresh_token 自动续期 (2e9f2363)
- :sparkles: (changpei): 书城榜单、书架与进度同步，修扫码登录与付费章判断 (33f100a8)
- :sparkles: (changpei): 登录态改用 Cookie，新增扫码与浏览器授权登录 (2a071ade)
- :sparkles: (lockscreen): 广告版 Kindle 在锁屏设置页提示并一键去广告 (c743b8e7)
- :sparkles: (source): 新增长佩、潇湘数据源，刮削可选小说数据来源 (f59a2b3a)
- :sparkles: (jjwxc): 接入 VIP 章节：网页解密、字体反爬、已购/未购标注 (98146ebd)

#### 修复

- :bug: (font): 微信读书字体转换失败不再伪装成已安装 (fa780ded)
- :bug: (sync): 后台推脏行只处理当前源，混合模式才推全部启用源 (e42514dc)
- :bug: (library): 文件夹视图列出未下载的 WebDAV 书，最近阅读不再列已删本地书 (bed515ea)
- :bug: (zlib): 登录先走 rpc.php 并串行请求，修复填了账号密码仍无法登录 (e861bedc)
- :bug: (wechat): 删除只有想法的笔记时连带删掉远端划线 (255f780c)
- :bug: (subscribe): 目录缓存过期后仍按旧目录挪章号，公众号笔记不再错位 (19b8aad8)
- :bug: (wechat): 想法列表拉不到时保留本地想法，新想法不再重复上传 (ba262d1e)
- :bug: (store): 章节源缓存过任意一章就给清理缓存入口 (eaf4f8a6)
- :bug: (wechat): 想法列表被拒(-2003)不再拖死划线上传 (753797d5)
- :bug: (changpei): 扫码登录带上网页 token，修确认后提示请登录 (6ef546b5)
- :bug: (topbar): 唤醒后补读一次 Wi-Fi 状态，避免图标停在断开 (671d42fb)
- :bug: (update): 转发接口失败时回落直连 GitHub 检查更新 (989b4fee)

#### 界面

- :lipstick: (home): 一言、书摘署名加粗，居中改为可选开关 (1aae20cf)

#### 性能

- :zap: (desktop): FM 改列空目录 ko-empty，取代延后列目录 (07e7828a)
- :zap: (startup): 启动即开桌面时延后 FM 首次列目录 (94f3827f)
- :zap: (startup): 插件模块直达加载，减少慢文件系统上的失败 open (373e9c44)
- :zap: (jjwxc): VIP 正文解密与字体解析放进子进程，避免卡 UI (237b54eb)

#### 重构

- :recycle: (setting): 账号页每个书源一行进二级页，书籍来源直接弹窗切换 (503faddf)
- :recycle: (scrape): 微信读书刮削改走数据源 searchAsync，删掉重复实现 (86e1d328)
- :recycle: (source): 起点与 QQ阅读未购 VIP 章给临时提示并标注已购/未购 (41d76393)

#### 变更

- :children_crossing: (setting): 设置分组重排，新增「外观」组，AI 接口归入阅读 (188b5e4d)
- :speech_balloon: (setting): 设置根页「书籍来源」改名「当前书库」 (13faa327)
- :children_crossing: (setting): 书架显示按「封面 / 书库 / 随机一本」分组 (09c12148)
- :children_crossing: (changpei): Cookie 登录失效时提示改用扫码登录 (9c5b27b8)
- :children_crossing: (scrape): 刮削改成书名行 + 候选来源列表，可依次换源重搜 (17fc08ba)
- :loud_sound: (zlib): 镜像选定与登录结果写入 info 日志 (8256e26d)
- :loud_sound: (startup): 启动各步超过 100ms 记日志，定位慢启动 (e27288a5)

### 完整对比

https://github.com/AnkioTomas/moon/compare/v0.2.27...v0.2.28

# v0.2.27 · 2026-10-20

## 月读 v0.2.27

KOReader 插件包：`book.koplugin-v0.2.27.zip`

输入法词库（整库，手动 sideload）：`dictionary.sqlite3 dictionary-wubi.sqlite3 dictionary-cangjie.sqlite3 dictionary-zhuyin.sqlite3`

安装：解压后将 `book.koplugin` 复制到 KOReader 的 `plugins` 目录，然后重启。

拓展书源（可选，需同时安装月读）：`moonsource-kavita.koplugin-v0.2.27.zip`（Kavita）、
`moonsource-bookorbit.koplugin-v0.2.27.zip`（BookOrbit）。解压后同样放进 `plugins` 目录。

词库 sideload：下载对应布局的词库，直接放入 KOReader 数据目录下的
`.moon/`（与 `book.sqlite3` 同级）。附件已使用最终文件名，无需重命名。

### 更新内容

相对上一版本 `v0.2.26`：

#### 重构

- :recycle: (ime): 键盘收起键并入输入法，修复停用 ime 后设置页报错 (52fda8fd)

### 完整对比

https://github.com/AnkioTomas/moon/compare/v0.2.26...v0.2.27

# v0.2.26 · 2026-10-20

## 月读 v0.2.26

KOReader 插件包：`book.koplugin-v0.2.26.zip`

输入法词库（整库，手动 sideload）：`dictionary.sqlite3 dictionary-wubi.sqlite3 dictionary-cangjie.sqlite3 dictionary-zhuyin.sqlite3`

安装：解压后将 `book.koplugin` 复制到 KOReader 的 `plugins` 目录，然后重启。

拓展书源（可选，需同时安装月读）：`moonsource-kavita.koplugin-v0.2.26.zip`（Kavita）、
`moonsource-bookorbit.koplugin-v0.2.26.zip`（BookOrbit）。解压后同样放进 `plugins` 目录。

词库 sideload：下载对应布局的词库，直接放入 KOReader 数据目录下的
`.moon/`（与 `book.sqlite3` 同级）。附件已使用最终文件名，无需重命名。

### 更新内容

相对上一版本 `v0.2.25`：

#### 新功能

- :sparkles: (source): 未登录的账号行提示可经远程管理浏览器授权 (0b2b369f)
- :sparkles: (mirror): GitHub 加速镜像失败落盘拉黑 7 天（更新探测与仓库文件共用） (19c6a10b)
- :sparkles: (zlib): 竞速失败的镜像落盘拉黑 7 天 (8eef7bb5)
- :sparkles: (reviews): 段评预缓存改为整本、每句只存前 10 条，离线只显示已缓存句；缓存失败时提示失败章节 (dd4e6b75)
- :sparkles: (zlib): 种子镜像补全 zlibrary.koplugin 的域名清单 (022e0b42)
- :sparkles: (reviews): 微信读书与番茄支持离线段评，缓存章节时可勾选同时缓存段评 (456ce987)
- :sparkles: (passcode): 密码页显示设备头像与名称，数字短暂明文，输错 5 次出现忘记密码入口 (cb308cac)

#### 修复

- :bug: (zlib): 一轮镜像全失败后种子窗口后移，后面的镜像才有机会被用到 (005dae76)
- :bug: (bluetooth): 连接设备没有名称时顶栏只显示图标，不再崩溃 (0023734d)

#### 性能

- :zap: (zlib): 镜像请求并发竞速（每次 5 个，取链接仍串行） (8c749c5c)

#### 重构

- :recycle: (zlib): 仅首次无可用镜像时并发竞速，之后固定用胜出镜像 (ffc9f2f8)

#### 变更

- :white_check_mark: (tests): 桩掉 pluginshare，CI 无 KOReader 源码也能跑 (4d8038c8)
- :rewind: 回滚 zlib 种子窗口后移（未经确认的改动） (3d3be9c9)
- :children_crossing: (tasks): 后台任务未结束时不再自动熄屏 (6b93ccc4)
- :children_crossing: (wallpaper): 界面壁纸默认关闭且透明度默认 30%，选图后不再铺满所有界面 (#51) (f0a2ca67)

### 完整对比

https://github.com/AnkioTomas/moon/compare/v0.2.25...v0.2.26
