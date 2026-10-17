# v0.2.11 · 2026-10-17

## 月读 v0.2.11

KOReader 插件包：`book.koplugin-v0.2.11.zip`

输入法词库（整库，手动 sideload）：`dictionary.sqlite3 dictionary-wubi.sqlite3 dictionary-cangjie.sqlite3 dictionary-zhuyin.sqlite3`

安装：解压后将 `book.koplugin` 复制到 KOReader 的 `plugins` 目录，然后重启。

拓展书源（可选，需同时安装月读）：`moonsource-kavita.koplugin-v0.2.11.zip`（Kavita）、
`moonsource-bookorbit.koplugin-v0.2.11.zip`（BookOrbit）。解压后同样放进 `plugins` 目录。

词库 sideload：下载对应布局的词库，直接放入 KOReader 数据目录下的
`.moon/`（与 `book.sqlite3` 同级）。附件已使用最终文件名，无需重命名。

### 更新内容

相对上一版本 `v0.2.10`：

#### 新功能

- :sparkles: (qqreader): 接入 QQ阅读，扫码登录与章节进度 (6454f1f0)
- :sparkles: (source): 起点和七猫同步章节进度 (c7229a57)
- :sparkles: (bars): 阅读页顶栏、底栏可选分割线 (073492eb)
- :sparkles: (qidian): 接入起点中文网，书架同步与 Cookie 登录 (033be26e)
- :sparkles: (jjwxc): 接入晋江文学城书源，收藏同步与 Cookie 登录 (def24014)
- :sparkles: (cookie): 加入京东浏览器授权并精简远程导航 (45e65238)
- :sparkles: (qimao): 接入七猫书源与浏览器授权登录 (d600440f)
- :sparkles: (wechat): 书架分类优先用自建分组名，没分组回退官方分类 (5139ff10)
- :sparkles: (dictionary): 新增「加载所有词典」，查词面板列出全部已安装词典 (33ff58be)
- :sparkles: (subscribe): 新增「网页本身」订阅与列表排序，修标题栏加图标后溢出 (9d559c99)
- :sparkles: (sidebar): 侧栏页面支持自定义排序 (940048ab)
- :sparkles: (remote): 新增「截图分享后自动删除」开关，默认关闭 (e2c11791)
- :sparkles: feat(ime): 候选条浅灰底并加粗首选词，新增九宫格拼音 (69b5610e)
- :sparkles: feat(remote): 备份改为整个 .moon 打包（不含日志缓存），入口移到首页 (6726fab4)
- :sparkles: feat(remote): 配置备份包含全部配置（登录态、Cookie、密钥、锁屏密码） (0cd0f0bb)

#### 修复

- :bug: (qimao): 章节正文加章名并去掉段首空白，避免双份缩进 (1758fdc0)
- :bug: (wechat): 公众号请求带上 ticket/wrpa 凭据头，-2041 与验证页先续期再重试 (257d31db)
- :bug: (subscribe): 订阅与网页正文按声明编码转 UTF-8，GBK 站点不再乱码 (63d63801)
- :bug: (rare): 子进程取框的时间预算放宽，首次翻到的页不再漏注音 (0363b7f2)
- :bug: (dictionary): 划词点「查词」固定打开词典栏，不再沿用上次的标签 (83cf1184)
- :bug: (lookup): 修复「加入生词本」按钮不显示 (bb552fca)
- :bug: fix(ime): 开关开着但键盘布局列表被重置时，启动补回 zh_CN，地球键才能切中文 (72388844)
- :bug: fix(remote): addPath 正常结束返回假，备份/打包误判失败 (b2ab4cd5)
- :bug: fix(remote): 备份按钮处理代码误嵌在 renderForms 内，移到文件末尾 (f332aba8)
- :bug: fix(remote): 备份下载增加进度反馈，设置页卡片间距 (8ef02c6f)
- :bug: fix(panel): 快捷面板页脚时间/电量在面板分支不刷新 (6bcd863e)

#### 界面

- :lipstick: feat(remote): 备份下载/恢复改用进度弹窗，可取消 (b8ff865b)

#### 性能

- :zap: (reviews): 关联书段评扫页改子进程，翻页不再同步 findText (bc11cb1d)
- :zap: (rare): 生僻字注音改子进程取框，翻页不再卡顿 (40af53e2)

#### 重构

- :recycle: (ai): 分批处理扫描结果以避免内存溢出 #47 (104c3ee1)

#### 文档

- :memo: (docs): README 补充游戏合集 ko-games 与订阅类型 (1e1ae70e)
- :memo: docs: README 增加 LINUX DO 社区链接 (9dbc382f)

#### 变更

- :white_check_mark: (source): 示例源断言不再写死内置源个数 (19b539fc)
- :fire: (remote): 文件管理不再限制在快捷入口内 (63caead6)
- :children_crossing: feat(rare): 选择「全部」注音范围时提示可能拖慢翻页 (af051170)

### 完整对比

https://github.com/AnkioTomas/moon/compare/v0.2.10...v0.2.11

# v0.2.10 · 2026-10-17

## 月读 v0.2.10

KOReader 插件包：`book.koplugin-v0.2.10.zip`

输入法词库（整库，手动 sideload）：`dictionary.sqlite3 dictionary-wubi.sqlite3 dictionary-cangjie.sqlite3 dictionary-zhuyin.sqlite3`

安装：解压后将 `book.koplugin` 复制到 KOReader 的 `plugins` 目录，然后重启。

拓展书源（可选，需同时安装月读）：`moonsource-kavita.koplugin-v0.2.10.zip`（Kavita）、
`moonsource-bookorbit.koplugin-v0.2.10.zip`（BookOrbit）。解压后同样放进 `plugins` 目录。

词库 sideload：下载对应布局的词库，直接放入 KOReader 数据目录下的
`.moon/`（与 `book.sqlite3` 同级）。附件已使用最终文件名，无需重命名。

### 更新内容

相对上一版本 `v0.2.9`：

#### 新功能

- :sparkles: feat(lookup): 统一查词窗口支持加入原生生词本 (48f43268)
- :sparkles: feat(subscribe): 新增订阅功能，支持 RSS/Atom、网页与微信公众号 (9d013250)
- :sparkles: feat(wechat): 公众号文章图落地，公众号不再进书库并清理旧数据 (a1081a09)
- :sparkles: feat(reader): 支持只读不记的 ephemeral 源与隐藏源注册，补章号重排和 emoji 清理 (32520437)

#### 修复

- :bug: fix(subscribe): 图片跳转不得落到内网，ephemeral 收成身份字段并清理吞错与重复 (71bd52d3)

#### 文档

- :memo: (readme): 新增游戏板块（小黑屋、阿页的阁楼） (8a23676d)
- :memo: docs: README 补充订阅功能与相关说明 (d7c0fcaa)

#### 变更

- :fire: chore: 删除误提交的 ocr-integration.diff (8224d061)
- :fire: refactor(rare): 去掉点击注音弹出查词窗口 (48ef475e)
- :globe_with_meridians: chore(l10n): 补订阅功能的繁体与英文翻译 (8b4aa507)
- feat(remote): 远程管理支持功能扩展页面与路由 (176898a1)
- fix(wechat): 优化微信读书认证续期与重试 (1bfd9179)
- fix(translate): 修复翻译与JSON中emoji代理对乱码 (b1ec8ad0)
- feat(rare): 生僻字注音改进：词库补繁体、生字本注音、快捷面板开关 (345a6900)
- refactor(features): 核心经通用扩展点接入 feature，移除端口表与核心直连 (86cf3317)
- fix(cover): 本地 mobi 按 EXTH 封面记录兜底取封面 (d7b0e0da)
- feat(sidebar): 阅读侧栏新增统计页 (47b154c6)
- feat(desktop): 支持反转实体翻页键 (ac64c739)
- fix(ui): 弹窗遮罩仅受全局设置控制 (d0b0869a)
- feat(reader): 默认关闭书籍内嵌字体 (5bd4fa11)
- feat(lockscreen): 锁屏支持透明背景图片 (c238fa42)
- feat(reader): 阅读面板支持保存为默认配置 (c55ed798)
- feat(translate): 章节书源支持双语对照 (3ddf194f)
- style(ai): 「AI token 上限」副标题改为「X-Ray 查询，AI 解释最大上限」 (aa42c644)
- feat(ai): AI 接口新增可配置的「AI token 上限」（步进器，默认 4000） (9502a50a)
- chore: 本地笔记加入 gitignore（.scratch/ 设计文档、GLOSSARY.md 术语表） (10b302b5)
- docs: README 更新阅读统计口径（合并开关按天/按时段、云端按本机时区换算、时段含云端） (bd5bcab8)
- feat(kavita): 云端按 UTC 时刻在本机时区分日/分时，阅读时段含云端时段桶 (005057ff)
- fix(kavita): 撤回物化变更信号的核心透传，回到核心零改动 (f358718b)
- docs: README 补充 Kavita 统计能力与多设备合并说明（P4） (0e9a11d8)
- refactor(kavita): 收紧 stats 头注并删除未用导出（P5） (9601778e)
- fix(kavita): 日桶替换窗口上界改到最后观测日日终（P6） (e753a41c)
- fix(kavita): 物化写入计入统计变更信号（P2） (ce11bccf)
- fix(kavita): 统计确认推送改 defer，返回可取消句柄（P3） (ee6e3f6e)
- fix(kavita): 卷物化标题改用持久化卷名，兜底标题不覆盖既有行（P1） (6bac00b4)
- test(kavita): 对账验收：全量 fixture 走拉取 → 入库 → 展示口径（151 断言） (db48cd95)
- feat(kavita): 缺行卷物化：云端读过的卷补隐藏身份行 (0eb838a7)
- fix(local): 优先使用 KOReader 中用户设置的自定义封面 (f100d84d)
- feat(kavita): 源统计钩子：能力申报 + 本地确认推送 + 分页拉全量 (a42aa91d)
- feat(kavita): 阅读统计纯核心：历史条目 → 单书 / 账户行与替换指令 (bc1fee23)
- feat(l10n): 「多设备统计合并」文案入 en / zh_TW 目录 (3e1ea48f)
- feat(kavita): 扩展设置页新增「多设备统计合并」开关 (87544792)
- feat(auth): 登录过期时自动重登或提示重新登录 (d9d83871)
- fix(wechat): 章节返回空响应时指数退避重试，修复部分章节缺失 (50c788e2)
- fix(remote): 日志发送完成后再删除压缩包，修复下载为 0KB (47a563db)
- fix(library): 最近阅读不再重复列出换身份重新上架的书 (e592d4f4)
- fix(remote): 日志打包 zip 条目权限改为 0644，修复解压后文件不可读 (2c52233f)
- fix(home): 书架小组件「更多 ›」靠右对齐 (b3554985)
- docs(readme): 补充扩展功能挂点说明 (2810bf2d)
- feat(extension): 第三方插件可扩展设置页、快捷面板、顶栏、数据事件与阅读器就绪钩子 (21a1b9bc)
- fix(selection): 防止滑动选词时事件循环导致栈溢出 (da84976a)

### 完整对比

https://github.com/AnkioTomas/moon/compare/v0.2.9...v0.2.10

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
