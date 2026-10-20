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

# v0.2.22 · 2026-10-19

## 月读 v0.2.22

KOReader 插件包：`book.koplugin-v0.2.22.zip`

输入法词库（整库，手动 sideload）：`dictionary.sqlite3 dictionary-wubi.sqlite3 dictionary-cangjie.sqlite3 dictionary-zhuyin.sqlite3`

安装：解压后将 `book.koplugin` 复制到 KOReader 的 `plugins` 目录，然后重启。

拓展书源（可选，需同时安装月读）：`moonsource-kavita.koplugin-v0.2.22.zip`（Kavita）、
`moonsource-bookorbit.koplugin-v0.2.22.zip`（BookOrbit）。解压后同样放进 `plugins` 目录。

词库 sideload：下载对应布局的词库，直接放入 KOReader 数据目录下的
`.moon/`（与 `book.sqlite3` 同级）。附件已使用最终文件名，无需重命名。

### 更新内容

相对上一版本 `v0.2.21`：

#### 新功能

- :sparkles: (manage): 精简功能支持全部 feature，删除时连带删依赖它的功能 (738c8008)
- :sparkles: (remote): 没连 Wi-Fi 时分享截图、开启远程管理会先询问是否开启 (b07b9503)
- :sparkles: (manage): 新增「精简功能」，可删除用不到的 feature 目录 (214c86c2)
- :sparkles: (rare): 生僻字注音快捷面板改为二级菜单，可直接切开关和范围 (e49da9d2)
- :sparkles: (panel): 新增手势动作「退出阅读回到月读」 (d1a76264)

#### 修复

- :bug: (desktop): 阅读菜单文件浏览器图标回月读桌面，改在桌面层启动时接管 (b538df1f)

#### 重构

- :recycle: (manage): 停用功能不再连带停用依赖方 (168ff1eb)
- :recycle: (manage): 精简功能改为功能开关，停用而不是删除 (52ce92cf)

### 完整对比

https://github.com/AnkioTomas/moon/compare/v0.2.21...v0.2.22

# v0.2.21 · 2026-10-19

## 月读 v0.2.21

KOReader 插件包：`book.koplugin-v0.2.21.zip`

输入法词库（整库，手动 sideload）：`dictionary.sqlite3 dictionary-wubi.sqlite3 dictionary-cangjie.sqlite3 dictionary-zhuyin.sqlite3`

安装：解压后将 `book.koplugin` 复制到 KOReader 的 `plugins` 目录，然后重启。

拓展书源（可选，需同时安装月读）：`moonsource-kavita.koplugin-v0.2.21.zip`（Kavita）、
`moonsource-bookorbit.koplugin-v0.2.21.zip`（BookOrbit）。解压后同样放进 `plugins` 目录。

词库 sideload：下载对应布局的词库，直接放入 KOReader 数据目录下的
`.moon/`（与 `book.sqlite3` 同级）。附件已使用最终文件名，无需重命名。

### 更新内容

相对上一版本 `v0.2.20`：

#### 新功能

- :sparkles: (ai): AI 设置新增服务商，按服务商发对应的关闭思考参数 (f5e6b758)

#### 修复

- :bug: (xray): 截断后缺段不再报错，并用 reasoning 参数关闭思考加速 (9150b9ce)
- :bug: (xray): 提高综合拉取的 token 预算，截断重试上限放宽到 32K (dad084a6)
- :bug: (xray): AI 输出被截断时保留已完整的人物、地点，不再整体失败 (f20db2a7)
- Revert ":bug: (panel): 旧版 KOReader 重建文件管理器菜单前补回顶栏按钮，修复下拉顶栏崩溃" (87851493)
- Revert ":bug: (panel): 阅读器菜单重建前同样补回顶栏按钮，修复旧版 KOReader 阅读页崩溃" (02352a2a)
- :bug: (panel): 阅读器菜单重建前同样补回顶栏按钮，修复旧版 KOReader 阅读页崩溃 (e92df477)
- :bug: (panel): 旧版 KOReader 重建文件管理器菜单前补回顶栏按钮，修复下拉顶栏崩溃 (1bec8ae6)
- :bug: (home): 保存后首页不再把略超高的钉页拆到下一页，添加组件按自定义高度判断能否放下 (c84f6743)

#### 重构

- :recycle: (ui): 单选弹窗统一改用主题 List，去掉手写的 ✓ 前缀 (2dc6934f)
- :recycle: (ai): 服务商选择改用主题单选列表 (f8e9ae64)
- :recycle: (setting): 整理设置分组与命名，新增「安全」组 (01cf1551)

#### 变更

- :children_crossing: (ai): 失败提示带状态码和上游原话，停留 8 秒 (c35bd386)
- :loud_sound: (ai): 请求失败一律记录状态码和响应体 (8df2274f)
- :speech_balloon: (legado): 账号登录里的「阅读」改称「开源阅读」 (d7c53e3b)
- :fire: (ai): 删除截断 JSON 补救 (8c890f65)
- :fire: (ai): 删除「AI token 上限」设置，默认上限提到 8000 (09c0a6ad)

### 完整对比

https://github.com/AnkioTomas/moon/compare/v0.2.20...v0.2.21
