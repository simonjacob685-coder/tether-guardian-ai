import streamlit as st
import random

st.set_page_config(page_title="Tether Guardian AI", page_icon="🛡️")

st.title("🛡️ Tether Guardian AI")
st.write("Analyze a transaction before sending USDT.")

amount = st.number_input("Transaction Amount ($)", min_value=0.0)
balance = st.number_input("Wallet Balance ($)", min_value=1.0)
trust = st.selectbox("Recipient Trust Level", ["low", "medium", "high"])

if st.button("Analyze Transaction"):

    risk_score = 0
    reasons = []

    ratio = amount / balance

    if ratio > 0.8:
        risk_score += 45
        reasons.append("Very large transaction.")
    elif ratio > 0.5:
        risk_score += 25
        reasons.append("Large transaction.")

    trust_map = {
        "low":45,
        "medium":20,
        "high":5
    }

    risk_score += trust_map[trust]

    anomaly = random.randint(0,15)
    risk_score += anomaly

    st.subheader("Risk Report")
    st.write("Risk Score:", risk_score)

    if reasons:
        st.write("Reasons:")
        for r in reasons:
            st.write("-", r)

    if risk_score >= 75:
        st.error("🚨 BLOCKED")
    elif risk_score >= 45:
        st.warning("⚠️ WARNING")
    else:
        st.success("✅ APPROVED")
