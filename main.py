import re, sys

SCAM_PHRASES = [r"free (match|final|vip) ticket", r"vip ticket", r"final match ticket", r"claim your (free|refund|prize|ticket)", r"send .*usdt.*to (claim|receive|unlock|reserve)", r"official ticket refund", r"official fifa", r"official tournament", r"official (club|fan zone)", r"exclusive hospitality", r"parking pass", r"merchandise discount", r"verify your wallet", r"limited time.*claim", r"you (have|has) won", r"congratulations.*selected", r"guaranteed match prediction", r"pay .* to unlock your (winnings|ticket|prize)", r"reserve your (seat|ticket)", r"act now", r"urgent.*wallet", r"cheap (match|final|vip) ticket", r"discount ticket", r"official (fifa|uefa|club) giveaway", r"telegram admin", r"whatsapp support"]
URGENCY_WORDS = ["urgent", "immediately", "act now", "limited time", "hurry", "last chance", "expires soon", "today only"]
FAKE_DOMAIN_HINTS = ["-win.", "-free.", "-ticket.", "-giveaway.", "-reward.", ".xyz", ".top", ".site", ".club"]

def looks_like_valid_address(address):
    address = address.strip()
    return bool(re.match(r"^0x[a-fA-F0-9]{40}$", address) or re.match(r"^T[a-zA-Z0-9]{33}$", address))

def check_domain(text):
    text_lower = text.lower()
    return [h for h in FAKE_DOMAIN_HINTS if h in text_lower]

def analyze_message(message):
    ml = message.lower()
    flags = [p for p in SCAM_PHRASES if re.search(p, ml)]
    urgency = [w for w in URGENCY_WORDS if w in ml]
    domains = check_domain(message)
    score = len(flags) * 2 + len(urgency) + len(domains) * 2
    return score, flags, urgency, domains

def analyze_address(address):
    if not address.strip():
        return None, "No wallet address provided."
    if not looks_like_valid_address(address):
        return False, "This does not match a standard wallet address format (Ethereum 0x... or TRON T...). Be cautious."
    return True, "Address format looks structurally valid (this does not confirm ownership or legitimacy)."

def get_verdict(score):
    if score >= 5:
        return "HIGH RISK - This strongly resembles a known tournament ticket scam. Do NOT send USDT."
    elif score >= 2:
        return "SUSPICIOUS - Some scam warning signs detected. Verify through official channels before sending."
    return "LOW RISK - No common scam patterns detected. Still verify independently before sending funds."

def print_reasons(flags, urgency, domains):
    print("Reasons:")
    print(f"  [{'x' if flags else ' '}] Scam phrase pattern detected ({len(flags)} match(es))" if flags else "  [ ] No scam phrase patterns matched")
    print(f"  [x] Urgency language detected: {', '.join(urgency)}" if urgency else "  [ ] No urgency language detected")
    print(f"  [x] Suspicious domain pattern(s): {', '.join(domains)}" if domains else "  [ ] No suspicious domain patterns detected")

def run():
    print("=" * 55)
    print("  TETHER FANSHIELD AI - Tournament Scam Checker")
    print("=" * 55)
    print("Paste a message and/or wallet address to check for scams.")
    print("(Press Enter to skip either field)\n")
    message = input("Message text: ").strip()
    address = input("Wallet address: ").strip()
    print("\n--- Analysis ---\n")
    if message:
        score, flags, urgency, domains = analyze_message(message)
        print_reasons(flags, urgency, domains)
        print(f"\n{get_verdict(score)}\n")
    else:
        print("No message provided - skipping message scan.\n")
    if address:
        valid, note = analyze_address(address)
        print("Wallet address check:")
        print(f"  {note}\n")
    else:
        print("No address provided - skipping address check.\n")
    print("Reminder: This tool flags patterns, it does not guarantee safety.")
    print("Always verify ticket sales, refunds, and prizes through official")
    print("club/tournament channels before sending USDT.\n")

if __name__ == "__main__":
    try:
        run()
    except KeyboardInterrupt:
        print("\nExiting Tether FanShield AI.")
        sys.exit(0)
