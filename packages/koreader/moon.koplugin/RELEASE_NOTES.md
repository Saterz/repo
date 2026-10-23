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

# v0.2.31 · 2026-10-22

## 月读 v0.2.31

KOReader 插件包：`book.koplugin-v0.2.31.zip`

输入法词库（整库，手动 sideload）：`dictionary.sqlite3 dictionary-wubi.sqlite3 dictionary-cangjie.sqlite3 dictionary-zhuyin.sqlite3`

安装：解压后将 `book.koplugin` 复制到 KOReader 的 `plugins` 目录，然后重启。

拓展书源（可选，需同时安装月读）：`moonsource-kavita.koplugin-v0.2.31.zip`（Kavita）、
`moonsource-bookorbit.koplugin-v0.2.31.zip`（BookOrbit）。解压后同样放进 `plugins` 目录。

词库 sideload：下载对应布局的词库，直接放入 KOReader 数据目录下的
`.moon/`（与 `book.sqlite3` 同级）。附件已使用最终文件名，无需重命名。

### 更新内容

相对上一版本 `v0.2.30`：

#### 修复

- :bug: (xray): 模型漏掉 aliases 时不再抛错，修复「分析全书」弹出月读出错页 (97b7b105)

### 完整对比

https://github.com/AnkioTomas/moon/compare/v0.2.30...v0.2.31

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
