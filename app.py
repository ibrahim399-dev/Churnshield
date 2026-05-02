import streamlit as st

# Simple rule-based predictor
def predict_churn(tenure, monthly_charges, senior_citizen, contract, internet_service):
    risk_score = 0
    reasons = []

    # Contract type
    if contract == "Month-to-month":
        risk_score += 40
        reasons.append("📋 Month-to-month contract — no commitment!")
    elif contract == "One year":
        risk_score += 10
        reasons.append("📋 One year contract — some commitment")

    # Monthly charges
    if monthly_charges > 70:
        risk_score += 25
        reasons.append("💰 High monthly charges!")
    elif monthly_charges > 50:
        risk_score += 10
        reasons.append("💰 Moderate monthly charges")

    # Tenure
    if tenure < 12:
        risk_score += 20
        reasons.append("📅 New customer — less loyalty!")
    elif tenure < 24:
        risk_score += 10
        reasons.append("📅 Relatively new customer")

    # Senior citizen
    if senior_citizen == "Yes":
        risk_score += 10
        reasons.append("👤 Senior citizen — higher risk group")

    # Internet service
    if internet_service == "Fiber optic":
        risk_score += 5
        reasons.append("🌐 Fiber optic users churn more!")

    return risk_score, reasons

# Page config
st.set_page_config(
    page_title="ChurnShield",
    page_icon="🛡️",
    layout="centered"
)

# Header
st.title("🛡️ ChurnShield")
st.subheader("Customer Churn Prediction App")
st.write("Built by **Ajayi Ibrahim Ademola** — Data Science & ML, AAUA")
st.write("---")

# Input section
st.subheader("📊 Enter Customer Details")

col1, col2 = st.columns(2)

with col1:
    tenure = st.slider("📅 Tenure (months)", 0, 72, 12)
    monthly_charges = st.number_input("💰 Monthly Charges ($)", 0.0, 200.0, 50.0)
    senior_citizen = st.selectbox("👤 Senior Citizen?", ["No", "Yes"])

with col2:
    contract = st.selectbox("📋 Contract Type", ["Month-to-month", "One year", "Two year"])
    internet_service = st.selectbox("🌐 Internet Service", ["DSL", "Fiber optic", "No"])
    payment_method = st.selectbox("💳 Payment Method", ["Bank transfer", "Credit card", "Electronic check", "Mailed check"])

st.write("---")

# Customer summary
st.subheader("👤 Customer Profile Summary")
col3, col4, col5 = st.columns(3)
col3.metric("Tenure", f"{tenure} months")
col4.metric("Monthly Bill", f"${monthly_charges}")
col5.metric("Contract", contract.split()[0])

st.write("---")

# Predict button
if st.button("🔍 Predict Churn Risk", use_container_width=True):
    score, reasons = predict_churn(tenure, monthly_charges,
                                   senior_citizen, contract,
                                   internet_service)

    st.write("---")
    st.subheader("📈 Risk Analysis")

    # Probability bar
    st.write(f"**Overall Risk Score: {score}/100**")
    if score >= 60:
        st.progress(score/100)
        st.error(f"⚠️ VERY HIGH RISK — {score}% chance of churning!")
        recommendation = "🚨 **Action Required:** Offer special discount or upgrade immediately!"
    elif score >= 40:
        st.progress(score/100)
        st.warning(f"🟡 HIGH RISK — {score}% chance of churning!")
        recommendation = "📞 **Action Required:** Call customer and offer loyalty rewards!"
    elif score >= 20:
        st.progress(score/100)
        st.info(f"🔵 MEDIUM RISK — {score}% chance of churning!")
        recommendation = "👀 **Monitor:** Send satisfaction survey to this customer!"
    else:
        st.progress(score/100)
        st.success(f"✅ LOW RISK — Only {score}% chance of churning!")
        recommendation = "😊 **No action needed:** Customer is happy and loyal!"

    # Reasons
    st.write("---")
    st.subheader("🔍 Why this prediction?")
    for reason in reasons:
        st.write(f"• {reason}")

    # Recommendation
    st.write("---")
    st.subheader("💡 Recommended Action")
    st.write(recommendation)
