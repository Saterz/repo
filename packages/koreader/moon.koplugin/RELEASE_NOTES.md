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

# v0.2.16 · 2026-10-18

## 月读 v0.2.16

KOReader 插件包：`book.koplugin-v0.2.16.zip`

输入法词库（整库，手动 sideload）：`dictionary.sqlite3 dictionary-wubi.sqlite3 dictionary-cangjie.sqlite3 dictionary-zhuyin.sqlite3`

安装：解压后将 `book.koplugin` 复制到 KOReader 的 `plugins` 目录，然后重启。

拓展书源（可选，需同时安装月读）：`moonsource-kavita.koplugin-v0.2.16.zip`（Kavita）、
`moonsource-bookorbit.koplugin-v0.2.16.zip`（BookOrbit）。解压后同样放进 `plugins` 目录。

词库 sideload：下载对应布局的词库，直接放入 KOReader 数据目录下的
`.moon/`（与 `book.sqlite3` 同级）。附件已使用最终文件名，无需重命名。

### 更新内容

相对上一版本 `v0.2.15`：

#### 新功能

- :sparkles: (fanqie): 漫画章节解密后打成 CBZ，按漫画文档打开 (7999dc59)
- :sparkles: (fanqie): 免登录搜索、书架同步、段评、漫画与进度定时上传 (7f954c10)
- :sparkles: (reader): 段评改为段尾对话气泡，不再画线 (046cd433)
- :sparkles: (library): 新增 Kindle / Kobo 封面风格与图书馆显示设置 (577348d8)

#### 修复

- :bug: (wechat): 旧 eink 前缀设备 ID 登录时换成数字 ID，避免手机渠道续期被风控 -2041 (43ff983f)

#### 界面

- :lipstick: (library): Kobo 底栏未下载改用下载图标，进度条右侧显示百分比 (07d8e546)
- :lipstick: (cover): 封面被高度压矮时向格子宽度拉伸，减小列间空隙 (7fc6975a)

#### 重构

- :recycle: (source): CBZ 打包抽成公共 source/cbz，章节载荷支持 file 直接登记 (5cd8af1c)
- :recycle: (fanqie): 定位器移到 book/annotations，清理 qrlogin 冗余 (d1b3bd12)
- :recycle: (setting): 重排设置项：界面显示拆成外观 / 屏幕与亮度 / 启动与按键，书架显示并入桌面 (d27f2346)

#### 变更

- :fire: (fanqie): 去掉阅读中定时上传进度，沿用关书 / 换章上传 (9e091113)

### 完整对比

https://github.com/AnkioTomas/moon/compare/v0.2.15...v0.2.16

# v0.2.15 · 2026-10-18

## 月读 v0.2.15

KOReader 插件包：`book.koplugin-v0.2.15.zip`

输入法词库（整库，手动 sideload）：`dictionary.sqlite3 dictionary-wubi.sqlite3 dictionary-cangjie.sqlite3 dictionary-zhuyin.sqlite3`

安装：解压后将 `book.koplugin` 复制到 KOReader 的 `plugins` 目录，然后重启。

拓展书源（可选，需同时安装月读）：`moonsource-kavita.koplugin-v0.2.15.zip`（Kavita）、
`moonsource-bookorbit.koplugin-v0.2.15.zip`（BookOrbit）。解压后同样放进 `plugins` 目录。

词库 sideload：下载对应布局的词库，直接放入 KOReader 数据目录下的
`.moon/`（与 `book.sqlite3` 同级）。附件已使用最终文件名，无需重命名。

### 更新内容

相对上一版本 `v0.2.14`：

#### 新功能

- :sparkles: (ime): 五笔/仓颉/小鹤新增「显示字根键帽」开关，默认关闭 (03d45e35)
- :sparkles: (wallpaper): 界面壁纸支持调整透明度 (7fcabb01)
- :sparkles: (wechat): 阅读时长与登录改走手机 App 协议，支持离线补报 (636ad410)
- :sparkles: (storage): 设置新增存储空间页，列出设备空间与各类数据占用 (#47) (6ae8f632)
- :sparkles: (storage): 可用空间不足 500MB 时进入桌面弹窗提醒 (781b1513)

#### 修复

- :bug: (db): 临时表改走内存，本地扫盘指纹逐批落盘 (061166ae)

#### 性能

- :zap: (cache): 体积统计移到子进程，封面最长边降到 600px (#47) (26e376a5)

#### 重构

- :recycle: (wechat): 去掉同步阅读时间开关，开章时顺手补报上一章时长 (c45eebb2)

### 完整对比

https://github.com/AnkioTomas/moon/compare/v0.2.14...v0.2.15
