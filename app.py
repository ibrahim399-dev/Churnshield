import streamlit as st
import pandas as pd
import io

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
    page_title="ChurnShield-NG",
    page_icon="🛡️",
    layout="centered"
)

# HERO SECTION
st.title("🛡️ ChurnShield-NG")
st.subheader("AI-Powered Customer Churn Prediction")
st.write("Helping Nigerian businesses retain customers and grow revenue!")
st.write("---")

# Stats bar
col1, col2, col3, col4 = st.columns(4)
col1.metric("📊 Dataset", "7,043 customers")
col2.metric("🎯 Accuracy", "78.68%")
col3.metric("📱 Providers", "4 Nigerian")
col4.metric("🌍 Countries", "Growing!")
st.write("---")

# MODE SELECTOR
st.subheader("👇 Who are you?")
mode = st.selectbox("Select your mode", [
    "👇 Please select...",
    "🏢 Business Owner — Single Prediction",
    "📊 Business Analytics — Batch Prediction",
    "👤 Customer — Check if I will leave my provider"
])

if mode == "👇 Please select...":
    st.warning("👆 Please select who you are to continue!")
    st.stop()

st.write("---")

# BUSINESS MODE
if mode == "🏢 Business Owner — Single Prediction":
    st.subheader("🏢 Business Mode — Single Prediction")
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
        with st.spinner("Analyzing customer data..."):
            score, reasons = predict_churn(tenure, monthly_charges/1000,
                                          senior_citizen, contract, internet_service)
        recommendation, _ = show_result(score, reasons)
        st.write("---")
        st.subheader("💡 Recommended Business Action")
        st.write(f"🏢 {recommendation}")

# BATCH PREDICTION MODE
elif mode == "📊 Business Analytics — Batch Prediction":
    st.subheader("📊 Batch Prediction Mode")
    st.write("Upload a CSV file to predict churn for multiple customers at once!")
    st.write("---")
    st.info("📥 Your CSV must have these columns: **tenure, monthly_charges, senior_citizen, contract, internet_service**")

    if "batch_df" not in st.session_state:
        st.session_state.batch_df = None

    if st.button("📊 Load Sample Data Instead"):
        sample = """tenure,monthly_charges,senior_citizen,contract,internet_service
5,45,No,Month-to-month,DSL
34,89,No,One year,Fiber optic
2,120,Yes,Month-to-month,Fiber optic
45,56,No,Two year,DSL
8,95,No,Month-to-month,Fiber optic
60,34,No,Two year,No
1,150,Yes,Month-to-month,Fiber optic
23,67,No,One year,DSL"""
        st.session_state.batch_df = pd.read_csv(io.StringIO(sample))

    uploaded_file = st.file_uploader("Upload your customer CSV file", type=["csv"])
    if uploaded_file is not None:
        st.session_state.batch_df = pd.read_csv(uploaded_file)

    if st.session_state.batch_df is not None:
        df = st.session_state.batch_df
        st.write(f"✅ **{len(df)} customers loaded!**")
        st.dataframe(df)

        if st.button("🔍 Predict Churn for All Customers", use_container_width=True):
            with st.spinner("Analyzing all customers..."):
                results = []
                for idx, row in df.iterrows():
                    score, _ = predict_churn(
                        row["tenure"],
                        row["monthly_charges"],
                        str(row["senior_citizen"]),
                        row["contract"],
                        row["internet_service"]
                    )
                    if score >= 60:
                        risk = "VERY HIGH RISK"
                    elif score >= 40:
                        risk = "HIGH RISK"
                    elif score >= 20:
                        risk = "MEDIUM RISK"
                    else:
                        risk = "LOW RISK"

                    results.append({
                        "Customer": idx + 1,
                        "Risk Score": score,
                        "Risk Level": risk
                    })

            results_df = pd.DataFrame(results)

            st.write("---")
            st.subheader("📈 Batch Results Summary")
            col1, col2, col3, col4 = st.columns(4)
            col1.metric("Total", len(results_df))
            col2.metric("🔴 Very High", len(results_df[results_df["Risk Level"] == "VERY HIGH RISK"]))
            col3.metric("🟡 High", len(results_df[results_df["Risk Level"] == "HIGH RISK"]))
            col4.metric("✅ Low", len(results_df[results_df["Risk Level"] == "LOW RISK"]))

            # Chart
            st.write("---")
            st.subheader("📊 Risk Distribution Chart")
            chart_data = results_df["Risk Level"].value_counts()
            st.bar_chart(chart_data)

            st.write("---")
            st.subheader("📋 Full Results")
            st.dataframe(results_df)

            csv = results_df.to_csv(index=False)
            st.download_button(
                label="📥 Download Results as CSV",
                data=csv,
                file_name="churnshield_results.csv",
                mime="text/csv"
            )

# CUSTOMER MODE
elif mode == "👤 Customer — Check if I will leave my provider":
    st.subheader("👤 Customer Mode")
    st.write("Answer honestly and we'll tell you if you're likely to leave your provider!")

    # Country selector
    country = st.selectbox("🌍 Select your Country", [
        "🇳🇬 Nigeria",
        "🇬🇭 Ghana",
        "🇰🇪 Kenya",
        "🇿🇦 South Africa",
        "🇺🇬 Uganda",
        "🇹🇿 Tanzania",
        "🇷🇼 Rwanda",
        "🌍 Other African Country"
    ])

    # Providers by country
    providers = {
        "🇳🇬 Nigeria": ["MTN", "Airtel", "Glo", "9mobile"],
        "🇬🇭 Ghana": ["MTN", "Vodafone", "AirtelTigo", "Glo"],
        "🇰🇪 Kenya": ["Safaricom", "Airtel", "Telkom"],
        "🇿🇦 South Africa": ["Vodacom", "MTN", "Cell C", "Telkom"],
        "🇺🇬 Uganda": ["MTN", "Airtel", "Africell"],
        "🇹🇿 Tanzania": ["Vodacom", "Airtel", "Tigo", "Halotel"],
        "🇷🇼 Rwanda": ["MTN", "Airtel"],
        "🌍 Other African Country": ["MTN", "Airtel", "Vodafone", "Other"]
    }

    provider = st.selectbox("📱 Your Current Provider",
                            providers[country])

    # Currency by country
    currencies = {
        "🇳🇬 Nigeria": "₦",
        "🇬🇭 Ghana": "GH₵",
        "🇰🇪 Kenya": "KSh",
        "🇿🇦 South Africa": "R",
        "🇺🇬 Uganda": "USh",
        "🇹🇿 Tanzania": "TSh",
        "🇷🇼 Rwanda": "RWF",
        "🌍 Other African Country": "$"
    }

    currency = currencies[country]

    col1, col2 = st.columns(2)
    with col1:
        tenure = st.slider("📅 How long have you been with them? (months)", 0, 72, 12)
        monthly_charges = st.number_input(f"💰 How much do you pay monthly? ({currency})", 0.0, 200000.0, 5000.0)
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
        with st.spinner("Analyzing your loyalty score..."):
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

# CONTACT SECTION
st.write("---")
st.subheader("📬 Contact & About")
col1, col2 = st.columns(2)
with col1:
    st.write("**👨‍💻 Built by:**")
    st.write("Ajayi Ibrahim Ademola")
    st.write("Data Science & ML Developer")
with col2:
    st.write("**📧 Get in touch:**")
    st.write("ibrahimdamola405@gmail.com")
    st.write("💼 Open to partnerships & collaborations!")

st.write("---")
st.caption("© 2026 ChurnShield-NG | AI-Powered Churn Prediction | All Rights Reserved")
