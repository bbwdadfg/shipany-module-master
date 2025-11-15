Fetching: https://shipany.ai/docs
Fetching: https://shipany.ai/docs/quick-start
Fetching: https://shipany.ai/docs/database
Fetching: https://shipany.ai/docs/auth
Fetching: https://shipany.ai/docs/payment


# Page: https://shipany.ai/docs

Introduction
What is ShipAny?
ShipAny is an AI SaaS development framework based on NextJS, with built-in rich components and business functions to help you quickly release your own product.
The current documentation is for the usage instructions of ShipAny Two, the usage instructions of ShipAny One please refer to
ShipAny One documentation
.
ShipAny Two
ShipAny Two is the second version of ShipAny, with extremely rich features, including the following parts:
Core system
Landing page（Landing Page）
User center（User Center）
Management background（Admin Dashboard）
Core modules（core）
Database（drizzle-orm）
Login authentication（better-auth）
Permission control（rbac）
Internationalization（next-intl）
Theme switching（themes）
Documentation system（fumadocs）
Credits system（credits）
Extension modules（extensions）
Payment（payment）
Supports stripe / creem / paypal
Storage（storage）
Supports cloudflare r2 / aws s3
Email（email）
Supports resend
AI generation（ai）
Supports openrouter / replicate / fal / kie
Data statistics（analytics）
Supports google analytics / clarity / plausible / openpanel / vercel analytics
Advertising（advertising）
Supports adsense
Affiliate marketing（affiliate）
Supports affonso / promotekit
Customer service（customer-service）
Supports tawk / crisp


# Page: https://shipany.ai/docs/quick-start

Quick Start
Before using ShipAny, please ensure you have
obtained ShipAny
and have access to the ShipAny Two code repository.
Local Development
Project Initialization
Pull ShipAny Two source code
git
clone
git@github.com:shipanyai/shipany-template-two
my-shipany-project
The default branch is
main
, which supports
nextjs 16
version, and can be deployed on Vercel, or through VPS + Dokploy deployment.
If you need to deploy on Cloudflare Workers, please pull the code from the
cf
branch, this branch is based on
nextjs 15.5.5
, and does not support
nextjs 16
git
clone
-b
cf
git@github.com:shipanyai/shipany-template-two
my-shipany-project
Install dependencies
# Enter the project root directory
cd
my-shipany-project
# Install dependencies
pnpm
install
Preview project
pnpm
dev
After executing the above command, the local development server will be started, and you can click the URL address output to preview the project.
Generally, the local preview address is:
http://localhost:3000
Configure environment variables
Create configuration file
Use the following command to copy a configuration file, which is used to configure the local development environment variables
cp
.env.example
.env.development
Modify environment variable values
# app
NEXT_PUBLIC_APP_URL =
"http://localhost:3000"
NEXT_PUBLIC_APP_NAME =
"ShipAny Two"
# theme
NEXT_PUBLIC_THEME =
"default"
# appearance
NEXT_PUBLIC_APPEARANCE =
"system"
# database
DATABASE_URL =
""
DATABASE_PROVIDER =
"postgresql"
DB_SINGLETON_ENABLED =
"true"
# auth secret
# openssl rand -base64 32
AUTH_SECRET =
""
Required items:
NEXT_PUBLIC_APP_URL
：Local development address. Copy the URL address output after the project starts and fill in
NEXT_PUBLIC_APP_NAME
：Application name. Change it to your project name
Optional items:
NEXT_PUBLIC_THEME
：Project theme. The default is
default
, which will display the landing page from the
src/themes/default
folder. If you have a custom landing page requirement, you can modify this option.
NEXT_PUBLIC_APPEARANCE
：Project appearance. The default is
system
, which will automatically switch based on the system theme. You can set it to
light
or
dark
to control the default appearance of the project.
DATABASE_URL
：Database connection URL. If you need user login, management background, etc., you need to configure this item.
DATABASE_PROVIDER
：Database provider. Currently only supports
postgresql
. Supports
supabase
,
neon
and other cloud databases and self-hosted PostgreSQL databases.
DB_SINGLETON_ENABLED
：Database singleton mode. The default is
true
, which will reuse the database connection. If deployed on Cloudflare Workers and other Serverless platforms, it needs to be set to
false
.
AUTH_SECRET
：Authentication secret. If you need to use login authentication, you need to configure this item.
You can generate a random key using the following command:
openssl
rand
-base64
32
Configure database
If you need to use login authentication, management background, etc., the project depends on the database, you need to configure the database according to the following steps
Create database
You can create a database on the
supabase
,
neon
and other cloud database platforms, and get the remote connection URL of the cloud database, similar to this:
# supabase remote database connection URL example
postgresql://postgres.xxx:xxxxxx@aws-0-ap-southeast-1.pooler.supabase.com:6543/postgres
You can also use a self-hosted PostgreSQL database, and get the database connection URL, similar to this:
# Self-hosted PostgreSQL database connection URL example
postgresql://aigc:aigc2025@127.0.0.1:5432/shipany_two
It is recommended to use a self-hosted PostgreSQL database for local development, and use a cloud database for online deployment.
Set environment variables
Fill in the database connection URL obtained in the previous step into the environment variable
DATABASE_URL
.
DATABASE_URL =
"postgresql://user:password@host:port/db"
DATABASE_PROVIDER =
"postgresql"
DB_SINGLETON_ENABLED =
"true"
Migrate database tables
Execute the following command to migrate the database tables
pnpm
db:generate
pnpm
db:migrate
The database connection defaults to the
DATABASE_URL
variable in the
.env.development
file.
It is recommended to migrate the database tables to the self-hosted database for local development, and migrate the database tables to the remote database before online deployment.
Configure administrator permissions
ShipAny has a built-in management system and access control based on permissions (RBAC), you need to complete the database configuration steps above, and then execute the following command to initialize the permission configuration:
Initialize permissions
pnpm
rbac:init
Register administrator account
Visit
http://your-domain/admin
to enter the management system, the first time you visit will encounter a login intercept, you need to register an administrator account through email first, such as
admin@xxx.com
Assign super administrator permissions
Execute the following command to assign super administrator permissions to the newly registered account
pnpm
rbac:assign
--
--email=admin@xxx.com
--role=super_admin
Visit the management background
Visit
http://your-domain/admin
again, use the administrator account to log in, and you can enter the management background.


# Page: https://shipany.ai/docs/database

Database
Database


# Page: https://shipany.ai/docs/auth

Authorization
Authorization


# Page: https://shipany.ai/docs/payment

Payment
Payment
