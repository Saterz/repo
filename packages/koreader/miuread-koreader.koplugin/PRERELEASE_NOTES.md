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

# v6.1.0-beta.2 · 2026-10-25

- 修复低内存下载启动时任务被直接拒绝的问题，复用原有持久化队列自动等待和重试
- 统一休眠恢复与新建下载子进程的内存安全检查，避免 72 MiB 与 96 MiB 冲突
- 增加后台工作租约存活校验，防止超时误释放导致进程重叠
- 增加下载资源诊断、重试退避和恢复后的唤醒，并保留账号及同步逻辑
