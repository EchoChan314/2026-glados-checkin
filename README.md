# 🎁 5 分钟配置 GLaDOS 自动签到

<div align="center">

**你不用写代码 · 不用买服务器 · 不用每天登录**

**一次配置，每天 9:30 自动签到；失败自动重试**

---

### ✨ 为什么选择本项目？

| 优势                  | 说明                                                |
| --------------------- | --------------------------------------------------- |
| ✅ **2026年验证可用** | 持续通过 Actions 日志和单元测试验证                 |
| ✅ **结果可信**       | 正确区分签到完成、重复签到和真实失败                |
| ✅ **新手友好**       | 全程图解，不会也能照着做                            |
| ✅ **作者持续维护**   | 遇到问题提Issue，作者很乐意帮忙                     |

---

### 📱 签到成功预览

![签到成功示例](images/success.jpg)

> **每天签到能获得 +12 ~ +20 积分，累积可兑换会员时长！**

---

### 🚀 3 步完成自动签到

```text
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│   ① Fork 项目    ──→  点一下右上角 Fork 按钮                 │
│                                                             │
│   ② 配置 Cookie  ──→  浏览器复制一下，贴到 GitHub Secrets    │
│                                                             │
│   ③ 启用 Actions  ──→  手动测试一次，之后每天自动运行         │
│                                                             │
│   ✅ 完成！每天自动签到 + 微信通知                            │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**[👉 点击开始配置](#-快速部署)**

---

[![Auto Checkin](https://github.com/lankerr/2026-glados-checkin/actions/workflows/checkin.yml/badge.svg)](https://github.com/lankerr/2026-glados-checkin/actions)
[![GitHub Stars](https://img.shields.io/github/stars/lankerr/2026-glados-checkin?style=social)](https://github.com/lankerr/2026-glados-checkin)

**⭐ 觉得有用？点个 Star 支持一下！**

</div>

---

## 💡 重要说明

> 默认只使用仓库内置的 **GitHub Actions** 定时任务，无需创建外部 cron。
>
> 本项目每月自动提交一次保活时间戳，避免公开仓库因 60 天无活动而停用计划任务。
>
> `cron-job.org` 仅作为可选备用方案。**内置 schedule 与外部 cron 二选一**，同时启用会重复签到和重复通知。
>
> 已经 Fork 很久的用户需要先点击 **Sync fork → Update branch**，再重新启用 Actions。

---

## 🔥 为什么你需要这个？

> > **⚠️ 重要：如果你使用其他签到脚本失败，显示 "please checkin via [https://glados.cloud](https://glados.cloud)"，请使用本项目！**

GLaDOS 在 2026 年初进行了 API 更新，**绝大多数旧签到脚本已失效**。我们通过抓包分析发现了问题：

| 问题       | 旧脚本                  | 本项目（已修复）           |
| ---------- | ----------------------- | -------------------------- |
| 签到 Token | `glados.one` ❌         | `glados.cloud` ✅          |
| 域名支持   | rocks/network ❌        | cloud ✅                   |
| 签到结果   | "please checkin via..." | "Checkin!" 或 "Repeats" ✅ |

<details>
<summary><b>🔬 技术细节：我们是怎样修复问题的（感兴趣的看）</b></summary>

### 🔬 我们的探索过程

#### 问题现象

- GitHub Actions 可以正常运行
- 推送消息显示 "成功0/1"
- 签到结果始终为 "please checkin via https://glados.cloud"
- 手动点击签到按钮正常，但机器人签到无效

#### 排查步骤

1️⃣ **浏览器抓包分析**

- 使用 Chrome DevTools 抓取真实签到请求
- 对比浏览器请求和 Python 脚本请求的差异

2️⃣ **尝试的方案（失败）**

- ❌ 添加更多 Headers（sec-ch-ua、sec-fetch-\* 等）
- ❌ 使用 requests.Session 保持会话
- ❌ 使用 curl_cffi 模拟浏览器 TLS 指纹
- ❌ 添加代理配置

3️⃣ **最终发现**
通过对比不同 token 值的请求结果：

```python
# 失败 ❌
{'token': 'glados.one'}  → "please checkin via https://glados.cloud"

# 成功 ✅
{'token': 'glados.cloud'} → "Checkin Repeats! Please Try Tomorrow"
```

**问题根源**：GLaDOS 更新了 API，签到 token 必须从 `glados.one` 改为 `glados.cloud`！

</details>

---

> **📢 重要提示**
>
> - GLaDOS 官网已迁移至 **glados.cloud**（不再是 glados.rocks）
> - 本项目专为 2026 积分制度优化，每天自动签到一次
> - 完全免费，使用 GitHub Actions，无需自己的服务器
> - 不会的话可以提 Issue，作者很乐意帮助技术新手！

---

## ✨ 功能特点

| 功能            | 说明                            |
| --------------- | ------------------------------- |
| 🎯 **精准积分** | 获取真实积分数据 + 每日变化量   |
| 🎁 **兑换提示** | 显示当前可兑换选项及差额        |
| ⏰ **每日一次** | 北京时间 9:30 自动签到          |
| 🔄 **失败重试** | 最多尝试三次，最终失败才报警    |
| 📱 **微信推送** | PushPlus 漂亮 HTML 报告         |
| ☁️ **2026 API** | 适配最新 glados.cloud API       |
| 🔧 **持续维护** | 发现问题及时修复                |

---

## 🛠 配置参数 (环境变量)

本项目支持以下环境变量配置：

| 变量名               | 必填  | 说明                                                                       |
| -------------------- | ----- | -------------------------------------------------------------------------- |
| `GLADOS_COOKIE`      | ✅ 是 | GLaDOS 的 Cookie。多个账号请用 `&` 或换行符分隔。                          |
| `PUSHPLUS_TOKEN`     | ❌ 否 | PushPlus 微信推送 Token。                                                  |
| `TELEGRAM_BOT_TOKEN` | ❌ 否 | Telegram 机器人的 Token（例如 `123456:ABC-DEF1234...`）                    |
| `TELEGRAM_CHAT_ID`   | ❌ 否 | 接收推送的 Telegram Chat ID                                                |
| `PUSH_LEVEL`         | ❌ 否 | 推送级别：`fail_only`（默认，仅失败推送）或 `all`（每次均推送）            |

---

<details>
<summary><b>📚 给小白的科普：什么是 Fork、Cookie、Secrets？（新手必看）</b></summary>

> 💡 如果你已经熟悉这些概念，可以跳过这部分直接看 [快速部署](#-快速部署)

<details>
<summary><b>🍴 什么是 Fork？</b></summary>

**Fork** = 把别人的项目复制一份到你自己的账号下。

就像复印一份文档，原件还在别人那里，你有一份自己的副本可以随便改。Fork 之后这个项目就属于你了，你可以自己配置和使用。

</details>

<details>
<summary><b>🍪 什么是 Cookie？</b></summary>

**Cookie** = 网站记住你是谁的"通行证"。

当你登录 GLaDOS 后，网站会给你的浏览器一个"通行证"（Cookie），下次访问时浏览器出示这个通行证，网站就知道你是谁了。

我们需要把这个通行证告诉签到程序，这样程序就能"假装"是你去签到。

</details>

<details>
<summary><b>🔐 什么是 Secrets？</b></summary>

**Secrets** = 保险箱，用来存放敏感信息。

你的 Cookie 和 Token 都是隐私信息，不能直接写在代码里（否则别人都能看到）。GitHub Secrets 就像一个保险箱，把这些敏感信息锁起来，只有你的程序运行时才能访问。

</details>

<details>
<summary><b>⚙️ 什么是 GitHub Actions？</b></summary>

**GitHub Actions** = 免费的自动化机器人。

它可以按照你设定的时间表（比如每天 9:30）自动运行程序。你不需要自己的服务器，GitHub 会免费帮你跑代码。

</details>

<details>
<summary><b>▶️ 什么是 Run workflow？</b></summary>

**Run workflow** = 手动测试按钮。

| 按钮             | 作用                                               |
| ---------------- | -------------------------------------------------- |
| **Run workflow** | 选择 `dispatch_source: manual` 后立即执行一次，用于测试配置是否正确 |
| **定时任务**     | 每天 9:30 自动执行，不需要手动操作                 |

简单说：点 Run workflow 是**测试**，以后会**自动运行**。

</details>
</details>

---

## 🚀 快速部署

### 第一步：Fork 本仓库

点击页面右上角的 **Fork** 按钮，将项目复制到你的账号下。

---

### 第二步：获取 Cookie 🍪

> ⚠️ **注意**：GLaDOS 官网已迁移到 **[https://glados.cloud](https://glados.cloud)**，请使用新域名！

#### 2.1 安装 Cookie 扩展

在 **Edge 浏览器** 的扩展商店搜索 `Cookie-Editor`，安装 Cookie 管理扩展：

![Cookie-Editor 扩展](images/cookie-extension.png)

> 💡 **提示**：以下任意一个扩展都可以使用，只要能显示 `koa:sess` 和 `koa:sess.sig` 这两个 Cookie 就行！

![可选的 Cookie 扩展](images/cookie-alternative.png)

#### 2.2 登录 GLaDOS 并获取 Cookie

1. 打开 [https://glados.cloud](https://glados.cloud) 并登录
2. 进入 **签到页面**（Console → Checkin）
3. 点击浏览器右上角的 **Cookie-Editor** 扩展图标
4. 找到并复制这两个值：
   - `koa:sess` → 一串很长的字符串
   - `koa:sess.sig` → 一串较短的字符串

![获取 Cookie](images/glados-cookies.png)

#### 2.3 组合 Cookie（重要！）

将两个值按以下格式组合，**注意格式必须完全正确**：

```text
koa:sess=你的长字符串; koa:sess.sig=你的短字符串
```

**正确示例**：

```text
koa:sess=eyJ1c2VySWQiOjEyMzQ1Njc4OTB9; koa:sess.sig=abcdef123456
```

**常见错误**：

- ❌ 缺少分号 `;`
- ❌ 缺少空格（分号后需要一个空格）
- ❌ 值两边多了引号
- ❌ 复制了多余的空格或换行

#### 2.4 验证你的 Cookie 格式

运行以下 Python 代码验证格式是否正确：

```python
# 将你的 Cookie 粘贴到下面的引号中
cookie = "koa:sess=你的长字符串; koa:sess.sig=你的短字符串"

# 验证
if "koa:sess=" in cookie and "koa:sess.sig=" in cookie and "; " in cookie:
    parts = cookie.split("; ")
    if len(parts) == 2 and parts[0].startswith("koa:sess=") and parts[1].startswith("koa:sess.sig="):
        print("✅ Cookie 格式正确！")
    else:
        print("❌ 格式错误，请检查分号和空格")
else:
    print("❌ Cookie 缺少必要的字段")
```

---

### 第三步：配置 GitHub Secrets 🔐

1. 进入你 Fork 的仓库
2. 点击 **Settings**（设置）
3. 左侧菜单找到 **Secrets and variables** → **Actions**
4. 点击右上角 **New repository secret**

![添加 Secret](images/add-secret.png)

添加以下两个 Secret：

| Name             | Value                    | 必需  |
| ---------------- | ------------------------ | ----- |
| `GLADOS_COOKIE`  | 第二步组合的 Cookie      | ✅ 是 |
| `PUSHPLUS_TOKEN` | 微信推送 Token（见下方） | ❌ 否 |

---

### 第四步：获取 PushPlus Token（可选）📱

如果你希望签到后收到**微信通知**，请配置 PushPlus：

1. 访问 [https://www.pushplus.plus](https://www.pushplus.plus)
2. 点击右上角 **登录**，使用微信扫码登录

![PushPlus 扫码登录](images/pushplus-checkin.png)

3. 登录后点击 **发送消息** → **一对一消息**
4. 复制页面上显示的 **Token**（类似 `05c3****dd36` 的字符串）

![获取 Token](images/pushplus-token.png)

5. 将 Token 添加到 GitHub Secrets，Name 填 `PUSHPLUS_TOKEN`

---

### 第五步：启用 Actions ⚡

1. 进入你 Fork 仓库的 **Actions** 标签页
2. 如果看到黄色提示，点击 **I understand my workflows, go ahead and enable them**
3. 点击左侧的 **GLaDOS 2026 Checkin**
4. 点击右侧 **Run workflow**，选择 `dispatch_source: manual` 后手动测试一次

![启用 Actions](images/workflow.png)

> [!IMPORTANT]
>
> 完成首次手动测试后，内置 schedule 会每天运行。请勿再配置相同时间的外部 cron，否则会重复执行。
>
> 新版要求 API 调用显式传入 `dispatch_source`；旧版仅发送 `{"ref":"main"}` 的外部任务不会再执行签到，可直接在 cron-job.org 删除。

---

## ⭐ 可选备用：cron-job.org

只有在你的网络环境或 GitHub 计划任务长期不触发时才需要外部 cron。使用它时，请删除或注释 `.github/workflows/checkin.yml` 中的 `schedule`，确保只保留一个调度器。

### 配置步骤

#### 第一步：获取 GitHub Personal Access Token

1. 访问 [https://github.com/settings/tokens](https://github.com/settings/tokens)
2. 推荐点击 **Generate new token** → **Fine-grained personal access token**
3. Repository access 只选择你自己的 `2026-glados-checkin` Fork
4. Repository permissions → **Actions: Read and write**
5. 生成后立即复制；不要把 Token 发到 Issue、截图或写入仓库

> 使用 classic PAT 时，此接口需要 `repo` scope；`workflow` scope 主要用于修改 workflow 文件，并不是调用 dispatch 接口的替代权限。优先使用权限更小的 fine-grained PAT。

#### 第二步：注册 cron-job.org

1. 访问 [https://cron-job.org](https://cron-job.org) 注册账号（免费）
2. 注册后登录，点击 **Create Cronjob** 创建任务

#### 第三步：创建签到任务（9:30）

![创建 Cron 任务](images/create_corn_job.png)

按照以下配置填写：

**基本信息**：

| 选项      | 填写                                                                                                   |
| --------- | ------------------------------------------------------------------------------------------------------ |
| **Title** | `GLaDOS 早签到`                                                                                        |
| **URL**   | `https://api.github.com/repos/你的用户名/2026-glados-checkin/actions/workflows/checkin.yml/dispatches` |

> ⚠️ **重要**：把 `你的用户名` 改成你的 GitHub 用户名！比如 `lankerr`

**执行时间**：选择每天 **09:30**（Asia/Shanghai 时区）

**高级配置**（点击 Advanced 展开）：

![高级配置](images/cron_advanced.png)

| 选项               | 值            |
| ------------------ | ------------- |
| **Request method** | POST          |
| **Time zone**      | Asia/Shanghai |

**请求头（Headers）**：点击 "+ 添加" 添加三行：

| Key             | Value                            |
| --------------- | -------------------------------- |
| `Accept`        | `application/vnd.github+json`     |
| `Authorization` | `Bearer 你复制的GitHub_Token`     |
| `Content-Type`  | `application/json`               |

> Authorization 示例只应写成占位形式：`Bearer github_pat_xxx`。不要公开真实 Token。

**请求体（Request body）**：选择 Raw Body，填入：

```json
{ "ref": "main", "inputs": { "dispatch_source": "external" } }
```

![常用配置预览](images/cron_common.png)

配置完成后点击 **Save** 保存。

#### 第四步：测试验证

1. 在任务列表点击 **Test run** 测试
2. 当前 GitHub API 成功时会返回 **200**；旧 API 版本可能返回 **204**，两者都代表 dispatch 已接受 ✅

![测试成功](images/cron_success.png)

3. 到 GitHub 仓库的 **Actions** 页面查看，应该有新的运行记录

---

### 🚨 常见陷阱与错误

| 错误                         | 现象         | 原因                   | 解决方法                                       |
| ---------------------------- | ------------ | ---------------------- | ---------------------------------------------- |
| **401 Unauthorized**         | 认证失败     | Authorization 格式错误 | 使用 `Bearer github_pat_xxx`                    |
| **422 Unprocessable Entity** | 请求无法处理 | Body 缺少 ref 或必填 input | 按上面的完整 Request body 填写                 |
| **404 Not Found**            | 找不到工作流 | Actions 未启用或文件不存在 | 先完成 Fork、启用 Actions 并手动运行一次      |
| Accept 被截断                | 配置错误     | 输入框显示不全         | 完整值：`application/vnd.github.v3+json`       |
| Token 有空格                 | 认证失败     | Token 被意外截断       | Token 是连续字符串，中间不能有空格             |
| 权限不足                     | 403 错误     | Token 无 Actions 写权限 | fine-grained PAT 设置 Actions: Read and write  |

> 💡 **小贴士**：遇到 401/422 错误时，先检查上面三行 Headers 是否完全正确！

**🎉 完成！** 外部 cron 会每天 9:30 触发一次。记得关闭内置 schedule，避免重复运行。

---

## 💻 本地/独立服务器部署教程

如果你有自己的长期运行的电脑（如树莓派、软路由、VPS 等），也可以非常简单地在本地运行：

### 第一步：安装依赖

首先确保你已经安装了 Python 3，然后安装依赖库：

```bash
git clone https://github.com/你的用户名/2026-glados-checkin.git
cd 2026-glados-checkin
pip install -r requirements.txt
```

### 第二步：配置并运行

使用环境变量传递 Cookie 并直接运行 Python 脚本：

```bash
# 配置 Cookie
export GLADOS_COOKIE="koa:sess=xxxxxx; koa:sess.sig=yyyyyy"

# 可选：配置推送
export PUSH_LEVEL="all"
export TELEGRAM_BOT_TOKEN="xxx"
export TELEGRAM_CHAT_ID="yyy"

# 执行签到
python3 checkin.py
```

### 第三步：设置定时任务 (Cron)

通过 `crontab -e` 配置每天自动执行（例如每天早上 9:30）：

```bash
30 9 * * * export GLADOS_COOKIE="koa:sess=xxx..."; cd /path/to/2026-glados-checkin && python3 checkin.py >> glados.log 2>&1
```

---

## ❄️ NixOS 服务配置

本项目提供了标准的 Nix Flake，你可以直接作为 inputs 引入，系统会自动管理 Python 环境和依赖包。

### 使用方法 (Flakes)

在你的 [`flake.nix`](flake.nix) 中引入本项目：

```nix
{
  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    glados-checkin.url = "github:lankerr/2026-glados-checkin"; # 若本地测试可改写为 path:/绝对路径
  };

  outputs = { self, nixpkgs, glados-checkin, ... }: {
    nixosConfigurations.my-server = nixpkgs.lib.nixosSystem {
      system = "x86_64-linux";
      modules = [
        # 引入 glados-checkin 的 NixOS 模块
        glados-checkin.nixosModules.default

        ({ config, pkgs, ... }: {
          # 配置服务
          services.glados-checkin = {
            enable = true;
            cookie = "koa:sess=xxx; koa:sess.sig=yyy";

            # 【可选】消息推送配置
            pushLevel = "all"; # 或 "fail_only"
            pushplusToken = "xxx";
            telegramBotToken = "yyy";
            telegramChatId = "zzz";
          };
        })
      ];
    };
  };
}
```

部署配置后执行 `sudo nixos-rebuild switch --flake .#my-server`，签到任务即会自动注册为 systemd timers。

---

## 📊 推送效果预览

签到成功后，你会在微信收到类似这样的推送：

```text
👤 your@email.com

当前积分: 46 (+20)
剩余天数: 353 天
签到结果: Bindweed! Bindweed!

🎁 兑换选项:
❌ 100分→10天 (差54分)
❌ 200分→30天 (差154分)
❌ 500分→100天 (差454分)
```

---

## ⏰ 自动运行时间

| 时间（北京时间） | 说明     |
| ---------------- | -------- |
| **09:30**        | 早间签到 |

> 默认使用 GitHub Actions；脚本内部最多尝试三次。外部 cron 是备用方案，不应与内置 schedule 同时启用。

---

## ❓ 常见问题

<details>
<summary><b>Q: GitHub Actions 会不会在两个月后停止？</b></summary>

GitHub 官方规则是：公开仓库连续 **60 天没有仓库活动**时，计划任务会自动停用。计划任务还可能因高负载延迟，尤其是在整点附近。

本项目的 `.github/workflows/keep-alive.yml` 每月更新一次 `.github/last-active.txt`，早于 60 天期限。若你是旧 Fork：

1. 点击 **Sync fork → Update branch**。
2. 打开 Actions，选择两个 workflow，确认状态为 Enabled。
3. 手动运行一次 `GLaDOS 2026 Checkin` 验证 Cookie。

[GitHub 官方 schedule 说明](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows#schedule)

</details>

<details>
<summary><b>Q: cron-job.org 测试返回 401/404/422 错误怎么办？</b></summary>

请对照以下检查：

**401 Unauthorized（认证失败）**：

```text
❌ Authorization: github_pat_xxx
✅ Authorization: Bearer github_pat_xxx
```

注意：`Bearer ` 前缀后面必须有一个**空格**。

**404 Not Found**：先完成 Fork，在 GitHub Actions 页面启用工作流并手动运行一次；同时确认 URL 中的用户名和仓库名正确。

**422 Unprocessable Entity（请求无法处理）**：

```text
❌ Body: {"ref": "main"}
✅ Body: {"ref": "main", "inputs": {"dispatch_source": "external"}}
```

本工作流要求同时指定分支名和 `dispatch_source`，用来阻止旧外部定时器继续重复签到。

**其他检查**：

- Accept 头是否完整：`application/vnd.github+json`
- Fine-grained PAT 是否有目标仓库的 `Actions: Read and write` 权限
- Token 是否过期（检查 Expiration 设置）

[🔝 查看完整陷阱列表](#-常见陷阱与错误)

</details>

<details>
<summary><b>Q: 显示 "please checkin via https://glados.cloud" 怎么办？</b></summary>

这表示你使用的签到脚本已过期！GLaDOS 在 2026 年更新了 API，旧脚本的 token 值 `glados.one` 已失效。

**解决方案**：使用本项目，我们已经修复了这个问题（token 改为 `glados.cloud`）。

</details>

<details>
<summary><b>Q: 显示 "Checkin Repeats! Please Try Tomorrow" 是什么意思？</b></summary>

这表示**今天已经成功签到过了**！这是正常的成功响应，说明签到功能正常工作。

</details>

<details>
<summary><b>Q: Cookie 多久过期？</b></summary>

没有固定保证。退出登录、修改密码、服务端会话策略变化都可能让 Cookie 提前失效。Actions 真正失败并提示登录/认证问题时，重新获取 Cookie 并更新 `GLADOS_COOKIE` 即可。

</details>

<details>
<summary><b>Q: 支持多个账号吗？</b></summary>

支持！用英文符号 `&` 分隔多个 Cookie：

```text
cookie1&cookie2&cookie3
```

</details>

<details>
<summary><b>Q: 没有收到微信推送怎么办？</b></summary>

1. 检查 `PUSHPLUS_TOKEN` 是否配置正确
2. 在 PushPlus 网站测试发送功能是否正常
3. 查看 Actions 运行日志是否有错误

PushPlus 完全可选，不影响签到。若 PushPlus 当前要求实名认证而你不想认证，可以删除 `PUSHPLUS_TOKEN`，或改用可选的 Telegram 推送；实名认证规则由 PushPlus 决定，本项目无法绕过。

</details>

<details>
<summary><b>Q: 为什么一天运行多次、收到多条通知？</b></summary>

通常是同时启用了 GitHub 内置 schedule 和 cron-job.org。请二选一；本项目默认只需内置 schedule。新版默认 `PUSH_LEVEL=fail_only`，正常完成时不会反复推送。

</details>

<details>
<summary><b>Q: 积分、兑换天数和流量怎么算？</b></summary>

本项目只读取 GLaDOS API 返回的积分、剩余天数和兑换选项，不制定会员或流量规则。服务条款可能变化，请以 GLaDOS 控制台当时显示的套餐与兑换页面为准；README 不对固定积分、流量或天数作长期承诺。

</details>

<details>
<summary><b>Q: Actions 运行失败怎么办？</b></summary>

1. 点击失败的运行记录查看详细日志
2. 检查 Cookie 格式是否正确
3. 如果还是不行，欢迎提 Issue！

</details>

---

## ⚠️ 运行机制与限制

GitHub 的 schedule 不是实时调度器：高负载时可能延迟，极端情况下可能丢弃排队任务；公开仓库连续 60 天无活动会自动停用 schedule。为降低风险，本项目采用非整点运行、脚本内三次重试和每月一次保活提交。

这仍不能保证第三方服务 100% 可用：GLaDOS 宕机、Cookie 失效、GitHub 故障或用户自行关闭 Actions 时，签到会失败。新版会让真正失败返回非零退出码，以便 Actions 邮件和可选通知准确报警。

---

## 📂 项目文件

| 文件                                                                         | 说明                |
| ---------------------------------------------------------------------------- | ------------------- |
| [`checkin.py`](checkin.py)                                                     | 核心签到脚本        |
| `.github/workflows/checkin.yml`                                              | GitHub Actions 配置 |
| [`requirements.txt`](requirements.txt)                                        | Python 依赖         |
| `tests/`                                                                       | 结果判断与重试测试  |
| `images/`                                                                    | 教程截图            |

---

## 🤝 需要帮助？

- 📝 **提 Issue**：遇到问题请提 Issue，作者很乐意帮助技术新手！
- ⭐ **Star**：如果对你有帮助，请点个 Star 支持一下
- 🍴 **Fork**：欢迎 Fork 并贡献代码

---

## 📝 更新日志

### v1.2.0 (2026-08-05)

- 识别 `Today's observation logged...` 等 2026 正常返回，不再显示“成功 0/1”
- 失败自动重试三次，最终失败返回非零退出码
- 默认仅失败推送，避免多个调度器造成通知轰炸
- 每天一次签到、每月一次保活，替代每天保活提交
- 修正 workflow dispatch 的 PAT 权限、HTTP 状态码和 404 排障说明

### v1.1.0 (2026-01-25) 🔥 重大修复

**问题**：签到始终返回 "please checkin via https://glados.cloud"，导致机器人无法签到。

**原因**：GLaDOS 官方更新了 API，签到 token 必须从 `glados.one` 改为 `glados.cloud`。

**修复**：更新 [`checkin.py`](checkin.py) 中的 token 参数。

**排查过程**：

1. 使用浏览器 DevTools 抓包分析真实签到请求
2. 对比 Python 脚本与浏览器请求的差异
3. 尝试添加 Headers、模拟 TLS 指纹等方案（均无效）
4. 最终通过测试不同 token 值发现问题根源

> 💡 如果你在使用其他签到项目遇到同样问题，可以参考本项目的修复方案！

### v1.0.0 (2026-01-20)

- 初始版本发布
- 支持 glados.cloud 域名
- PushPlus 微信推送
- GitHub Actions 自动签到

---

## 📝 License

MIT

---

<div align="center">

**Made with ❤️ for GLaDOS users in 2026**

**🔧 本项目最近一次维护验证：2026-08-05**

**⭐ Star 一下，支持作者持续更新！⭐**

</div>
