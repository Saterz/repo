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

# v6.1.0-beta.1 · 2026-10-21

- 修复自动发布

# v6.0.0-beta.1 · 2026-10-07

- 以 5.9.1-beta.4 的已收口代码作为 6.0 Beta 基线；不新增实验性认证桥接，不改变 Schema 136、同步主链路或主页结构。
- 延续安装包减重结果：压缩 stillness 背景，发布包继续排除仅用于编译的 `native/` 源码，运行时 codec 与 Kindle/Kobo/Android 支持保持不变。
- 延续双登录收口：主登录与书架管理授权继续独立；同账号重新扫码保留既有书架管理授权，并支持单独取消该授权。
- 延续书城轻量整理与日志降噪；同时修正两条历史回归测试的版本硬编码，使 6.0 系列继续验证功能契约而不是旧版本号。
