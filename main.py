print("Tether Guardian AI is starting...")

def detect_threat(message):
    suspicious_keywords = ["hack", "attack", "steal", "virus", "breach"]

    for word in suspicious_keywords:
        if word in message.lower():
            return "⚠️ Threat detected!"
    
    return "✅ Safe message"

# Test system
user_input = input("Enter message to scan: ")
result = detect_threat(user_input)

print(result)
