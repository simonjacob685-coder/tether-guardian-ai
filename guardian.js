import { analyzeMessage } from "./qvac_analyzer.js";

export function checkBeforeSending(message, walletAddress) {
    const result = analyzeMessage(message);

    return {
        wallet: walletAddress,
        verdict: result.verdict,
        reason: result.reason,
        action:
            result.verdict === "HIGH RISK"
                ? "BLOCK TRANSACTION"
                : result.verdict === "SUSPICIOUS"
                ? "ASK USER TO CONFIRM"
                : "ALLOW TRANSACTION"
    };
}