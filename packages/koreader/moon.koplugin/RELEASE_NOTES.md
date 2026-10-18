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

# v0.2.12 · 2026-10-18

## 月读 v0.2.12

KOReader 插件包：`book.koplugin-v0.2.12.zip`

输入法词库（整库，手动 sideload）：`dictionary.sqlite3 dictionary-wubi.sqlite3 dictionary-cangjie.sqlite3 dictionary-zhuyin.sqlite3`

安装：解压后将 `book.koplugin` 复制到 KOReader 的 `plugins` 目录，然后重启。

拓展书源（可选，需同时安装月读）：`moonsource-kavita.koplugin-v0.2.12.zip`（Kavita）、
`moonsource-bookorbit.koplugin-v0.2.12.zip`（BookOrbit）。解压后同样放进 `plugins` 目录。

词库 sideload：下载对应布局的词库，直接放入 KOReader 数据目录下的
`.moon/`（与 `book.sqlite3` 同级）。附件已使用最终文件名，无需重命名。

### 更新内容

相对上一版本 `v0.2.11`：

#### 新功能

- :sparkles: (qidian): 已购 VIP 章节正文本地解密 (5d5274e2)

#### 修复

- :bug: (remote): 远程输入同时认主题输入面板和原生输入框 (5bc134a7)
- :bug: (reviews): 段评扫描结果经 JSON 回传后序号变字符串键导致空指针 (5f289b9e)
- :bug: (wechat): 公众号刷新遇 -2041 时也走凭据续期再重试 (2d43ca95)
- :bug: (lockscreen): 文字海报关键词不再被按字节削成半个字 (90b9e501)
- :bug: (remote): 恢复备份不再删换被 mmap 的字体，避免 KOReader 崩溃 (7d0ec5b3)

#### 文档

- :memo: (ui): 更新 README 中数据源与功能描述 (760528b9)

#### 变更

- :green_heart: (test): 热力图用例周日没有留空格子时不再误报 (ac8d8644)
- :children_crossing: (reader): 超大 EPUB 默认关内嵌字体样式，首次打开前提示可能卡死 (724216cc)

### 完整对比

https://github.com/AnkioTomas/moon/compare/v0.2.11...v0.2.12

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
