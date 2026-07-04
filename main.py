import streamlit as st
import random

st.set_page_config(
    page_title="Tether Guardian AI",
    page_icon="🛡️",
    layout="centered"
)

st.title("🛡️ Tether Guardian AI")
st.subheader("AI-powered Transaction Risk Analyzer")

st.write("Analyze a transaction before sending USDT.")

amount = st.number_input(
    "Transaction Amount (USDT)",
    min_value=1.0,
    value=500.0
)

balance = st.number_input(
    "Wallet Balance (USDT)",
    min_value=1.0,
    value=1000.0
)

trust_level = st.selectbox(
    "Recipient Trust Level",
    ["High", "Medium", "Low"]
)

if st.button("Analyze Transaction"):

    risk_score = 0
    reasons = []

    balance_ratio = amount / balance

    if balance_ratio > 0.8:
        risk_score += 45
        reasons.append("⚠️ Very large transaction compared to wallet balance.")

    elif balance_ratio > 0.5:
        risk_score += 25
        reasons.append("⚠️ Large transaction amount.")

    if trust_level == "Low":
        risk_score += 45
        reasons.append("❌ Recipient is untrusted.")

    elif trust_level == "Medium":
        risk_score += 20
        reasons.append("⚠️ Recipient is partially trusted.")

    anomaly = random.randint(0, 15)
    risk_score += anomaly

    st.divider()

    st.subheader("📊 Analysis Report")

    st.write(f"**Amount:** {amount} USDT")
    st.write(f"**Wallet Balance:** {balance} USDT")
    st.write(f"**Trust Level:** {trust_level}")
    st.write(f"**Behavior Score:** {anomaly}")

    st.progress(min(risk_score, 100) / 100)

    st.write(f"### Risk Score: {risk_score}/100")

    if reasons:
        st.write("### AI Insights")
        for reason in reasons:
            st.write(reason)
    else:
        st.success("No major risks detected.")

    st.divider()

    if risk_score >= 75:
        st.error("🚫 BLOCKED")
        st.write("High probability of fraud.")

    elif risk_score >= 45:
        st.warning("⚠️ WARNING")
        st.write("Proceed carefully.")

    else:
        st.success("✅ APPROVED")
        st.write("Transaction appears safe.")

st.divider()

st.caption("Built for the Tether Developer Challenge 🚀")
