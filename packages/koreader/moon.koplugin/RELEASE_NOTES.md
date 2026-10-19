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

# v0.2.20 · 2026-10-19

## 月读 v0.2.20

KOReader 插件包：`book.koplugin-v0.2.20.zip`

输入法词库（整库，手动 sideload）：`dictionary.sqlite3 dictionary-wubi.sqlite3 dictionary-cangjie.sqlite3 dictionary-zhuyin.sqlite3`

安装：解压后将 `book.koplugin` 复制到 KOReader 的 `plugins` 目录，然后重启。

拓展书源（可选，需同时安装月读）：`moonsource-kavita.koplugin-v0.2.20.zip`（Kavita）、
`moonsource-bookorbit.koplugin-v0.2.20.zip`（BookOrbit）。解压后同样放进 `plugins` 目录。

词库 sideload：下载对应布局的词库，直接放入 KOReader 数据目录下的
`.moon/`（与 `book.sqlite3` 同级）。附件已使用最终文件名，无需重命名。

### 更新内容

相对上一版本 `v0.2.19`：

#### 新功能

- :sparkles: (library): 详情页删除分软删除与彻底删除，书架可筛选软删除 (df51f8e6)
- :sparkles: (library): 随机一本支持设置范围并避开已读，书库骰子可开关 (fad610e4)
- :sparkles: (remote): 远程管理改动文件后自动重扫本地书架 (083a89b1)
- :sparkles: (detail): 软删除：只删本地文档，保留书架条目与封面 (e6786b91)
- :sparkles: (translate): 双语译文颜色与字号可单独设置 (0d652522)

#### 修复

- :bug: (online): 摸鱼日报图尺寸限制在接口允许的 240-2560，避免 HTTP 400 (1960c3a3)
- :bug: (ui): 旋转屏幕后桌面、弹窗、侧栏按新尺寸重排，横屏放不下的首页顺延成多页 (2deb9b0c)
- :bug: (reviews): 修复段评定位结果含 json.null 导致绘制崩溃 (c9b3ace7)

#### 性能

- :zap: (settings): get/save 按拥有者缓存配置文件，绘制热路径不再拼路径 (7abf8f05)
- :zap: (ui): 已读斜条的白字像素只算一次并缓存，重绘不再逐像素旋转 (fe78bf3a)
- :zap: (workers): 子进程并发为主进程留 48MB 余量并限制最多 8 路，避免小内存设备 OOM (ce8ec830)
- :zap: (webdav): 上传改为分块流式发送，不再把整文件读进内存 (065efbee)

#### 重构

- :recycle: (wallpaper): 壁纸改为全局设置，各界面可单独覆盖 (0a82841f)

#### 变更

- :globe_with_meridians: (l10n): 清理已删除的软删除确认文案 (abfb7da5)
- :children_crossing: (desktop): 切换书源后留在当前页签，不再跳回首页 (53b4b28d)
- :globe_with_meridians: (l10n): 补充壁纸设置与随机书文案，清理已删除的壁纸文案 (a7df1975)

### 完整对比

https://github.com/AnkioTomas/moon/compare/v0.2.19...v0.2.20

# v0.2.19 · 2026-10-19

## 月读 v0.2.19

KOReader 插件包：`book.koplugin-v0.2.19.zip`

输入法词库（整库，手动 sideload）：`dictionary.sqlite3 dictionary-wubi.sqlite3 dictionary-cangjie.sqlite3 dictionary-zhuyin.sqlite3`

安装：解压后将 `book.koplugin` 复制到 KOReader 的 `plugins` 目录，然后重启。

拓展书源（可选，需同时安装月读）：`moonsource-kavita.koplugin-v0.2.19.zip`（Kavita）、
`moonsource-bookorbit.koplugin-v0.2.19.zip`（BookOrbit）。解压后同样放进 `plugins` 目录。

词库 sideload：下载对应布局的词库，直接放入 KOReader 数据目录下的
`.moon/`（与 `book.sqlite3` 同级）。附件已使用最终文件名，无需重命名。

### 更新内容

相对上一版本 `v0.2.18`：

#### 修复

- :bug: (fanqie): 修复每次开书都跳回章首，不再把云端 read_progress=0 当章内位置 (698a1e0c)

### 完整对比

https://github.com/AnkioTomas/moon/compare/v0.2.18...v0.2.19

# v0.2.18 · 2026-10-18

## 月读 v0.2.18

KOReader 插件包：`book.koplugin-v0.2.18.zip`

输入法词库（整库，手动 sideload）：`dictionary.sqlite3 dictionary-wubi.sqlite3 dictionary-cangjie.sqlite3 dictionary-zhuyin.sqlite3`

安装：解压后将 `book.koplugin` 复制到 KOReader 的 `plugins` 目录，然后重启。

拓展书源（可选，需同时安装月读）：`moonsource-kavita.koplugin-v0.2.18.zip`（Kavita）、
`moonsource-bookorbit.koplugin-v0.2.18.zip`（BookOrbit）。解压后同样放进 `plugins` 目录。

词库 sideload：下载对应布局的词库，直接放入 KOReader 数据目录下的
`.moon/`（与 `book.sqlite3` 同级）。附件已使用最终文件名，无需重命名。

### 更新内容

相对上一版本 `v0.2.17`：

#### 新功能

- :sparkles: (storage): 存储空间按目录归类，手机式占比展示与清理 (6110c44e)
- :sparkles: (sidebar): 统计页补回时长/页数/划线/笔记等维度并加预计读完 (41ec589c)

#### 重构

- :recycle: (sidebar): 统计页改读月读自己的 reading_stats，不再依赖 KOReader 统计插件 (685713e1)

### 完整对比

https://github.com/AnkioTomas/moon/compare/v0.2.17...v0.2.18

# v0.2.17 · 2026-10-18

## 月读 v0.2.17

KOReader 插件包：`book.koplugin-v0.2.17.zip`

输入法词库（整库，手动 sideload）：`dictionary.sqlite3 dictionary-wubi.sqlite3 dictionary-cangjie.sqlite3 dictionary-zhuyin.sqlite3`

安装：解压后将 `book.koplugin` 复制到 KOReader 的 `plugins` 目录，然后重启。

拓展书源（可选，需同时安装月读）：`moonsource-kavita.koplugin-v0.2.17.zip`（Kavita）、
`moonsource-bookorbit.koplugin-v0.2.17.zip`（BookOrbit）。解压后同样放进 `plugins` 目录。

词库 sideload：下载对应布局的词库，直接放入 KOReader 数据目录下的
`.moon/`（与 `book.sqlite3` 同级）。附件已使用最终文件名，无需重命名。

### 更新内容

相对上一版本 `v0.2.16`：

#### 新功能

- :sparkles: (ai): 支持多窗口时限制插件固定数量 (fd63f271)
- :sparkles: (extensions): 支持根据屏幕宽度动态限制扩展页签最大 pinned 数量 (dd55fb1b)
- :sparkles: (extensions): 拓展入口可固定到底栏并自选图标，与拓展菜单互斥 (1167bf6f)

#### 修复

- :bug: (wechat): App 协议续期改用 guest_token 防重放签名，修复 -2041 (94583edf)
- :bug: (text): RSS 正文解码常见 HTML 命名实体（&nbsp; &mdash; 等） (8d15df46)
- :bug: (subscribe): 修复翻章取消预取时图片下载句柄 cancel 崩溃 (63245c6b)

#### 性能

- :zap: (subscribe): 订阅刷新 4 路并发，被截断的 RSS 摘要改抓原文 (584082b0)

### 完整对比

https://github.com/AnkioTomas/moon/compare/v0.2.16...v0.2.17
