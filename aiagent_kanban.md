# 📌 AI Agent CLI 项目任务看板（Kanban）

---

## 🧪 V0.1 - MVP 原型版

### 📋 To Do

- [ ] 初始化项目结构（`aiagent/cli.py` + `core/` + `storage/`）
- [ ] 实现 `track`, `list`, `remove` 命令
- [ ] 使用 GitHub API 拉取基础数据（stars, issues, commits）
- [ ] 存储跟踪的项目列表（使用 JSON 或 SQLite）
- [ ] 实现 `update` 命令：拉取并打印更新数据

### 🚧 In Progress
<!-- 正在做的任务放这里 -->

### ✅ Done
<!-- 完成的任务放这里 -->

---

## 🤖 V0.2 - 核心功能版

### 📋 To Do

- [ ] 整合 OpenAI API，生成项目更新摘要（`summary` 命令）
- [ ] 实现开发计划预测（从 milestone / issues 中抽取）
- [ ] 添加数据缓存机制（避免重复请求）
- [ ] 支持导出 Markdown / JSON 格式摘要报告
- [ ] 美化 CLI 输出（使用 `click.style()`）

### 🚧 In Progress
<!-- 正在做的任务放这里 -->

### ✅ Done
<!-- 完成的任务放这里 -->

---

## 🔥 V0.3 - 增强功能版

### 📋 To Do
- [ ] 实现热门项目趋势榜单（基于 stars 增长）
- [ ] 多项目比较功能（展示对比指标）
- [ ] 实现关键词订阅（自动发现新项目）
- [ ] 可选：集成 Telegram/Slack Bot 通知
- [ ] 设置计划任务支持（定时更新）
- [ ] 打包为 PyPI CLI 工具（`aiagent` 命令）

### 🚧 In Progress
<!-- 正在做的任务放这里 -->

### ✅ Done
<!-- 完成的任务放这里 -->
