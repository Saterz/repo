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

# v5.9.1-beta.1 · 2026-10-05

- 修复 beta.19 `passive_exact_cache` 的原生 `chapterUid + wr_data_co` 快照遗漏 `safe=true`：此前同一精确位置可能先记录 `final_position_captured`，Reader 关闭后又被 `upload_progress()` 判成 `position_unavailable`，并留下“有失败记录但没有可执行动作”的 pending；本版统一恢复 `safe / coordinate_safe / precise` 语义，并在启动时一次性修复现有 beta.19 精确 pending。
- 新增 ReadingEnd `Progress Recovery Capsule`：精确 source mapping 失败时，把 Reader 仍存活时捕获的 immutable source anchor、XPointer、显示进度、sequence/epoch 持久化；Home 可直接用保存的锚点重跑本地 source cache / fresh Web Reader source，无需为了新产生的失败记录重新打开书。
- `pending_unresolved_position` 正式进入进度恢复状态机：Home/“全部重新同步”优先执行 saved-anchor recovery，再补全整书坐标、fresh GET 云端、按既有 latest-wins 规则发送或验证；失败详情新增“恢复精确位置”。任何旧记录若缺少安全重放坐标和恢复锚点，会明确作为可清理失效记录，不再出现 `items=1` 但 send/verify/resubmit/coordinate 全为 0 的无解释状态。
- ReadReport 生命周期区分主动停止与真实异常退出：ReadingEnd/进度优先抢占后 worker 正常退出不再记为 `unexpected`，也不会被无意义拉起；Reader 活跃期间真实异常退出仍保留一次自动重启。
- 不改变 beta.19 的多锚点精确映射、beta.18 fresh context、beta.17 progress epoch/conflict lifecycle、beta.15/16 `remote_wire_anchor + fresh GET before POST`、exact cloud readback、remote-first freshness resolver、ProgressFence 与 rollback。网络或 source mapping 暂不可用时继续 fail closed：最多延迟同步，不允许用近似百分比或未知远端状态覆盖云端。Schema 保持 136。
