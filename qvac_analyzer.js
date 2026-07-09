export async function analyzeMessage(message, walletAddress = null) {
  const lower = message.toLowerCase().trim();
  
  const highRiskPatterns = [
    /claim.*(free|vip|prize|refund|ticket)/i,
    /send.*usdt.*(now|urgent|fast)/i,
    /official.*(merch|link|deal)/i,
    /double your.*(money|usdt)/i
  ];

  const suspiciousPatterns = [
    /my friend|trust me|support|verify.*wallet/i,
    /send first|help me send/i
  ];

  if (highRiskPatterns.some(p => p.test(lower))) {
    return {
      text: "HIGH RISK",
      reason: "Matches common tournament scams (fake prizes, urgency tactics)"
    };
  }
  
  if (suspiciousPatterns.some(p => p.test(lower))) {
    return {
      text: "SUSPICIOUS",
      reason: "Social engineering language detected - verify before sending"
    };
  }

  return {
    text: "SAFE",
    reason: "No scam patterns detected. Seems safe."
  };
}