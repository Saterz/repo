# v1.2.3 · 2026-10-12

## 更新说明

- 元数据：微信读书源现在会自动更新skill版本信息，不再因skill版本升级而丢弃搜索结果
- 元数据：封面编辑器在缺少 API Key 时会直接弹框填写，填完自动继续封面搜索，而不是只弹提示让用户去设置里手动配置
- 快捷操作：微阅标注（拉取微阅想法的内置动作）改为依赖插件weread，配套修改weread.koplugin，不再依赖wereadannotationlite.koplugin

### 配套修改weread.koplugin v1.6.0
> 添加“拉取当前章节想法”菜单，可注册快捷手势。
- 点击自动拉取当前章节想法（几秒内渲染），之后翻到任意章节均会自动拉取该章节想法（随着你的阅读位置自动拉取）。
- 首次比如未匹配书籍时点击该按钮会先弹出书籍匹配界面，用户选定书籍之后会自动执行拉取当前章节想法。
- 整个过程仅顶部小通知，不影响整体阅读体验，无需提前批量下载某些章节甚至所有章节想法
> 整本下载伴随失败章节时会无法打包成EPUB，修改后即使有失败章节也可以打包成EPUB，失败章节正文内容提示"获取内容失败“

# v1.2.2 · 2026-10-01

## 更新内容
>可搭配[simpleui v2.7.1-b](https://github.com/gytwo/simpleui.koplugin/releases/v2.7.1-b)使用

1. 快捷操作：新增内置动作
- 切换翻页方向
- 番茄-拉取段评：可为本地书籍匹配书源段评-需安装[fanqie.koplugin v2.2.1-b](https://github.com/gytwo/fanqie.koplugin/releases)
- 页面浏览器：类似kindle原生页面缩略图，可快速预览页面、快速跳转下一章-需安装[page_scrubber.koplugin](https://github.com/lautaroelkin/page_scrubber.koplugin)
2. 阅读滑块：新增配置区 —— 可直接在滑块弹窗中应用、创建、删除 KOReader 配置文件
3. 阅读滑块：新增文档设置区 —— 重置文档设置为默认、保存文档设置为默认
4. 阅读滑块：样式微调区改为可折叠
5. 默认设置：修改部分默认设置

# v1.2.1 · 2026-09-28

## 更新说明
> 元数据编辑模块（封面、标题、作者、系列、分类、语言、出版社、出版时间、简介）
> 可搭配[simpleui v2.7.1-b](https://github.com/gytwo/simpleui.koplugin/releases/v2.7.1-b)使用
-  元数据: 添加编辑自定义封面-从设备获取、在线源预览、移除自定义封面
-  元数据: 添加在线获取元数据来源-微信阅读（打开微信读书skill以获取API key)
-  元数据: 添加可编辑字段-出版日期
-  元数据: 完善中文翻译

# v1.2.0 · 2026-09-27

## 更新说明
> 新增书籍元数据编辑模块（标题、作者、系列、分类、语言、出版社、简介）
> 💡 **功能来源**:
> [zenos.koplugin](https://github.com/xZenLabs/zen-os)
>  [metadata.koplugin](https://github.com/ZHA30/metadata.koplugin) 
> 可搭配[simpleui v2.7.1-b](https://github.com/gytwo/simpleui.koplugin/releases/v2.7.1-b)使用
- 元数据：支持 EPUB 内嵌元数据读写，可恢复
- 元数据：非 EPUB 书籍的元数据保存到sdr文件
- 元数据：文件管理器界面长按书籍弹出菜单，点击「编辑元数据」
- 元数据：在线元数据源 —— 豆瓣、Google Books、Hardcover、Open Library
- 元数据：搜索源选择界面支持配置各自的 API key、修改搜索关键词、分页预览结果
- 元数据：逐字段应用结果，手动修改过的字段不会被覆盖
- 元数据：可恢复上一版元数据（仅 EPUB，单步撤销）
- 元数据：添加到koreader快捷手势动作及QA内置动作
- 元数据：QuickUI 设置新增「元数据设置」子菜单，含「启用元数据编辑器」开关
- 元数据：支持标准预设系统（保存 / 应用 / 重置）

# v1.1.1 · 2026-09-24

## 更新说明
> 修复一些已知问题
> 如果要同时安装simpleui，请搭配本仓库[simpleui v2.7.1-b](https://github.com/gytwo/simpleui.koplugin/releases/tag/v2.7.1-b)使用
- 底部栏: 阅读界面由原来的直接替换原生footer改为与原生footer共存，上下排布（保持与Menu patch一致）
- 底部栏: 取消勾选“在阅读器中显示”时立即清除底栏触摸区域（避免误触）而非等到重排结束才彻底清除
- 底部栏:  仅当底栏高度发生变化时才重排，修复打开书籍时闪烁一下的问题
- 底部栏: 修复从阅读界面返回simpleui主屏幕后移除或添加底栏按钮无法立即更新的问题
- 页眉页脚: 修复缩略图生成失败的问题——渲染离屏缓冲区（缩略图、书籍地图、页面浏览器）时跳过页眉/页脚叠加
- 侧边栏: 删除无效的文件引用避免可能的崩溃
