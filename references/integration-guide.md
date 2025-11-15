# ShipAny 模块集成最佳实践指南

## 集成前准备

### 1. 环境检查
- Next.js 版本兼容性（主分支需要 16+，cf 分支需要 15.5.5）
- Node.js 版本（推荐 18+）
- 包管理器（pnpm 推荐）
- 数据库准备（如需要）

### 2. 项目结构规划
```
your-project/
├── app/                    # Next.js App Router
├── components/             # 共享组件
├── lib/                    # 工具库和配置
│   ├── db/                # 数据库（如需要）
│   ├── auth/              # 认证（如需要）
│   └── ...
├── public/                 # 静态资源
└── styles/                 # 样式文件
```

## 模块集成顺序

### 阶段 1: 基础设施（如需要）
1. **数据库 (Database)**
   - 复制 `/lib/db/*`
   - 复制 `drizzle.config.ts`
   - 配置 `DATABASE_URL`
   - 运行迁移: `pnpm db:push`

2. **认证 (Auth)**
   - 复制 `/lib/auth/*`
   - 复制 `/app/api/auth/[...all]/route.ts`
   - 配置 `BETTER_AUTH_SECRET` 和 `BETTER_AUTH_URL`
   - 测试登录流程

3. **权限控制 (RBAC)** - 可选
   - 复制 `/lib/rbac/*`
   - 配置角色和权限
   - 更新数据库 schema

### 阶段 2: 核心功能
4. **国际化 (Internationalization)** - 推荐
   - 复制 `/messages/*`
   - 复制 `/lib/i18n/*`
   - 更新 `next.config.js`
   - 配置支持的语言

5. **主题系统 (Themes)** - 推荐
   - 复制 `/styles/*`
   - 更新 `tailwind.config.ts`
   - 复制主题切换组件

### 阶段 3: 业务模块
6. **按需集成业务模块**
   - 着陆页
   - 用户中心
   - 管理后台
   - 其他扩展模块

## 详细集成步骤

### 数据库模块集成

**文件清单:**
```
lib/db/
├── index.ts              # 数据库连接
├── schema.ts             # 数据表定义
└── migrations/           # 迁移文件
drizzle.config.ts         # Drizzle 配置
```

**步骤:**
1. 复制文件到目标项目
2. 安装依赖: `pnpm add drizzle-orm @neondatabase/serverless`
3. 配置环境变量:
   ```env
   DATABASE_URL=postgresql://user:pass@host:5432/dbname
   ```
4. 运行迁移: `pnpm drizzle-kit push`

**验证:**
```bash
# 测试数据库连接
pnpm tsx -e "import { db } from './lib/db'; console.log(await db.query.users.findMany())"
```

### 认证模块集成

**文件清单:**
```
lib/auth/
├── config.ts             # Better Auth 配置
├── client.ts             # 客户端 hooks
└── server.ts             # 服务端工具
app/api/auth/[...all]/route.ts  # API 路由
```

**步骤:**
1. 复制文件到目标项目
2. 安装依赖: `pnpm add better-auth`
3. 配置环境变量:
   ```env
   BETTER_AUTH_SECRET=your-secret-key
   BETTER_AUTH_URL=http://localhost:3000
   ```
4. 更新数据库 schema（如果使用数据库）

**验证:**
```bash
# 访问认证端点
curl http://localhost:3000/api/auth/session
```

### 用户中心模块集成

**文件清单:**
```
app/(user)/
├── layout.tsx            # 用户中心布局
└── user/
    ├── profile/          # 个人资料
    ├── settings/         # 设置
    └── ...
components/user/          # 用户相关组件
```

**依赖检查:**
- ✅ 数据库已配置
- ✅ 认证已配置
- ✅ 主题系统已配置（推荐）

**步骤:**
1. 复制 `app/(user)/*` 目录
2. 复制 `components/user/*` 组件
3. 检查并更新导入路径
4. 测试用户中心页面

### 支付模块集成

**文件清单:**
```
lib/payment/
├── stripe.ts             # Stripe 集成
├── webhook.ts            # Webhook 处理
└── types.ts              # 类型定义
app/api/payment/
├── checkout/route.ts     # 创建支付
└── webhook/route.ts      # Webhook 端点
```

**依赖检查:**
- ✅ 数据库已配置
- ✅ 认证已配置
- ⚠️ 积分系统（可选）

**步骤:**
1. 复制支付相关文件
2. 安装依赖: `pnpm add stripe`
3. 配置环境变量:
   ```env
   STRIPE_SECRET_KEY=sk_test_...
   STRIPE_WEBHOOK_SECRET=whsec_...
   STRIPE_PUBLISHABLE_KEY=pk_test_...
   ```
4. 配置 Stripe Webhook（生产环境）
5. 测试支付流程

## 配置文件调整

### next.config.js
```javascript
// 如果使用国际化
const withNextIntl = require('next-intl/plugin')();

module.exports = withNextIntl({
  // 其他配置
});
```

### tailwind.config.ts
```typescript
// 确保包含所有模块的路径
content: [
  './app/**/*.{js,ts,jsx,tsx,mdx}',
  './components/**/*.{js,ts,jsx,tsx,mdx}',
  './lib/**/*.{js,ts,jsx,tsx,mdx}',
]
```

### package.json
```json
{
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "db:push": "drizzle-kit push",
    "db:studio": "drizzle-kit studio"
  }
}
```

## 常见问题排查

### 导入路径错误
**问题:** `Module not found: Can't resolve '@/lib/...'`

**解决:**
1. 检查 `tsconfig.json` 中的路径别名
2. 确保所有依赖模块都已复制
3. 重启开发服务器

### 数据库连接失败
**问题:** `Error: connect ECONNREFUSED`

**解决:**
1. 验证 `DATABASE_URL` 格式正确
2. 确保数据库服务正在运行
3. 检查网络连接和防火墙设置

### 认证不工作
**问题:** 登录后立即退出

**解决:**
1. 检查 `BETTER_AUTH_SECRET` 是否设置
2. 验证 `BETTER_AUTH_URL` 与实际域名匹配
3. 清除浏览器 cookies 重试

### 样式不生效
**问题:** 组件样式丢失

**解决:**
1. 确保 Tailwind 配置包含所有组件路径
2. 检查 `globals.css` 是否正确导入
3. 验证主题系统是否正确配置

## 测试清单

### 基础功能测试
- [ ] 页面正常加载
- [ ] 路由导航正常
- [ ] 样式显示正确
- [ ] 国际化切换正常（如使用）

### 认证功能测试
- [ ] 用户注册
- [ ] 用户登录
- [ ] 会话保持
- [ ] 退出登录
- [ ] 权限验证（如使用 RBAC）

### 业务功能测试
- [ ] 用户中心访问
- [ ] 数据读写
- [ ] 支付流程（如使用）
- [ ] 文件上传（如使用）
- [ ] 邮件发送（如使用）

## 性能优化建议

1. **代码分割**
   - 使用动态导入 `next/dynamic`
   - 按路由分割代码

2. **图片优化**
   - 使用 `next/image` 组件
   - 配置图片域名白名单

3. **数据库优化**
   - 添加适当的索引
   - 使用连接池
   - 实施查询缓存

4. **缓存策略**
   - 配置 Next.js 缓存
   - 使用 Redis（生产环境）
   - 实施 CDN 缓存

## 部署注意事项

### Vercel 部署
1. 配置环境变量
2. 设置数据库连接
3. 配置 Webhook URLs

### Cloudflare Workers 部署
1. 使用 `cf` 分支代码
2. 配置 Cloudflare 绑定
3. 调整不兼容的 API

### VPS + Dokploy 部署
1. 配置 Docker 环境
2. 设置反向代理
3. 配置 SSL 证书

## 维护建议

1. **定期更新**
   - 关注 ShipAny 更新
   - 更新依赖包
   - 应用安全补丁

2. **文档记录**
   - 记录自定义修改
   - 维护模块清单
   - 更新环境变量文档

3. **备份策略**
   - 定期备份数据库
   - 版本控制代码
   - 保存配置文件
