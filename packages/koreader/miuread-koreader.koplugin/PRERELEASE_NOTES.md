# v6.1.0-beta.13 · 2026-10-28

- 统一正文 EPUB 下载，整书、单章、范围及预下载不再新建带评论 EPUB；旧文件保留识别与打开能力。
- 公开评论由阅读器主动获取，保存到现有每书 SQLite，支持离线查看、增量合并、部分失败续传及独立更新。
- 在纯净 EPUB 中使用保守 XPointer 定位和非侵入式划线覆盖层；无法准确定位的评论仍在章节离线列表保留。
- 评论数据库 V4 迁移保留历史数据。删除书籍清理关联本地缓存、保留全局评论收藏；删除前的安全上传不执行云端删除。
- 主页顶栏按内容宽度均匀分配留白，支持逐项与整栏隐藏；Wi-Fi 仅显示状态图标，点击后进入连接详情与网络管理。
- 修复弹窗内容裁切、大小弹窗切换残影及背景恢复时序，尽量保持 E-Ink 局部刷新。
- B7 整合修复：删除后的只读评论查询不再重建缓存目录；章节失效时清除旧覆盖标记；划线绘制限制在阅读视口；极窄屏避免顶栏溢出。
- 保留阅读进度、阅读时间、个人批注同步及原有 Beta/Tag 发布工作流；Kindle 实机显示与微信读书线上接口仍需验证。

# v6.1.0-beta.12 · 2026-10-28

- 修复 Lua 5.1/LuaJIT 发布回归测试的模块搜索路径
- 已准备版本允许在发布前更新 CHANGELOG 说明
- 统一发布测试配置并保留 Beta 手动与 Tag 两种入口
- 正式版改为测试通过后创建不可变 Tag，不再强制移动已有 Tag
- 保留现有阅读同步、阅读时间和下载业务逻辑，Schema 136 不变

# v6.1.0-beta.9 · 2026-10-26

- Keep PR #156 verified-sequence callback fix and twelve transaction regression scenarios.
- Remove the cached exact-alignment shortcut on new book opens; fetch fresh Web progress asynchronously.
- Parse isolated reading-time Web progress consistently, validate chapter UID/index before committing the anchor, and retain safe unsent time on context/authentication failure.
- Distinguish accepted-but-unconfirmed progress from actual write failure, including subsequent cloud changes; never replay old writes blindly.
- Preserve end-of-reading-only network uploads and Schema 136; leave downloads, annotations and account transport unchanged.

# v6.1.0-beta.8 · 2026-10-26

- Revert beta.6 low-level ReaderUI upload vetoes; retain the established end-of-reading upload lifecycle and the removed one-shot upload on book open.
- Anchor-aware latest-wins decision: prefer independently verified common chapter/co over server write timestamps; no 30-second ambiguous conflict UI.
- When the server is newer, keep an UNSENT local transaction until cloud position is verified on the device; never erase it after merely fetching cloud progress.
- Preserve Web-only verification of uploaded chapter/co, pending progress on failure, and account/sequence isolation.
- Revert global menu greying/truncation changes; use opt-in readable readonly rows and a full-text reason dialog for progress details.
- Keep reading-time and legacy migration data protections; add regression coverage for cloud adoption and retained pending rows.
- Retain automatic tag releases and changelog normalization. No database schema bump.

# v6.1.0-beta.5 · 2026-10-26

- 以 beta.2 为基线，选择性移植进度恢复锚点、E-Ink ZIP、HTTP 暂停与 KOReader 退出修复。
- Web 上传只由 Web 回读确认；普通云端进度仍使用 Web/Agent 综合读取，保留原坐标字段优先级及原持久化写入。
- 阅读时间兼容写入采用 Web 进度；缺失章节索引时只允许同章节 UID 的目录信息补齐。缺少可信上下文时保持既有失败补报路径。
- 下载等待队列在延迟启动前重查队列身份和运行条件；历史无账号标记的等待任务需要手动确认后才能自动运行。
- 同一笔进度上传的重复校验共享回调；扩充功能等价和异常恢复测试。
- 本版未更改 SQLite Schema、下载协议、登录协议、原有 Tag 自动发布触发条件。
- 尚未通过真实微信读书服务端与 Kindle 实机验证；历史 `co=368 → co=0` 的服务器侧原因仍待确认。
