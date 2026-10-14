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

# v0.2.0 · 2026-10-13

## 月读 v0.2.0

KOReader 插件包：`book.koplugin-v0.2.0.zip`

输入法词库（整库，手动 sideload）：`dictionary.sqlite3 dictionary-wubi.sqlite3 dictionary-cangjie.sqlite3 dictionary-zhuyin.sqlite3`

安装：解压后将 `book.koplugin` 复制到 KOReader 的 `plugins` 目录，然后重启。

拓展书源（可选，需同时安装月读）：`moonsource-kavita.koplugin-v0.2.0.zip`（Kavita）、
`moonsource-bookorbit.koplugin-v0.2.0.zip`（BookOrbit）。解压后同样放进 `plugins` 目录。

词库 sideload：下载对应布局的词库，直接放入 KOReader 数据目录下的
`.moon/`（与 `book.sqlite3` 同级）。附件已使用最终文件名，无需重命名。

### 更新内容

相对上一版本 `v0.1.9`：

#### 新功能

- :sparkles: feat(xray): 一次分析全书生成全部人物、地点和专有名词 (18efe1db)
- :sparkles: feat(keyboard): 虚拟键盘加收起键 (58b5f1fb)
- :sparkles: (library): 图书馆改为 Kobo 式书籍/作者/系列/分类页签 (d879824b)
- :sparkles: (detail): 详情页改为 Kobo 式布局，补全书籍元数据 (64934d9f)
- :sparkles: (build): 支持拓展书源插件的独立打包与发布 (460bf008)
- :sparkles: feat(remote): 远程管理新增月读更新：上传安装包即自动安装并重启 (fbf455fa)
- :sparkles: feat(ai): 问书：不用划词，直接就已读内容向 AI 提问 (d755a784)
- :sparkles: feat(stats): 首页热力图、阅读时段统计页与详情页读完预测 (75bf71ac)
- :sparkles: feat(stats): 设置维护页可导入 KOReader 自带统计插件的阅读记录 (4447ce6b)
- :sparkles: feat(clock): 时间与日期设置：时区、手动改时间、进入桌面自动 NTP 校时 (3a73feab)
- :sparkles: feat(ai): 章节摘要、前情提要、读书报告，解释可追问并存为笔记 (df739129)
- :sparkles: feat(reflow): 重新排版支持所有能取出文字的文档，排版版另存到缓存不替换原书 (e9b66fb9)
- :sparkles: feat(reader): 长按菜单自动扫描其它插件的按钮，可逐个屏蔽并标明来源 (75eb20a7)
- :sparkles: feat(reader): AI 解释带上划词所在的整句和段落 (68f05112)
- :sparkles: feat(reviews): 段评下划线可选虚线 / 实线 (4476399a)
- :sparkles: feat(ime): 候选词支持简繁转换 (7618eb53)
- :sparkles: feat(extensions): 底栏「拓展」列出其它插件入口 (1d8527d1)
- :sparkles: feat(bluetooth): 联动 kindle-hid-passthrough 开关、配对、连接蓝牙 (5f3ec55d)
- :sparkles: feat(extensions): BookOrbit 第三方书源（按库同步书架、下载原件、kosync 进度双向、划线上传） (1edf102e)
- :sparkles: feat(extensions): Kavita 第三方书源（下载 / 选卷、进度双向、划线上传、kamare 看漫画、首页 On Deck） (655805e6)
- :sparkles: feat(examples): 第三方书源示例 moonsource-demo（离线三章静态书） (1c80ba14)
- :sparkles: feat(home): 第三方源可追加首页组件（id 须 ext. 开头，不得重名） (3db66f40)
- :sparkles: feat(source): 源可自行展示内容，openBookAsync 回调 meta.handled 时桌面不开阅读器 (6d893a31)
- :sparkles: feat(source): 插件目录的 moon_source.lua 登记第三方书源 (842aa6ae)
- :sparkles: feat(tasks): 顶栏任务计数与可分页的后台任务列表 (7daf57cd)
- :sparkles: (ai): 添加逐小时天气预报支持 (3e4761f4)
- :sparkles: feat(translate): 新增整书双语对照，支持 Edge 与 AI 翻译 (9c3ef9c5)
- :sparkles: feat(reviews): 本地书可关联微信读书书目显示段评 (15c7e71d)
- :sparkles: feat(sidebar): 底栏改为图标页签，用户可选显示哪些页面 (412060d9)
- :sparkles: feat(passcode): 新增锁屏密码，冷启动和唤醒时需输入数字 PIN (e51d3400)
- :sparkles: feat(wechat): 新增「合并本地阅读时长」选项，补上离线阅读 (24eb8447)
- :sparkles: feat(panel): 阅读页快捷面板新增推送进度、拉取进度 (13e22eb3)
- :sparkles: feat(theme): 新增路径选择组件 PathPicker，支持选文件夹 / 选文件与图片缩略图 (525650c0)
- :sparkles: feat(lockscreen): 斜边海报旋转改为插值剪切，消除斜边锯齿 (fef5e27a)
- :sparkles: feat(lockscreen): 自定义图 / 壁纸文件夹可在设置页选择，精简锁屏代码 (bc0d47ee)
- :sparkles: feat(bars): 修复顶底栏刷新，新增章内页码与状态图标 (56845aaa)
- :sparkles: feat(reader): 会话提供当前页在本章的页码与本章页数 (53cd3f12)
- :sparkles: (detail): 章节缓存支持选择范围：全本 / 当前进度到结尾 / 往后 10·20·50·100 章 (2894822a)
- :sparkles: (ui): TextViewer 支持全屏与卡片两种风格，修复短文本浮在屏幕中间 (118f6e53)
- :sparkles: (ai): 添加段评标记与列表功能 (8d4b030a)
- :sparkles: (ai): 添加段评标记与列表功能 (2b1f587d)
- :sparkles: feat(wechat): 章节原样渲染，资源本地化，脚注可点击弹出 (13c79d92)
- :sparkles: feat(text): 新增 Text.stripHtml，简介统一清理 HTML (29784120)
- :sparkles: (detail): 详情页书名可换行，简介回到封面右栏，零碎信息收成一行图标条 (6327fe71)
- :sparkles: (detail): 未下载的整本书可下载，已读/未读按钮改短，标已读在线即推进度 (14f90ac6)
- :sparkles: (ui): 支持开关行的 toggle 选项 (e6579915)
- :sparkles: (online): ensure 一并下载必应与摸鱼日报图 (848af5ba)
- :sparkles: (utils): 添加 online 缓存目录路径 (057123b1)
- :sparkles: (ai): 补全 AI 阅读助手架构与配置支持 (c0b77325)
- :sparkles: (store): 添加 OPDS 和 Z-Library 书城支持 (aa95324a)
- :sparkles: (store): 添加书城底栏入口开关配置 (4e3108db)
- :sparkles: (ui): 添加 UI 配置模块 (f673709c)
- :sparkles: (ai): 添加进程内同步事件系统 (b0b4ddd3)
- :sparkles: (ai): 添加设备标识生成逻辑 (0dbf9022)
- :sparkles: (crypto): 新增纯 LuaJIT 加密库，覆盖国密与 RSA (1f8ed202)
- :sparkles: (plugin): 集成月读插件主菜单与系统 UI 配置 (d5e1cbfd)
- :sparkles: (ui): 优化初始化脚本并添加图标选择功能 (55a62da0)
- :sparkles: (ai): 添加 workers 模块文档 (5c56f18d)
- :sparkles: (build): 新增图标名生成工具 (0f474b03)
- :sparkles: (ui): 后台任务对话框重构，任务列表弹窗 + 单个任务进度弹窗，顶栏文案复用 (f4c5b411)
- :sparkles: (ai): 添加 BlitBuffer 和 ArchiverWriter 接口及文档类扩展功能 (c2725f6b)
- :sparkles: (ui): 添加书籍展示组件 (7e7b4920)
- :sparkles: (ai): add icon names from MaterialSymbolsOutlined-Regular.ttf to themes/icons/names.lua and update icon picker tool (e5811660)
- :sparkles: (ai): add icon names from MaterialSymbolsOutlined-Regular.ttf to themes/icons/names.lua and update icon picker tool (ab11e208)
- :sparkles: (ui): 增加主题配置和界面组件更新 (4d6a4341)
- :sparkles: (ai): 添加月读插件字体管理功能 (76176a0f)
- :sparkles: (ui): 统一组件主题令牌键命名 (d5b620dd)
- :sparkles: (ui): 添加图片控件和菜单项 UI 增强功能 (49ae47ed)
- :sparkles: (ai): add streaming commit message generation (01a8b83d)
- :sparkles: (ai): 更新发布流程和 UI 事件处理 (81ce2a61)
- :sparkles: (ai): 实现功能生命周期分发机制 (7300a124)
- :sparkles: (ai): add background task for caching full chapters (e0af48d2)
- :sparkles: (ai): add background task for caching full chapters (bd315d11)
- :sparkles: (ai): 优化书籍目录处理和图片加载逻辑 (8442a0a4)
- :sparkles: (ai): 添加 WebDAV 支持 (9c43f27b)
- :sparkles: (ai): 新增 Kindle 源支持 (655b0913)
- :sparkles: (ai): 新增 Kindle 源支持 (29c6dc11)
- :sparkles: (ai): 新增 Kindle 源支持 (c24c36a8)
- :sparkles: (ai): 新增 AI 解释功能 (67546b06)
- :sparkles: (ai): 添加清理书籍目录缓存的功能 (e1ee9139)
- :sparkles: (ai): 添加多语言支持并优化群组链接 (42614534)
- :sparkles: (ai): 优化微信统计支持 (300f1243)

#### 修复

- :bug: (ui): 数值选择弹窗列放不下时收窄，修复日期和时间五列溢出 (39dcde37)
- :bug: (review): 修复审查问题，X-Ray 全书分析支持断点续跑 (6d3cdda9)
- :bug: (library): 列表模式右侧「已下载」与菜单按钮固定靠右 (70350e08)
- :bug: fix(ui): 输入框焦点字段被虚拟键盘挡住时面板上移 (91c62e62)
- :bug: (home): 天气与时钟更新文字后重排，修复整块偏右 (6c0f6492)
- :bug: fix(reflow): 重新排版不再卡住界面，分析中可以取消 (aa97c171)
- :bug: fix(stats): 首页热力图跨过零点后回到桌面会重画 (a3a25832)
- :bug: fix(reader): 卸载的插件按钮不再残留在划词菜单排序里 (ae18f805)
- :bug: fix(clock): 自动 NTP 校时 6 小时内只做一次，不能改时间的设备直接跳过 (f6ce03d4)
- :bug: fix(reader): 重新排版不再丢掉原书搜不到的划线，内联目录误识别修正 (4ec8c9d6)
- :bug: fix(ai): 修正放大重试误判、取消后仍弹提示与摘要截断 (40d811ab)
- :bug: fix(stats): 导入的 KOReader 阅读记录不再被下次拉取当作已同步删掉 (fc0ed148)
- :bug: fix(ui): 嵌套点击区不再截走外层点按，顶栏空白处不再误开数据源选择 (13dacb45)
- :bug: fix(panel): 快捷面板设置预览的图标一行放不下时折行，不再溢出 (c5447923)
- :bug: fix(ai): 推理模型思考吃光 max_tokens 时按 4 倍上限重试一次 (02287e78)
- :bug: fix(reader): 衍生版补画中途关书后，原书删掉的划线不再被加回来 (118e6c2d)
- :bug: fix(reflow): 按书的目录切章，标题不是「第X章」写法的书也能正常排版 (4e922773)
- :bug: fix(reader): 衍生版划线不再丢失或错位，AI 解释定位到选中的那一句 (177733c2)
- :bug: fix(reader): 双语版和排版版的划线不再把错位坐标写进笔记库 (0a16e87e)
- :bug: fix(audit): 流式回调全经 guard、任务列表快刷、蓝牙未装不出顶栏 (b787a899)
- :bug: fix(source): 第三方书源等插件全部加载完再扫描，真机上能注册 (645b95d7)
- :bug: fix(audit): 入口补 Guard、遮罩全刷、压内存与卡顿 (07d74ea4)
- :bug: fix(desktop): 桌面收到非 Event 的原始输入时不再崩溃 (4ed410c8)
- :bug: (ime): 修复网络状态检测逻辑 (5fec7dd6)
- :bug: (ui): 修复 modal 在接收到非事件对象输入时的崩溃 (531d5640)
- :bug: fix(update): 装完更新立即重启，避免新旧代码混跑 (fff62fbd)
- :bug: fix(ui): 有方向键的设备点主题输入框不再报错 (758581d0)
- :bug: fix(ui): 键盘弹出时主题输入框的按钮点按没反应 (55f21478)
- :bug: fix(book): 删除 / 移动书籍时同步清理 KOReader 的 .sdr、阅读历史与收藏 (4c209ea6)
- :bug: fix(wechat): 阅读时长改为定时心跳上报，对齐 weread.koplugin (f67cd8e8)
- :bug: fix(progress): 只有本地和云端在上次同步后都改过才弹进度冲突 (691605ef)
- :bug: fix(wechat): 网文目录补「第 N 章」，章首补章名 (a6dc3942)
- :bug: fix(store): 限制书城下载文件名长度，修复书名过长下载失败 (9fc28f8e)
- :bug: fix(lockscreen): 锁屏前生成组合图，补全缓存键 (36b29ebd)
- :bug: fix(dictionary): 桌面安装 / 切换词典后刷新 KOReader 词典缓存 (de12f2c1)
- :bug: fix(progress): 云端只记到章时同章以本地为准，不再假冲突 (04cbd031)
- :bug: fix(baike): 长按动作与手势名开启百科后显示百度百科 (9983c78f)
- :bug: (animation): 动画后全刷改读 KOReader 刷新队列，修复章节边界全刷丢失 (7383c446)
- :bug: (book): 修复旧库书架迁移、身份行加入时间、已读修订号与笔记同步队列 (79cad174)
- :bug: (fanqie): 书架详情并发拉取与失败语义、取消与异步回调修正、目录解析去重 (f561a9f8)
- :bug: (jdread): 按文件成章修复《三盏灯》重复下载与空封面，目录保留锚点小节 (5fc8cb9b)
- :bug: (local): 堵 WebDAV 书目路径穿越，重复书移动不再丢进度，导入/替换不吞错误 (95d152f3)
- :bug: (books): 加入时间不再丢：旧库 fetched_at 回填，身份行首次上架补写 inserted_at (81df27ee)
- :bug: (webdav): 错误提示点明是 WebDAV，区分认证/权限/路径/空间/连不上，本地写盘失败不误报 (51cfdcc2)
- :bug: (fanqie): 设备注册被拦时用中文说明，不再丢 connection refused (02460a0d)
- :bug: (jdread): 扫码成功后跟跳转拿会话 Cookie，失败自动换新码 (da479f93)
- :bug: (ui): 背景遮罩改稀，Oasis 上不再糊成灰雾 (49c7f704)
- :bug: (reader): 章文件用书名、微信脚注可点并保留原书样式，字体选择器加回系统字库 (585d1ea7)
- :bug: (nightmode): 离线时定位直接失败，测试钉死日期 (68b55430)
- :bug: (plugin): 修正 Theme 模块的 require 路径 (4ac874f2)
- :bug: (ui): 修正 themes 模块引用路径并收紧弹窗交互 (6cab9bb8)
- :bug: (ui): 添加错误隔离机制 (f4ede30b)
- :bug: (koreader_ui): 修正 koreader_ui.lua 中的 Widget:free() 函数定义 (65038d9c)
- :bug: (测试): 修复首次同步测试用例 (32a2dd15)
- :bug: (client): fix crash and improve loop logic (d93918a2)
- :bug: (local): 修复本地扫盘每轮重开全部书籍 (7c7e37be)
- :bug: (jdread): 更新京东读书无权限提示信息 (71ffd9c0)

#### 界面

- :lipstick: (home): 历史上的今天与热点新闻的标记列左对齐，列宽按文字实测 (9bc13a63)
- :lipstick: fix(detail): 刮削结果卡片加上下间距 (a1a74f9e)
- :lipstick: feat(ui): 无封面时生成色块封面（按书名取色 + 内框 + 竖排书名 + 作者） (dbdc6fbd)
- :lipstick: fix(ui): bold 主题封面阴影挤压书名、详情统计格日期截断 (639c0a02)
- :lipstick: (ui): 主题按钮支持紧凑规格与文字后置图标 (31418d8e)
- :lipstick: fix(ui): paper 主题封面与按钮改为直角，封面图贴紧边框 (d8e74448)
- :lipstick: fix(ui): 主题圆角边框开启抗锯齿，圆形按钮不再有锯齿 (1306cadc)
- :lipstick: style(ui): 文本卡片底部按钮与卡片底边留出间距 (fba5247f)
- :lipstick: style(bars): 顶栏改用底栏的字体与字号，不再比底栏大一号 (219c0f60)
- :lipstick: (home): 优化首页组件排版，新增每小时天气预报 (79227c63)
- :lipstick: (reviews): 段评列表用上主题图标 (4da268a4)
- :lipstick: style(progress): 进度冲突弹窗按钮只显示本地/云端，正文分行列出两边位置 (6542e9e8)

#### 性能

- :zap: (azw3): KF8 重建内存降一个数量级，残缺缓存自动重建 (9c56cb6b)
- :zap: (azw3): 只取元数据时探头读取，整本重建推迟到阅读 (ba314d4e)

#### 重构

- :recycle: (library): 书籍扩展元数据收进 meta JSON 列，入库即规范化 (16a5806b)
- :recycle: (translate): 整书双语对照改为前台不可取消进度窗，任务队列撤回 cancelable (2809738a)
- :recycle: refactor(ai): AI 解释移出阅读器成为独立 feature，只出纯文本、不带思考过程 (54f35672)
- :recycle: refactor(topbar): 顶栏项改为 feature 约定文件收集，蓝牙项移回 feature (bff4b7f7)
- :recycle: refactor(setting): 词典、百科并入划词页，翻页动画、侧栏并入阅读行为页 (4128bb6b)
- :recycle: (ui): 重构底栏字体大小计算逻辑 (30b17eb3)
- :recycle: refactor(setting): 语言设置去掉中间页，只列插件支持的语言 (c65d1d04)
- :recycle: (ai): refactor Xray marks to use PageMarks API and simplify event handling (5e96eefd)
- :recycle: (desktop/detail): 重构详情获取逻辑并支持从作者源补充简介 (1a00da58)
- :recycle: refactor(remote): 清理远程管理冗余代码，修复发送空转并隔离服务错误 (dd4ae0a5)
- :recycle: refactor(reflow): 删除转换器死代码，预览直传全文，MOBI 提取并入重排 (55a6514c)
- :recycle: refactor(panel): 动作列表收口到 action_list，编辑排序按可见邻居交换 (2691d49e)
- :recycle: refactor(panel): 快捷面板执行收口、遮罩全刷，按钮按主题分形 (ec7a8041)
- :recycle: refactor(nightmode): 亮度菜单常开就地刷新，删除定位死代码 (0e128241)
- :recycle: refactor(lockscreen): 背景与主体严格拆分，修复列表翻页叠影与书卡文字重叠 (13a75f92)
- :recycle: (ime): 精简候选状态与词库下载，删除冗余防御 (5fec0322)
- :recycle: (db): 优化书籍路径与同步状态逻辑 (10694561)
- :recycle: (utils): 简化 `saw_data` 逻辑判断 (f50fd57c)
- :recycle: (source): 重构源管理与缓存逻辑，增强缓存判定与脏行处理 (8e83abca)
- :recycle: (desktop): 图书馆/统计直查 book.catalog，书架同步错误提示去重 (b1a4a37d)
- :recycle: (copymanga): 精简门面与客户端，章节按 uuid 落盘，修复图书馆封面 (5e9de795)
- :recycle: (wechat): 精简微信读书源，拆出笔记推送 (06e7842b)
- :recycle: (ui): 移除段评角标数字显示 (410f2e82)
- :recycle: (moon): 映射对齐服务端真实字段，删除 errText 与多余防御 (ca7b24c7)
- :recycle: (shelf): 推墓碑收口为 Shelf.pushDeletes，无待推时异步回调；syncAsync 参数精简 (cb55c152)
- :recycle: (ai): 重构注册表实现，支持多源缓存与配置驱动 (77fc2be0)
- :recycle: (ai): 重构生命周期钩子为按需推脏行 (33f38734)
- :recycle: (source): 源基类改为 pushDirty 后台推脏 + defer/skipped 异步回调；local 源扫盘索引入库、WebDAV 同步重写 (ffb99165)
- :recycle: (http): 流式请求不再 hook turbo _finalize_request，最后一跳由 yield 统一收尾 (54146288)
- :recycle: (desktop): 删除重复规整与过度防御，首页布局改为模块函数、顶栏单心跳 (c662f788)
- :recycle: (core): l10n、补丁管理器、后台任务与文档随重构更新 (74db8fe9)
- :recycle: (book): 删死代码与重复，同步入口去掉多余判空 (0b548a61)
- :recycle: (db): 表模块迁到使用方目录，撕墓碑连带清依附表 (a7203aad)
- :recycle: (reader): 阅读器模块，清理死代码并合并重复跳转 (9d4e4e34)
- :recycle: (main): 启动与联网时转发 online.onNetworkConnected (7ddc347c)
- :recycle: (utils): 收口图片后缀与文件头判断到 utils/image (34737ada)
- :recycle: (docs): 重构文档结构，重命名模块与路径，移除废弃表 (6864a372)
- :recycle: (ui): 重构下载状态判断逻辑与设置项路径 (72f11123)
- :recycle: (ui): 修正 UI 字体设置作用域，统一使用 "ui" 命名空间 (3d9236e4)
- :recycle: (demo): 修正主题切换配置路径为 ui.ui_theme (5c483d56)
- :recycle: (http): 重构缓存实现，使用统一 DB 表替代独立模块 (3390a102)
- :recycle: (ai): refactor settings to per-owner partitioning with legacy migration (825bbd69)
- :recycle: (db): 重构数据库模块，规范建表与事务管理 (995f1ac6)
- :recycle: (book.sync): 替换 onNetworkConnected 的调用方式 (a5a76e8f)
- :recycle: (dev): 重构 run.sh 支持 --watch 模式自动重启模拟器 (14408c61)
- :recycle: (db): 重构数据库模块命名与逻辑，统一为 book.* / http.* / crypto.* (1d421329)
- :recycle: (convert): 优化 html2epub 解码逻辑并清理代码规范 (dfc8b637)
- :recycle: (utils): 简化毫秒级性能计时逻辑 (7e3236f7)
- :recycle: (ui): 重构组件主题导入并优化字体选择器逻辑 (77b41e16)
- :recycle: (font): 重构字体目录扫描与 WOFF 解析逻辑 (387f9753)
- :recycle: (utils): 重构日志与路径工具，精简逻辑与完善文档 (fac6d16f)
- :recycle: 重构生命周期事件处理逻辑 (3ed98efb)
- :recycle: (http): 重构 http 模块并添加 HTTP 代理支持 (946b139c)
- :recycle: (http): 重构 http 模块并添加 HTTP 代理支持 (fb5a5b1f)
- :recycle: (ui): 简化主题加载路径 (18d1a8c5)
- :recycle: 重构插件生命周期管理和初始化流程 (74410c3f)
- :recycle: (ui): 修改l10n.lua文件中的代码 (7c146ea1)
- :recycle: (ui): 重构任务对话框 UI (17d36263)
- :recycle: (ui): 重构下载组件与弹窗绘制逻辑 (75c17bf5)
- :recycle: refactor UI components for better readability and performance (9baeceba)
- :recycle: (ai): 更新 Lua 文件中的类型注释 (8a7db353)
- :recycle: (config): 更新 .luarc.json 配置 (b0bb45ae)
- :recycle: (ui): 类型定义更新 (e7c5947c)
- :recycle: (core): 重构任务模块引用路径 统一将 `tasks` 模块引用改为 `workers.tasks`，以保持代码一致性和模块化管理。 (0b27d7f8)
- :recycle: (ui): SVG 图片处理逻辑重构 (3d7f56e0)
- :recycle: (client): 修改客户端配置机制以支持原地更新 (fccbca66)
- :recycle: (ui): 优化语言按钮宽度设置 (83540409)
- :recycle: (client): 更新本地客户端逻辑以处理文件内容变更 (13ca3ae2)
- :recycle: (ui): 优化缓存机制 (f6e7ddd2)

#### 文档

- :memo: (ui): 优化图书馆和书籍详情页的界面布局与交互 (a425f48b)
- :memo: (docs): 更新 README 中截图路径与描述 (086a76d4)
- :memo: (docs): 更新 README 中截图路径与描述 (3a1303cf)
- :memo: docs(local): WebDAV 同步注释去掉已删除的排版替换 (0c39679c)
- :memo: docs(source): 第三方书源契约文档，注册表 / 基类文档跟上现状 (c095e12b)
- :memo: (docs): 补充 font 字体辅助工具的文档说明 (83b598f3)
- :memo: (docs): 修正 workers 文档中数据库模块引用错误 (1361bcc8)
- :memo: (docs): 修正任务句柄生命周期描述 (e65052ab)

#### 其他

- :wrench: 添加本地 WebDAV 测试服务脚本 (fd3c4323)
- :wrench: (run): --watch 重启整组杀进程防孤儿模拟器，改动静默 5 秒后再重启 (6bd10a2b)
- :wrench: (utils): 修正 debug 开关的设置路径 (8cb9b717)
- :wrench: (menu): 将启动项设置逻辑从 Settings 移至 Menu 模块 (7e209eb6)

#### 变更

- :white_check_mark: (tests): 补齐无 KOReader 环境下缺失的测试桩，修复 CI 9 个失败 (58562c69)
- :bento: (readme): 更新图书馆与书籍详情截图 (e17c31d8)
- :speech_balloon: (moon): 令牌提示改为「个人Token」，服务端已取消 bk_ 设备令牌 (1de47291)
- :hammer: (tools): 模拟器驱动，外部投递 Lua 执行与截图 (6afdede1)
- :children_crossing: (ui): 前台等待统一改为不可取消的进度窗 (e746b751)
- :children_crossing: feat(reflow): 排版与双语对照改用任务进度窗，不可取消并显示进度 (2fce74e5)
- :children_crossing: feat(setting): 排序列表可直接输入第几位 (6f9f6388)
- :children_crossing: feat(setting): 划词菜单单独成页，不再埋在「划词与查询」末尾 (b2891423)
- :coffin: refactor(local): 删除本地源「转换后替换原书」，重新排版改为另存后已无调用方 (eb07d289)
- :white_check_mark: test: 字体选择器测试跟上系统分栏，清零 LuaLS 警告 (3503ed8b)
- :busts_in_silhouette: (kavita): 补记 Kavita 书源共建者 #40 (231d4eec)
- :busts_in_silhouette: (fanqie): 补记番茄数据源共建者 #29 (95eae039)
- :white_check_mark: test: 测试、文案与文档跟上已提交的改动 (b359458b)
- :truck: (features): feature 模板 tpl 改名为 demo，打包时剔除 (b4001279)
- :white_check_mark: (source): 补章节缓存复用测试 (800fd8bb)
- :white_check_mark: (wechat): 跟进微信读书源精简的测试 (ea716554)
- :white_check_mark: (registry): 测试与文档跟进单实例缓存：current 与 resolve 共用实例、换源不关旧实例、源加载失败直接抛出 (49ab8518)
- :white_check_mark: (source): 补 local 源与源基类测试（扫盘索引、init、WebDAV 同步、defer/skipped） (53fbd9ee)
- :fire: (kindle): 移除 Kindle 源相关模块 (72a9c8b8)
- :fire: (db): 删除已废弃的 HTTP 响应缓存模块 (c23fdabe)
- :fire: (plugin): 移除软件翻页动画补丁文件 (e617ff05)
- :fire: (nightmode): 移除自动夜间模式和自动亮度逻辑 (5be4b3e4)
- :fire: (nightmode): 移除自动夜间模式和自动亮度逻辑 (b32be60c)
- :white_check_mark: (tests): 修正测试桩与断言逻辑 (207ac8d1)

- （无提交记录）

### 完整对比

https://github.com/AnkioTomas/moon/compare/v0.1.9...v0.2.0

# v0.1.9 · 2026-09-27

## 月读 v0.1.9

KOReader 插件包：`book.koplugin-v0.1.9.zip`

输入法词库（整库，手动 sideload）：`dictionary.sqlite3 dictionary-wubi.sqlite3 dictionary-cangjie.sqlite3 dictionary-zhuyin.sqlite3`

安装：解压后将 `book.koplugin` 复制到 KOReader 的 `plugins` 目录，然后重启。

词库 sideload：下载对应布局的词库，直接放入 KOReader 数据目录下的
`.moon/`（与 `book.sqlite3` 同级）。附件已使用最终文件名，无需重命名。

### 更新内容

相对上一版本 `v0.1.8`：

#### 新功能

- :sparkles: (ui): 添加设置项并启用桌面图标打开桌面功能 (2a16975)
- :sparkles: (ai): 优化上下文显示逻辑和实体处理 (c5dcbd8)
- :sparkles: (ai): 优化锁屏组件显示逻辑 (10b2fe4)
- :sparkles: (ai): 优化锁屏组件显示逻辑 (fcd5112)
- :sparkles: (ai): 优化 X-Ray 数据获取逻辑，增加首次初始化和章节增量逻辑 (ebf5ff3)

#### 修复

- :bug: (local): fix book scanning crash and retry logic (176336d)
- :bug: (ui): 修复登录流程中的取消逻辑 (9bc4408)
- :bug: (ui): 修复登录流程中的取消逻辑 (e3766ee)
- :bug: (db): 修复文件移动/重命名逻辑 (9d8ea63)

#### 重构

- :recycle: (auth): 重构 auth 模块逻辑以适配 token 与 wlfstk_smdl 的配对校验 (5b4f2cb)

#### 文档

- :memo: (docs): 更新 xray README.md (2e5dd7f)

### 完整对比

https://github.com/AnkioTomas/moon/compare/v0.1.8...v0.1.9
