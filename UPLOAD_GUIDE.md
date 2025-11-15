# GitHub 上传指南

## 快速上传到 GitHub

### 方法 1: 使用 GitHub 网页界面（推荐新手）

1. **创建新仓库**
   - 访问 https://github.com/new
   - 仓库名称: `shipany-module-master`
   - 描述: `Claude AI Skill for ShipAny modular extraction and integration`
   - 选择 Public
   - 不要勾选 "Add a README file"（我们已经有了）
   - 点击 "Create repository"

2. **上传文件**
   - 在新仓库页面，点击 "uploading an existing file"
   - 将整个 `shipany-module-master` 文件夹拖入
   - 或者选择文件上传
   - 填写 commit 信息: `Initial commit: ShipAny Module Master Skill`
   - 点击 "Commit changes"

### 方法 2: 使用命令行（推荐开发者）

```bash
# 1. 进入 skill 目录
cd shipany-module-master

# 2. 初始化 Git 仓库
git init

# 3. 添加所有文件
git add .

# 4. 创建首次提交
git commit -m "Initial commit: ShipAny Module Master Skill"

# 5. 在 GitHub 创建仓库后，关联远程仓库
git remote add origin https://github.com/YOUR_USERNAME/shipany-module-master.git

# 6. 推送到 GitHub
git branch -M main
git push -u origin main
```

### 方法 3: 使用 GitHub Desktop（推荐 Mac 用户）

1. 打开 GitHub Desktop
2. File → Add Local Repository
3. 选择 `shipany-module-master` 文件夹
4. 点击 "Create a repository"
5. 填写信息后点击 "Publish repository"

## 上传后的配置

### 1. 更新 README.md 中的链接

将 README.md 中的 `YOUR_USERNAME` 替换为你的 GitHub 用户名：

```bash
# 使用命令行替换
sed -i '' 's/YOUR_USERNAME/你的用户名/g' README.md
git add README.md
git commit -m "Update GitHub username in README"
git push
```

### 2. 添加 Topics（标签）

在 GitHub 仓库页面：
1. 点击右侧的 ⚙️ (Settings)
2. 在 "Topics" 部分添加：
   - `claude-ai`
   - `claude-skill`
   - `shipany`
   - `nextjs`
   - `ai-saas`
   - `modular-framework`

### 3. 设置 About（关于）

在仓库首页右侧：
1. 点击 ⚙️ 编辑
2. Description: `Claude AI Skill for intelligent ShipAny module extraction and integration`
3. Website: `https://shipany.ai`
4. 勾选 "Releases" 和 "Packages"

### 4. 创建 Release（可选）

```bash
# 打标签
git tag -a v1.0.0 -m "Release v1.0.0: Initial release"
git push origin v1.0.0
```

然后在 GitHub 上：
1. 进入 Releases 页面
2. 点击 "Draft a new release"
3. 选择 tag `v1.0.0`
4. Release title: `v1.0.0 - Initial Release`
5. 描述发布内容
6. 点击 "Publish release"

## 推广你的 Skill

### 1. 在 ShipAny 社区分享

- ShipAny Discord/Slack
- ShipAny 用户群
- 相关技术论坛

### 2. 社交媒体

发布推文/帖子模板：

```
🚀 刚发布了一个 Claude AI Skill！

ShipAny Module Master - 智能提取 ShipAny 模板模块

✨ 功能：
- 自动分析模块依赖
- 生成提取计划
- 配置指导

🔗 GitHub: https://github.com/YOUR_USERNAME/shipany-module-master

#ClaudeAI #ShipAny #NextJS #AITools
```

### 3. 提交到 Claude Skills 社区

- 在 Anthropic 论坛分享
- 提交到 Claude Skills 精选列表

## 维护建议

### 定期更新

```bash
# 更新 ShipAny 文档
python3 scripts/fetch_docs.py > references/shipany-docs.md

# 提交更新
git add references/shipany-docs.md
git commit -m "Update ShipAny documentation"
git push
```

### 处理 Issues

- 及时回复用户问题
- 标记 bug 和 feature requests
- 创建 milestone 规划版本

### 接受 Pull Requests

1. Review 代码
2. 测试功能
3. Merge 到 main 分支
4. 感谢贡献者

## 文件检查清单

上传前确保包含：

- [x] SKILL.md（英文版）
- [x] SKILL_zh.md（中文版）
- [x] README.md（双语说明）
- [x] LICENSE（MIT 许可证）
- [x] .gitignore（忽略文件）
- [x] references/（参考文档）
  - [x] modules-overview.md
  - [x] shipany-docs.md
  - [x] integration-guide.md
- [x] scripts/（工具脚本）
  - [x] analyze-dependencies.py
  - [x] fetch_docs.py

## 常见问题

**Q: 需要删除哪些文件？**
A: 不需要删除任何文件，所有文件都是必需的。

**Q: 如何更新仓库？**
A: 使用 `git pull` 拉取最新代码，修改后 `git push` 推送。

**Q: 可以设为私有仓库吗？**
A: 可以，但建议公开以便社区使用和贡献。

**Q: 如何处理敏感信息？**
A: 本 skill 不包含敏感信息，所有内容都可以公开。
