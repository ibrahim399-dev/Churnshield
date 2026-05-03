import streamlit as st

# Prediction logic
def predict_churn(tenure, monthly_charges, senior_citizen, contract, internet_service):
    risk_score = 0
    reasons = []

    if contract == "Month-to-month":
        risk_score += 40
        reasons.append("📋 Month-to-month contract — no commitment!")
    elif contract == "One year":
        risk_score += 10
        reasons.append("📋 One year contract — some commitment")

    if monthly_charges > 70:
        risk_score += 25
        reasons.append("💰 High monthly charges!")
    elif monthly_charges > 50:
        risk_score += 10
        reasons.append("💰 Moderate monthly charges")

    if tenure < 12:
        risk_score += 20
        reasons.append("📅 New customer — less loyalty!")
    elif tenure < 24:
        risk_score += 10
        reasons.append("📅 Relatively new customer")

    if senior_citizen == "Yes":
        risk_score += 10
        reasons.append("👤 Senior citizen — higher risk group")

    if internet_service == "Fiber optic":
        risk_score += 5
        reasons.append("🌐 Fiber optic users churn more!")

    return risk_score, reasons

def show_result(score, reasons):
    st.write("---")
    st.subheader("📈 Risk Analysis")
    st.write(f"**Overall Risk Score: {score}/100**")
    st.progress(score/100)

    if score >= 60:
        st.error(f"⚠️ VERY HIGH RISK — {score}% chance of churning!")
        recommendation = "🚨 Offer special discount or upgrade immediately!"
        customer_advice = "⚠️ You are very likely to leave! Consider negotiating a better plan!"
    elif score >= 40:
        st.warning(f"🟡 HIGH RISK — {score}% chance of churning!")
        recommendation = "📞 Call customer and offer loyalty rewards!"
        customer_advice = "🟡 You might leave soon! Ask your provider for a better deal!"
    elif score >= 20:
        st.info(f"🔵 MEDIUM RISK — {score}% chance of churning!")
        recommendation = "👀 Send satisfaction survey to this customer!"
        customer_advice = "🔵 You're somewhat satisfied but could be happier!"
    else:
        st.success(f"✅ LOW RISK — Only {score}% chance of churning!")
        recommendation = "😊 Customer is happy and loyal — no action needed!"
        customer_advice = "✅ You're happy with your provider! Keep enjoying your service!"

    st.write("---")
    st.subheader("🔍 Why this prediction?")
    for reason in reasons:
        st.write(f"• {reason}")

    return recommendation, customer_advice

# Page config
st.set_page_config(
    page_title="ChurnShield",
    page_icon="🛡️",
    layout="centered"
)

# Header
st.title("🛡️ ChurnShield-NG")
st.write("Built by **Ajayi Ibrahim** — Data Science & ML")
st.write("---")

# MODE SELECTOR
st.subheader("👇 Who are you?")
mode = st.selectbox("Select your mode", [
    "👇 Please select...",
    "🏢 Business Owner — Predict if my customer will churn",
    "👤 Customer — Check if I will leave my provider"
])

if mode == "👇 Please select...":
    st.warning("👆 Please select who you are to continue!")
    st.stop()

st.write("---")

# BUSINESS MODE
if mode == "🏢 Business Owner — Predict if my customer will churn":
    st.subheader("🏢 Business Mode")
    st.write("Enter your customer's details below!")

    col1, col2 = st.columns(2)
    with col1:
        tenure = st.slider("📅 Customer Tenure (months)", 0, 72, 12)
        monthly_charges = st.number_input("💰 Monthly Charges (₦)", 0.0, 200000.0, 5000.0)
        senior_citizen = st.selectbox("👤 Senior Citizen?", ["No", "Yes"])
    with col2:
        contract = st.selectbox("📋 Contract Type", ["Month-to-month", "One year", "Two year"])
        internet_service = st.selectbox("🌐 Internet Service", ["DSL", "Fiber optic", "No"])
        payment_method = st.selectbox("💳 Payment Method", ["Bank transfer", "Credit card", "Electronic check", "Mailed check"])

    st.write("---")
    st.subheader("👤 Customer Profile Summary")
    col3, col4, col5 = st.columns(3)
    col3.metric("Tenure", f"{tenure} months")
    col4.metric("Monthly Bill", f"₦{monthly_charges:,.0f}")
    col5.metric("Contract", contract.split()[0])

    if st.button("🔍 Predict Customer Churn Risk", use_container_width=True):
        score, reasons = predict_churn(tenure, monthly_charges/1000,
                                      senior_citizen, contract, internet_service)
        recommendation, _ = show_result(score, reasons)
        st.write("---")
        st.subheader("💡 Recommended Business Action")
        st.write(f"🏢 {recommendation}")

# CUSTOMER MODE
else:
    st.subheader("👤 Customer Mode")
    st.write("Answer honestly and we'll tell you if you're likely to leave your provider!")

    provider = st.selectbox("📱 Your Current Provider",
                            ["MTN", "Airtel", "Glo", "9mobile"])

    col1, col2 = st.columns(2)
    with col1:
        tenure = st.slider("📅 How long have you been with them? (months)", 0, 72, 12)
        monthly_charges = st.number_input("💰 How much do you pay monthly? (₦)", 0.0, 200000.0, 5000.0)
        senior_citizen = st.selectbox("👤 Are you a senior citizen?", ["No", "Yes"])
    with col2:
        contract = st.selectbox("📋 Your Plan Type", ["Month-to-month", "One year", "Two year"])
        internet_service = st.selectbox("🌐 Your Internet Type", ["DSL", "Fiber optic", "No"])
        satisfaction = st.selectbox("😊 How satisfied are you?",
                                    ["Very satisfied", "Satisfied", "Neutral", "Unsatisfied", "Very unsatisfied"])

    satisfaction_scores = {
        "Very satisfied": -15,
        "Satisfied": -10,
        "Neutral": 0,
        "Unsatisfied": 15,
        "Very unsatisfied": 25
    }

    if st.button("🔍 Check My Loyalty Score", use_container_width=True):
        score, reasons = predict_churn(tenure, monthly_charges/1000,
                                      senior_citizen, contract, internet_service)
        score = min(100, score + satisfaction_scores[satisfaction])
        if satisfaction in ["Unsatisfied", "Very unsatisfied"]:
            reasons.append(f"😞 You are {satisfaction.lower()} with your provider!")

        _, customer_advice = show_result(score, reasons)
        st.write("---")
        st.subheader(f"💡 Our Advice for You as a {provider} Customer")
        st.write(customer_advice)
        if score >= 40:
            st.write("---")
            st.info(f"💡 **Pro tip:** Call {provider} customer care and negotiate a better plan!")
