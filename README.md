# ShipAny Module Master - Claude Skill

一个专门用于 ShipAny 模板模块化提取与集成的 Claude Skill，帮助开发者根据产品需求选择性地提取和集成 ShipAny 的特定模块。

[English](#english) | [中文](#中文)

---

## 中文

### 📖 简介

ShipAny Module Master 是一个 Claude AI Skill，专门设计用于帮助开发者从 [ShipAny](https://shipany.ai) 模板中智能提取所需模块。

**💡 核心理念**

不同于直接使用完整模板，我们提倡**按需裁剪**的开发方式：
- 🎯 **只取所需** - 根据项目实际需求，仅提取必要的模块
- ⚡ **代码精简** - 避免冗余代码，保持项目轻量高效
- 🔧 **灵活组合** - 自由组合模块，打造最适合的技术栈
- 📈 **提升利用率** - 每个模块都有明确用途，避免资源浪费

ShipAny 是一个功能丰富的 Next.js AI SaaS 开发框架，包含着陆页、用户中心、管理后台、支付系统等 18+ 模块。通过模块化提取，你可以构建出真正符合产品需求的精简项目，而不是被迫接受整个庞大的模板。

**核心功能：**
- 🎯 智能识别项目所需模块
- 🔍 自动分析模块依赖关系
- 📋 生成详细的提取和集成计划
- ✅ 提供配置调整和验证指导

### 🚀 快速开始

#### 1. 下载 Skill

```bash
# 克隆仓库
git clone https://github.com/YOUR_USERNAME/shipany-module-master.git

# 或直接下载 ZIP
wget https://github.com/YOUR_USERNAME/shipany-module-master/archive/main.zip
```

#### 2. 在 Claude 中使用

**Claude.ai (网页版):**
1. 访问 [Claude.ai](https://claude.ai)
2. 点击项目设置 → Skills
3. 上传 `shipany-module-master` 文件夹或 ZIP 文件
4. 开始对话，提及需要提取的模块

**Claude Desktop:**
1. 打开 Claude Desktop
2. 进入 Settings → Skills
3. 添加 skill 文件夹路径
4. 重启 Claude Desktop

**Claude Code (VS Code):**
```bash
# 安装 skill
/plugin install shipany-module-master

# 使用 skill
# 直接在对话中提及 ShipAny 模块即可自动触发
```

#### 3. 使用示例

```
用户: 我想从 ShipAny 中提取用户中心和支付模块到我的项目

Claude: 我来帮你分析需要提取的模块和依赖关系...

📦 依赖分析：
✅ 请求的模块: user-center, payment
⚠️  必需依赖: database, auth
📋 总共需要提取: 4 个模块

接下来我会为你提供详细的提取步骤...
```

### 📦 支持的模块

#### 核心系统
- **着陆页** - 营销展示页面
- **用户中心** - 用户资料和设置
- **管理后台** - 后台管理系统

#### 基础设施
- **数据库** (drizzle-orm) - 数据持久化
- **认证** (better-auth) - 用户认证
- **权限控制** (RBAC) - 角色权限
- **国际化** (next-intl) - 多语言
- **主题系统** - 主题切换
- **文档系统** (fumadocs) - 文档
- **积分系统** - 用户积分

#### 扩展功能
- **支付** - Stripe/PayPal 集成
- **存储** - R2/S3 文件上传
- **邮件** - Resend 邮件服务
- **AI** - AI 生成功能
- **数据统计** - Analytics 集成
- **广告** - AdSense 集成
- **联盟营销** - Affiliate 系统
- **客服** - 在线客服集成

### 🛠️ 工具脚本

#### 依赖分析工具

```bash
# 分析模块依赖
python3 scripts/analyze-dependencies.py --modules user-center payment

# 包含可选依赖
python3 scripts/analyze-dependencies.py --modules landing-page --include-optional
```

#### 文档获取工具

```bash
# 更新 ShipAny 文档
python3 scripts/fetch_docs.py > references/shipany-docs.md
```

### 📚 文档结构

```
shipany-module-master/
├── SKILL.md                    # 英文版 Skill 指令
├── SKILL_zh.md                 # 中文版 Skill 指令
├── README.md                   # 本文件
├── references/                 # 参考文档
│   ├── modules-overview.md    # 模块详细说明
│   ├── shipany-docs.md        # ShipAny 官方文档
│   └── integration-guide.md   # 集成最佳实践
└── scripts/                    # 辅助工具
    ├── analyze-dependencies.py # 依赖分析
    └── fetch_docs.py           # 文档获取
```

### 💡 使用场景

**场景 1: 简单着陆页项目**
```
需求: 只需要一个营销页面
模块: 着陆页 + 国际化 + 主题
```

**场景 2: 用户认证系统**
```
需求: 需要用户登录和个人中心
模块: 数据库 + 认证 + 用户中心
```

**场景 3: 完整 SaaS 平台**
```
需求: 完整的 SaaS 产品
模块: 数据库 + 认证 + 权限 + 用户中心 + 管理后台 + 支付 + 积分
```

### 🤝 贡献

欢迎提交 Issue 和 Pull Request！

1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启 Pull Request

### 📄 许可证

MIT License - 详见 [LICENSE](LICENSE) 文件

### 🔗 相关链接

- [ShipAny 官网](https://shipany.ai)
- [ShipAny 文档](https://shipany.ai/docs)
- [Claude AI](https://claude.ai)
- [Claude Skills 文档](https://support.claude.com/en/articles/12512198-creating-custom-skills)

---

## English

### 📖 Introduction

ShipAny Module Master is a Claude AI Skill designed to help developers intelligently extract required modules from the [ShipAny](https://shipany.ai) template.

**💡 Core Philosophy**

Instead of using the entire template, we advocate for a **modular extraction** approach:
- 🎯 **Take Only What You Need** - Extract only necessary modules based on actual project requirements
- ⚡ **Lean Codebase** - Avoid redundant code, keep projects lightweight and efficient
- 🔧 **Flexible Composition** - Freely combine modules to build the perfect tech stack
- 📈 **Maximize Utilization** - Every module serves a clear purpose, eliminating waste

ShipAny is a feature-rich Next.js AI SaaS development framework with 18+ modules including landing pages, user centers, admin dashboards, and payment systems. Through modular extraction, you can build truly tailored projects that match your product needs, rather than being forced to accept a massive template.

**Core Features:**
- 🎯 Intelligently identify required modules
- 🔍 Automatically analyze module dependencies
- 📋 Generate detailed extraction and integration plans
- ✅ Provide configuration and verification guidance

### 🚀 Quick Start

#### 1. Download Skill

```bash
# Clone repository
git clone https://github.com/YOUR_USERNAME/shipany-module-master.git

# Or download ZIP
wget https://github.com/YOUR_USERNAME/shipany-module-master/archive/main.zip
```

#### 2. Use in Claude

**Claude.ai (Web):**
1. Visit [Claude.ai](https://claude.ai)
2. Click Project Settings → Skills
3. Upload `shipany-module-master` folder or ZIP file
4. Start conversation, mention modules to extract

**Claude Desktop:**
1. Open Claude Desktop
2. Go to Settings → Skills
3. Add skill folder path
4. Restart Claude Desktop

**Claude Code (VS Code):**
```bash
# Install skill
/plugin install shipany-module-master

# Use skill
# Simply mention ShipAny modules in conversation
```

#### 3. Usage Example

```
User: I want to extract user center and payment modules from ShipAny

Claude: Let me analyze the modules and dependencies...

📦 Dependency Analysis:
✅ Requested Modules: user-center, payment
⚠️  Required Dependencies: database, auth
📋 Total modules to extract: 4

I'll provide detailed extraction steps...
```

### 📦 Supported Modules

#### Core System
- **Landing Page** - Marketing showcase
- **User Center** - User profile and settings
- **Admin Dashboard** - Backend management

#### Infrastructure
- **Database** (drizzle-orm) - Data persistence
- **Auth** (better-auth) - User authentication
- **RBAC** - Role-based access control
- **Internationalization** (next-intl) - Multi-language
- **Themes** - Theme switching
- **Documentation** (fumadocs) - Docs system
- **Credits** - User credits system

#### Extensions
- **Payment** - Stripe/PayPal integration
- **Storage** - R2/S3 file upload
- **Email** - Resend email service
- **AI** - AI generation features
- **Analytics** - Analytics integration
- **Advertising** - AdSense integration
- **Affiliate** - Affiliate marketing
- **Customer Service** - Live chat integration

### 🛠️ Utility Scripts

#### Dependency Analyzer

```bash
# Analyze module dependencies
python3 scripts/analyze-dependencies.py --modules user-center payment

# Include optional dependencies
python3 scripts/analyze-dependencies.py --modules landing-page --include-optional
```

#### Documentation Fetcher

```bash
# Update ShipAny documentation
python3 scripts/fetch_docs.py > references/shipany-docs.md
```

### 📚 Documentation Structure

```
shipany-module-master/
├── SKILL.md                    # English Skill instructions
├── SKILL_zh.md                 # Chinese Skill instructions
├── README.md                   # This file
├── references/                 # Reference docs
│   ├── modules-overview.md    # Module details
│   ├── shipany-docs.md        # ShipAny official docs
│   └── integration-guide.md   # Integration best practices
└── scripts/                    # Utility tools
    ├── analyze-dependencies.py # Dependency analyzer
    └── fetch_docs.py           # Documentation fetcher
```

### 💡 Use Cases

**Scenario 1: Simple Landing Page**
```
Need: Just a marketing page
Modules: Landing Page + Internationalization + Themes
```

**Scenario 2: User Authentication System**
```
Need: User login and profile
Modules: Database + Auth + User Center
```

**Scenario 3: Full SaaS Platform**
```
Need: Complete SaaS product
Modules: Database + Auth + RBAC + User Center + Admin + Payment + Credits
```

### 🤝 Contributing

Issues and Pull Requests are welcome!

1. Fork the repository
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open Pull Request

### 📄 License

MIT License - see [LICENSE](LICENSE) file

### 🔗 Links

- [ShipAny Website](https://shipany.ai)
- [ShipAny Documentation](https://shipany.ai/docs)
- [Claude AI](https://claude.ai)
- [Claude Skills Documentation](https://support.claude.com/en/articles/12512198-creating-custom-skills)
