import random
import time

print("\n==============================")
print("🛡️ TETHER GUARDIAN AI")
print("AI Financial Safety Assistant")
print("==============================\n")

def analyze_transaction(amount, balance, trust_level):

    print("\nAnalyzing transaction...")
    time.sleep(1)

    risk_score = 0

    if amount > balance * 0.7:
        risk_score += 40

    if trust_level == "low":
        risk_score += 40
    elif trust_level == "medium":
        risk_score += 20

    risk_score += random.randint(0, 20)

    print("\n--- AI REPORT ---")
    print(f"Transaction Amount: ${amount}")
    print(f"Wallet Balance: ${balance}")
    print(f"Recipient Trust Level: {trust_level}")
    print(f"Risk Score: {risk_score}/100")

    print("\n--- DECISION ---")

    if risk_score >= 70:
        return "🚨 BLOCKED: High Risk Transaction"
    elif risk_score >= 40:
        return "⚠️ WARNING: Proceed with caution"
    else:
        return "✅ APPROVED: Safe transaction"


# APP INTERFACE
print("Welcome to your secure financial assistant.\n")

amount = float(input("💰 Enter amount to send: "))
balance = float(input("💳 Enter wallet balance: "))
trust = input("👤 Recipient trust level (low/medium/high): ")

result = analyze_transaction(amount, balance, trust)

print("\n==============================")
print("FINAL RESULT:", result)
print("==============================\n")

print("💡 Powered by Tether Guardian AI")
