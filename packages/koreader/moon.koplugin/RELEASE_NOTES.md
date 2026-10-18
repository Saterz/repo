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

# v0.2.14 · 2026-10-18

## 月读 v0.2.14

KOReader 插件包：`book.koplugin-v0.2.14.zip`

输入法词库（整库，手动 sideload）：`dictionary.sqlite3 dictionary-wubi.sqlite3 dictionary-cangjie.sqlite3 dictionary-zhuyin.sqlite3`

安装：解压后将 `book.koplugin` 复制到 KOReader 的 `plugins` 目录，然后重启。

拓展书源（可选，需同时安装月读）：`moonsource-kavita.koplugin-v0.2.14.zip`（Kavita）、
`moonsource-bookorbit.koplugin-v0.2.14.zip`（BookOrbit）。解压后同样放进 `plugins` 目录。

词库 sideload：下载对应布局的词库，直接放入 KOReader 数据目录下的
`.moon/`（与 `book.sqlite3` 同级）。附件已使用最终文件名，无需重命名。

### 更新内容

相对上一版本 `v0.2.13`：

#### 新功能

- :sparkles: (iread): 支持浏览器扩展授权，用网页 Cookie 登录 (a7059c43)
- :sparkles: (store): 合并 Z站 / OPDS 为书城，支持切换来源搜索与总开关 (a4384828)
- :sparkles: (source): 微信、七猫、拷贝、晋江、QQ阅读、起点、iRead 支持书城搜索 (b0e362de)

#### 修复

- :bug: (wechat): 续期超时或断网不再判登录失效，只有服务器明确拒绝才算 (50aebf33)
- :bug: (charset): 设备缺 GBK 的 iconv 模块时用纯 Lua 兜底，修复晋江授权报 gb18030 (9c0af571)
- :bug: (legado): 空白正文不再当成功章节缓存 (ffe6a736)
- :bug: (store): 书城开关与 OPDS 地址变更不再跳回首页 (e50cd7ae)

#### 文档

- :memo: (docs): README 补充 WebDAV 上传停手与起点跨章崩溃修复说明 (0196add9)

#### 变更

- :loud_sound: (legado): 章节为空时记录书地址与序号 (717dc270)
- :children_crossing: (legado): 章节为空的提示带上章节序号 (a08f3b95)

### 完整对比

https://github.com/AnkioTomas/moon/compare/v0.2.13...v0.2.14

# v0.2.13 · 2026-10-18

## 月读 v0.2.13

KOReader 插件包：`book.koplugin-v0.2.13.zip`

输入法词库（整库，手动 sideload）：`dictionary.sqlite3 dictionary-wubi.sqlite3 dictionary-cangjie.sqlite3 dictionary-zhuyin.sqlite3`

安装：解压后将 `book.koplugin` 复制到 KOReader 的 `plugins` 目录，然后重启。

拓展书源（可选，需同时安装月读）：`moonsource-kavita.koplugin-v0.2.13.zip`（Kavita）、
`moonsource-bookorbit.koplugin-v0.2.13.zip`（BookOrbit）。解压后同样放进 `plugins` 目录。

词库 sideload：下载对应布局的词库，直接放入 KOReader 数据目录下的
`.moon/`（与 `book.sqlite3` 同级）。附件已使用最终文件名，无需重命名。

### 更新内容

相对上一版本 `v0.2.12`：

#### 新功能

- :sparkles: (ai): 新增全局 AI 回答语言，繁体、英文用本地用语 (fccb7703)
- :sparkles: (iread): 接入 iRead 源，个人 Token 登录与在线阅读 (de2e6175)
- :sparkles: (wallpaper): 新增界面壁纸，桌面与弹窗可铺自定义图 (43b8fff5)
- :sparkles: (source): 新增阅读（Legado）数据源，直连阅读 App 的 Web 服务 (f012c31d)

#### 修复

- :bug: (local): WebDAV 上传超时后本轮停手，失败的书 1 小时内不重传 (5b134307)
- :bug: (ui): 开壁纸后底栏选中格底色被摘掉，白字落在白底上 (16b7c4db)
- :bug: (online): 没放对应组件时不再后台拉天气、一言、日报、必应 (7c074ff1)
- :bug: (qidian): VIP 章节解密放进子进程并关 JIT，修复 Kindle 上跳章崩溃 (320c838c)
- :bug: (kindle): 修复 Kindle 书库同步报 no such collation sequence: icu (eaaff12d)
- :bug: (topbar): 旧版 KOReader 的 df 没有 available，剩余存储读不到 (d1696d71)

#### 界面

- :lipstick: (panel): 快捷面板磁贴改灰色胶囊，换 Wi-Fi 图标 (2b1b1612)

#### 性能

- :zap: (nightmode): 自动亮度不再自己拉天气，只读首页缓存 (eee4d92b)

#### 变更

- :rewind: (panel): 撤回 bold 主题快捷面板的灰色胶囊，保留 Wi-Fi 新图标 (782cd40a)
- :children_crossing: (library): 随机抽书后先弹详情页 (8e8a2bf9)
- :globe_with_meridians: (l10n): 补回答语言文案，繁体「刮削」改「資料抓取」 (f12b02a9)
- :label: (wallpaper): 补 BlitBuffer 类型标注，消除 LuaLS 警告 (989e355e)
- :globe_with_meridians: (webdav): 补上传失败汇总提示的繁体与英文文案 (d60e153b)
- :children_crossing: (webdav): 上传失败时汇总提示失败本数和原因 (7f6a29d6)

### 完整对比

https://github.com/AnkioTomas/moon/compare/v0.2.12...v0.2.13
