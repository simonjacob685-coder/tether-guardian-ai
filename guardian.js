import { analyzeMessage } from "./qvac_analyzer.js";

export async function checkBeforeSending(message, walletAddress) {
  const ai = await analyzeMessage(message, walletAddress);
  
  let action = ai.text === "HIGH RISK" ? "BLOCK TRANSACTION" :
               ai.text === "SUSPICIOUS" ? "ASK USER TO CONFIRM" : 
               "ALLOW TRANSACTION";

  return {
    status: "success",
    verdict: ai.text,
    reason: ai.reason,
    action: action,
    wallet: walletAddress ? walletAddress.substring(0, 10) + "..." : null,
    timestamp: new Date().toISOString()
  };
}

// Run test
checkBeforeSending("Send 50 USDT to claim your free VIP ticket now!", "0x1234567890abcdef")
  .then(console.log);// === TEST WHEN RUN DIRECTLY ===
if (import.meta.url === `file://${process.argv[1]}`) {
  console.log("🛡️ Tether FanShield AI Test\n");
  checkBeforeSending("Send 50 USDT to claim your free VIP ticket now!", "0x1234567890abcdef")
    .then(console.log)
    .catch(console.error);
}