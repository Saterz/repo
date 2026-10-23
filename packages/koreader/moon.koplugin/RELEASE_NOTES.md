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
