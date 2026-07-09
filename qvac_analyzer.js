/**
 * FanShield AI Local Analyzer
 * QVAC-ready architecture
 */

export function analyzeMessage(message) {
    const text = message.toLowerCase();

    if (
        text.includes("seed phrase") ||
        text.includes("private key") ||
        text.includes("send usdt") ||
        text.includes("claim reward") ||
        text.includes("wallet verification")
    ) {
        return {
            verdict: "HIGH RISK",
            reason: "Possible crypto scam detected."
        };
    }

    if (
        text.includes("urgent") ||
        text.includes("limited time") ||
        text.includes("click here")
    ) {
        return {
            verdict: "SUSPICIOUS",
            reason: "Message contains common scam indicators."
        };
    }

    return {
        verdict: "SAFE",
        reason: "No obvious scam indicators detected."
    };
}