# v0.2.36 · 2026-10-24

## 月读 v0.2.36

KOReader 插件包：`book.koplugin-v0.2.36.zip`

输入法词库（整库，手动 sideload）：`dictionary.sqlite3 dictionary-wubi.sqlite3 dictionary-cangjie.sqlite3 dictionary-zhuyin.sqlite3`

安装：解压后将 `book.koplugin` 复制到 KOReader 的 `plugins` 目录，然后重启。

拓展书源（可选，需同时安装月读）：`moonsource-kavita.koplugin-v0.2.36.zip`（Kavita）、
`moonsource-bookorbit.koplugin-v0.2.36.zip`（BookOrbit）。解压后同样放进 `plugins` 目录。

词库 sideload：下载对应布局的词库，直接放入 KOReader 数据目录下的
`.moon/`（与 `book.sqlite3` 同级）。附件已使用最终文件名，无需重命名。

### 更新内容

相对上一版本 `v0.2.35`：

#### 新功能

- :sparkles: feat(copymanga): 书城增加题材分类浏览 (24fab61f)
- :sparkles: feat(source): 本地书籍设置可关闭上传本地加架的书到云书架 (d704f91c)
- :sparkles: (init): 启动自检安装完整性，缺文件时提示重新解压而不是报模块找不到 (8c8a8d79)
- :sparkles: feat(update): 已装词库（注音、输入法）有新版本时提醒更新 (75567bb1)
- :sparkles: (zlib): 书城语言栏新增意大利语等八种语言 (0f4b5f25)
- :sparkles: feat(rare): 汉字拼音词库补全字表外冷僻字 (ea686050)
- :sparkles: (lookup): 查词面板支持翻页键 / 音量键翻页，翻到头尾自动换词典 (b6efc926)
- :sparkles: (ui): 外观新增「字体加粗」，界面文字偏灰时可整体加粗 (78687a36)
- :sparkles: (lockscreen): 锁屏壁纸可设为统计页面，指定或每天随机 (a38f55bf)
- :sparkles: (reader): 快捷面板新增「重新下载本章」，只清当前章缓存 (154e9abf)
- :sparkles: (wechat): 跨章注释做成脚注弹窗，找不到的只留文字 (62f594cd)
- :sparkles: (kavita): 注释删除双向收敛 (0ea16b04)
- :sparkles: (book): 注解删除事件与远端删除回流 (5f4b2b59)
- :sparkles: (kavita): 开书把云端注解定位成本地 xpointer (eea5ef57)
- :sparkles: (kavita): 推送按章对账并回填注解 id (d02d706b)
- :sparkles: (kavita): 开书拉取云端注解并全字段落库 (ed45b87b)
- :sparkles: (stats): 漫画云端页数写入统计并参与聚合 (3d17e335)
- :sparkles: (kavita): 注解线上形态与同一性 (3ab92399)

#### 修复

- :bug: (local): 书指向排版版时扫盘不再每次判定需要全量重扫 (5aec5b28)
- :bug: (store): 直接开原书不再把排版版 / 双语版的记忆冲掉 (9ceb9275)
- :bug: (jdread): 未登录逛榜单不再因 uuid 为空报错 (4f7477de)
- :bug: (xiaoxiang): 字体还原直接用 yuewen_fonts，超时 120→600 秒 (e763f6d8)
- :bug: (init): KOReader 版本门禁提前到 main.lua 顶部，旧版不再因缺模块报错 (b61ac25b)
- :bug: (home): 正在阅读卡片在书架顺序变化后回到第一张 (d6235f07)
- :bug: (home): 长按进入编辑模式时停留在同一个组件所在页 (288dd467)
- :bug: (wechat): 阅读时长上报不再因章节目录缓存过期而被丢弃 (e41ef27b)
- :bug: (reader): 章节切换时样式微调与自定义 CSS 跟着全书走 (15c847c2)
- :bug: (qidian): 还原 cES=2 字体层并丢弃诱饵副本 (39917852)
- :bug: (insight): 页面跳转方法避开 LuaJIT 保留字 goto (d2edc628)
- :bug: (kavita): 同键远端注解只画最小 id，空备注落 nil (d2e59f3e)
- :bug: (kavita): pull 保留 pageNumber 供多 spine 定位 (0af258ee)
- :bug: (kavita): 漫画已读页数按最远进度而非页次累加 (3fef4ae8)
- :bug: (kavita): 认领远端注解后不把远端备注写成基线 (dfa42892)

#### 界面

- :lipstick: (panel): 阅读快捷面板头部改为封面 + 书籍信息 + 退出按钮 (70d2406b)

#### 重构

- :recycle: (reflow): 上次读的衍生版记在原书 sidecar，books.path 不再指向排版 / 双语版 (94e4c485)
- :recycle: refactor(copymanga): 书城 chip 压缩为两行 (69c1bf70)
- :recycle: refactor(local): 上传本地书开关只作用于 WebDAV，撤掉云书架通用实现 (d0ecbcdb)
- :recycle: (yuewen_fonts): 起点/QQ阅读字体还原迁到 source/yuewen_fonts 并提升准确度 (21d69793)
- :recycle: (insight): 页面跳转方法 goTo 改名 switchPage，与桌面 switchTab 对齐 (61842c39)
- :recycle: (book): 注解保存参数归位与远端快照幂等 (3c073a10)
- :recycle: (kavita): 收敛评审意见 (0c7f4cf6)

#### 文档

- :memo: (stats): 注释跟上漫画页数的新口径 (fbdb1068)

#### 变更

- :globe_with_meridians: (l10n): 删除已不用的词库更新副标题旧文案 (f38a1002)
- :children_crossing: (lookup): 记住的词典没结果时默认显示有结果的，翻页键跳过无结果词典 (5eb930e6)
- :children_crossing: (kindle): KFX 首次打开转换改为后台任务，不再卡死界面 (0a7d8163)
- :truck: (crypto): 晋江 DES 移到 crypto/des (c90668dc)

### 完整对比

https://github.com/AnkioTomas/moon/compare/v0.2.35...v0.2.36

# v0.2.35 · 2026-10-23

## 月读 v0.2.35

KOReader 插件包：`book.koplugin-v0.2.35.zip`

输入法词库（整库，手动 sideload）：`dictionary.sqlite3 dictionary-wubi.sqlite3 dictionary-cangjie.sqlite3 dictionary-zhuyin.sqlite3`

安装：解压后将 `book.koplugin` 复制到 KOReader 的 `plugins` 目录，然后重启。

拓展书源（可选，需同时安装月读）：`moonsource-kavita.koplugin-v0.2.35.zip`（Kavita）、
`moonsource-bookorbit.koplugin-v0.2.35.zip`（BookOrbit）。解压后同样放进 `plugins` 目录。

词库 sideload：下载对应布局的词库，直接放入 KOReader 数据目录下的
`.moon/`（与 `book.sqlite3` 同级）。附件已使用最终文件名，无需重命名。

### 更新内容

相对上一版本 `v0.2.34`：

#### 修复

- :bug: (wechat): 搜索封面用大图，章首标题页还原原书背景 (293400d1)
- :bug: (insight): 云端阅读会话进入阅读记录，漫画详情不再空白 (cf3d5f54)

#### 重构

- :recycle: (stats): summaryByBooks 去掉多余的判空与类型转换 (58d9f3d9)

#### 变更

- :white_check_mark: (kavita): 补漫画 cbz 进度上报的回归测试 (df28d72b)

### 完整对比

https://github.com/AnkioTomas/moon/compare/v0.2.34...v0.2.35

# v0.2.34 · 2026-10-23

## 月读 v0.2.34

KOReader 插件包：`book.koplugin-v0.2.34.zip`

输入法词库（整库，手动 sideload）：`dictionary.sqlite3 dictionary-wubi.sqlite3 dictionary-cangjie.sqlite3 dictionary-zhuyin.sqlite3`

安装：解压后将 `book.koplugin` 复制到 KOReader 的 `plugins` 目录，然后重启。

拓展书源（可选，需同时安装月读）：`moonsource-kavita.koplugin-v0.2.34.zip`（Kavita）、
`moonsource-bookorbit.koplugin-v0.2.34.zip`（BookOrbit）。解压后同样放进 `plugins` 目录。

词库 sideload：下载对应布局的词库，直接放入 KOReader 数据目录下的
`.moon/`（与 `book.sqlite3` 同级）。附件已使用最终文件名，无需重命名。

### 更新内容

相对上一版本 `v0.2.33`：

#### 新功能

- :sparkles: (qidian): 接入段评 (5ea71abc)
- :sparkles: (jjwxc): 支持账号密码登录 (c5815c72)
- :sparkles: (jjwxc): 接入段评 (dbdf30b4)
- :sparkles: (cookie): 远程授权成功后支持重新授权，长佩人机验证标记登录失效 (901c4a88)

#### 修复

- :bug: (wechat): 划线合并去掉同 range 孪生记录与未确认的本地重复划线 (90c3c69b)

#### 文档

- :memo: (readme): 数据源表重写为能力矩阵，补晋江、起点段评 (02eb0eaf)

### 完整对比

https://github.com/AnkioTomas/moon/compare/v0.2.33...v0.2.34

# v0.2.33 · 2026-10-23

## 月读 v0.2.33

KOReader 插件包：`book.koplugin-v0.2.33.zip`

输入法词库（整库，手动 sideload）：`dictionary.sqlite3 dictionary-wubi.sqlite3 dictionary-cangjie.sqlite3 dictionary-zhuyin.sqlite3`

安装：解压后将 `book.koplugin` 复制到 KOReader 的 `plugins` 目录，然后重启。

拓展书源（可选，需同时安装月读）：`moonsource-kavita.koplugin-v0.2.33.zip`（Kavita）、
`moonsource-bookorbit.koplugin-v0.2.33.zip`（BookOrbit）。解压后同样放进 `plugins` 目录。

词库 sideload：下载对应布局的词库，直接放入 KOReader 数据目录下的
`.moon/`（与 `book.sqlite3` 同级）。附件已使用最终文件名，无需重命名。

### 更新内容

相对上一版本 `v0.2.32`：

#### 新功能

- :sparkles: (subscribe): 订阅列表支持按分组筛选 (c60780bd)
- :sparkles: (reader): 按章阅读的全书页码估算，缺字数的章用平均值，读过的章回填字数 (720af3d9)
- :sparkles: (desktop): 读书退出回桌面时还原页签与书架浏览位置 (8a14c8e5)

#### 修复

- :bug: (storage): 存储空间页改用与顶栏相同的 df，旧版 KOReader 可用空间不再为空 (6dad9da7)
- :bug: (bars): 阅读栏剩余运存改用 util.calcFreeMem，与桌面顶栏同源 (9d97b912)

#### 性能

- :zap: (cache): http 缓存限制 500 行，评论缓存写入时清过期 (b010acbc)

#### 变更

- :lock: (net): 订阅图片与公众号文章改流式下载并限制体积，公开抓取再校验解析后的 IP (cd978354)

### 完整对比

https://github.com/AnkioTomas/moon/compare/v0.2.32...v0.2.33

# v0.2.32 · 2026-10-22

## 月读 v0.2.32

KOReader 插件包：`book.koplugin-v0.2.32.zip`

输入法词库（整库，手动 sideload）：`dictionary.sqlite3 dictionary-wubi.sqlite3 dictionary-cangjie.sqlite3 dictionary-zhuyin.sqlite3`

安装：解压后将 `book.koplugin` 复制到 KOReader 的 `plugins` 目录，然后重启。

拓展书源（可选，需同时安装月读）：`moonsource-kavita.koplugin-v0.2.32.zip`（Kavita）、
`moonsource-bookorbit.koplugin-v0.2.32.zip`（BookOrbit）。解压后同样放进 `plugins` 目录。

词库 sideload：下载对应布局的词库，直接放入 KOReader 数据目录下的
`.moon/`（与 `book.sqlite3` 同级）。附件已使用最终文件名，无需重命名。

### 更新内容

相对上一版本 `v0.2.31`：

#### 修复

- :bug: (legado): 正文夹带 <img> 时保留图片、丢弃 svg 占位，不再显示标签原文 (ad2a0950)
- :bug: (wechat): 脚注链接带原文件名时改写成本章锚点，修复「无效或外部链接」 (49cb618a)

### 完整对比

https://github.com/AnkioTomas/moon/compare/v0.2.31...v0.2.32
