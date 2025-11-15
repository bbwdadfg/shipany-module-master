---
name: shipany-module-master
description: Specialized skill for modular extraction and integration of ShipAny template components. Use this skill when users need to selectively extract specific modules (landing page, user center, admin dashboard, payment system, etc.) from the ShipAny template and integrate them into their own projects based on product requirements.
---

# ShipAny Module Master

## Overview

To extract and integrate specific modules from the ShipAny template into custom projects, use this skill. ShipAny is a comprehensive Next.js-based AI SaaS development framework with rich built-in modules. This skill helps identify required modules, analyze dependencies, and guide the extraction process.

## When to Use This Skill

Use this skill when:
- Starting a new project that needs only specific ShipAny modules
- Adding ShipAny functionality to an existing project
- Understanding ShipAny's modular architecture
- Planning which modules to include based on product requirements
- Analyzing dependencies between ShipAny modules

## Core Workflow

### Step 1: Requirement Analysis

To begin, understand the project requirements:

1. **Identify needed functionality**
   - What features does the product need?
   - Which ShipAny modules provide these features?
   - Are there any specific constraints (budget, timeline, technical)?

2. **Consult module overview**
   - Read `references/modules-overview.md` for complete module descriptions
   - Identify primary modules needed
   - Note any optional enhancements

### Step 2: Dependency Analysis

To ensure extracted modules work correctly, analyze dependencies:

1. **Check module dependencies**
   - Review the dependency graph in `references/modules-overview.md`
   - Identify all required dependencies for selected modules
   - Note optional dependencies that enhance functionality

2. **Use dependency analysis script**
   ```bash
   python3 scripts/analyze-dependencies.py --modules landing-page user-center
   ```

3. **Validate completeness**
   - Ensure all required dependencies are included
   - Decide on optional dependencies based on requirements

### Step 3: Module Extraction Planning

To create an extraction plan:

1. **List all modules to extract**
   - Primary modules (user-requested)
   - Required dependencies
   - Optional enhancements

2. **Identify file locations**
   - Refer to module overview for file paths
   - Note configuration files needed
   - List environment variables required

3. **Plan integration order**
   - Start with foundational modules (database, auth)
   - Add dependent modules progressively
   - End with UI/feature modules

### Step 4: Extraction Guidance

To guide the extraction process:

1. **For each module, provide:**
   - Exact file/directory paths to copy
   - Configuration files to modify
   - Environment variables to set
   - Dependencies to install (npm packages)

2. **Configuration adjustments:**
   - Update import paths if needed
   - Modify configuration files for the target project
   - Remove unused module references

3. **Integration verification:**
   - List files to check after extraction
   - Provide test commands to verify functionality
   - Suggest debugging steps if issues arise

## Module Categories

### Core System Modules
- **Landing Page**: Marketing/product showcase page (minimal dependencies)
- **User Center**: User profile and settings (requires auth + database)
- **Admin Dashboard**: Backend management (requires auth + rbac + database)

### Core Infrastructure Modules
- **Database (drizzle-orm)**: Data persistence (no dependencies, required by most modules)
- **Auth (better-auth)**: User authentication (requires database)
- **RBAC**: Role-based access control (requires auth + database)
- **Internationalization (next-intl)**: Multi-language support (no dependencies)
- **Themes**: Theme switching (no dependencies)
- **Documentation (fumadocs)**: Documentation system (optional i18n)
- **Credits**: User credits system (requires auth + database)

### Extension Modules
- **Payment**: Stripe/Creem/PayPal integration (requires auth + database)
- **Storage**: R2/S3 file upload (optional auth)
- **Email**: Resend email service (no dependencies)
- **AI**: AI generation features (optional credits + auth)
- **Analytics**: Google Analytics/Plausible/etc (no dependencies)
- **Advertising**: AdSense integration (no dependencies)
- **Affiliate**: Affiliate marketing (requires auth + database)
- **Customer Service**: Tawk/Crisp chat (no dependencies)

## Common Extraction Scenarios

### Scenario 1: Simple Landing Page
**Modules needed:**
- Landing Page
- Internationalization (optional)
- Themes (optional)

**Extraction steps:**
1. Copy `/app/(landing)/*` directory
2. Copy theme configuration from `/styles/*` and `tailwind.config.ts`
3. Copy i18n messages if using internationalization
4. Update `next.config.js` for i18n if needed

### Scenario 2: User Authentication System
**Modules needed:**
- Database (drizzle-orm)
- Auth (better-auth)
- User Center
- Internationalization
- Themes

**Extraction steps:**
1. Set up database: Copy `/lib/db/*`, `drizzle.config.ts`
2. Set up auth: Copy `/lib/auth/*`, `/app/api/auth/*`
3. Copy user center: `/app/(user)/*`
4. Copy shared components: `/components/user/*`
5. Configure environment variables for database and auth
6. Run database migrations

### Scenario 3: Full SaaS Platform
**Modules needed:**
- Database
- Auth
- RBAC
- User Center
- Admin Dashboard
- Credits
- Payment
- Email

**Extraction steps:**
1. Foundation: Database + Auth + RBAC
2. User features: User Center + Credits
3. Payment integration: Payment module + webhooks
4. Admin features: Admin Dashboard
5. Communication: Email templates
6. Configure all environment variables
7. Set up payment provider webhooks

## Best Practices

### Before Extraction
1. Read ShipAny documentation in `references/shipany-docs.md`
2. Review module overview in `references/modules-overview.md`
3. Create a checklist of required modules
4. Verify target project compatibility (Next.js version, etc.)

### During Extraction
1. Extract modules in dependency order (foundation first)
2. Copy entire module directories to maintain structure
3. Update import paths systematically
4. Test each module after integration before adding the next

### After Extraction
1. Remove unused ShipAny references
2. Update package.json with only needed dependencies
3. Clean up unused configuration
4. Test all integrated functionality
5. Document any customizations made

## Resources

### references/
- **modules-overview.md**: Complete module descriptions and dependencies
- **shipany-docs.md**: Official ShipAny documentation
- **integration-guide.md**: Best practices for module integration

### scripts/
- **analyze-dependencies.py**: Automated dependency analysis tool
- **fetch_docs.py**: Documentation fetcher utility
