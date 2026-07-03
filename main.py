import random

print("🛡️ Tether Guardian AI is running...\n")

def analyze_transaction(amount, balance, recipient_trust_level):
    print("Analyzing transaction...\n")

    risk_score = 0

    # Rule 1: Large amount risk
    if amount > balance * 0.7:
        risk_score += 40

    # Rule 2: Unknown recipient
    if recipient_trust_level == "low":
        risk_score += 40
    elif recipient_trust_level == "medium":
        risk_score += 20

    # Rule 3: Random AI uncertainty (simulated AI behavior)
    risk_score += random.randint(0, 20)

    print(f"Risk Score: {risk_score}/100")

    if risk_score >= 70:
        return "🚨 HIGH RISK: Transaction blocked"
    elif risk_score >= 40:
        return "⚠️ MEDIUM RISK: Proceed with caution"
    else:
        return "✅ SAFE: Transaction approved"


# Demo test
amount = float(input("Enter amount to send: "))
balance = float(input("Enter your wallet balance: "))
trust = input("Recipient trust level (low/medium/high): ")

result = analyze_transaction(amount, balance, trust)

print("\nResult:", result)
