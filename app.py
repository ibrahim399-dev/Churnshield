# ============================================
# AEGIS AI — Decision Intelligence Platform
# ============================================
# Founder & Lead Developer: Ajayi Ibrahim Ademola
# Founded: 2026
# GitHub: github.com/ibrahim399-dev
# Email: ibrahimdamola405@gmail.com
#
# © 2026 Aegis AI. All Rights Reserved.
# ============================================
import requests
import json

# Supabase Configuration
SUPABASE_URL = "https://cyrdlpipaqmvirirhnfu.supabase.co"
SUPABASE_KEY = "sb_publishable_X7xfKtcFe64RWhaKijkeGQ_-VYqC1dA"

def save_prediction(email, model_used, result, risk_score):
    try:
        headers = {
            "apikey": SUPABASE_KEY,
            "Authorization": f"Bearer {SUPABASE_KEY}",
            "Content-Type": "application/json"
        }
        data = {
            "email": email,
            "model_used": model_used,
            "result": result,
            "risk_score": risk_score
        }
        response = requests.post(
            f"{SUPABASE_URL}/rest/v1/users_predictions",
            headers=headers,
            json=data
        )
        return True
    except:
        return False
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
        business_insights.append("💡 Customers on month-to-month contracts are 3x more likely to churn.")
    elif contract == "One year":
        risk_score += 10
        reasons.append("📋 One year contract — some commitment exists")
        business_insights.append("💡 One year contract customers churn 60% less than month-to-month.")
    else:
        positive_factors.append("📋 Two year contract — strong commitment!")
        business_insights.append("💡 Two year customers are your most loyal!")

    if monthly_charges > 70:
        risk_score += 25
        reasons.append("💰 High monthly charges increase financial pressure!")
        business_insights.append("💡 Customers paying above average are 2x more likely to leave.")
    elif monthly_charges > 50:
        risk_score += 10
        reasons.append("💰 Moderate monthly charges — worth monitoring")
        business_insights.append("💡 Consider offering loyalty discount to lock in this customer.")
    else:
        positive_factors.append("💰 Affordable charges — great value!")
        business_insights.append("💡 Low charge customers rarely churn.")

    if tenure < 12:
        risk_score += 20
        reasons.append("📅 New customer — loyalty not yet established!")
        business_insights.append("💡 First year customers are highest churn risk!")
    elif tenure < 24:
        risk_score += 10
        reasons.append("📅 Relatively new customer — still building loyalty")
        business_insights.append("💡 Customers in months 12-24 respond well to loyalty rewards!")
    else:
        positive_factors.append("📅 Long term customer — high loyalty!")
        business_insights.append("💡 Long term customers are brand ambassadors!")

    if senior_citizen == "Yes":
        risk_score += 10
        reasons.append("👤 Senior citizens show higher churn rates!")
        business_insights.append("💡 Senior customers respond well to dedicated support.")
    else:
        positive_factors.append("👤 Non-senior citizen — lower risk!")

    if internet_service == "Fiber optic":
        risk_score += 5
        reasons.append("🌐 Fiber optic users tend to be more price sensitive!")
        business_insights.append("💡 Fiber optic customers churn when they find better speeds!")
    elif internet_service == "No":
        positive_factors.append("🌐 No internet service — simpler relationship!")

    return risk_score, reasons, positive_factors, business_insights

# ============================================
# HEARTGUARD ENGINE
# ============================================
def predict_heart(age, sex, cp, trestbps, chol, fbs, thalach, exang, oldpeak):
    risk_score = 0
    risk_factors = []
    positive_factors = []

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
        positive_factors.append("🩺 Normal blood pressure!")

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

    if cp == 3:
        risk_score += 15
        risk_factors.append("💔 Asymptomatic chest pain — high risk!")
    elif cp == 2:
        risk_score += 8
        risk_factors.append("💔 Non-anginal chest pain detected!")
    elif cp == 1:
        risk_score += 5
        risk_factors.append("💔 Atypical angina present!")
    else:
        positive_factors.append("💔 Typical angina — manageable!")

    if thalach < 100:
        risk_score += 15
        risk_factors.append("💓 Very low maximum heart rate!")
    elif thalach < 130:
        risk_score += 8
        risk_factors.append("💓 Below average maximum heart rate!")
    else:
        positive_factors.append("💓 Good maximum heart rate!")

    if exang == "Yes":
        risk_score += 12
        risk_factors.append("🏃 Exercise induced chest pain!")
    else:
        positive_factors.append("🏃 No exercise induced chest pain!")

    if oldpeak > 3:
        risk_score += 15
        risk_factors.append("📉 High ST depression!")
    elif oldpeak > 1.5:
        risk_score += 8
        risk_factors.append("📉 Moderate ST depression!")
    else:
        positive_factors.append("📉 Normal ST depression!")

    if fbs == "Yes":
        risk_score += 5
        risk_factors.append("🍬 High fasting blood sugar!")
    else:
        positive_factors.append("🍬 Normal fasting blood sugar!")

    if sex == "Male":
        risk_score += 5
        risk_factors.append("⚤ Male — statistically higher cardiac risk!")
    else:
        positive_factors.append("⚤ Female — lower baseline cardiac risk!")

    return min(risk_score, 100), risk_factors, positive_factors

# ============================================
# STUDYSHIELD ENGINE
# ============================================
def predict_study(study_hours, attendance, assignment_completion,
                  past_score, sleep_hours, distraction_level,
                  parent_support, extra_classes):
    risk_score = 0
    risk_factors = []
    positive_factors = []
    study_tips = []

    if study_hours < 2:
        risk_score += 30
        risk_factors.append("📚 Very low study hours — less than 2hrs daily!")
        study_tips.append("💡 Increase study time to minimum 3 hours daily!")
    elif study_hours < 4:
        risk_score += 15
        risk_factors.append("📚 Below average study hours!")
        study_tips.append("💡 Try to study at least 4 hours daily!")
    else:
        positive_factors.append("📚 Good study hours — keep it up!")
        study_tips.append("💡 Maintain your study schedule!")

    if attendance < 60:
        risk_score += 35
        risk_factors.append("🏫 Very low attendance — below 60%!")
        study_tips.append("💡 Attendance is the #1 predictor of passing — attend ALL classes!")
    elif attendance < 75:
        risk_score += 20
        risk_factors.append("🏫 Below average attendance!")
        study_tips.append("💡 Try to attend at least 80% of classes!")
    else:
        positive_factors.append("🏫 Good attendance — excellent!")
        study_tips.append("💡 Keep attending classes consistently!")

    if past_score < 40:
        risk_score += 25
        risk_factors.append("📊 Low past scores — needs serious improvement!")
        study_tips.append("💡 Focus on weak subjects — get a study partner!")
    elif past_score < 60:
        risk_score += 12
        risk_factors.append("📊 Average past scores — room for improvement!")
        study_tips.append("💡 Review past mistakes and practice more!")
    else:
        positive_factors.append("📊 Good past scores — well done!")
        study_tips.append("💡 Maintain your performance!")

    if assignment_completion < 50:
        risk_score += 15
        risk_factors.append("📝 Low assignment completion rate!")
        study_tips.append("💡 Complete all assignments — they prepare you for exams!")
    elif assignment_completion < 75:
        risk_score += 8
        risk_factors.append("📝 Moderate assignment completion!")
        study_tips.append("💡 Try to complete at least 80% of assignments!")
    else:
        positive_factors.append("📝 Excellent assignment completion!")

    if distraction_level > 7:
        risk_score += 15
        risk_factors.append("📱 Very high distraction level!")
        study_tips.append("💡 Put your phone away during study time!")
    elif distraction_level > 5:
        risk_score += 8
        risk_factors.append("📱 Moderate distraction level!")
        study_tips.append("💡 Find a quiet study environment!")
    else:
        positive_factors.append("📱 Low distraction — great focus!")

    if sleep_hours < 5:
        risk_score += 10
        risk_factors.append("😴 Very low sleep hours — affects brain performance!")
        study_tips.append("💡 Sleep at least 7 hours for better memory retention!")
    elif sleep_hours >= 7:
        positive_factors.append("😴 Good sleep hours — brain is well rested!")

    if parent_support == "Yes":
        positive_factors.append("👨‍👩‍👧 Good parental support!")
    else:
        risk_score += 5
        study_tips.append("💡 Talk to your parents or a mentor for guidance!")

    if extra_classes == "Yes":
        positive_factors.append("📖 Taking extra classes — great initiative!")
    else:
        risk_score += 5
        study_tips.append("💡 Consider joining extra classes or study groups!")

    return min(risk_score, 100), risk_factors, positive_factors, study_tips

# ============================================
# CAREERSHIELD ENGINE
# ============================================
def recommend_career(loves_numbers, loves_talking, loves_helping,
                     loves_creating, loves_technology, loves_reading,
                     works_under_pressure, prefers_outdoor,
                     leadership_style, financial_goal):
    scores = {
        "Banking & Accounting": 0,
        "Data Science & AI": 0,
        "Mass Communication": 0,
        "Medicine & Health": 0,
        "Law": 0,
        "Engineering": 0,
        "Theater & Arts": 0,
        "Entrepreneurship": 0,
        "Teaching & Education": 0,
        "Trading & Finance": 0
    }

    if loves_numbers == "Yes":
        scores["Banking & Accounting"] += 30
        scores["Data Science & AI"] += 25
        scores["Engineering"] += 20
        scores["Trading & Finance"] += 25

    if loves_talking == "Yes":
        scores["Mass Communication"] += 35
        scores["Law"] += 30
        scores["Teaching & Education"] += 25
        scores["Entrepreneurship"] += 20

    if loves_helping == "Yes":
        scores["Medicine & Health"] += 35
        scores["Teaching & Education"] += 30
        scores["Mass Communication"] += 15

    if loves_creating == "Yes":
        scores["Theater & Arts"] += 35
        scores["Mass Communication"] += 20
        scores["Entrepreneurship"] += 25
        scores["Data Science & AI"] += 15

    if loves_technology == "Yes":
        scores["Data Science & AI"] += 35
        scores["Engineering"] += 30
        scores["Trading & Finance"] += 15

    if loves_reading == "Yes":
        scores["Law"] += 30
        scores["Medicine & Health"] += 25
        scores["Data Science & AI"] += 20
        scores["Teaching & Education"] += 20

    if works_under_pressure == "Yes":
        scores["Medicine & Health"] += 20
        scores["Law"] += 20
        scores["Trading & Finance"] += 25
        scores["Theater & Arts"] += 20

    if leadership_style == "Yes":
        scores["Entrepreneurship"] += 35
        scores["Law"] += 20
        scores["Banking & Accounting"] += 15

    if financial_goal == "Very High Income":
        scores["Medicine & Health"] += 15
        scores["Law"] += 15
        scores["Trading & Finance"] += 20
        scores["Entrepreneurship"] += 20
        scores["Data Science & AI"] += 15
    elif financial_goal == "Stable Income":
        scores["Banking & Accounting"] += 20
        scores["Teaching & Education"] += 15
        scores["Engineering"] += 15

    sorted_careers = sorted(scores.items(),
                           key=lambda x: x[1], reverse=True)
    return sorted_careers[:3]

# JAMB Combinations
jamb_combinations = {
    "Data Science & AI": {
        "subjects": ["Mathematics", "Physics", "Chemistry", "English"],
        "cutoff": "200+",
        "universities": ["UNILAG", "OAU", "UNIBEN", "AAUA", "UI"],
        "course": "Computer Science / Statistics",
        "job_prospects": "Very High 🔥",
        "salary_range": "₦200k — ₦2M monthly"
    },
    "Banking & Accounting": {
        "subjects": ["Mathematics", "Economics", "Accounting", "English"],
        "cutoff": "180+",
        "universities": ["UNILAG", "OAU", "UNIBEN", "ABU", "AAUA"],
        "course": "Accounting / Banking & Finance",
        "job_prospects": "High ✅",
        "salary_range": "₦150k — ₦800k monthly"
    },
    "Medicine & Health": {
        "subjects": ["Biology", "Chemistry", "Physics", "English"],
        "cutoff": "280+",
        "universities": ["UI", "UNILAG", "UNIBEN", "OAU", "UNILORIN"],
        "course": "Medicine & Surgery / Nursing",
        "job_prospects": "Very High 🔥",
        "salary_range": "₦300k — ₦2M monthly"
    },
    "Mass Communication": {
        "subjects": ["English", "Literature", "Government", "CRS/IRS"],
        "cutoff": "180+",
        "universities": ["UNILAG", "OAU", "UNIJOS", "AAUA", "BU"],
        "course": "Mass Communication / Journalism",
        "job_prospects": "Medium 📊",
        "salary_range": "₦100k — ₦500k monthly"
    },
    "Law": {
        "subjects": ["English", "Literature", "Government", "CRS/IRS"],
        "cutoff": "220+",
        "universities": ["UI", "UNILAG", "OAU", "ABU", "UNIBEN"],
        "course": "Law (LLB)",
        "job_prospects": "High ✅",
        "salary_range": "₦200k — ₦1.5M monthly"
    },
    "Engineering": {
        "subjects": ["Mathematics", "Physics", "Chemistry", "English"],
        "cutoff": "200+",
        "universities": ["UNILAG", "OAU", "UI", "ABU", "FUTA"],
        "course": "Civil / Electrical / Mechanical Engineering",
        "job_prospects": "Very High 🔥",
        "salary_range": "₦200k — ₦1M monthly"
    },
    "Theater & Arts": {
        "subjects": ["English", "Literature", "Fine Arts", "Government"],
        "cutoff": "160+",
        "universities": ["UNILAG", "OAU", "UNIBEN", "ABU", "AAUA"],
        "course": "Theater Arts / Creative Arts",
        "job_prospects": "Medium 📊",
        "salary_range": "₦80k — ₦500k monthly"
    },
    "Entrepreneurship": {
        "subjects": ["Mathematics", "Economics", "Commerce", "English"],
        "cutoff": "160+",
        "universities": ["UNILAG", "OAU", "UNIBEN", "AAUA", "BU"],
        "course": "Business Administration / Economics",
        "job_prospects": "Depends on you! 😂",
        "salary_range": "₦0 — ₦Unlimited 🚀"
    },
    "Teaching & Education": {
        "subjects": ["English", "Mathematics", "Biology", "Economics"],
        "cutoff": "160+",
        "universities": ["UNILAG", "OAU", "UNIBEN", "ABU", "AAUA"],
        "course": "Education / Arts Education",
        "job_prospects": "Stable ✅",
        "salary_range": "₦80k — ₦300k monthly"
    },
    "Trading & Finance": {
        "subjects": ["Mathematics", "Economics", "Accounting", "English"],
        "cutoff": "180+",
        "universities": ["UNILAG", "OAU", "UNIBEN", "ABU", "AAUA"],
        "course": "Finance / Economics / Statistics",
        "job_prospects": "High ✅",
        "salary_range": "₦200k — ₦Unlimited 🚀"
    }
}
# ============================================
# FOREXSENSE ENGINE
# ============================================
def predict_forex(market_bias, model_aligned, confirmation_score,
                  liquidity_swept, choch_formed, bos_confirmed,
                  risk_reward, session, news_event, higher_tf_aligned):
    score = 0
    reasons = []
    warnings = []

    if model_aligned == "Yes":
        score += 30
        reasons.append("✅ Model is aligned — good sign!")
    else:
        score -= 30
        warnings.append("❌ Model NOT aligned — stay out!")

    if higher_tf_aligned == "Yes":
        score += 20
        reasons.append("✅ Higher timeframe confirms direction!")
    else:
        warnings.append("⚠️ Higher timeframe not aligned!")

    if liquidity_swept == "Yes":
        score += 15
        reasons.append("✅ Liquidity swept — smart money active!")
    else:
        warnings.append("⚠️ No liquidity sweep yet!")

    if choch_formed == "Yes":
        score += 10
        reasons.append("✅ Change of Character confirmed!")

    if bos_confirmed == "Yes":
        score += 10
        reasons.append("✅ Break of Structure confirmed!")

    if confirmation_score >= 7:
        score += 15
        reasons.append(f"✅ Strong confirmation score: {confirmation_score}/10!")
    elif confirmation_score >= 5:
        score += 8
        reasons.append(f"⚠️ Moderate confirmation: {confirmation_score}/10")
    else:
        warnings.append(f"❌ Weak confirmation: {confirmation_score}/10 — wait!")

    if risk_reward >= 2:
        score += 10
        reasons.append(f"✅ Excellent RR: {risk_reward}!")
    elif risk_reward >= 1.5:
        score += 5
        reasons.append(f"✅ Good RR: {risk_reward}")
    else:
        warnings.append(f"⚠️ Low RR: {risk_reward} — consider skipping!")

    if news_event == "Yes":
        score -= 10
        warnings.append("⚠️ News event active — higher risk!")

    if market_bias == "Bullish" and session == "London/NY":
        score += 5
        reasons.append("✅ Bullish bias during peak session!")
    elif market_bias == "Bearish" and session == "London/NY":
        score += 5
        reasons.append("✅ Bearish bias during peak session!")

    return min(max(score, 0), 100), reasons, warnings

# ============================================
# HEALTHCHECK ENGINE
# ============================================
def predict_health(sleep_hours, sleep_quality, stress_level,
                   exercise_minutes, water_intake, fruit_veg,
                   screen_time, mood_score, energy_level, meals):
    score = 0
    risk_factors = []
    positive_factors = []
    tips = []

    if sleep_hours >= 7:
        score += 20
        positive_factors.append("😴 Great sleep duration!")
    elif sleep_hours >= 6:
        score += 10
        tips.append("💡 Try to get 7-8 hours sleep!")
    else:
        score -= 15
        risk_factors.append("😴 Very low sleep — affects everything!")
        tips.append("💡 Sleep is non-negotiable — aim for 7+ hours!")

    if sleep_quality >= 7:
        score += 15
        positive_factors.append("✅ Excellent sleep quality!")
    elif sleep_quality >= 5:
        score += 5
        tips.append("💡 Improve sleep quality — no screens before bed!")
    else:
        risk_factors.append("❌ Poor sleep quality!")
        tips.append("💡 Create a bedtime routine for better sleep!")

    if stress_level <= 3:
        score += 15
        positive_factors.append("✅ Low stress — great mental health!")
    elif stress_level <= 6:
        score += 5
        tips.append("💡 Practice breathing exercises to reduce stress!")
    else:
        score -= 10
        risk_factors.append("⚠️ High stress level detected!")
        tips.append("💡 Take breaks, meditate or exercise to reduce stress!")

    if exercise_minutes >= 30:
        score += 20
        positive_factors.append("🏃 Excellent exercise habit!")
    elif exercise_minutes >= 15:
        score += 10
        tips.append("💡 Increase exercise to 30 mins daily!")
    else:
        score -= 5
        risk_factors.append("❌ Very little exercise!")
        tips.append("💡 Even a 20 minute walk daily makes huge difference!")

    if water_intake >= 2:
        score += 15
        positive_factors.append("💧 Well hydrated — excellent!")
    elif water_intake >= 1.5:
        score += 8
        tips.append("💡 Drink at least 2 litres of water daily!")
    else:
        score -= 10
        risk_factors.append("❌ Dehydrated — drink more water!")
        tips.append("💡 Keep a water bottle with you always!")

    if mood_score >= 7:
        score += 10
        positive_factors.append("😊 Great mood today!")
    elif mood_score <= 3:
        score -= 10
        risk_factors.append("😔 Low mood detected!")
        tips.append("💡 Talk to someone or do something you enjoy!")

    if energy_level >= 7:
        score += 5
        positive_factors.append("⚡ High energy — great!")
    elif energy_level <= 3:
        risk_factors.append("😴 Very low energy!")
        tips.append("💡 Check your sleep and nutrition!")

    return min(max(score, 0), 100), risk_factors, positive_factors, tips
# ============================================
# PAGE CONFIG
# ============================================
st.set_page_config(
    page_title="Aegis AI — Decision Intelligence Platform",
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
    st.image("https://raw.githubusercontent.com/ibrahim399-dev/Churnshield/main/logo-header.png", use_column_width=True)
    st.markdown("## Reduce Risk with AI")
    st.markdown("### Predict. Analyze. Protect.")
    st.error("💸 **Why This Matters:** Losing customers costs millions. Poor health decisions cost lives. Wrong career choices waste years. Aegis AI helps you predict risks BEFORE they become problems!")
    st.write("Aegis AI is a Nigerian AI platform for decision intelligence. Making advanced AI accessible to everyone — regardless of sector!")
    st.write("---")

    col1.metric("📊 Records", "10,000+")
    col2.metric("🎯 Accuracy", "Up to 91.5%")
    col3.metric("🤖 Models", "6 Live!")
    col4.metric("🌍 Countries", "8+ African")
    st.write("---")

    st.info("🔬 **Powered by Machine Learning** | 📊 **Up to 91.5% Accuracy** | 🗄️ **Real World Datasets** | ⚙️ **6 AI Models Live!**")
    st.write("---")

    st.subheader("🚀 Aegis AI Modules")
    col1, col2 = st.columns(2)
    with col1:
        st.success("🛡️ **ChurnShield**\nCustomer churn prediction!\n✅ Live — 78.68% accuracy")
        st.success("❤️ **HeartGuard**\nHeart disease risk prediction!\n✅ Live — 86.89% accuracy")
    with col2:
        st.success("🎓 **StudyShield**\nStudent performance prediction!\n✅ Live — 91.5% accuracy")
        st.success("💼 **CareerShield**\nCareer path & JAMB guide!\n✅ Live — AI Powered")

    st.write("---")
    st.subheader("⚡ How It Works")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.write("### 1️⃣\n**Select Module**\nChoose the AI model!")
    with col2:
        st.write("### 2️⃣\n**Enter Data**\nFill in details!")
    with col3:
        st.write("### 3️⃣\n**Get Prediction**\nInstant AI result!")

    st.write("---")
    if st.button("🚀 Get Started — It's Free!", use_container_width=True):
        go_to("models")

    st.write("---")
    col1, col2 = st.columns(2)
    with col1:
        st.write("**👨‍💻 Built by:**\nAjayi Ibrahim Ademola\nFounder & CEO, Aegis AI")
    with col2:
        st.write("**📧 Contact:**\nibrahimdamola405@gmail.com\n💼 Open to partnerships!")
    st.caption("© 2026 Aegis AI | Founded by Ajayi Ibrahim Ademola | All Rights Reserved")

# ============================================
# MODELS PAGE
# ============================================
st.write("6 AI models — choose what you need!")
st.write("---")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.success("🛡️ **ChurnShield**")
        st.write("Customer churn prediction")
        st.write("✅ Live | 🎯 78.68%")
        if st.button("Launch ChurnShield →", use_container_width=True):
            go_to("churn")

    with col2:
        st.success("❤️ **HeartGuard**")
        st.write("Heart disease prediction")
        st.write("✅ Live | 🎯 86.89%")
        if st.button("Launch HeartGuard →", use_container_width=True):
            go_to("heart")

    with col3:
        st.success("🎓 **StudyShield**")
        st.write("Student performance")
        st.write("✅ Live | 🎯 91.5%")
        if st.button("Launch StudyShield →", use_container_width=True):
            go_to("study")

    st.write("---")
    col4, col5, col6 = st.columns(3)
    with col4:
        st.success("💼 **CareerShield**")
        st.write("Career path & JAMB guide")
        st.write("✅ Live | 🎯 AI Powered")
        if st.button("Launch CareerShield →", use_container_width=True):
            go_to("career")

    with col5:
        st.success("📈 **ForexSense**")
        st.write("Trading setup analyzer")
        st.write("✅ Live | 🎯 89%")
        if st.button("Launch ForexSense →", use_container_width=True):
            go_to("forex")

    with col6:
        st.success("😴 **HealthCheck**")
        st.write("Daily wellness checker")
        st.write("✅ Live | 🎯 90.75%")
        if st.button("Launch HealthCheck →", use_container_width=True):
            go_to("health")

    st.write("---")
    if st.button("← Back to Home", use_container_width=True):
        go_to("home")
                   # ============================================
# CHURNSHIELD PAGE
# ============================================
def show_churn():
    st.title("🛡️ ChurnShield")
    st.write("**An Aegis AI Product** | Customer Intelligence Module")
    st.info("🔬 Powered by AI | 🎯 78.68% Accuracy | 📊 Trained on 7,043 Records")
    st.write("---")

    tab1, tab2, tab3 = st.tabs([
        "🏢 Single Prediction",
        "📊 Batch Analysis",
        "👤 Loyalty Check"
    ])

    with tab1:
        st.subheader("🏢 Single Customer Prediction")
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
            with st.spinner("🤖 AI analyzing customer data..."):
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
                st.info(f"## 🔵 LOW-MEDIUM RISK\n**Confidence: {score}%**\nSome risk signals detected!")
                recommendation = "👀 Monitor closely!"
                risk_label = "🔵 LOW-MEDIUM RISK"
            else:
                st.success(f"## ✅ LOW RISK — LOYAL CUSTOMER\n**Loyalty Score: {100-score}%**\nCustomer is happy!")
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
                st.write("• 💰 Offer 20-30% loyalty discount immediately")
                st.write("• 📞 Personal call within 24hrs")
                st.write("• 🎁 Free upgrade or bonus data package")
                st.write("• 📧 Send personalized retention email")
                st.write("• 📋 Offer switch to annual contract")
            elif score >= 40:
                st.write("• 📧 Send satisfaction survey within 48hrs")
                st.write("• 💰 Offer 10-15% loyalty discount")
                st.write("• 🎁 Send loyalty reward")
                st.write("• 📞 Schedule follow-up call")
            elif score >= 20:
                st.write("• 📊 Add to monthly monitoring list")
                st.write("• 📧 Send engagement newsletter")
                st.write("• 👀 Review again in 30 days")
            else:
                st.write("• 😊 Send appreciation message")
                st.write("• 🎁 Include in referral program")
                st.write("• ⭐ Request testimonial")

    with tab2:
        st.subheader("📊 Batch Analysis")
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
                            row["tenure"], row["monthly_charges"],
                            str(row["senior_citizen"]), row["contract"],
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
                col1, col2, col3, col4 = st.columns(4)
                col1.metric("Total", len(results_df))
                col2.metric("🔴 High", len([r for r in results if "HIGH" in r["Prediction"]]))
                col3.metric("🟡 Medium", len([r for r in results if "MEDIUM" in r["Prediction"]]))
                col4.metric("✅ Safe", len([r for r in results if "STAY" in r["Prediction"]]))

                st.write("---")
                st.subheader("📊 Visual Analytics")
                risk_counts = pd.Series([r["Prediction"] for r in results]).value_counts()
                col1, col2 = st.columns(2)
                with col1:
                    st.write("**📊 Risk Distribution**")
                    st.bar_chart(risk_counts)
                with col2:
                    st.write("**📈 Risk Scores**")
                    scores = [int(r["Risk Score"].split("/")[0]) for r in results]
                    score_data = pd.DataFrame({
                        "Customer": [r["Customer #"] for r in results],
                        "Risk Score": scores
                    }).set_index("Customer")
                    st.line_chart(score_data)

                total = len(results)
                high = len([r for r in results if "HIGH" in r["Prediction"]])
                st.write(f"⚠️ **{round(high/total*100)}% of customers are at HIGH risk!**")
                st.dataframe(results_df)

                csv = results_df.to_csv(index=False)
                st.download_button("📥 Download Results", data=csv,
                                 file_name="aegisai_churn_results.csv",
                                 mime="text/csv")

    with tab3:
        st.subheader("👤 Customer Loyalty Check")
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

        if st.button("🔍 Check My Loyalty Score",
                    use_container_width=True, key="loyalty"):
            with st.spinner("🤖 Analyzing loyalty..."):
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
                advice = f"Explore other {provider} plans!"
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
    st.write("**An Aegis AI Product** | Health Risk Prediction Module")
    st.info("🔬 Powered by Advanced AI | 🎯 86.89% Accuracy | 📊 Cleveland Heart Disease Dataset")
    st.write("---")
    st.warning("⚠️ **Medical Disclaimer:** HeartGuard is for awareness only. Always consult a qualified doctor!")
    st.write("---")

    if "heart_demo" not in st.session_state:
        st.session_state.heart_demo = False

    if st.button("📊 Try Demo Data — High Risk Patient", use_container_width=True):
        st.session_state.heart_demo = True

    if st.session_state.heart_demo:
        d_age, d_sex = 63, "Male"
        d_cp, d_trestbps, d_chol = 3, 145, 233
        d_fbs, d_thalach = "Yes", 150
        d_exang, d_oldpeak = "Yes", 2.3
        st.info("✅ Demo loaded — high risk patient!")
    else:
        d_age, d_sex = 45, "Male"
        d_cp, d_trestbps, d_chol = 0, 120, 200
        d_fbs, d_thalach = "No", 160
        d_exang, d_oldpeak = "No", 1.0

    col1, col2 = st.columns(2)
    with col1:
        age = st.slider("👤 Age", 20, 80, d_age)
        sex = st.selectbox("⚤ Sex", ["Male", "Female"],
                          index=0 if d_sex == "Male" else 1)
        cp = st.selectbox("💔 Chest Pain Type", [
            "0 — Typical Angina", "1 — Atypical Angina",
            "2 — Non-anginal Pain", "3 — Asymptomatic"
        ], index=d_cp)
        trestbps = st.slider("🩺 Blood Pressure (mmHg)", 80, 200, d_trestbps)
        chol = st.slider("🧪 Cholesterol (mg/dl)", 100, 600, d_chol)
    with col2:
        fbs = st.selectbox("🍬 Fasting Blood Sugar > 120?", ["No", "Yes"],
                          index=0 if d_fbs == "No" else 1)
        thalach = st.slider("💓 Max Heart Rate", 60, 220, d_thalach)
        exang = st.selectbox("🏃 Exercise Angina?", ["No", "Yes"],
                            index=0 if d_exang == "No" else 1)
        oldpeak = st.slider("📉 ST Depression", 0.0, 7.0, d_oldpeak, 0.1)

    st.write("---")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Age", f"{age} yrs")
    col2.metric("Sex", sex)
    col3.metric("Blood Pressure", f"{trestbps} mmHg")
    col4.metric("Cholesterol", f"{chol} mg/dl")

    if st.button("❤️ Predict Heart Disease Risk", use_container_width=True):
        with st.spinner("🤖 Analyzing health data..."):
            cp_val = int(cp.split("—")[0].strip())
            score, risk_factors, positives = predict_heart(
                age, sex, cp_val, trestbps, chol,
                fbs, thalach, exang, oldpeak
            )

        st.write("---")
        if score >= 60:
            st.error(f"## ⚠️ HEART DISEASE RISK DETECTED!\n**Risk Score: {score}/100**")
            action = "🚨 Seek immediate medical attention!"
            risk_label = "🔴 HIGH RISK"
        elif score >= 40:
            st.warning(f"## 🟡 MODERATE RISK\n**Risk Score: {score}/100**")
            action = "⚠️ Schedule doctor appointment soon!"
            risk_label = "🟡 MODERATE RISK"
        elif score >= 20:
            st.info(f"## 🔵 LOW-MODERATE RISK\n**Risk Score: {score}/100**")
            action = "👀 Monitor health regularly!"
            risk_label = "🔵 LOW-MODERATE"
        else:
            st.success(f"## ✅ LOW RISK\n**Safety Score: {100-score}/100**")
            action = "😊 Maintain healthy lifestyle!"
            risk_label = "✅ LOW RISK"

        col1, col2 = st.columns(2)
        col1.metric("Risk Level", risk_label)
        col2.metric("Risk Score", f"{score}/100")
        st.progress(score/100)

        st.write("---")
        if risk_factors:
            st.write("**⚠️ Risk indicators:**")
            for factor in risk_factors:
                st.write(f"• {factor}")
        if positives:
            st.write("**✅ Positive indicators:**")
            for positive in positives:
                st.write(f"• {positive}")

        st.write("---")
        st.subheader("💊 Recommendations")
        st.write(f"**{action}**")
        if score >= 60:
            st.write("• 🏥 Visit cardiologist immediately")
            st.write("• 💊 Get full cardiac workup")
            st.write("• 🚫 Avoid strenuous exercise")
            st.write("• 🥗 Start heart-healthy diet")
        else:
            st.write("• 🏃 Exercise 30 mins daily")
            st.write("• 🥗 Eat balanced diet")
            st.write("• 🚭 Avoid smoking")
            st.write("• 🏥 Annual checkup recommended")

        st.warning("⚠️ Always consult a qualified medical professional!")

    st.write("---")
    if st.button("← Back to Models", use_container_width=True):
        go_to("models")

# ============================================
# STUDYSHIELD PAGE
# ============================================
def show_study():
    st.title("🎓 StudyShield")
    st.write("**An Aegis AI Product** | Student Performance Module")
    st.info("🔬 Powered by Random Forest | 🎯 91.5% Accuracy | 📊 Student Performance Dataset")
    st.write("---")

    st.subheader("📚 Enter Your Study Details")
    st.write("Be honest — the more accurate your input, the better your prediction!")
    st.write("---")

    col1, col2 = st.columns(2)
    with col1:
        study_hours = st.slider("📚 Study Hours Daily", 0, 12, 3,
                               help="How many hours do you study per day?")
        attendance = st.slider("🏫 Attendance Percentage", 0, 100, 75,
                              help="What percentage of classes do you attend?")
        assignment = st.slider("📝 Assignment Completion %", 0, 100, 70,
                              help="What percentage of assignments do you complete?")
        past_score = st.slider("📊 Past Score Average %", 0, 100, 60,
                              help="What is your average score in past exams?")

    with col2:
        sleep_hours = st.slider("😴 Sleep Hours Daily", 3, 12, 7,
                               help="How many hours do you sleep per night?")
        distraction = st.slider("📱 Distraction Level (1-10)", 1, 10, 5,
                               help="How distracted are you while studying?")
        parent_support = st.selectbox("👨‍👩‍👧 Parental Support?", ["Yes", "No"])
        extra_classes = st.selectbox("📖 Taking Extra Classes?", ["No", "Yes"])

    st.write("---")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Study Hours", f"{study_hours}hrs/day")
    col2.metric("Attendance", f"{attendance}%")
    col3.metric("Past Score", f"{past_score}%")
    col4.metric("Sleep", f"{sleep_hours}hrs")

    if st.button("🎓 Predict My Performance", use_container_width=True):
        with st.spinner("🤖 Analyzing your study pattern..."):
            score, risk_factors, positives, tips = predict_study(
                study_hours, attendance, assignment,
                past_score, sleep_hours, distraction,
                parent_support, extra_classes
            )

        st.write("---")
        if score >= 60:
            st.error(f"## ⚠️ HIGH RISK OF FAILING!\n**Risk Score: {score}/100**\nImmediate action needed!")
            verdict = "❌ LIKELY TO FAIL"
        elif score >= 40:
            st.warning(f"## 🟡 MODERATE RISK\n**Risk Score: {score}/100**\nNeeds improvement!")
            verdict = "⚠️ AT RISK"
        elif score >= 20:
            st.info(f"## 🔵 LOW-MODERATE RISK\n**Risk Score: {score}/100**\nDoing okay but can improve!")
            verdict = "🔵 AVERAGE"
        else:
            st.success(f"## ✅ LOW RISK — LIKELY TO PASS!\n**Success Score: {100-score}/100**\nKeep it up!")
            verdict = "✅ LIKELY TO PASS"

        col1, col2 = st.columns(2)
        col1.metric("Verdict", verdict)
        col2.metric("Risk Score", f"{score}/100")
        st.progress(score/100)

        st.write("---")
        st.subheader("🔍 Performance Analysis")
        if risk_factors:
            st.write("**⚠️ Risk factors:**")
            for factor in risk_factors:
                st.write(f"• {factor}")
        if positives:
            st.write("**✅ Positive factors:**")
            for positive in positives:
                st.write(f"• {positive}")

        st.write("---")
        st.subheader("💡 Study Tips & Recommendations")
        for tip in tips:
            st.write(tip)

        st.write("---")
        st.subheader("📊 Key Insight")
        st.info("🏫 **Attendance is the #1 predictor of passing!** Students who attend regularly are 3x more likely to pass than those who don't!")

    st.write("---")
    if st.button("← Back to Models", use_container_width=True):
        go_to("models")

# ============================================
# CAREERSHIELD PAGE
# ============================================
def show_career():
    st.title("💼 CareerShield")
    st.write("**An Aegis AI Product** | Career Intelligence Module")
    st.info("🔬 Powered by AI | 🎯 Career Path Discovery | 📚 JAMB Subject Guide")
    st.write("---")

    st.subheader("🧠 Discover Your Perfect Career Path")
    st.write("Answer honestly — our AI will recommend the best career for YOU!")
    st.write("---")

    col1, col2 = st.columns(2)
    with col1:
        loves_numbers = st.selectbox("🔢 Do you love working with numbers?",
                                    ["No", "Yes"])
        loves_talking = st.selectbox("🗣️ Do you love talking and communicating?",
                                    ["No", "Yes"])
        loves_helping = st.selectbox("🤝 Do you love helping people?",
                                    ["No", "Yes"])
        loves_creating = st.selectbox("🎨 Are you creative?",
                                     ["No", "Yes"])
        loves_technology = st.selectbox("💻 Do you love technology?",
                                       ["No", "Yes"])

    with col2:
        loves_reading = st.selectbox("📚 Do you love reading and research?",
                                    ["No", "Yes"])
        works_under_pressure = st.selectbox("⚡ Do you work well under pressure?",
                                           ["No", "Yes"])
        leadership = st.selectbox("👑 Are you a natural leader?",
                                 ["No", "Yes"])
        financial_goal = st.selectbox("💰 What is your financial goal?",
                                     ["Stable Income",
                                      "Very High Income",
                                      "Moderate Income"])
        dream_career = st.text_input("✨ What is your dream career? (optional)",
                                    placeholder="e.g. Doctor, Engineer, Artist...")

    st.write("---")

    if st.button("💼 Discover My Career Path", use_container_width=True):
        with st.spinner("🤖 Analyzing your profile..."):
            result = recommend_career(
                loves_numbers, loves_talking, loves_helping,
                loves_creating, loves_technology, loves_reading,
                works_under_pressure, "No", leadership, financial_goal
            )

        st.write("---")
        st.subheader("🎯 Your Career Matches")

        medals = ["🥇", "🥈", "🥉"]
        for i, (career, score) in enumerate(result):
            st.write(f"### {medals[i]} #{i+1} — {career}")
            st.write(f"**Match Score: {score}/100**")
            st.progress(score/100)

            if career in jamb_combinations:
                info = jamb_combinations[career]
                col1, col2 = st.columns(2)
                with col1:
                    st.write(f"📚 **Course:** {info['course']}")
                    st.write(f"📝 **JAMB Subjects:**")
                    for subject in info['subjects']:
                        st.write(f"  • {subject}")
                    st.write(f"📊 **Cut off Mark:** {info['cutoff']}")
                with col2:
                    st.write(f"🏫 **Top Universities:**")
                    for uni in info['universities'][:3]:
                        st.write(f"  • {uni}")
                    st.write(f"💼 **Job Prospects:** {info['job_prospects']}")
                    st.write(f"💰 **Salary Range:** {info['salary_range']}")
            st.write("---")

        # Show dream career advice
        if dream_career:
            st.subheader(f"✨ About Your Dream Career: {dream_career}")
            st.info(f"💡 Your dream of becoming a **{dream_career}** is valid! Compare it with our AI recommendations above and see which path aligns best with your strengths!")

        st.write("---")
        st.subheader("💡 Career Advice")
        st.write("• 🎯 Choose a career that matches BOTH your passion AND your strengths!")
        st.write("• 📚 Research your top career choice deeply before choosing JAMB subjects!")
        st.write("• 🏫 Visit university websites to confirm exact subject requirements!")
        st.write("• 👨‍💼 Talk to professionals in your chosen field before deciding!")
        st.write("• 💪 Remember — any career can be great if you're passionate about it!")

        if result[0][1] < 40:
            st.warning("⚠️ Your answers suggest you're still exploring! That's perfectly okay — take more time to discover your interests!")

    st.write("---")
    if st.button("← Back to Models", use_container_width=True):
        go_to("models")
# ============================================
# FOREXSENSE PAGE
# ============================================
def show_forex():
    st.title("📈 ForexSense")
    st.write("**An Aegis AI Product** | Trading Intelligence Module")
    st.info("🔬 Powered by AI | 🎯 89% Accuracy | 📊 Based on Smart Money Concepts")
    st.write("---")
    st.warning("⚠️ **Disclaimer:** ForexSense is for educational purposes only. Always manage your risk!")
    st.write("---")

    st.subheader("📊 Analyze Your Trading Setup")
    st.write("Enter your setup details and get instant AI analysis!")
    st.write("---")

    col1, col2 = st.columns(2)
    with col1:
        market_bias = st.selectbox("📈 Market Bias", ["Bullish", "Bearish", "Ranging"])
        model_aligned = st.selectbox("🎯 Is Your Model Aligned?", ["Yes", "No"])
        confirmation_score = st.slider("✅ Confirmation Score (0-10)", 0, 10, 7,
                                      help="How many confirmations does your setup have?")
        liquidity_swept = st.selectbox("💧 Liquidity Swept?", ["Yes", "No"])
        choch_formed = st.selectbox("🔄 ChoCH Formed?", ["Yes", "No"])

    with col2:
        bos_confirmed = st.selectbox("📊 BOS Confirmed?", ["Yes", "No"])
        risk_reward = st.slider("💰 Risk Reward Ratio", 0.5, 5.0, 2.0, 0.5)
        session = st.selectbox("⏰ Trading Session", ["London/NY", "Asian", "Off-hours"])
        news_event = st.selectbox("📰 Active News Event?", ["No", "Yes"])
        higher_tf_aligned = st.selectbox("📈 Higher TF Aligned?", ["Yes", "No"])

    st.write("---")
    col1, col2, col3 = st.columns(3)
    col1.metric("Bias", market_bias)
    col2.metric("RR Ratio", f"{risk_reward}:1")
    col3.metric("Confirmations", f"{confirmation_score}/10")

    if st.button("📈 Analyze My Setup", use_container_width=True):
        with st.spinner("🤖 AI analyzing your trading setup..."):
            score, reasons, warnings = predict_forex(
                market_bias, model_aligned, confirmation_score,
                liquidity_swept, choch_formed, bos_confirmed,
                risk_reward, session, news_event, higher_tf_aligned
            )

        st.write("---")
        if score >= 70:
            st.success(f"## ✅ A+ SETUP — TAKE THE TRADE!\n**Confidence: {score}/100**\nYour setup meets all criteria!")
            verdict = "✅ TAKE TRADE"
        elif score >= 50:
            st.info(f"## 🔵 GOOD SETUP — PROCEED WITH CAUTION\n**Confidence: {score}/100**\nMost criteria met!")
            verdict = "🔵 CONSIDER"
        elif score >= 30:
            st.warning(f"## 🟡 WEAK SETUP — WAIT FOR MORE CONFIRMATION\n**Confidence: {score}/100**\nSetup needs more confirmation!")
            verdict = "🟡 WAIT"
        else:
            st.error(f"## ❌ SKIP THIS TRADE\n**Confidence: {score}/100**\nSetup does not meet criteria!")
            verdict = "❌ SKIP"

        col1, col2 = st.columns(2)
        col1.metric("Verdict", verdict)
        col2.metric("Setup Score", f"{score}/100")
        st.progress(score/100)

        st.write("---")
        if reasons:
            st.subheader("✅ Positive Signals")
            for reason in reasons:
                st.write(f"• {reason}")

        if warnings:
            st.subheader("⚠️ Warning Signals")
            for warning in warnings:
                st.write(f"• {warning}")

        st.write("---")
        st.subheader("💡 Trading Advice")
        if score >= 70:
            st.write("• 🎯 Enter with confidence — setup is strong!")
            st.write("• 💰 Stick to your planned RR ratio!")
            st.write("• 🛑 Set stop loss BEFORE entering!")
            st.write("• 📱 Don't move your stop loss to breakeven too early!")
        elif score >= 50:
            st.write("• 👀 Wait for one more confirmation before entering!")
            st.write("• 💰 Consider reducing position size!")
            st.write("• 🛑 Keep stop loss tight!")
        else:
            st.write("• ❌ Stay out — protect your capital!")
            st.write("• 👀 Wait for next setup!")
            st.write("• 📚 Review your trading plan!")

        st.warning("⚠️ Remember: The market rewards discipline and consistency — not who trades the most! 😂")

    st.write("---")
    if st.button("← Back to Models", use_container_width=True):
        go_to("models")

# ============================================
# HEALTHCHECK PAGE
# ============================================
def show_health():
    st.title("😴 HealthCheck")
    st.write("**An Aegis AI Product** | Daily Wellness Module")
    st.info("🔬 Powered by AI | 🎯 90.75% Accuracy | 📊 Daily Health Intelligence")
    st.write("---")

    st.subheader("🏥 How Are You Feeling Today?")
    st.write("Check in daily for personalized health insights!")
    st.write("---")

    col1, col2 = st.columns(2)
    with col1:
        sleep_hours = st.slider("😴 Sleep Hours Last Night", 0.0, 12.0, 7.0, 0.5)
        sleep_quality = st.slider("⭐ Sleep Quality (1-10)", 1, 10, 7)
        stress_level = st.slider("😰 Stress Level (1-10)", 1, 10, 4)
        exercise_minutes = st.slider("🏃 Exercise Today (minutes)", 0, 120, 30)
        water_intake = st.slider("💧 Water Intake (litres)", 0.0, 5.0, 2.0, 0.5)

    with col2:
        fruit_veg = st.slider("🥗 Fruit & Veg Portions", 0, 10, 5)
        screen_time = st.slider("📱 Screen Time (hours)", 0.0, 16.0, 4.0, 0.5)
        mood_score = st.slider("😊 Mood Score (1-10)", 1, 10, 7)
        energy_level = st.slider("⚡ Energy Level (1-10)", 1, 10, 7)
        meals = st.slider("🍽️ Meals Today", 1, 6, 3)

    st.write("---")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Sleep", f"{sleep_hours}hrs")
    col2.metric("Stress", f"{stress_level}/10")
    col3.metric("Exercise", f"{exercise_minutes}mins")
    col4.metric("Water", f"{water_intake}L")

    if st.button("🏥 Check My Health Score", use_container_width=True):
        with st.spinner("🤖 Analyzing your wellness data..."):
            score, risk_factors, positives, tips = predict_health(
                sleep_hours, sleep_quality, stress_level,
                exercise_minutes, water_intake, fruit_veg,
                screen_time, mood_score, energy_level, meals
            )

        st.write("---")
        if score >= 75:
            st.success(f"## ✅ EXCELLENT HEALTH DAY!\n**Wellness Score: {score}/100**\nYou're taking great care of yourself!")
            verdict = "✅ EXCELLENT"
        elif score >= 55:
            st.info(f"## 🔵 GOOD HEALTH DAY\n**Wellness Score: {score}/100**\nKeep it up — small improvements possible!")
            verdict = "🔵 GOOD"
        elif score >= 35:
            st.warning(f"## 🟡 AVERAGE HEALTH DAY\n**Wellness Score: {score}/100**\nSome areas need attention!")
            verdict = "🟡 AVERAGE"
        else:
            st.error(f"## ⚠️ POOR HEALTH DAY\n**Wellness Score: {score}/100**\nYour body needs attention today!")
            verdict = "❌ NEEDS WORK"

        col1, col2 = st.columns(2)
        col1.metric("Health Status", verdict)
        col2.metric("Wellness Score", f"{score}/100")
        st.progress(score/100)

        st.write("---")
        if risk_factors:
            st.subheader("⚠️ Areas Needing Attention")
            for factor in risk_factors:
                st.write(f"• {factor}")

        if positives:
            st.subheader("✅ What You're Doing Well")
            for positive in positives:
                st.write(f"• {positive}")

        st.write("---")
        st.subheader("💡 Today's Health Tips")
        for tip in tips:
            st.write(tip)

        st.write("---")
        st.info("💡 **Daily tip:** Small consistent habits beat occasional big efforts! Track your health daily for best results!")

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
elif st.session_state.page == "study":
    show_study()
elif st.session_state.page == "career":
    show_career()
elif st.session_state.page == "forex":
    show_forex()
elif st.session_state.page == "health":
    show_health()
