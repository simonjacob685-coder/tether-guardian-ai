import { analyzeMessage } from "./qvac_analyzer.js";

export async function checkBeforeSending(message, walletAddress) {
    const aiResult = await analyzeMessage(message);

    return {
        wallet: walletAddress,
        verdict: aiResult,
        action:
            aiResult.includes("HIGH RISK")
                ? "BLOCK TRANSACTION"
                : aiResult.includes("SUSPICIOUS")
                ? "ASK USER TO CONFIRM"
                : "ALLOW TRANSACTION"
    };
}