import streamlit as st
import pandas as pd
import io

# ============================================
# PREDICTION ENGINE
# ============================================
def predict_churn(tenure, monthly_charges, senior_citizen, contract, internet_service):
    risk_score = 0
    reasons = []
    positive_factors = []

    if contract == "Month-to-month":
        risk_score += 40
        reasons.append("📋 Month-to-month contract means no commitment — easy to leave!")
    elif contract == "One year":
        risk_score += 10
        reasons.append("📋 One year contract shows some commitment")
    else:
        positive_factors.append("📋 Two year contract — strong commitment!")

    if monthly_charges > 70:
        risk_score += 25
        reasons.append("💰 High monthly charges increase likelihood of leaving!")
    elif monthly_charges > 50:
        risk_score += 10
        reasons.append("💰 Moderate monthly charges — worth monitoring")
    else:
        positive_factors.append("💰 Affordable charges — customer gets good value!")

    if tenure < 12:
        risk_score += 20
        reasons.append("📅 New customer — loyalty not yet established!")
    elif tenure < 24:
        risk_score += 10
        reasons.append("📅 Relatively new customer — still building loyalty")
    else:
        positive_factors.append("📅 Long term customer — high loyalty!")

    if senior_citizen == "Yes":
        risk_score += 10
        reasons.append("👤 Senior citizens statistically churn more!")
    else:
        positive_factors.append("👤 Non-senior citizen — lower risk group!")

    if internet_service == "Fiber optic":
        risk_score += 5
        reasons.append("🌐 Fiber optic users tend to churn more!")
    elif internet_service == "No":
        positive_factors.append("🌐 No internet service — simpler relationship!")

    return risk_score, reasons, positive_factors

# ============================================
# PAGE CONFIG
# ============================================
st.set_page_config(
    page_title="ShieldAI",
    page_icon="🛡️",
    layout="centered"
)

# ============================================
# SESSION STATE
# ============================================
if "page" not in st.session_state:
    st.session_state.page = "home"
if "selected_model" not in st.session_state:
    st.session_state.selected_model = None
if "batch_df" not in st.session_state:
    st.session_state.batch_df = None

# ============================================
# NAVIGATION
# ============================================
def go_to(page):
    st.session_state.page = page
    st.rerun()

# ============================================
# HOME PAGE
# ============================================
def show_home():
    st.title("🛡️ ShieldAI")
    st.subheader("AI-Powered Predictions That Protect")
    st.write("Making advanced AI accessible to everyone — regardless of sector!")
    st.write("---")

    # Stats
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("📊 Records", "7,043+")
    col2.metric("🎯 Accuracy", "78.68%")
    col3.metric("🌍 Countries", "8+")
    col4.metric("🤖 Models", "Growing!")

    st.write("---")

    # What we do
    st.subheader("🚀 What ShieldAI Does")
    st.write("ShieldAI uses Machine Learning to help you make smarter decisions by predicting outcomes before they happen!")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.info("🛡️ **ChurnShield**\nPredict if customers will leave before they do!")
    with col2:
        st.info("❤️ **HeartGuard**\nPredict heart disease risk from health data!")
    with col3:
        st.info("🎓 **StudyShield**\nPredict student performance and dropout risk!")

    st.write("---")
    st.subheader("👇 Ready to get started?")

    if st.button("🚀 Explore Our Models", use_container_width=True):
        go_to("models")

    st.write("---")
    # Contact
    col1, col2 = st.columns(2)
    with col1:
        st.write("**👨‍💻 Built by:**")
        st.write("Ajayi Ibrahim Ademola")
        st.write("Data Science & ML Developer")
    with col2:
        st.write("**📧 Contact:**")
        st.write("ibrahimdamola405@gmail.com")
        st.write("💼 Open to partnerships!")

    st.caption("© 2026 ShieldAI | AI-Powered Predictions | All Rights Reserved")

# ============================================
# MODELS PAGE
# ============================================
def show_models():
    st.title("🛡️ ShieldAI")
    st.subheader("📊 Our AI Models")
    st.write("Select a model to get started!")
    st.write("---")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.success("🛡️ **ChurnShield**")
        st.write("Predict customer churn for telecom businesses!")
        st.write("**Accuracy:** 78.68%")
        st.write("**Users:** Businesses & Customers")
        if st.button("Use ChurnShield →", use_container_width=True):
            st.session_state.selected_model = "churn"
            go_to("churn")

    with col2:
        st.warning("❤️ **HeartGuard**")
        st.write("Predict heart disease risk from health data!")
        st.write("**Status:** 🔄 Coming Soon!")
        st.write("**Users:** Individuals & Hospitals")
        st.button("Coming Soon", disabled=True, use_container_width=True)

    with col3:
        st.info("🎓 **StudyShield**")
        st.write("Predict student performance and dropout risk!")
        st.write("**Status:** 🔄 Coming Soon!")
        st.write("**Users:** Schools & Students")
        st.button("Coming Soon ", disabled=True, use_container_width=True)

    st.write("---")
    if st.button("← Back to Home", use_container_width=True):
        go_to("home")

# ============================================
# CHURNSHIELD PAGE
# ============================================
def show_churn():
    st.title("🛡️ ChurnShield")
    st.write("A **ShieldAI** Product")
    st.write("---")

    # Tabs
    tab1, tab2, tab3 = st.tabs([
        "🏢 Single Prediction",
        "📊 Batch Analysis",
        "👤 Loyalty Check"
    ])

    # ---- TAB 1: SINGLE PREDICTION ----
    with tab1:
        st.subheader("🏢 Business — Single Customer Prediction")
        st.write("Enter your customer's details to predict if they will churn!")
        st.write("---")

        col1, col2 = st.columns(2)
        with col1:
            tenure = st.slider("📅 Customer Tenure (months)", 0, 72, 12,
                             help="How long has this customer been with you?")
            monthly_charges = st.number_input("💰 Monthly Charges (₦)", 0.0, 200000.0, 5000.0,
                                            help="How much does this customer pay monthly?")
            senior_citizen = st.selectbox("👤 Senior Citizen?", ["No", "Yes"],
                                        help="Is this customer a senior citizen?")
        with col2:
            contract = st.selectbox("📋 Contract Type",
                                  ["Month-to-month", "One year", "Two year"],
                                  help="What type of contract does this customer have?")
            internet_service = st.selectbox("🌐 Internet Service",
                                          ["DSL", "Fiber optic", "No"],
                                          help="What internet service does this customer use?")
            payment_method = st.selectbox("💳 Payment Method",
                                        ["Bank transfer", "Credit card",
                                         "Electronic check", "Mailed check"])

        st.write("---")
        # Customer summary
        st.subheader("👤 Customer Profile")
        col3, col4, col5 = st.columns(3)
        col3.metric("Tenure", f"{tenure} months")
        col4.metric("Monthly Bill", f"₦{monthly_charges:,.0f}")
        col5.metric("Contract", contract.split()[0])

        if st.button("🔍 Predict Churn Risk", use_container_width=True, key="single_predict"):
            with st.spinner("🤖 Analyzing customer data..."):
                score, reasons, positives = predict_churn(
                    tenure, monthly_charges/1000,
                    senior_citizen, contract, internet_service
                )

            st.write("---")
            # Result
            st.subheader("🎯 Prediction Result")

            # Confidence score
            confidence = score
            col1, col2 = st.columns(2)

            if score >= 60:
                col1.error("⚠️ WILL CHURN")
                col2.metric("Confidence", f"{confidence}%", "High Risk")
                recommendation = "🚨 Act immediately — offer special discount or upgrade!"
            elif score >= 40:
                col1.warning("🟡 LIKELY TO CHURN")
                col2.metric("Confidence", f"{confidence}%", "Medium Risk")
                recommendation = "📞 Call customer and offer loyalty rewards!"
            elif score >= 20:
                col1.info("🔵 MIGHT CHURN")
                col2.metric("Confidence", f"{confidence}%", "Low-Medium Risk")
                recommendation = "👀 Monitor closely and send satisfaction survey!"
            else:
                col1.success("✅ WILL STAY")
                col2.metric("Confidence", f"{100-confidence}%", "Low Risk")
                recommendation = "😊 Customer is loyal — maintain good service!"

            st.progress(score/100)

            # Explanation
            st.write("---")
            st.subheader("🔍 Why this prediction?")

            if reasons:
                st.write("**⚠️ Risk Factors:**")
                for reason in reasons:
                    st.write(f"• {reason}")

            if positives:
                st.write("**✅ Positive Factors:**")
                for positive in positives:
                    st.write(f"• {positive}")

            # Recommendation
            st.write("---")
            st.subheader("💡 Recommended Action")
            st.write(recommendation)

    # ---- TAB 2: BATCH ANALYSIS ----
    with tab2:
        st.subheader("📊 Business Analytics — Batch Prediction")
        st.write("Predict churn for multiple customers at once!")
        st.write("---")
        st.info("📥 Your CSV must have: **tenure, monthly_charges, senior_citizen, contract, internet_service**")

        if st.button("📊 Load Sample Data", key="load_sample"):
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

        uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])
        if uploaded_file is not None:
            st.session_state.batch_df = pd.read_csv(uploaded_file)

        if st.session_state.batch_df is not None:
            df = st.session_state.batch_df
            st.write(f"✅ **{len(df)} customers loaded!**")
            st.dataframe(df)

            if st.button("🔍 Predict All Customers", use_container_width=True, key="batch_predict"):
                with st.spinner("🤖 Analyzing all customers..."):
                    results = []
                    for idx, row in df.iterrows():
                        score, _, _ = predict_churn(
                            row["tenure"],
                            row["monthly_charges"],
                            str(row["senior_citizen"]),
                            row["contract"],
                            row["internet_service"]
                        )
                        if score >= 60:
                            risk = "WILL CHURN"
                        elif score >= 40:
                            risk = "LIKELY TO CHURN"
                        elif score >= 20:
                            risk = "MIGHT CHURN"
                        else:
                            risk = "WILL STAY"

                        results.append({
                            "Customer": idx + 1,
                            "Risk Score": score,
                            "Prediction": risk
                        })

                results_df = pd.DataFrame(results)

                st.write("---")
                st.subheader("📈 Results Summary")
                col1, col2, col3, col4 = st.columns(4)
                col1.metric("Total", len(results_df))
                col2.metric("🔴 Will Churn", len(results_df[results_df["Prediction"] == "WILL CHURN"]))
                col3.metric("🟡 Likely", len(results_df[results_df["Prediction"] == "LIKELY TO CHURN"]))
                col4.metric("✅ Will Stay", len(results_df[results_df["Prediction"] == "WILL STAY"]))

                st.write("---")
                st.subheader("📊 Risk Distribution")
                chart_data = results_df["Prediction"].value_counts()
                st.bar_chart(chart_data)

                st.write("---")
                st.subheader("📋 Full Results")
                st.dataframe(results_df)

                csv = results_df.to_csv(index=False)
                st.download_button(
                    label="📥 Download Results",
                    data=csv,
                    file_name="churnshield_results.csv",
                    mime="text/csv"
                )

    # ---- TAB 3: LOYALTY CHECK ----
    with tab3:
        st.subheader("👤 Customer Loyalty Check")
        st.write("Find out if YOU are likely to leave your provider!")
        st.write("---")

        country = st.selectbox("🌍 Your Country", [
            "🇳🇬 Nigeria", "🇬🇭 Ghana", "🇰🇪 Kenya",
            "🇿🇦 South Africa", "🇺🇬 Uganda",
            "🇹🇿 Tanzania", "🇷🇼 Rwanda",
            "🌍 Other African Country"
        ])

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

        currencies = {
            "🇳🇬 Nigeria": "₦", "🇬🇭 Ghana": "GH₵",
            "🇰🇪 Kenya": "KSh", "🇿🇦 South Africa": "R",
            "🇺🇬 Uganda": "USh", "🇹🇿 Tanzania": "TSh",
            "🇷🇼 Rwanda": "RWF", "🌍 Other African Country": "$"
        }

        provider = st.selectbox("📱 Your Provider", providers[country])
        currency = currencies[country]

        col1, col2 = st.columns(2)
        with col1:
            tenure = st.slider("📅 Months with provider", 0, 72, 12, key="loyalty_tenure")
            monthly_charges = st.number_input(f"💰 Monthly payment ({currency})",
                                            0.0, 200000.0, 5000.0, key="loyalty_charges")
            senior_citizen = st.selectbox("👤 Senior citizen?", ["No", "Yes"], key="loyalty_senior")
        with col2:
            contract = st.selectbox("📋 Plan type",
                                  ["Month-to-month", "One year", "Two year"],
                                  key="loyalty_contract")
            internet_service = st.selectbox("🌐 Internet type",
                                          ["DSL", "Fiber optic", "No"],
                                          key="loyalty_internet")
            satisfaction = st.selectbox("😊 Satisfaction level",
                                      ["Very satisfied", "Satisfied",
                                       "Neutral", "Unsatisfied", "Very unsatisfied"])

        satisfaction_scores = {
            "Very satisfied": -15, "Satisfied": -10,
            "Neutral": 0, "Unsatisfied": 15, "Very unsatisfied": 25
        }

        if st.button("🔍 Check My Loyalty Score", use_container_width=True, key="loyalty_predict"):
            with st.spinner("🤖 Analyzing your loyalty..."):
                score, reasons, positives = predict_churn(
                    tenure, monthly_charges/1000,
                    senior_citizen, contract, internet_service
                )
            score = min(100, score + satisfaction_scores[satisfaction])

            st.write("---")
            st.subheader("🎯 Your Loyalty Result")

            col1, col2 = st.columns(2)
            if score >= 60:
                col1.error("⚠️ VERY LIKELY TO LEAVE")
                col2.metric("Risk Score", f"{score}/100")
                advice = f"⚠️ You are very likely to leave {provider}! Call them NOW and negotiate a better deal!"
            elif score >= 40:
                col1.warning("🟡 MIGHT LEAVE SOON")
                col2.metric("Risk Score", f"{score}/100")
                advice = f"🟡 You might leave {provider} soon! Consider asking for a loyalty discount!"
            elif score >= 20:
                col1.info("🔵 SOMEWHAT SATISFIED")
                col2.metric("Risk Score", f"{score}/100")
                advice = f"🔵 You're okay with {provider} but could be happier. Explore your options!"
            else:
                col1.success("✅ VERY LOYAL")
                col2.metric("Risk Score", f"{score}/100")
                advice = f"✅ You're happy with {provider}! Keep enjoying your service!"

            st.progress(score/100)

            st.write("---")
            st.subheader("🔍 Why this result?")
            if reasons:
                st.write("**⚠️ Risk factors:**")
                for reason in reasons:
                    st.write(f"• {reason}")
            if positives:
                st.write("**✅ Good factors:**")
                for positive in positives:
                    st.write(f"• {positive}")

            st.write("---")
            st.subheader("💡 Our Advice")
            st.write(advice)
            if score >= 40:
                st.info(f"💡 **Pro tip:** Call {provider} customer care and say you're thinking of leaving — they'll offer you a deal! 😂")

    st.write("---")
    if st.button("← Back to Models", use_container_width=True):
        go_to("models")

# ============================================
# ROUTER
# ============================================
if st.session_state.page == "home":
    show_home()
elif st.session_state.page == "models":
    show_models()
elif st.session_state.page == "churn":
    show_churn()
