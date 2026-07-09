/**
 * QVAC Local Analysis Module
 * Tether FanShield AI
 */

import { loadModel, completion } from "@qvac/sdk";

export async function analyzeMessage(message) {
  const model = await loadModel("qvac-small");

  const prompt = `
You are a football scam detector.

Classify this message as:
- SAFE
- SUSPICIOUS
- HIGH RISK

Explain why.

Message:
${message}
`;

  const result = await completion(model, prompt);

  return result.text;
} */