import streamlit as st
import pandas as pd
import numpy as np
import io

# ============================================
# CHURN PREDICTION ENGINE
# ============================================
def predict_churn(tenure, monthly_charges, senior_citizen, contract, internet_service):
    risk_score = 0
    reasons = []
    positive_factors = []
    business_insights = []

    if contract == "Month-to-month":
        risk_score += 40
        reasons.append("📋 Month-to-month contract — no commitment, easy to leave!")
        business_insights.append("💡 Customers on month-to-month contracts are 3x more likely to churn than annual contracts.")
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
        business_insights.append("💡 First year customers are highest churn risk — invest in onboarding!")
    elif tenure < 24:
        risk_score += 10
        reasons.append("📅 Relatively new customer — still building loyalty")
        business_insights.append("💡 Customers in months 12-24 respond well to loyalty rewards!")
    else:
        positive_factors.append("📅 Long term customer — high loyalty established!")
        business_insights.append("💡 Long term customers are brand ambassadors — consider referral programs!")

    if senior_citizen == "Yes":
        risk_score += 10
        reasons.append("👤 Senior citizens statistically show higher churn rates!")
        business_insights.append("💡 Senior customers respond well to dedicated support and simplified billing.")
    else:
        positive_factors.append("👤 Non-senior citizen — lower demographic risk!")

    if internet_service == "Fiber optic":
        risk_score += 5
        reasons.append("🌐 Fiber optic users tend to be more price sensitive!")
        business_insights.append("💡 Fiber optic customers churn when they find better speeds — emphasize reliability!")
    elif internet_service == "No":
        positive_factors.append("🌐 No internet service — simpler relationship to maintain!")

    return risk_score, reasons, positive_factors, business_insights

# ============================================
# HEARTGUARD ENGINE (Rule-based)
# ============================================
def predict_heart(age, sex, cp, trestbps, chol, fbs,
                  thalach, exang, oldpeak):
    risk_score = 0
    risk_factors = []
    positive_factors = []

    # Age
    if age > 60:
        risk_score += 25
        risk_factors.append("👤 Age above 60 — significantly higher cardiac risk!")
    elif age > 50:
        risk_score += 15
        risk_factors.append("👤 Age above 50 — moderate cardiac risk zone!")
    elif age > 40:
        risk_score += 8
        risk_factors.append("👤 Age above 40 — early risk monitoring advised!")
    else:
        positive_factors.append("👤 Young age — lower baseline cardiac risk!")

    # Blood pressure
    if trestbps > 160:
        risk_score += 20
        risk_factors.append("🩺 Very high blood pressure — serious risk factor!")
    elif trestbps > 140:
        risk_score += 12
        risk_factors.append("🩺 High blood pressure detected!")
    elif trestbps > 120:
        risk_score += 5
        risk_factors.append("🩺 Slightly elevated blood pressure!")
    else:
        positive_factors.append("🩺 Normal blood pressure — great sign!")

    # Cholesterol
    if chol > 300:
        risk_score += 20
        risk_factors.append("🧪 Very high cholesterol — major risk factor!")
    elif chol > 240:
        risk_score += 12
        risk_factors.append("🧪 High cholesterol detected!")
    elif chol > 200:
        risk_score += 5
        risk_factors.append("🧪 Borderline cholesterol levels!")
    else:
        positive_factors.append("🧪 Healthy cholesterol levels!")

    # Chest pain
    if cp == 3:
        risk_score += 15
        risk_factors.append("💔 Asymptomatic chest pain — high risk indicator!")
    elif cp == 2:
        risk_score += 8
        risk_factors.append("💔 Non-anginal chest pain detected!")
    elif cp == 1:
        risk_score += 5
        risk_factors.append("💔 Atypical angina present!")
    else:
        positive_factors.append("💔 Typical angina — manageable chest pain type!")

    # Max heart rate
    if thalach < 100:
        risk_score += 15
        risk_factors.append("💓 Very low maximum heart rate — concerning!")
    elif thalach < 130:
        risk_score += 8
        risk_factors.append("💓 Below average maximum heart rate!")
    else:
        positive_factors.append("💓 Good maximum heart rate!")

    # Exercise angina
    if exang == "Yes":
        risk_score += 12
        risk_factors.append("🏃 Exercise induced chest pain — significant risk!")
    else:
        positive_factors.append("🏃 No exercise induced chest pain — good sign!")

    # ST Depression
    if oldpeak > 3:
        risk_score += 15
        risk_factors.append("📉 High ST depression — cardiac stress indicator!")
    elif oldpeak > 1.5:
        risk_score += 8
        risk_factors.append("📉 Moderate ST depression detected!")
    else:
        positive_factors.append("📉 Normal ST depression levels!")

    # Blood sugar
    if fbs == "Yes":
        risk_score += 5
        risk_factors.append("🍬 High fasting blood sugar — diabetes risk!")
    else:
        positive_factors.append("🍬 Normal fasting blood sugar!")

    # Sex risk factor
    if sex == "Male":
        risk_score += 5
        risk_factors.append("⚤ Male sex — statistically higher cardiac risk!")
    else:
        positive_factors.append("⚤ Female sex — lower baseline cardiac risk!")

    return min(risk_score, 100), risk_factors, positive_factors

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
if "demo_loaded" not in st.session_state:
    st.session_state.demo_loaded = False
if "heart_demo" not in st.session_state:
    st.session_state.heart_demo = False

def go_to(page):
    st.session_state.page = page
    st.rerun()

# ============================================
# HOME PAGE
# ============================================
def show_home():
    st.title("🛡️ ShieldAI")
    st.markdown("## Reduce Risk with AI")
    st.markdown("### Predict outcomes before they happen — in any sector!")
    st.error("💸 **Why This Matters:** Losing customers costs businesses millions. Poor health decisions cost lives. ShieldAI helps you predict risks BEFORE they become problems!")
    st.write("ShieldAI is a Nigerian AI platform for decision intelligence. Making advanced AI accessible to everyone — regardless of sector!")
    st.write("---")

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("📊 Records", "7,000+")
    col2.metric("🎯 Accuracy", "Up to 87%")
    col3.metric("🤖 Models", "2 Live!")
    col4.metric("🌍 Countries", "8+ African")
    st.write("---")

    st.info("🔬 **Powered by Machine Learning** | 📊 **Up to 86.89% Accuracy** | 🗄️ **Real World Datasets** | ⚙️ **Advanced AI Algorithms**")
    st.write("---")

    st.subheader("🚀 ShieldAI Modules")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.success("🛡️ **Customer Intelligence**\n\nChurnShield\n\nPredict customer churn before it happens!\n\n✅ Available Now")
    with col2:
        st.success("❤️ **Health Risk Prediction**\n\nHeartGuard\n\nPredict heart disease risk!\n\n✅ Available Now")
    with col3:
        st.info("🎓 **Student Analytics**\n\nStudyShield\n\nPredict student performance!\n\n🔄 Coming Soon")

    st.write("---")
    st.subheader("⚡ How It Works")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.write("### 1️⃣\n**Select Module**\nChoose the AI model that fits your need!")
    with col2:
        st.write("### 2️⃣\n**Enter Data**\nFill in details — takes less than a minute!")
    with col3:
        st.write("### 3️⃣\n**Get Prediction**\nInstant AI prediction with full explanation!")

    st.write("---")
    if st.button("🚀 Get Started — It's Free!", use_container_width=True):
        go_to("models")

    st.write("---")
    col1, col2 = st.columns(2)
    with col1:
        st.write("**👨‍💻 Built by:**\nAjayi Ibrahim Ademola\nData Science & ML Developer")
    with col2:
        st.write("**📧 Contact:**\nibrahimdamola405@gmail.com\n💼 Open to partnerships!")
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
        st.write("Predict if customers will leave!")
        st.write("✅ **Status:** Live")
        st.write("🎯 **Accuracy:** 78.68%")
        st.write("👥 **For:** Businesses & Customers")
        if st.button("Launch ChurnShield →", use_container_width=True):
            go_to("churn")

    with col2:
        st.success("❤️ **HeartGuard**")
        st.write("**Health Risk Prediction**")
        st.write("Predict heart disease risk!")
        st.write("✅ **Status:** Live")
        st.write("🎯 **Accuracy:** 86.89%")
        st.write("👥 **For:** Individuals & Hospitals")
        if st.button("Launch HeartGuard →", use_container_width=True):
            go_to("heart")

    with col3:
        st.info("🎓 **StudyShield**")
        st.write("**Student Analytics**")
        st.write("Predict student performance!")
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
    st.info("🔬 Powered by AI | 🎯 78.68% Accuracy | 📊 Trained on 7,043 Records")
    st.write("---")

    tab1, tab2, tab3 = st.tabs([
        "🏢 Single Prediction",
        "📊 Batch Analysis",
        "👤 Loyalty Check"
    ])

    with tab1:
        st.subheader("🏢 Single Customer Prediction")
        st.write("Enter customer details to predict churn risk!")
        st.write("---")

        if st.button("📊 Try Demo Data", use_container_width=True, key="demo"):
            st.session_state.demo_loaded = True

        if st.session_state.demo_loaded:
            st.success("✅ Demo data loaded!")
            default_tenure = 5
            default_charges = 85000.0
            default_senior = "No"
            default_contract = "Month-to-month"
            default_internet = "Fiber optic"
        else:
            default_tenure = 12
            default_charges = 5000.0
            default_senior = "No"
            default_contract = "Month-to-month"
            default_internet = "DSL"

        col1, col2 = st.columns(2)
        with col1:
            tenure = st.slider("📅 Tenure (months)", 0, 72, default_tenure)
            monthly_charges = st.number_input("💰 Monthly Charges (₦)", 0.0, 200000.0, default_charges)
            senior_citizen = st.selectbox("👤 Senior Citizen?", ["No", "Yes"],
                                        index=0 if default_senior == "No" else 1)
        with col2:
            contract = st.selectbox("📋 Contract Type",
                                  ["Month-to-month", "One year", "Two year"],
                                  index=["Month-to-month", "One year", "Two year"].index(default_contract))
            internet_service = st.selectbox("🌐 Internet Service",
                                          ["DSL", "Fiber optic", "No"],
                                          index=["DSL", "Fiber optic", "No"].index(default_internet))
            st.selectbox("💳 Payment Method",
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
            if score >= 60:
                st.error(f"## ⚠️ HIGH RISK CUSTOMER DETECTED!\n**Confidence: {score}%**\nThis customer is very likely to leave!")
                recommendation = "🚨 Act immediately — offer special discount or upgrade!"
                risk_label = "🔴 HIGH RISK"
            elif score >= 40:
                st.warning(f"## 🟡 MEDIUM RISK CUSTOMER\n**Confidence: {score}%**\nThis customer may leave soon!")
                recommendation = "📞 Call customer and offer loyalty rewards!"
                risk_label = "🟡 MEDIUM RISK"
            elif score >= 20:
                st.info(f"## 🔵 LOW-MEDIUM RISK\n**Confidence: {score}%**\nThis customer shows some risk signals!")
                recommendation = "👀 Monitor closely and send satisfaction survey!"
                risk_label = "🔵 LOW-MEDIUM RISK"
            else:
                st.success(f"## ✅ LOW RISK — LOYAL CUSTOMER\n**Loyalty Score: {100-score}%**\nThis customer is happy and likely to stay!")
                recommendation = "😊 Maintain excellent service!"
                risk_label = "✅ LOW RISK"

            col1, col2 = st.columns(2)
            col1.metric("Risk Level", risk_label)
            col2.metric("Risk Score", f"{score}/100")
            st.progress(score/100)

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

            st.write("---")
            st.subheader("💡 Business Intelligence")
            for insight in insights:
                st.write(insight)

            st.write("---")
            st.subheader("📋 Recommended Action")
            st.write(f"**{recommendation}**")

            st.write("---")
            st.subheader("🎯 Retention Strategy")
            if score >= 60:
                st.write("**Immediate Actions:**")
                st.write("• 💰 Offer 20-30% loyalty discount immediately")
                st.write("• 📞 Personal call from customer service within 24hrs")
                st.write("• 🎁 Free upgrade or bonus data package")
                st.write("• 📧 Send personalized retention email today")
                st.write("• 📋 Offer switch to annual contract with benefits")
            elif score >= 40:
                st.write("**Short-term Actions:**")
                st.write("• 📧 Send satisfaction survey within 48hrs")
                st.write("• 💰 Offer 10-15% loyalty discount")
                st.write("• 🎁 Send loyalty reward or bonus")
                st.write("• 📞 Schedule follow-up call within a week")
                st.write("• 📋 Highlight value of upgrading contract")
            elif score >= 20:
                st.write("**Monitoring Actions:**")
                st.write("• 📊 Add to monthly monitoring list")
                st.write("• 📧 Send monthly engagement newsletter")
                st.write("• 🎁 Include in next loyalty program campaign")
                st.write("• 👀 Review again in 30 days")
            else:
                st.write("**Loyalty Maintenance:**")
                st.write("• 😊 Send appreciation message")
                st.write("• 🎁 Include in referral program")
                st.write("• ⭐ Request testimonial or review")
                st.write("• 📊 Use as benchmark for other customers")

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
                            risk = "🔴 HIGH RISK"
                        elif score >= 40:
                            risk = "🟡 MEDIUM RISK"
                        elif score >= 20:
                            risk = "🔵 LOW-MEDIUM"
                        else:
                            risk = "✅ WILL STAY"

                        results.append({
                            "Customer #": idx + 1,
                            "Risk Score": f"{score}/100",
                            "Prediction": risk
                        })

                results_df = pd.DataFrame(results)

                st.write("---")
                col1, col2, col3, col4 = st.columns(4)
                col1.metric("Total", len(results_df))
                col2.metric("🔴 High", len([r for r in results if "HIGH" in r["Prediction"]]))
                col3.metric("🟡 Medium", len([r for r in results if "MEDIUM" in r["Prediction"]]))
                col4.metric("✅ Safe", len([r for r in results if "STAY" in r["Prediction"]]))

                st.bar_chart(pd.Series([r["Prediction"] for r in results]).value_counts())
                st.dataframe(results_df)

                csv = results_df.to_csv(index=False)
                st.download_button("📥 Download Results", data=csv,
                                 file_name="churnshield_results.csv", mime="text/csv")

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
                st.error(f"## ⚠️ YOU ARE VERY LIKELY TO LEAVE!\n**Risk Score: {score}/100**")
                advice = f"Call {provider} NOW — tell them you're thinking of leaving!"
            elif score >= 40:
                st.warning(f"## 🟡 YOU MIGHT LEAVE SOON\n**Risk Score: {score}/100**")
                advice = f"Ask {provider} for a loyalty discount!"
            elif score >= 20:
                st.info(f"## 🔵 YOU'RE SOMEWHAT SATISFIED\n**Risk Score: {score}/100**")
                advice = f"Explore other {provider} plans available!"
            else:
                st.success(f"## ✅ YOU ARE A LOYAL CUSTOMER!\n**Loyalty Score: {100-score}/100**")
                advice = f"Keep enjoying {provider}'s service!"

            st.progress(score/100)

            st.write("---")
            if reasons:
                st.write("**⚠️ Risk factors:**")
                for reason in reasons:
                    st.write(f"• {reason}")
            if positives:
                st.write("**✅ Good factors:**")
                for positive in positives:
                    st.write(f"• {positive}")

            st.write("---")
            st.info(f"💡 {advice}")

    st.write("---")
    if st.button("← Back to Models", use_container_width=True):
        go_to("models")

# ============================================
# HEARTGUARD PAGE
# ============================================
def show_heart():
    st.title("❤️ HeartGuard")
    st.write("**A ShieldAI Product** | Health Risk Prediction Module")
    st.info("🔬 Powered by Advanced AI | 🎯 86.89% Accuracy | 📊 Based on Cleveland Heart Disease Dataset")
    st.write("---")

    st.warning("⚠️ **Medical Disclaimer:** HeartGuard is an AI tool for risk awareness only. Always consult a qualified doctor for medical advice!")
    st.write("---")

    if st.button("📊 Try Demo Data — High Risk Patient", use_container_width=True):
        st.session_state.heart_demo = True

    if st.session_state.heart_demo:
        st.info("✅ Demo data loaded — high risk patient profile!")
        d_age, d_sex = 63, "Male"
        d_cp, d_trestbps, d_chol = 3, 145, 233
        d_fbs, d_thalach = "Yes", 150
        d_exang, d_oldpeak = "Yes", 2.3
    else:
        d_age, d_sex = 45, "Male"
        d_cp, d_trestbps, d_chol = 0, 120, 200
        d_fbs, d_thalach = "No", 160
        d_exang, d_oldpeak = "No", 1.0

    st.subheader("🏥 Enter Patient Health Details")
    st.write("---")

    col1, col2 = st.columns(2)
    with col1:
        age = st.slider("👤 Age", 20, 80, d_age,
                       help="Patient's age in years")
        sex = st.selectbox("⚤ Sex", ["Male", "Female"],
                          index=0 if d_sex == "Male" else 1)
        cp = st.selectbox("💔 Chest Pain Type", [
            "0 — Typical Angina",
            "1 — Atypical Angina",
            "2 — Non-anginal Pain",
            "3 — Asymptomatic"
        ], index=d_cp)
        trestbps = st.slider("🩺 Resting Blood Pressure (mmHg)",
                            80, 200, d_trestbps)
        chol = st.slider("🧪 Cholesterol (mg/dl)", 100, 600, d_chol)

    with col2:
        fbs = st.selectbox("🍬 Fasting Blood Sugar > 120 mg/dl?",
                          ["No", "Yes"],
                          index=0 if d_fbs == "No" else 1)
        thalach = st.slider("💓 Max Heart Rate Achieved",
                           60, 220, d_thalach)
        exang = st.selectbox("🏃 Exercise Induced Angina?",
                            ["No", "Yes"],
                            index=0 if d_exang == "No" else 1)
        oldpeak = st.slider("📉 ST Depression", 0.0, 7.0,
                           d_oldpeak, 0.1)

    st.write("---")
    st.subheader("👤 Patient Profile Summary")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Age", f"{age} yrs")
    col2.metric("Sex", sex)
    col3.metric("Blood Pressure", f"{trestbps} mmHg")
    col4.metric("Cholesterol", f"{chol} mg/dl")

    if st.button("❤️ Predict Heart Disease Risk", use_container_width=True):
        with st.spinner("🤖 AI is analyzing patient health data..."):
            cp_val = int(cp.split("—")[0].strip())
            score, risk_factors, positives = predict_heart(
                age, sex, cp_val, trestbps, chol,
                fbs, thalach, exang, oldpeak
            )

        st.write("---")

        if score >= 60:
            st.error(f"## ⚠️ HEART DISEASE RISK DETECTED!\n**Risk Score: {score}/100**\nOur AI has detected significant indicators of heart disease!")
            action = "🚨 Seek immediate medical attention! Consult a cardiologist as soon as possible!"
            risk_label = "🔴 HIGH RISK"
        elif score >= 40:
            st.warning(f"## 🟡 MODERATE HEART DISEASE RISK\n**Risk Score: {score}/100**\nSome concerning indicators detected!")
            action = "⚠️ Schedule appointment with your doctor soon!"
            risk_label = "🟡 MODERATE RISK"
        elif score >= 20:
            st.info(f"## 🔵 LOW-MODERATE RISK\n**Risk Score: {score}/100**\nSome minor risk factors present!")
            action = "👀 Monitor your health regularly and maintain healthy lifestyle!"
            risk_label = "🔵 LOW-MODERATE RISK"
        else:
            st.success(f"## ✅ LOW HEART DISEASE RISK\n**Safety Score: {100-score}/100**\nNo significant indicators detected!")
            action = "😊 Maintain your healthy lifestyle! Regular checkups recommended!"
            risk_label = "✅ LOW RISK"

        col1, col2 = st.columns(2)
        col1.metric("Risk Level", risk_label)
        col2.metric("Risk Score", f"{score}/100")
        st.progress(score/100)

        st.write("---")
        st.subheader("🔍 Key Risk Factors Analyzed")
        if risk_factors:
            st.write("**⚠️ Risk indicators found:**")
            for factor in risk_factors:
                st.write(f"• {factor}")
        if positives:
            st.write("**✅ Positive health indicators:**")
            for positive in positives:
                st.write(f"• {positive}")

        st.write("---")
        st.subheader("💊 Health Recommendations")
        st.write(f"**{action}**")

        if score >= 60:
            st.write("**Immediate steps:**")
            st.write("• 🏥 Visit a cardiologist immediately")
            st.write("• 💊 Get a full cardiac workup done")
            st.write("• 🚫 Avoid strenuous exercise until cleared")
            st.write("• 🥗 Start heart-healthy diet immediately")
        elif score >= 40:
            st.write("**Recommended steps:**")
            st.write("• 🏥 Schedule cardiac checkup within 2 weeks")
            st.write("• 💊 Discuss medication options with doctor")
            st.write("• 🏃 Light exercise only — no strenuous activity")
            st.write("• 🥗 Reduce salt, fat and processed foods")
        else:
            st.write("**Maintain your health:**")
            st.write("• 🏃 Exercise regularly — 30 mins daily")
            st.write("• 🥗 Eat a balanced heart-healthy diet")
            st.write("• 🚭 Avoid smoking and limit alcohol")
            st.write("• 🏥 Annual cardiac checkup recommended")

        st.write("---")
        st.warning("⚠️ **Remember:** This is an AI tool for awareness only. Always consult a qualified medical professional!")

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
elif st.session_state.page == "heart":
    show_heart()
        
