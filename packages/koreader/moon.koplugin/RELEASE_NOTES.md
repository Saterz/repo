# v0.2.9 · 2026-10-16

## 月读 v0.2.9

KOReader 插件包：`book.koplugin-v0.2.9.zip`

输入法词库（整库，手动 sideload）：`dictionary.sqlite3 dictionary-wubi.sqlite3 dictionary-cangjie.sqlite3 dictionary-zhuyin.sqlite3`

安装：解压后将 `book.koplugin` 复制到 KOReader 的 `plugins` 目录，然后重启。

拓展书源（可选，需同时安装月读）：`moonsource-kavita.koplugin-v0.2.9.zip`（Kavita）、
`moonsource-bookorbit.koplugin-v0.2.9.zip`（BookOrbit）。解压后同样放进 `plugins` 目录。

词库 sideload：下载对应布局的词库，直接放入 KOReader 数据目录下的
`.moon/`（与 `book.sqlite3` 同级）。附件已使用最终文件名，无需重命名。

### 更新内容

相对上一版本 `v0.2.8`：

#### 变更

- docs(readme): 补充扩展开发说明 (a0af48a3)
- feat(extension): 插件自行声明能力并支持注入首页组件 (b7c1f518)
- feat(library): 工具栏增加随机一本 (62cf0d75)
- feat(home): 新增随机一本与书架组件 (84fdd08b)
- feat(library): 最近阅读排序列出整个书架并使用云端阅读时间 (6995b206)
- fix(bluetooth): 顶栏蓝牙设备名最多显示 4 个字 (c8a8c960)
- docs: 删除开发文档，要点移入源码注释并更新 README (dd6493c9)

### 完整对比

https://github.com/AnkioTomas/moon/compare/v0.2.8...v0.2.9

# v0.2.8 · 2026-10-16

## 月读 v0.2.8

KOReader 插件包：`book.koplugin-v0.2.8.zip`

输入法词库（整库，手动 sideload）：`dictionary.sqlite3 dictionary-wubi.sqlite3 dictionary-cangjie.sqlite3 dictionary-zhuyin.sqlite3`

安装：解压后将 `book.koplugin` 复制到 KOReader 的 `plugins` 目录，然后重启。

拓展书源（可选，需同时安装月读）：`moonsource-kavita.koplugin-v0.2.8.zip`（Kavita）、
`moonsource-bookorbit.koplugin-v0.2.8.zip`（BookOrbit）。解压后同样放进 `plugins` 目录。

词库 sideload：下载对应布局的词库，直接放入 KOReader 数据目录下的
`.moon/`（与 `book.sqlite3` 同级）。附件已使用最终文件名，无需重命名。

### 更新内容

相对上一版本 `v0.2.7`：

#### 变更

- test(remote): 备份用例打桩 dump，兼容无 KOReader 的 CI (f8328a81)
- feat(remote): 远程管理支持配置备份与恢复 (bd501f19)
- fix(library): 删书后同步书架数量异常 (2923dad3)
- fix(progress): 无章节的已读进度按末章上报，推不上的行标记丢弃且不中断整次同步 (11f8ea22)
- perf(ui): 书籍文件复制改为分块流式 (4105ef64)
- refactor(ui): 封面格打开动作由页面注入，字体排版偏好移回面板层 (c4d99039)
- fix(settings): 补齐功能设置项登记并加校验用例 (33daeb2f)
- refactor(utils): 事件监听由 main 注入，utils 不再反向依赖 features (4603aa35)
- fix(xray): 释放标记缓存 (ae9733ef)
- fix(features): 词典与输入法下载出错时关闭文件句柄 (4f4ae293)
- fix(book): 分页文档划线按坐标内容去重 (a44b0c41)
- fix(jdread): 详情缺 ebook_id 时不写入缓存 (16f3911e)
- fix(copymanga): 收藏接口使用重登后的最新 token (efab2358)
- fix(wechat): 取消后不再回调并加快划线定位 (3e1bf8dd)
- perf(fanqie): Cookie 未变化时不重复写设置 (cc73a46d)
- fix(registry): 第三方源 new() 出错时记日志并跳过 (00087908)
- fix(source): 回调同步触发时不再用旧句柄覆盖在途请求 (5344ac04)
- fix(chapter): 没有书籍记录时准备框不再崩溃 (c64c905a)
- fix(local): 解析元数据出错时也关闭文档 (d59ea7ce)
- fix(fanqie): 19 位设备 id 按 uint64 精确编码 (eaf34522)
- perf(sync): 判断笔记待上传只查存在性不读整份快照 (48811301)
- fix(reader): 标记已读失败时同一会话不再每次翻页重试 (b6723050)
- fix(remote): 停服释放静态资源缓存并补路径越界用例 (530b5b40)
- fix(wechat): 段评跳过已删除条目与缺作者数据 (6b913dbb)
- fix(webdav): 兼容默认命名空间的目录列表 (761dba64)
- fix(http): 镜像同步失败换源时取消正在进行的请求 (0cf1e236)
- test(runner): 补齐沙盒并接入模拟器 sqlite，新增扫码登录与想法推送用例 (d784676e)
- fix(http): Android 上 turbo 响应头查找缺少 strncasecmp 导致崩溃 (53c682e1)
- fix(remote): 日志打包脱敏避免长串超时导致空包 (ed365573)
- fix(baike): 百科查询改用四合一查词窗口 (d2f71bcb)
- fix(rare): 点击普通文字不再弹出生僻字窗口 (9d285f89)
- fix(local): azw3 书籍扫描取不到封面 (97968a17)
- feat(topbar): 蓝牙图标移到 Wi-Fi 旁边 (eca377cc)

### 完整对比

https://github.com/AnkioTomas/moon/compare/v0.2.7...v0.2.8

# v0.2.7 · 2026-10-15

## 月读 v0.2.7

KOReader 插件包：`book.koplugin-v0.2.7.zip`

输入法词库（整库，手动 sideload）：`dictionary.sqlite3 dictionary-wubi.sqlite3 dictionary-cangjie.sqlite3 dictionary-zhuyin.sqlite3`

安装：解压后将 `book.koplugin` 复制到 KOReader 的 `plugins` 目录，然后重启。

拓展书源（可选，需同时安装月读）：`moonsource-kavita.koplugin-v0.2.7.zip`（Kavita）、
`moonsource-bookorbit.koplugin-v0.2.7.zip`（BookOrbit）。解压后同样放进 `plugins` 目录。

词库 sideload：下载对应布局的词库，直接放入 KOReader 数据目录下的
`.moon/`（与 `book.sqlite3` 同级）。附件已使用最终文件名，无需重命名。

### 更新内容

相对上一版本 `v0.2.6`：

#### 变更

- fix(wechat): 进度上传使用阅读会话并补全想法分页 (cde009e4)
- fix(jdread): 修正登录跳转地址并提示京东安全验证 (1b86caa7)
- fix(home): 添加组件列表支持分页 (3fa396e1)
- feat(reviews): 导入书和京东读书关联正版段评 (1bfc5fef)
- perf(http): assets 下载支持多镜像自动切换，优先上次成功的源 (274fbb04)
- perf(lockscreen): 缓存 logo 解码结果，颗粒纹理直接读写像素 (7069bef5)
- perf(fonts): 按字体路径解析，只读取所选字体信息，不再扫描整个字体目录 (c6512bbd)
- docs(readme): 更新查词窗口、生僻字注音、文字海报与单向历说明及截图 (42c8dd11)
- fix(lockscreen): 选择海报字体时不再提前重新生成 (5065bfab)

### 完整对比

https://github.com/AnkioTomas/moon/compare/v0.2.6...v0.2.7

# v0.2.6 · 2026-10-15

## 月读 v0.2.6

KOReader 插件包：`book.koplugin-v0.2.6.zip`

输入法词库（整库，手动 sideload）：`dictionary.sqlite3 dictionary-wubi.sqlite3 dictionary-cangjie.sqlite3 dictionary-zhuyin.sqlite3`

安装：解压后将 `book.koplugin` 复制到 KOReader 的 `plugins` 目录，然后重启。

拓展书源（可选，需同时安装月读）：`moonsource-kavita.koplugin-v0.2.6.zip`（Kavita）、
`moonsource-bookorbit.koplugin-v0.2.6.zip`（BookOrbit）。解压后同样放进 `plugins` 目录。

词库 sideload：下载对应布局的词库，直接放入 KOReader 数据目录下的
`.moon/`（与 `book.sqlite3` 同级）。附件已使用最终文件名，无需重命名。

### 更新内容

相对上一版本 `v0.2.5`：

#### 变更

- perf(lockscreen): 词表改为数值存储并在排版后释放，挑句按划线变更戳缓存 (d99161c3)
- feat(lockscreen): 新增单向历锁屏背景，本地绘制日历页，农历干支节气读摸鱼日报缓存 (6f047979)
- feat(lockscreen): 新增文字海报锁屏背景，分词挑关键词排版，支持多种版式与海报字体选择 (d04f612b)
- feat(myrl): 解析日期、干支、生肖、节气、节日字段，兼容 almanac 新结构 (445adbac)
- fix(rare): 注音全屏统一字号，点注音或被注音字打开查词窗口，英文词库补常用词档位 (2998941e)
- feat(lookup): 统一查词窗口，底部 词典/翻译/AI/百科 标签切换，词典可手动切换并渲染 HTML 词条，移除旧翻译弹窗 (9af1f1e8)
- feat(xray): 全书文本提取与「按当前位置更新」改为后台任务，共用任务键，查词可取消 (0be948dc)
- fix(wechat): 「注」图标固定为 0.8 字高并上标对齐，样式表缺失时不再显示成大方块 (2240121d)
- chore(reviews): 段评匹配失败时记录诊断日志（多处命中、引擎未找到、用字不一致） (3768edd3)
- fix(local): 扫描跳过无权限目录只写日志并保留其中的书，有跳过时中止 WebDAV 同步；不再跟随软链接，提交阶段失败注明步骤 (4e70de08)
- fix(exit): 退出流程开始后不再弹出新窗口，修复退出后错误页残留导致 KOReader 卡死 (4b7db044)
- feat(rare): 生僻字注音，页面图层在生僻字上方画拼音/音标；词库复用输入法在线下载（assets/rare 经 jsdelivr），中文仅收通用规范汉字表 8105 字，英文整词匹配 (3e84f38b)
- feat(reflow/translate): 全书翻译与重新排版改为后台任务，可取消、可放后台；重新排版去掉预览确认，分析到生成全程后台运行 (4a50cc0d)
- fix(fonts): 在线字体下载校验完整性与 zip 格式，按写出大小判定解压成功并记录失败原因 (d70e5225)
- fix(remote): 修复手机端「更多」按钮触摸区域铺满列表，导致点哪都弹菜单且列表无法滚动 (5766989e)
- docs: 更新 README 与远程管理截图 (b72e830e)
- fix(fonts): 本地字体列表跳过粗体/斜体文件，修复选择后不生效 (554d9852)
- fix(home): 首页组件只有一页时隐藏翻页箭头，编辑模式下保留 (944cda2b)

### 完整对比

https://github.com/AnkioTomas/moon/compare/v0.2.5...v0.2.6

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
