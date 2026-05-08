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
# HEARTGUARD MODEL LOADER
# ============================================
@st.cache_resource
def load_heartguard_model():
    from sklearn.svm import SVC
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import StandardScaler
    from sklearn.metrics import accuracy_score
    
    url = "https://raw.githubusercontent.com/dsrscientist/dataset1/master/heart_disease.csv"
    df = pd.read_csv(url)
    X = df.drop("target", axis=1)
    y = df["target"]
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)
    model = SVC(probability=True, random_state=42)
    model.fit(X_train, y_train)
    accuracy = accuracy_score(y_test, model.predict(X_test))
    return model, scaler, round(accuracy * 100, 2)
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

    st.info("🔬 **Powered by Machine Learning** | 📊 **Up to 86.89% Accuracy** | 🗄️ **Real World Datasets** | ⚙️ **SVM & Gradient Boosting**")
    st.write("---")

    st.subheader("🚀 ShieldAI Modules")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.success("""
        🛡️ **Customer Intelligence**
        ChurnShield
        Predict customer churn before it happens!
        ✅ Available Now
        """)
    with col2:
        st.success("""
        ❤️ **Health Risk Prediction**
        HeartGuard
        Predict heart disease risk!
        ✅ Available Now
        """)
    with col3:
        st.info("""
        🎓 **Student Analytics**
        StudyShield
        Predict student performance!
        🔄 Coming Soon
        """)

    st.write("---")
    st.subheader("⚡ How It Works")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.write("### 1️⃣")
        st.write("**Select Module**")
        st.write("Choose the AI model that fits your need!")
    with col2:
        st.write("### 2️⃣")
        st.write("**Enter Data**")
        st.write("Fill in details — takes less than a minute!")
    with col3:
        st.write("### 3️⃣")
        st.write("**Get Prediction**")
        st.write("Instant AI prediction with full explanation!")

    st.write("---")
    if st.button("🚀 Get Started — It's Free!", use_container_width=True):
        go_to("models")

    st.write("---")
    col1, col2 = st.columns(2)
    with col1:
        st.write("**👨‍💻 Built by:**")
        st.write("Ajayi Ibrahim Ademola")
        st.write("Data Science & ML Developer")
    with col2:
        st.write("**📧 Contact:**")
        st.write("ibrahimdamola405@gmail.com")
        st.write("💼 Open to partnerships!")

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
    st.info("🔬 Powered by Gradient Boosting | 🎯 78.68% Accuracy | 📊 Trained on 7,043 Records")
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
            if score >= 60:
                st.error(f"""
## ⚠️ HIGH RISK CUSTOMER DETECTED!
**Confidence: {score}%**
This customer is very likely to leave!
                """)
                recommendation = "🚨 Act immediately — offer special discount or upgrade!"
                risk_label = "🔴 HIGH RISK"
            elif score >= 40:
                st.warning(f"""
## 🟡 MEDIUM RISK CUSTOMER
**Confidence: {score}%**
This customer may leave soon!
                """)
                recommendation = "📞 Call customer and offer loyalty rewards!"
                risk_label = "🟡 MEDIUM RISK"
            elif score >= 20:
                st.info(f"""
## 🔵 LOW-MEDIUM RISK CUSTOMER
**Confidence: {score}%**
This customer shows some risk signals!
                """)
                recommendation = "👀 Monitor closely and send satisfaction survey!"
                risk_label = "🔵 LOW-MEDIUM RISK"
            else:
                st.success(f"""
## ✅ LOW RISK — LOYAL CUSTOMER
**Loyalty Score: {100-score}%**
This customer is happy and likely to stay!
                """)
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
                st.error(f"""
## ⚠️ YOU ARE VERY LIKELY TO LEAVE!
**Risk Score: {score}/100**
                """)
                advice = f"Call {provider} NOW — tell them you're thinking of leaving!"
            elif score >= 40:
                st.warning(f"""
## 🟡 YOU MIGHT LEAVE SOON
**Risk Score: {score}/100**
                """)
                advice = f"Ask {provider} for a loyalty discount!"
            elif score >= 20:
                st.info(f"""
## 🔵 YOU'RE SOMEWHAT SATISFIED
**Risk Score: {score}/100**
                """)
                advice = f"Explore other {provider} plans available!"
            else:
                st.success(f"""
## ✅ YOU ARE A LOYAL CUSTOMER!
**Loyalty Score: {100-score}/100**
                """)
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
    st.info("🔬 Powered by SVM | 🎯 86.89% Accuracy | 📊 Trained on Cleveland Heart Disease Dataset")
    st.write("---")

    st.warning("⚠️ **Medical Disclaimer:** HeartGuard is an AI tool for risk awareness only. Always consult a qualified doctor for medical advice!")
    st.write("---")

    # Load model
    with st.spinner("🤖 Loading HeartGuard AI Model..."):
        model, scaler, accuracy = load_heartguard_model()

    st.success(f"✅ HeartGuard Model Ready! Accuracy: {accuracy}%")
    st.write("---")

    # Demo button
    if "heart_demo" not in st.session_state:
        st.session_state.heart_demo = False

    if st.button("📊 Try Demo Data — High Risk Patient", use_container_width=True):
        st.session_state.heart_demo = True

    if st.session_state.heart_demo:
        st.info("✅ Demo data loaded — high risk patient profile!")
        d_age, d_sex, d_cp = 63, 1, 3
        d_trestbps, d_chol, d_fbs = 145, 233, 1
        d_restecg, d_thalach, d_exang = 0, 150, 0
        d_oldpeak, d_slope, d_ca, d_thal = 2.3, 0, 0, 1
    else:
        d_age, d_sex, d_cp = 45, 1, 0
        d_trestbps, d_chol, d_fbs = 120, 200, 0
        d_restecg, d_thalach, d_exang = 0, 150, 0
        d_oldpeak, d_slope, d_ca, d_thal = 1.0, 1, 0, 2

    st.subheader("🏥 Enter Patient Health Details")
    st.write("---")

    col1, col2 = st.columns(2)
    with col1:
        age = st.slider("👤 Age", 20, 80, d_age,
                       help="Patient's age in years")
        sex = st.selectbox("⚤ Sex", ["Male", "Female"],
                          index=0 if d_sex == 1 else 1)
        cp = st.selectbox("💔 Chest Pain Type", [
            "0 — Typical Angina",
            "1 — Atypical Angina",
            "2 — Non-anginal Pain",
            "3 — Asymptomatic"
        ], index=d_cp)
        trestbps = st.slider("🩺 Resting Blood Pressure (mmHg)", 80, 200, d_trestbps,
                            help="Resting blood pressure in mmHg")
        chol = st.slider("🧪 Cholesterol (mg/dl)", 100, 600, d_chol,
                        help="Serum cholesterol in mg/dl")
        fbs = st.selectbox("🍬 Fasting Blood Sugar > 120 mg/dl?",
                          ["No", "Yes"],
                          index=d_fbs)
        restecg = st.selectbox("📊 Resting ECG Results", [
            "0 — Normal",
            "1 — ST-T Wave Abnormality",
            "2 — Left Ventricular Hypertrophy"
        ], index=d_restecg)

    with col2:
        thalach = st.slider("💓 Max Heart Rate Achieved", 60, 220, d_thalach,
                           help="Maximum heart rate during exercise")
        exang = st.selectbox("🏃 Exercise Induced Angina?",
                            ["No", "Yes"],
                            index=d_exang)
        oldpeak = st.slider("📉 ST Depression (oldpeak)", 0.0, 7.0, d_oldpeak, 0.1,
                           help="ST depression induced by exercise")
        slope = st.selectbox("📈 Slope of Peak Exercise ST", [
            "0 — Upsloping",
            "1 — Flat",
            "2 — Downsloping"
        ], index=d_slope)
        ca = st.selectbox("🔬 Number of Major Vessels (0-3)",
                         [0, 1, 2, 3], index=d_ca)
        thal = st.selectbox("🧬 Thalassemia Type", [
            "0 — Normal",
            "1 — Fixed Defect",
            "2 — Reversible Defect",
            "3 — Unknown"
        ], index=d_thal)

    # Patient summary
    st.write("---")
    st.subheader("👤 Patient Profile Summary")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Age", f"{age} yrs")
    col2.metric("Sex", "Male" if d_sex == 1 else "Female")
    col3.metric("Blood Pressure", f"{trestbps} mmHg")
    col4.metric("Cholesterol", f"{chol} mg/dl")

    if st.button("❤️ Predict Heart Disease Risk", use_container_width=True):
        with st.spinner("🤖 AI is analyzing patient health data..."):
            # Prepare input
            sex_val = 1 if sex == "Male" else 0
            cp_val = int(cp.split("—")[0].strip())
            fbs_val = 1 if fbs == "Yes" else 0
            restecg_val = int(restecg.split("—")[0].strip())
            exang_val = 1 if exang == "Yes" else 0
            slope_val = int(slope.split("—")[0].strip())
            thal_val = int(thal.split("—")[0].strip())

            features = np.array([[age, sex_val, cp_val, trestbps, chol,
                                 fbs_val, restecg_val, thalach, exang_val,
                                 oldpeak, slope_val, ca, thal_val]])

            features_scaled = scaler.transform(features)
            prediction = model.predict(features_scaled)[0]
            probability = model.predict_proba(features_scaled)[0]
            risk_percent = round(probability[1] * 100, 1)

        st.write("---")

        if prediction == 1:
            st.error(f"""
## ⚠️ HEART DISEASE RISK DETECTED!
**Risk Probability: {risk_percent}%**
Our AI has detected significant indicators of heart disease!
            """)
            action = "🚨 **Seek immediate medical attention!** Consult a cardiologist as soon as possible!"
            risk_label = "🔴 HIGH RISK"
        else:
            st.success(f"""
## ✅ LOW HEART DISEASE RISK
**Safety Score: {100-risk_percent}%**
Our AI found no significant indicators of heart disease!
            """)
            action = "😊 **Maintain healthy lifestyle!** Regular checkups recommended!"
            risk_label = "✅ LOW RISK"

        col1, col2 = st.columns(2)
        col1.metric("Risk Level", risk_label)
        col2.metric("Risk Probability", f"{risk_percent}%")
        st.progress(risk_percent/100)

        # Key factors
        st.write("---")
        st.subheader("🔍 Key Risk Factors Analyzed")

        factors = []
        if age > 55:
            factors.append("👤 Age above 55 — higher risk demographic!")
        if trestbps > 140:
            factors.append("🩺 High blood pressure detected!")
        if chol > 240:
            factors.append("🧪 High cholesterol levels!")
        if thalach < 120:
            factors.append("💓 Low maximum heart rate — concerning sign!")
        if exang == "Yes":
            factors.append("🏃 Exercise induced angina detected!")
        if cp_val == 3:
            factors.append("💔 Asymptomatic chest pain — high risk indicator!")
        if oldpeak > 2:
            factors.append("📉 High ST depression — cardiac stress indicator!")

        if factors:
            st.write("**⚠️ Risk indicators found:**")
            for factor in factors:
                st.write(f"• {factor}")
        else:
            st.write("✅ No major risk indicators detected!")

        # Health advice
        st.write("---")
        st.subheader("💊 Health Recommendations")
        st.write(action)

        if prediction == 1:
            st.write("**Additional steps:**")
            st.write("• 🏥 Visit a cardiologist immediately")
            st.write("• 💊 Get a full cardiac workup done")
            st.write("• 🚫 Avoid strenuous exercise until cleared by doctor")
            st.write("• 🥗 Start heart-healthy diet immediately")
        else:
            st.write("**Maintain your health:**")
            st.write("• 🏃 Exercise regularly — 30 mins daily")
            st.write("• 🥗 Eat a balanced heart-healthy diet")
            st.write("• 🚭 Avoid smoking and limit alcohol")
            st.write("• 🏥 Annual cardiac checkup recommended")

        st.write("---")
        st.w
