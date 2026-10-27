# v0.3.2 · 2026-10-27

## 月读 v0.3.2

KOReader 插件包：`book.koplugin-v0.3.2.zip`

输入法词库（整库，手动 sideload）：`dictionary.sqlite3 dictionary-wubi.sqlite3 dictionary-cangjie.sqlite3 dictionary-zhuyin.sqlite3`

安装：解压后将 `book.koplugin` 复制到 KOReader 的 `plugins` 目录，然后重启。

拓展书源（可选，需同时安装月读）：`moonsource-kavita.koplugin-v0.3.2.zip`（Kavita）、
`moonsource-bookorbit.koplugin-v0.3.2.zip`（BookOrbit）。解压后同样放进 `plugins` 目录。

词库 sideload：下载对应布局的词库，直接放入 KOReader 数据目录下的
`.moon/`（与 `book.sqlite3` 同级）。附件已使用最终文件名，无需重命名。

### 更新内容

相对上一版本 `v0.3.1`：

#### 修复

- :bug: (store): Z站浏览补上 id，避免 StoreCache 拼键炸掉 (711d52b9)

### 完整对比

https://github.com/AnkioTomas/moon/compare/v0.3.1...v0.3.2

# v0.3.1 · 2026-10-27

## 月读 v0.3.1

KOReader 插件包：`book.koplugin-v0.3.1.zip`

输入法词库（整库，手动 sideload）：`dictionary.sqlite3 dictionary-wubi.sqlite3 dictionary-cangjie.sqlite3 dictionary-zhuyin.sqlite3`

安装：解压后将 `book.koplugin` 复制到 KOReader 的 `plugins` 目录，然后重启。

拓展书源（可选，需同时安装月读）：`moonsource-kavita.koplugin-v0.3.1.zip`（Kavita）、
`moonsource-bookorbit.koplugin-v0.3.1.zip`（BookOrbit）。解压后同样放进 `plugins` 目录。

词库 sideload：下载对应布局的词库，直接放入 KOReader 数据目录下的
`.moon/`（与 `book.sqlite3` 同级）。附件已使用最终文件名，无需重命名。

### 更新内容

相对上一版本 `v0.3.0`：

#### 新功能

- :sparkles: (http): 大文件下载支持断点续传 (dc3be5b5)
- :sparkles: (remote): 打开远程管理显示二维码与地址 (bc9880b3)
- :sparkles: (bluetooth): 睡眠前记录蓝牙状态，唤醒后自动恢复 (5ee99306)
- :sparkles: (rotation): 记住全局屏幕方向，下次进桌面与开书沿用 (e3c82ece)
- :sparkles: (reader): 支持中西文字体分开选择 (608be953)
- :sparkles: (wechat): 书架改走 synckey 增量同步，全量加 bookCount 对账 (033b6a37)

#### 修复

- :bug: (reader): 库外打开只 touch 不上架，EndOfBook 交回原生 (77b5005d)
- :bug: (ui): 斜向截图手势按 northeast 等真实方向放行 (59435824)
- :bug: (test): 补齐旋转合入后缺失的测试桩 (ba59e82a)
- :bug: (wake): 看门狗不再强制关锁屏，只记日志 (972dce5f)
- :bug: (bars): 书名等弹性组件居中靠右按内容宽偏移，不再贴槽左缘 (0912b10a)

#### 性能

- :zap: (local): 扫盘与补齐拆开，日常同步回到分钟级并可续跑 (1369894c)

#### 重构

- :recycle: (store): 书城缓存收敛到数据获取层，源退回纯拉取 (a6369e2b)

#### 变更

- :globe_with_meridians: (l10n): 补齐本地书补封面文案并删掉废弃键 (354915b7)
- :fire: (source): 删除起点/QQ阅读/潇湘/长佩书架分页的 50 页上限 (53daf2d1)

### 完整对比

https://github.com/AnkioTomas/moon/compare/v0.3.0...v0.3.1

# v0.3.0 · 2026-10-27

## 月读 v0.3.0

KOReader 插件包：`book.koplugin-v0.3.0.zip`

输入法词库（整库，手动 sideload）：`dictionary.sqlite3 dictionary-wubi.sqlite3 dictionary-cangjie.sqlite3 dictionary-zhuyin.sqlite3`

安装：解压后将 `book.koplugin` 复制到 KOReader 的 `plugins` 目录，然后重启。

拓展书源（可选，需同时安装月读）：`moonsource-kavita.koplugin-v0.3.0.zip`（Kavita）、
`moonsource-bookorbit.koplugin-v0.3.0.zip`（BookOrbit）。解压后同样放进 `plugins` 目录。

词库 sideload：下载对应布局的词库，直接放入 KOReader 数据目录下的
`.moon/`（与 `book.sqlite3` 同级）。附件已使用最终文件名，无需重命名。

### 更新内容

相对上一版本 `v0.2.50`：

#### 新功能

- :sparkles: (desktop): 首次欢迎弹窗加「加入交流群」按钮 (61d83b78)
- :sparkles: (panel): 快捷面板加后台任务按钮 (bf441146)

#### 修复

- :bug: (ui): 文字不再自带白底矩形，并加扫描防回归 (01b5eb22)
- :bug: (ui): 对角滑动截图手势不再被弹窗与桌面吞掉 (334e2c20)
- :bug: (reviews): 段评首条按首页剩余高度截断，不再整条跳页 (62eaac34)
- :bug: (cover): 封面一律拉满框，宽框不再按比例缩进留白 (c9a910b2)
- :bug: (reader): 修复正式版 KOReader 阅读页点抽屉不回月读 (84cd1a94)
- :bug: (reader): 保存为默认带上高亮格式，换书不再丢 (d109d2a9)

#### 性能

- :zap: (reflow): 提取全文只落盘，避免主进程 OOM (35a5a4b1)

### 完整对比

https://github.com/AnkioTomas/moon/compare/v0.2.50...v0.3.0

# v0.2.50 · 2026-10-26

## 月读 v0.2.50

KOReader 插件包：`book.koplugin-v0.2.50.zip`

输入法词库（整库，手动 sideload）：`dictionary.sqlite3 dictionary-wubi.sqlite3 dictionary-cangjie.sqlite3 dictionary-zhuyin.sqlite3`

安装：解压后将 `book.koplugin` 复制到 KOReader 的 `plugins` 目录，然后重启。

拓展书源（可选，需同时安装月读）：`moonsource-kavita.koplugin-v0.2.50.zip`（Kavita）、
`moonsource-bookorbit.koplugin-v0.2.50.zip`（BookOrbit）。解压后同样放进 `plugins` 目录。

词库 sideload：下载对应布局的词库，直接放入 KOReader 数据目录下的
`.moon/`（与 `book.sqlite3` 同级）。附件已使用最终文件名，无需重命名。

### 更新内容

相对上一版本 `v0.2.49`：

#### 修复

- :bug: (reviews): 段评全屏配图按比例显示，不再拉满变形 (7c1cd621)
- :bug: fix(jdread): 修复书城缓存菜单后的请求取消 (cc77220c)

### 完整对比

https://github.com/AnkioTomas/moon/compare/v0.2.49...v0.2.50

# v0.2.49 · 2026-10-26

## 月读 v0.2.49

KOReader 插件包：`book.koplugin-v0.2.49.zip`

输入法词库（整库，手动 sideload）：`dictionary.sqlite3 dictionary-wubi.sqlite3 dictionary-cangjie.sqlite3 dictionary-zhuyin.sqlite3`

安装：解压后将 `book.koplugin` 复制到 KOReader 的 `plugins` 目录，然后重启。

拓展书源（可选，需同时安装月读）：`moonsource-kavita.koplugin-v0.2.49.zip`（Kavita）、
`moonsource-bookorbit.koplugin-v0.2.49.zip`（BookOrbit）。解压后同样放进 `plugins` 目录。

词库 sideload：下载对应布局的词库，直接放入 KOReader 数据目录下的
`.moon/`（与 `book.sqlite3` 同级）。附件已使用最终文件名，无需重命名。

### 更新内容

相对上一版本 `v0.2.48`：

#### 新功能

- :sparkles: (fanqie): 书架按平台分组浏览，分组名落分类 (fc02aebf)
- :sparkles: (qidian): 书架按平台分组浏览，分组名落分类 (b53d3943)
- :sparkles: (home): 最近阅读与书架可独立开关书名和作者 (61093af4)

#### 修复

- :bug: (wechat): 目录去掉同名同层自锚点，一章不再出两行 (089129f5)
- :bug: (subscribe): 恢复 RSS 自动刷新，周期与图书馆一致 (04ce15f1)
- :bug: (test): 离线测试不再被真实内存与主题模块顶掉替身 (932c543f)
- :bug: (desktop): 桌面页空状态与订阅标题不再铺白色底 (64f304d8)
- :bug: (hero): 英雄卡简介与多行书名不再铺白色底 (763c7890)
- :bug: (log): 业务里的 logger.err 全部改为 logger.error (b2ea13f0)

#### 界面

- :lipstick: (ui): 主题色改为八套预设色板，整套只用一色 (58a91dea)
- :lipstick: (ui): 彩色模式统一补饱和，彩屏颜色不再发淡 (b13f756a)

#### 重构

- :recycle: (setting): 弹窗关闭手势挪到启动与按键分页与弹窗 (fdbaed05)

#### 变更

- :children_crossing: (open): 大文件按可用内存提醒，KFX 转换前确认 (de3619eb)

### 完整对比

https://github.com/AnkioTomas/moon/compare/v0.2.48...v0.2.49
