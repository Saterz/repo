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

# v0.4.0 · 2026-10-29

## 月读 v0.4.0

KOReader 插件包：`book.koplugin-v0.4.0.zip`

输入法词库（整库，手动 sideload）：`dictionary.sqlite3 dictionary-wubi.sqlite3 dictionary-cangjie.sqlite3 dictionary-zhuyin.sqlite3`

安装：解压后将 `book.koplugin` 复制到 KOReader 的 `plugins` 目录，然后重启。

拓展书源（可选，需同时安装月读）：`moonsource-kavita.koplugin-v0.4.0.zip`（Kavita）、
`moonsource-bookorbit.koplugin-v0.4.0.zip`（BookOrbit）。解压后同样放进 `plugins` 目录。

词库 sideload：下载对应布局的词库，直接放入 KOReader 数据目录下的
`.moon/`（与 `book.sqlite3` 同级）。附件已使用最终文件名，无需重命名。

### 更新内容

相对上一版本 `v0.3.4`：

#### 新功能

- :sparkles: feat(webdav): books.sync 带版本谱系，只认比记录新的书目删本地文件 (b757995d)
- :sparkles: (local): 本地书可同步到 Google Drive (a230db19)
- :sparkles: (ime): 新增速成输入法，仓颉词库按字频重建 (072bd217)
- :sparkles: (kavita): 漫画离线缓存、卷列表与缓存清理（kamare v0.10.2） (5c97adfb)
- :sparkles: (lookup): 查词面板开放扩展 Tab 与操作按钮 (dee09aec)
- :sparkles: (reader): 阅读完成面板增加软删除 (851cec83)
- :sparkles: (remote): 下载日志附带脱敏诊断快照 (5b50b63d)
- :sparkles: (azw3): 支持 HUFF/CDIC 压缩，努力的意义等书可打开 (f3bd06da)

#### 修复

- :bug: fix(reader): 开书时修掉 KOReader 归档开关开着却没目录的坏状态，关书不再必炸 (1dc435e9)
- :bug: fix(prefs): 「保存为默认」只替换各书快照的排版，保留书自己的 doc (239cba36)
- :bug: fix(shelf): 远端源强制刷新不再把空书架当下架依据 (d054c53d)
- :bug: fix(desktop): 阅读中打开桌面改走 reader_exit 异步关书 (ff531626)
- :bug: fix(http): 网络层五处行为缺陷（审计批 2b） (46eac4b5)
- :bug: fix: 本地优先与持久化的八处行为缺陷（审计批 2a） (1c4e2b24)
- :bug: fix(remote): 一条畸形请求不再关停服务；恢复备份落位失败可回滚；/api/zip 发完才删 (cd7c4de9)
- :bug: fix(source): 推脏行只算源能推的域，删掉 jjwxc 的假进度桩 (a02a239b)
- :bug: fix(source): 五处异步句柄丢失，取消后回调照常落库 / 开文档 (4d6dd642)
- :bug: fix(http): 续传撞 416 时显式删掉 .part (13260469)
- :bug: fix(reflow): 提取文字写盘失败要报错，不交出半本书 (a98e224c)
- :bug: fix(local): Google Drive 同步锁键拼 nil、取消句柄被令牌句柄盖掉 (0e8c86a6)
- :bug: (bars): 页眉子项全关导致高度为零时补开时钟占位 (de456e0b)
- :bug: (bookorbit): 简介剥掉 HTML，详情页显示文件路径 (83efbef3)
- :bug: (xray): 全书分析按临时文件分段，修复进度假死 (43f633c1)
- :bug: (wechat): 章内字符比不再写入页比例字段，避免进度乱跳 (b7242c1b)
- :bug: (animation): Kobo 彩屏翻页动画分条不对齐，消除 CFA 竖缝 (#74) (460f1a49)
- :bug: (http): 自建非阻塞 DNS 解析，DNS 不通时阅读页不再卡死 (3252d29c)
- :bug: (rotation): 桌面和弹窗把陀螺仪方向交给宿主转屏 (dc469579)
- :bug: (bars): 顶栏已开但页眉高度为零时强制重发状态栏事件重排 (1daa5d97)
- :bug: (wechat): 书架同步不再因 bookCount 对不上整次失败 (9411e622)
- :bug: (qimao): 书城浏览节点按四段解析，不再拼崩 cat2 (1698c67d)
- :bug: (jjwxc): 网页VIP正文拼回CSS段缝，不再整段缺字 (d23134d4)
- :bug: (bars): 底栏长按只吞栏内，正文最后一行恢复选字 (d8dd9f80)
- :bug: (wechat): 划线定位复用章节原文缓存，不再每条重拉整章 (a2a5de07)
- :bug: (bars): 滚动模式同样绘制顶栏，不再只限分页模式 (86dae006)

#### 界面

- :art: style: 裸 `_` 改成带 `_` 前缀的具名变量（14 处） (a3efff28)

#### 性能

- :zap: perf(utils): Text.base64Decode 改算术解码，三条 base64 路收成一条 (32376548)

#### 重构

- :recycle: refactor(catalog): random 并进分页 SELECT；洞察页日桶只扫一遍 (7a8a37f2)
- :recycle: refactor: 去掉 pcall 后静默回退的三处 (58b89367)
- :recycle: refactor: 业务内部不再用 Guard / pcall 兜底 coverRequest 与 ensure (4014515c)
- :recycle: refactor(workers): job 回调经 ui/guard 隔离，调用方不再自己 pcall (dad20901)
- :recycle: refactor(remote): logs_zip 刷日志不再 pcall (08bdf9c2)
- :recycle: refactor: 删掉为测试桩写的生产分支 (a174984d)
- :recycle: refactor(book): 书库 / 详情页不再用 pcall 包自家源调用 (535882d8)
- :recycle: refactor(ui): 单选设置行收成 Row.choice (b89a0637)
- :recycle: refactor(utils): UTF-8 逐字 pattern 收成 Text.UTF8_CHAR / Text.chars (92b997a5)
- :recycle: refactor(utils): libz inflate 三份 FFI 副本收成 utils/inflate.stream (d57a9969)
- :recycle: refactor(source): Cookie 登录设置页六份手抄收成 source/cookie_login (d934c455)
- :recycle: refactor(source): 阅文 Fock 三份 wasm 宿主收成 source/yuewen_fock (8dfa797d)
- :recycle: refactor(source): 删书「未登录撕墓碑」收进基类，删 7 份覆盖与 8 组空同步覆盖 (210983fe)
- :recycle: refactor(audit): 第二批 2c：缓存与进程边界 (8466d198)
- :recycle: (bars): 删掉页眉占位的多余包装，开时钟后只发一次事件 (0b8cdee2)
- :recycle: (bars): 页眉高度为零并进 setSystemTop 早退，去掉 forceTopHeader 与诊断日志 (845acd04)

#### 文档

- :memo: docs: v0.2.0→HEAD 代码审计报告 (6c641276)

#### 变更

- :white_check_mark: test(azw3): HUFF 夹具按二进制入库，CI 检出不再丢 CRLF (2fa44803)
- :fire: feat(local): 删掉 Google Drive 网盘后端 (6c39f57f)
- :lock: feat(remote): 浏览器首次访问须在设备上授权 (ef80cbb8)
- :fire: chore(copymanga): 删 PERIODS / AUDIENCES 的重复声明 (c6138d0b)
- :fire: refactor: 删掉契约已保证的防御代码 (9e8c308c)
- :fire: refactor(features): 删 Features.try/wrap/prefix/external 四个别名 (2b0344da)
- :fire: refactor: 删除零调用的死函数、纯转发与别名令牌 (97057cf3)
- :fire: refactor(crypto): 删掉自带 md5 / sha1 / sha256，统一用 KOReader ffi/sha2 (52d3bfba)
- :green_heart: test: 修复 HEAD 四个红测试并清零 LuaLS 警告 (a2448407)
- :globe_with_meridians: (l10n): 补全书正文和路径的译文 (3904d049)
- :mag: (bars): 开书落一行顶栏诊断日志，定位个别设备顶栏不显示 (01323d11)

### 完整对比

https://github.com/AnkioTomas/moon/compare/v0.3.4...v0.4.0
