# ShipAny 模块详细概览

## 模块分类

### 1. 核心系统 (Core System)

#### 1.1 着陆页 (Landing Page)
- **功能**: 产品展示、营销页面
- **位置**: `/app/(landing)/page.tsx`
- **依赖**:
  - 国际化 (next-intl)
  - 主题系统 (themes)
- **独立性**: 可独立使用
- **配置文件**:
  - `app/(landing)/layout.tsx`
  - `components/landing/*`

#### 1.2 用户中心 (User Center)
- **功能**: 用户个人信息管理、设置
- **位置**: `/app/(user)/user/*`
- **依赖**:
  - 登录鉴权 (better-auth) - 必需
  - 数据库 (drizzle-orm) - 必需
  - 权限控制 (rbac) - 可选
- **独立性**: 需要认证系统支持
- **配置文件**:
  - `app/(user)/layout.tsx`
  - `components/user/*`

#### 1.3 管理后台 (Admin Dashboard)
- **功能**: 后台管理、数据统计
- **位置**: `/app/(admin)/admin/*`
- **依赖**:
  - 登录鉴权 (better-auth) - 必需
  - 权限控制 (rbac) - 必需
  - 数据库 (drizzle-orm) - 必需
- **独立性**: 需要完整的认证和权限系统
- **配置文件**:
  - `app/(admin)/layout.tsx`
  - `components/admin/*`

### 2. 核心模块 (Core Modules)

#### 2.1 数据库 (drizzle-orm)
- **功能**: 数据持久化、ORM
- **位置**: `/lib/db/*`
- **依赖**: 无
- **被依赖**: 几乎所有模块
- **配置文件**:
  - `drizzle.config.ts`
  - `lib/db/schema.ts`
  - `.env` 中的数据库连接配置

#### 2.2 登录鉴权 (better-auth)
- **功能**: 用户认证、会话管理
- **位置**: `/lib/auth/*`
- **依赖**:
  - 数据库 (drizzle-orm) - 必需
- **被依赖**: 用户中心、管理后台
- **配置文件**:
  - `lib/auth/config.ts`
  - `app/api/auth/[...all]/route.ts`

#### 2.3 权限控制 (rbac)
- **功能**: 角色权限管理
- **位置**: `/lib/rbac/*`
- **依赖**:
  - 登录鉴权 (better-auth) - 必需
  - 数据库 (drizzle-orm) - 必需
- **被依赖**: 管理后台
- **配置文件**:
  - `lib/rbac/permissions.ts`

#### 2.4 国际化 (next-intl)
- **功能**: 多语言支持
- **位置**: `/messages/*`, `/lib/i18n/*`
- **依赖**: 无
- **被依赖**: 所有页面组件
- **配置文件**:
  - `next.config.js` (i18n 配置)
  - `messages/en.json`, `messages/zh.json`

#### 2.5 多主题切换 (themes)
- **功能**: 主题样式管理
- **位置**: `/lib/themes/*`, `/styles/*`
- **依赖**: 无
- **被依赖**: 所有 UI 组件
- **配置文件**:
  - `tailwind.config.ts`
  - `app/globals.css`

#### 2.6 文档系统 (fumadocs)
- **功能**: 产品文档展示
- **位置**: `/app/(docs)/docs/*`
- **依赖**:
  - 国际化 (next-intl) - 可选
- **独立性**: 可独立使用
- **配置文件**:
  - `content/docs/*`
  - `fumadocs.config.ts`

#### 2.7 积分系统 (credits)
- **功能**: 用户积分管理
- **位置**: `/lib/credits/*`
- **依赖**:
  - 数据库 (drizzle-orm) - 必需
  - 登录鉴权 (better-auth) - 必需
- **被依赖**: 支付系统
- **配置文件**:
  - `lib/credits/config.ts`

### 3. 扩展模块 (Extension Modules)

#### 3.1 支付 (payment)
- **功能**: 支付集成 (Stripe/Creem/PayPal)
- **位置**: `/lib/payment/*`
- **依赖**:
  - 数据库 (drizzle-orm) - 必需
  - 登录鉴权 (better-auth) - 必需
  - 积分系统 (credits) - 可选
- **独立性**: 需要认证系统
- **配置文件**:
  - `lib/payment/stripe.ts`
  - `app/api/payment/*/route.ts`
  - `.env` 中的支付密钥

#### 3.2 存储 (storage)
- **功能**: 文件上传 (R2/S3)
- **位置**: `/lib/storage/*`
- **依赖**:
  - 登录鉴权 (better-auth) - 可选
- **独立性**: 可独立使用
- **配置文件**:
  - `lib/storage/config.ts`
  - `.env` 中的存储配置

#### 3.3 邮件 (email)
- **功能**: 邮件发送 (Resend)
- **位置**: `/lib/email/*`
- **依赖**: 无
- **独立性**: 可独立使用
- **配置文件**:
  - `lib/email/templates/*`
  - `.env` 中的邮件配置

#### 3.4 AI 生成 (ai)
- **功能**: AI 功能集成
- **位置**: `/lib/ai/*`
- **依赖**:
  - 积分系统 (credits) - 可选
  - 登录鉴权 (better-auth) - 可选
- **独立性**: 可独立使用
- **配置文件**:
  - `lib/ai/providers/*`
  - `.env` 中的 AI API 密钥

#### 3.5 数据统计 (analytics)
- **功能**: 访问统计
- **位置**: `/lib/analytics/*`
- **依赖**: 无
- **独立性**: 可独立使用
- **配置文件**:
  - `app/layout.tsx` (脚本注入)
  - `.env` 中的统计 ID

#### 3.6 广告 (advertising)
- **功能**: 广告展示 (AdSense)
- **位置**: `/components/ads/*`
- **依赖**: 无
- **独立性**: 可独立使用
- **配置文件**:
  - `.env` 中的广告 ID

#### 3.7 联盟营销 (affiliate)
- **功能**: 推广返佣
- **位置**: `/lib/affiliate/*`
- **依赖**:
  - 数据库 (drizzle-orm) - 必需
  - 登录鉴权 (better-auth) - 必需
- **独立性**: 需要认证系统
- **配置文件**:
  - `lib/affiliate/config.ts`

#### 3.8 客服 (customer-service)
- **功能**: 在线客服 (Tawk/Crisp)
- **位置**: `/components/customer-service/*`
- **依赖**: 无
- **独立性**: 可独立使用
- **配置文件**:
  - `app/layout.tsx` (脚本注入)
  - `.env` 中的客服配置

## 模块依赖关系图

```
数据库 (drizzle-orm)
  ├─→ 登录鉴权 (better-auth)
  │     ├─→ 权限控制 (rbac)
  │     │     └─→ 管理后台
  │     ├─→ 用户中心
  │     ├─→ 积分系统 (credits)
  │     │     └─→ 支付 (payment)
  │     └─→ 联盟营销 (affiliate)
  │
  └─→ 积分系统 (credits)

国际化 (next-intl) → 所有页面

主题系统 (themes) → 所有 UI 组件

独立模块:
  - 着陆页 (可选依赖国际化、主题)
  - 文档系统 (可选依赖国际化)
  - 存储 (storage)
  - 邮件 (email)
  - AI 生成 (ai)
  - 数据统计 (analytics)
  - 广告 (advertising)
  - 客服 (customer-service)
```

## 模块提取优先级

### 最小可用配置
1. 着陆页 + 国际化 + 主题系统

### 基础用户系统
1. 数据库
2. 登录鉴权
3. 用户中心
4. 国际化
5. 主题系统

### 完整管理系统
1. 数据库
2. 登录鉴权
3. 权限控制
4. 管理后台
5. 用户中心

### 电商/SaaS 系统
1. 数据库
2. 登录鉴权
3. 积分系统
4. 支付系统
5. 用户中心
