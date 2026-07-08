# 🛡️⚽ Tether FanShield AI

**AI-powered wallet safety assistant for football tournament fans.**

Built for the **Tether Developers Cup 2026** — WDK (Wallets) track.

---

## 🎯 Problem

During major football tournaments, scammers flood fans with fake ticket
refunds, fake prize claims, and fake "official" merchandise deals — all
designed to trick people into sending USDT to a scammer's wallet.

Most fans have no easy way to check if a message or wallet address is
safe before sending money. Existing security tools are too technical
for everyday users who just want to know: *"Is this safe to send to?"*

---

## 💡 Solution

**Tether FanShield AI** checks a message and/or wallet address **before**
a user sends any USDT, and gives a clear, plain-language risk verdict:

- ✅ **Low Risk** — no known scam patterns detected
- ⚠️ **Suspicious** — some warning signs found, verify before sending
- 🚨 **High Risk** — strongly matches known tournament scam patterns

Built using the **Tether Wallet Development Kit (WDK)** for real,
self-custodial wallet generation and balance checks — the user always
stays in control of their own funds and decisions.

---

## ✨ Features

- 🔍 Scans messages for known tournament-scam phrases (fake ticket
  refunds, fake prize claims, urgency tactics, fake giveaways)
- 🏦 Checks wallet address formatting for basic red flags
- 👛 Real self-custodial wallet generation and balance checks via WDK
- 🗣️ Plain-language explanations with clear reasons for every verdict
- 📱 Built entirely on a mobile phone via GitHub Codespaces
- ⚡ Fast, local, no external API calls required for scam detection

---

## 🛠️ Technology Stack

- Python 3 (scam detection engine)
- Node.js + Tether WDK (`@tetherto/wdk`, `@tetherto/wdk-wallet-evm`)
- Regex-based pattern analysis engine
- GitHub Codespaces (mobile-built development, zero laptop used)

---

## 🚀 How It Works

**Scam Detection (`main.py`):**
1. User pastes a suspicious message (e.g. *"Send 50 USDT to claim your
   free VIP match ticket now!"*)
2. User optionally pastes the wallet address they were asked to send to
3. The tool scans for known scam phrase patterns, urgency language, and
   suspicious domain patterns
4. A clear risk verdict is shown with explainable reasons, so the user
   can decide safely — no funds are ever moved by the tool itself

**Wallet Safety (`wallet_check.js`):**
1. Generates a real self-custodial wallet using Tether's WDK
2. Retrieves the wallet address and checks its balance
3. Demonstrates genuine self-custody — the user holds their own keys,
   not Tether, not FanShield, not any exchange

---

## ▶️ Running the Project

**Scam checker:**
```bash
python3 main.py
## 👨‍💻 Developer

**Simon Yakubu**
GitHub: [https://github.com/simonjacob685-coder](https://github.com/simonjacob685-coder)
## 📄 License

MIT License