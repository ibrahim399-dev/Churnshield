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
    business_insights = []

    if contract == "Month-to-month":
        risk_score += 40
        reasons.append("📋 Month-to-month contract — no commitment, easy to leave!")
        business_insights.append("💡 Customers on month-to-month contracts are 3x more likely to churn than those on annual contracts.")
    elif contract == "One year":
        risk_score += 10
        reasons.append("📋 One year contract — some commitment exists")
        business_insights.append("💡 One year contract customers churn 60% less than month-to-month customers.")
    else:
        positive_factors.append("📋 Two year contract — strong long term commitment!")
        business_insights.append("💡 Two year contract customers are your most loyal — focus on upselling them!")

    if monthly_charges > 70:
        risk_score += 25
        reasons.append("💰 High monthly charges increase financial pressure!")
        business_insights.append("💡 Customers paying above average are 2x more likely to seek cheaper alternatives.")
    elif monthly_charges > 50:
        risk_score += 10
        reasons.append("💰 Moderate monthly charges — worth monitoring")
        business_insights.append("💡 Consider offering a loyalty discount to lock in this customer long term.")
    else:
        positive_factors.append("💰 Affordable charges — customer gets great value!")
        business_insights.append("💡 Low charge customers rarely churn — focus retention budget elsewhere.")

    if tenure < 12:
        risk_score += 20
        reasons.append("📅 New customer — loyalty not yet established!")
        business_insights.append("💡 First year customers are the highest churn risk — invest in onboarding and early engagement.")
    elif tenure < 24:
        risk_score += 10
        reasons.append("📅 Relatively new customer — still building loyalty")
        business_insights.append("💡 Customers in months 12-24 respond well to loyalty rewards and milestone recognition.")
    else:
        positive_factors.append("📅 Long term customer — high loyalty established!")
        business_insights.append("💡 Long term customers are brand ambassadors — consider referral programs for them.")

    if senior_citizen == "Yes":
        risk_score += 10
        reasons.append("👤 Senior citizens statistically show higher churn rates!")
        business_insights.append("💡 Senior customers respond well to dedicated support lines and simplified billing.")
    else:
        positive_factors.append("👤 Non-senior citizen — lower demographic risk!")

    if internet_service == "Fiber optic":
        risk_score += 5
        reasons.append("🌐 Fiber optic users tend to be more price sensitive!")
        business_insights.append("💡 Fiber optic customers churn when they find better speeds or prices — emphasize your reliability!")
    elif internet_service == "No":
        positive_factors.append("🌐 No internet service — simpler relationship to maintain!")

    return risk_score, reasons, positive_factors, business_insights

# ============================================
# PAGE CONFIG
# ============================================
st.set_page_config(
    page_title="ShieldAI — Decision Intelligence Platform",
    page_icon="🛡️",
    layout="centered"
)

# ============================================
# SESSION STATE
# ============================================
if "page" not in st.session_state:
    st.session_state.page = "home"
if "batch_df" not in st.session_state:
    st.session_state.batch_df = None

def go_to(page):
    st.session_state.page = page
    st.rerun()

# ============================================
# HOME PAGE
# ============================================
def show_home():
    # Hero section
    st.title("🛡️ ShieldAI")
    st.markdown("## Reduce Customer Loss with AI")
    st.markdown("### Predict which customers will leave — before they do.")
    st.write("ShieldAI is a Nigerian AI platform for decision intelligence. We help businesses and individuals make smarter decisions using Machine Learning.")
    st.write("---")

    # Trust elements
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("📊 Dataset", "7,043+ Records")
    col2.metric("🎯 Accuracy", "78.68%")
    col3.metric("🤖 Algorithm", "Gradient Boost")
    col4.metric("🌍 Countries", "8+ African")
    st.write("---")

    # Powered by section
    st.info("🔬 **Powered by Machine Learning** | 📊 **Model Accuracy: 78.68%** | 🗄️ **Dataset: 7,000+ Records** | ⚙️ **Algorithm: Gradient Boosting**")
    st.write("---")

    # Modules
    st.subheader("🚀 ShieldAI Modules")
    st.write("One platform — multiple AI models — every sector!")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.success("""
        🛡️ **Customer Intelligence**
        
        ChurnShield
        
        Predict customer churn before it happens!
        
        ✅ Available Now
        """)
    with col2:
        st.warning("""
        ❤️ **Health Risk Prediction**
        
        HeartGuard
        
        Predict heart disease risk from health data!
        
        🔄 Coming Soon
        """)
    with col3:
        st.info("""
        🎓 **Student Performance Analytics**
        
        StudyShield
        
        Predict student outcomes and dropout risk!
        
        🔄 Coming Soon
        """)

    st.write("---")

    # How it works
    st.subheader("⚡ How It Works")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.write("### 1️⃣")
        st.write("**Select Module**")
        st.write("Choose the AI model that fits your need!")
    with col2:
        st.write("### 2️⃣")
        st.write("**Enter Data**")
        st.write("Fill in the details — takes less than a minute!")
    with col3:
        st.write("### 3️⃣")
        st.write("**Get Prediction**")
        st.write("Receive instant AI prediction with full explanation!")

    st.write("---")
    if st.button("🚀 Get Started — It's Free!", use_container_width=True):
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
        st.write("💼 Open to partnerships & collaborations!")

    st.caption("© 2026 ShieldAI | Nigerian AI Platform for Decision Intelligence | All Rights Reserved")

# ============================================
# MODELS PAGE
# ============================================
def show_models():
    st.title("🛡️ ShieldAI")
    st.subheader("📊 Select Your Module")
    st.write("Choose an AI model to get started!")
    st.write("---")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.success("🛡️ **ChurnShield**")
        st.write("**Customer Intelligence**")
        st.write("Predict if customers will leave before they do!")
        st.write("")
        st.write("✅ **Status:** Live")
        st.write("🎯 **Accuracy:** 78.68%")
        st.write("👥 **For:** Businesses & Customers")
        if st.button("Launch ChurnShield →", use_container_width=True):
            go_to("churn")

    with col2:
        st.warning("❤️ **HeartGuard**")
        st.write("**Health Risk Prediction**")
        st.write("Predict heart disease risk from your health data!")
        st.write("")
        st.write("🔄 **Status:** Coming Soon")
        st.write("🎯 **Accuracy:** In training")
        st.write("👥 **For:** Individuals & Hospitals")
        st.button("Coming Soon ❤️", disabled=True, use_container_width=True)

    with col3:
        st.info("🎓 **StudyShield**")
        st.write("**Student Analytics**")
        st.write("Predict student performance and dropout risk!")
        st.write("")
        st.write("🔄 **Status:** Coming Soon")
        st.write("🎯 **Accuracy:** In training")
        st.write("👥 **For:** Schools & Students")
        st.button("Coming Soon 🎓", disabled=True, use_container_width=True)

    st.write("---")
    if st.button("← Back to Home", use_container_width=True):
        go_to("home")

# ============================================
# CHURNSHIELD PAGE
# ============================================
def show_churn():
    st.title("🛡️ ChurnShield")
    st.write("**A ShieldAI Product** | Customer Intelligence Module")
    st.info("🔬 Powered by Machine Learning | 🎯 78.68% Accuracy | 📊 Trained on 7,043 Records")
    st.write("---")

    tab1, tab2, tab3 = st.tabs([
        "🏢 Single Prediction",
        "📊 Batch Analysis",
        "👤 Loyalty Check"
    ])

    # ---- TAB 1 ----
    with tab1:
        st.subheader("🏢 Single Customer Prediction")
        st.write("Enter customer details below to predict churn risk!")
        st.write("---")

        col1, col2 = st.columns(2)
        with col1:
            tenure = st.slider("📅 Tenure (months)", 0, 72, 12,
                             help="How long has this customer been with you?")
            monthly_charges = st.number_input("💰 Monthly Charges (₦)", 0.0, 200000.0, 5000.0,
                                            help="How much does this customer pay monthly?")
            senior_citizen = st.selectbox("👤 Senior Citizen?", ["No", "Yes"])
        with col2:
            contract = st.selectbox("📋 Contract Type",
                                  ["Month-to-month", "One year", "Two year"])
            internet_service = st.selectbox("🌐 Internet Service",
                                          ["DSL", "Fiber optic", "No"])
            payment_method = st.selectbox("💳 Payment Method",
                                        ["Bank transfer", "Credit card",
                                         "Electronic check", "Mailed check"])

        st.write("---")
        col3, col4, col5 = st.columns(3)
        col3.metric("Tenure", f"{tenure} months")
        col4.metric("Monthly Bill", f"₦{monthly_charges:,.0f}")
        col5.metric("Contract", contract.split()[0])

        if st.button("🔍 Predict Churn Risk", use_container_width=True, key="single"):
            with st.spinner("🤖 AI is analyzing customer data..."):
                score, reasons, positives, insights = predict_churn(
                    tenure, monthly_charges/1000,
                    senior_citizen, contract, internet_service
                )

            st.write("---")

            # WOW MOMENT
            if score >= 60:
                st.error(f"""
                ## ⚠️ HIGH CHURN RISK DETECTED!
                **Confidence: {score}%**
                This customer is very likely to leave!
                """)
                recommendation = "🚨 Act immediately — offer special discount or upgrade plan!"
                risk_label = "🔴 HIGH RISK"
            elif score >= 40:
                st.warning(f"""
                ## 🟡 MEDIUM CHURN RISK DETECTED
                **Confidence: {score}%**
                This customer may leave soon!
                """)
                recommendation = "📞 Call customer and offer loyalty rewards!"
                risk_label = "🟡 MEDIUM RISK"
            elif score >= 20:
                st.info(f"""
                ## 🔵 LOW-MEDIUM CHURN RISK
                **Confidence: {score}%**
                This customer shows some risk signals!
                """)
                recommendation = "👀 Monitor closely and send satisfaction survey!"
                risk_label = "🔵 LOW-MEDIUM RISK"
            else:
                st.success(f"""
                ## ✅ LOW CHURN RISK
                **Loyalty Score: {100-score}%**
                This customer is likely to stay!
                """)
                recommendation = "😊 Customer is loyal — maintain excellent service!"
                risk_label = "✅ LOW RISK"

            # Risk meter
            col1, col2 = st.columns(2)
            col1.metric("Risk Level", risk_label)
            col2.metric("Risk Score", f"{score}/100")
            st.progress(score/100)

            # Explanation
            st.write("---")
            st.subheader("🔍 Why This Prediction?")

            if reasons:
                st.write("**⚠️ Risk Factors:**")
                for reason in reasons:
                    st.write(f"• {reason}")

            if positives:
                st.write("**✅ Positive Factors:**")
                for positive in positives:
                    st.write(f"• {positive}")

            # Business Insights
            st.write("---")
            st.subheader("💡 Business Intelligence")
            st.write("*Data-driven insights to help you act smarter:*")
            for insight in insights:
                st.write(insight)

            # Recommended Action
            st.write("---")
            st.subheader("📋 Recommended Action")
            st.write(f"**{recommendation}**")

    # ---- TAB 2 ----
    with tab2:
        st.subheader("📊 Batch Analysis")
        st.write("Predict churn for multiple customers at once!")
        st.write("---")
        st.info("📥 CSV must have: **tenure, monthly_charges, senior_citizen, contract, internet_service**")

        if st.button("📊 Load Sample Data", key="sample"):
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

        uploaded_file = st.file_uploader("Upload CSV", type=["csv"])
        if uploaded_file is not None:
            st.session_state.batch_df = pd.read_csv(uploaded_file)

        if st.session_state.batch_df is not None:
            df = st.session_state.batch_df
            st.write(f"✅ **{len(df)} customers loaded!**")
            st.dataframe(df)

            if st.button("🔍 Predict All", use_container_width=True, key="batch"):
                with st.spinner("🤖 Analyzing all customers..."):
                    results = []
                    for idx, row in df.iterrows():
                        score, _, _, _ = predict_churn(
                            row["tenure"],
                            row["monthly_charges"],
                            str(row["senior_citizen"]),
                            row["contract"],
                            row["internet_service"]
                        )
                        if score >= 60:
                            risk = "HIGH RISK — Will Churn"
                        elif score >= 40:
                            risk = "MEDIUM RISK — Likely to Churn"
                        elif score >= 20:
                            risk = "LOW-MEDIUM RISK"
                        else:
                            risk = "LOW RISK — Will Stay"

                        results.append({
                            "Customer #": idx + 1,
                            "Risk Score": f"{score}/100",
                            "Prediction": risk
                        })

                results_df = pd.DataFrame(results)

                st.write("---")
                st.subheader("📈 Analysis Summary")
                col1, col2, col3, col4 = st.columns(4)
                col1.metric("Total Analyzed", len(results_df))
                col2.metric("🔴 High Risk", len([r for r in results if "HIGH RISK" in r["Prediction"] and "MEDIUM" not in r["Prediction"]]))
                col3.metric("🟡 Medium Risk", len([r for r in results if "MEDIUM" in r["Prediction"]]))
                col4.metric("✅ Low Risk", len([r for r in results if "LOW RISK — Will Stay" in r["Prediction"]]))

                st.write("---")
                st.subheader("📊 Risk Distribution")
                chart_data = pd.Series([r["Prediction"].split("—")[0].strip() for r in results]).value_counts()
                st.bar_chart(chart_data)

                st.write("---")
                st.subheader("📋 Full Results")
                st.dataframe(results_df)

                csv = results_df.to_csv(index=False)
                st.download_button(
                    "📥 Download Results",
                    data=csv,
                    file_name="churnshield_results.csv",
                    mime="text/csv"
                )

    # ---- TAB 3 ----
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
            tenure = st.slider("📅 Months with provider", 0, 72, 12, key="lt")
            monthly_charges = st.number_input(f"💰 Monthly payment ({currency})",
                                            0.0, 200000.0, 5000.0, key="lc")
            senior_citizen = st.selectbox("👤 Senior citizen?", ["No", "Yes"], key="ls")
        with col2:
            contract = st.selectbox("📋 Plan type",
                                  ["Month-to-month", "One year", "Two year"], key="lco")
            internet_service = st.selectbox("🌐 Internet type",
                                          ["DSL", "Fiber optic", "No"], key="li")
            satisfaction = st.selectbox("😊 How satisfied are you?",
                                      ["Very satisfied", "Satisfied",
                                       "Neutral", "Unsatisfied", "Very unsatisfied"])

        satisfaction_scores = {
            "Very satisfied": -15, "Satisfied": -10,
            "Neutral": 0, "Unsatisfied": 15, "Very unsatisfied": 25
        }

        if st.button("🔍 Check My Loyalty Score", use_container_width=True, key="loyalty"):
            with st.spinner("🤖 Analyzing your loyalty score..."):
                score, reasons, positives, _ = predict_churn(
                    tenure, monthly_charges/1000,
                    senior_citizen, contract, internet_service
                )
            score = min(100, score + satisfaction_scores[satisfaction])

            st.write("---")

            if score >= 60:
                st.error(f"""
                ## ⚠️ YOU ARE VERY LIKELY TO LEAVE!
                **Risk Score: {score}/100**
                Our AI predicts you will leave {provider} soon!
                """)
                advice = f"Call {provider} NOW and tell them you're thinking of leaving — they'll offer you a deal!"
            elif score >= 40:
   
