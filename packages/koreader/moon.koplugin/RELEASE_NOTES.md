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

# v0.2.25 · 2026-10-20

## 月读 v0.2.25

KOReader 插件包：`book.koplugin-v0.2.25.zip`

输入法词库（整库，手动 sideload）：`dictionary.sqlite3 dictionary-wubi.sqlite3 dictionary-cangjie.sqlite3 dictionary-zhuyin.sqlite3`

安装：解压后将 `book.koplugin` 复制到 KOReader 的 `plugins` 目录，然后重启。

拓展书源（可选，需同时安装月读）：`moonsource-kavita.koplugin-v0.2.25.zip`（Kavita）、
`moonsource-bookorbit.koplugin-v0.2.25.zip`（BookOrbit）。解压后同样放进 `plugins` 目录。

词库 sideload：下载对应布局的词库，直接放入 KOReader 数据目录下的
`.moon/`（与 `book.sqlite3` 同级）。附件已使用最终文件名，无需重命名。

### 更新内容

相对上一版本 `v0.2.24`：

#### 新功能

- :sparkles: (xray): 识别档位改为节约 / 标准 / 高质量 (2ccefe92)
- :sparkles: (xray): 新增「省 token」开关 (876b8ee6)
- :sparkles: (panel): 桌面快捷面板的亮度、冷暖色调滑块可在设置里单独关闭 (f644acd2)
- :sparkles: (store): 京东读书接入榜单与分类浏览 (d5bc221c)
- :sparkles: (store): 番茄接入阅读榜/新书榜与分类浏览 (12b23cd6)
- :sparkles: (store): iRead 发现入口、Z站排序/语言/格式接入书城浏览 (7334c113)
- :sparkles: (store): 七猫书城接入频道/分类/排序浏览 (11f0a76c)
- :sparkles: (store): 起点、QQ阅读、晋江、拷贝漫画接入榜单/分类浏览 (eec37b0f)
- :sparkles: (store): 书城支持按榜单/分类浏览，微信读书率先接入 (709cb0f8)
- :sparkles: (fanqie): 段评里的配图显示为缩略图，HEIC 图改用 webp 地址 (419aa756)
- :sparkles: (fanqie): 章节正文里的插图下载到本地后再显示 (5efc96e1)

#### 修复

- :bug: (subscribe): 纯图摘要的订阅条目直接当正文，不再抓原文页 (182f2ad3)
- :bug: (online): ensureImage 成功时不再误报 image 错误 (35a80ea8)
- :bug: (store): 加载态没有 chip 时不再多画一空行，修复整页上移/溢出 (b075a53f)
- :bug: (store): chip 折叠改为保留前几项加「更多」，选中项不再丢失 (e588a911)
- :bug: (http): 适配 turbo 2.1.5 流式回调，修复 download incomplete: 0/N (f072ac44)
- :bug: (store): 修复拷贝漫画榜单周期参数，京东读书补搜索使其出现在书城来源里 (f61fc948)
- :bug: (http): 修复响应体随头部到达时流式读取丢数据（download incomplete: 0/N） (98849067)
- :bug: (wechat): TXT 书段首缩进统一，不再出现首段 2 字符其余 4 字符 (95047201)

#### 界面

- :lipstick: (store): 书城 chip 区靠左、最多两行，放不下的分组折成下拉 (664540f5)
- :lipstick: (jdread): 扫码登录弹窗的长提示按宽度折行居中，不再溢出 (6e7a8a00)

#### 重构

- :recycle: (chapter): 章节段首缩进统一由 CSS 给，textToBody 与外壳剥掉正文自带空白 (65d5650c)

### 完整对比

https://github.com/AnkioTomas/moon/compare/v0.2.24...v0.2.25

# v0.2.24 · 2026-10-20

## 月读 v0.2.24

KOReader 插件包：`book.koplugin-v0.2.24.zip`

输入法词库（整库，手动 sideload）：`dictionary.sqlite3 dictionary-wubi.sqlite3 dictionary-cangjie.sqlite3 dictionary-zhuyin.sqlite3`

安装：解压后将 `book.koplugin` 复制到 KOReader 的 `plugins` 目录，然后重启。

拓展书源（可选，需同时安装月读）：`moonsource-kavita.koplugin-v0.2.24.zip`（Kavita）、
`moonsource-bookorbit.koplugin-v0.2.24.zip`（BookOrbit）。解压后同样放进 `plugins` 目录。

词库 sideload：下载对应布局的词库，直接放入 KOReader 数据目录下的
`.moon/`（与 `book.sqlite3` 同级）。附件已使用最终文件名，无需重命名。

### 更新内容

相对上一版本 `v0.2.23`：

#### 新功能

- :sparkles: (subscribe): 远程管理添加网站订阅可填「链接包含」关键词 (1badd75d)
- :sparkles: (lockscreen): 新增「今日报纸」锁屏壁纸 (63c9bd8a)

#### 修复

- :bug: (webdav): 修复 PUT 上传卡死，流式发送不再重复生成请求头 (4e70f09b)

#### 界面

- :lipstick: (library): 窄屏下工具条自动收成图标，分组标题不再顶掉返回键 (c5337799)

#### 文档

- :memo: 添加宣传物料工作区到 .gitignore (9bace279)

### 完整对比

https://github.com/AnkioTomas/moon/compare/v0.2.23...v0.2.24

# v0.2.23 · 2026-10-19

## 月读 v0.2.23

KOReader 插件包：`book.koplugin-v0.2.23.zip`

输入法词库（整库，手动 sideload）：`dictionary.sqlite3 dictionary-wubi.sqlite3 dictionary-cangjie.sqlite3 dictionary-zhuyin.sqlite3`

安装：解压后将 `book.koplugin` 复制到 KOReader 的 `plugins` 目录，然后重启。

拓展书源（可选，需同时安装月读）：`moonsource-kavita.koplugin-v0.2.23.zip`（Kavita）、
`moonsource-bookorbit.koplugin-v0.2.23.zip`（BookOrbit）。解压后同样放进 `plugins` 目录。

词库 sideload：下载对应布局的词库，直接放入 KOReader 数据目录下的
`.moon/`（与 `book.sqlite3` 同级）。附件已使用最终文件名，无需重命名。

### 更新内容

相对上一版本 `v0.2.22`：

#### 新功能

- :sparkles: (qqreader): 支持已购 VIP 加密章节解密与乱序字体还原 (8721754b)

#### 修复

- :bug: (reflow): 记住上次打开的排版版，切换后按页首文字精确落位 (ac854484)

#### 变更

- :adhesive_bandage: (qqreader): 写入新的字形签名缓存后清掉旧版本缓存 (f8f8f1ce)

### 完整对比

https://github.com/AnkioTomas/moon/compare/v0.2.22...v0.2.23
