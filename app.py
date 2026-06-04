# ============================================
# AEGIS AI — Decision Intelligence Platform
# ============================================
# Founder & Lead Developer: Ajayi Ibrahim Ademola
# Founded: 2026
# GitHub: github.com/ibrahim399-dev
# Email: ibrahimdamola405@gmail.com
# © 2026 Aegis AI. All Rights Reserved.
# ============================================

import streamlit as st
import pandas as pd
import numpy as np
import io
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
        requests.post(
            f"{SUPABASE_URL}/rest/v1/users_predictions",
            headers=headers,
            json=data
        )
        return True
    except:
        return False

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
# HEARTGUARD ENGINE — Plain Language Version
# ============================================
def predict_heart(age, sex, chest_pain_exercise, chest_pain_type,
                  blood_pressure_level, cholesterol_level, 
                  blood_sugar_high, max_heart_rate, 
                  exercise_causes_pain, stress_test_result):
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

    # Sex
    if sex == "Male":
        risk_score += 5
        risk_factors.append("⚤ Male — statistically higher cardiac risk!")
    else:
        positive_factors.append("⚤ Female — lower baseline cardiac risk!")

    # Chest pain during exercise
    if chest_pain_exercise == "Yes — severe pain":
        risk_score += 25
        risk_factors.append("💔 Severe chest pain during exercise — high risk indicator!")
    elif chest_pain_exercise == "Yes — mild discomfort":
        risk_score += 12
        risk_factors.append("💔 Mild chest discomfort during exercise detected!")
    elif chest_pain_exercise == "Rarely":
        risk_score += 5
        risk_factors.append("💔 Occasional chest discomfort noted!")
    else:
        positive_factors.append("💔 No chest pain during exercise — good sign!")

    # Chest pain type
    if chest_pain_type == "No pain at all":
        risk_score += 15
        risk_factors.append("💔 Asymptomatic — no pain despite potential risk!")
    elif chest_pain_type == "Sharp stabbing pain":
        risk_score += 8
        risk_factors.append("💔 Non-anginal chest pain detected!")
    elif chest_pain_type == "Pressure or squeezing":
        risk_score += 5
        risk_factors.append("💔 Atypical angina present!")
    else:
        positive_factors.append("💔 Typical angina — manageable chest pain!")

    # Blood pressure
    if blood_pressure_level == "Very High (160+)":
        risk_score += 20
        risk_factors.append("🩺 Very high blood pressure — serious risk factor!")
    elif blood_pressure_level == "High (140-160)":
        risk_score += 12
        risk_factors.append("🩺 High blood pressure detected!")
    elif blood_pressure_level == "Slightly High (120-140)":
        risk_score += 5
        risk_factors.append("🩺 Slightly elevated blood pressure!")
    else:
        positive_factors.append("🩺 Normal blood pressure — great!")

    # Cholesterol
    if cholesterol_level == "Very High (300+)":
        risk_score += 20
        risk_factors.append("🧪 Very high cholesterol — major risk factor!")
    elif cholesterol_level == "High (240-300)":
        risk_score += 12
        risk_factors.append("🧪 High cholesterol detected!")
    elif cholesterol_level == "Borderline (200-240)":
        risk_score += 5
        risk_factors.append("🧪 Borderline cholesterol levels!")
    else:
        positive_factors.append("🧪 Healthy cholesterol levels!")

    # Blood sugar
    if blood_sugar_high == "Yes":
        risk_score += 10
        risk_factors.append("🍬 High fasting blood sugar — diabetes risk!")
    else:
        positive_factors.append("🍬 Normal fasting blood sugar!")

    # Max heart rate
    if max_heart_rate == "Very Low — I get tired very quickly":
        risk_score += 15
        risk_factors.append("💓 Very low exercise capacity — concerning!")
    elif max_heart_rate == "Below Average — I tire faster than most":
        risk_score += 8
        risk_factors.append("💓 Below average exercise capacity!")
    else:
        positive_factors.append("💓 Good exercise capacity!")

    # Exercise causes pain
    if exercise_causes_pain == "Yes — always":
        risk_score += 15
        risk_factors.append("🏃 Exercise consistently causes chest pain!")
    elif exercise_causes_pain == "Sometimes":
        risk_score += 8
        risk_factors.append("🏃 Exercise occasionally causes discomfort!")
    else:
        positive_factors.append("🏃 No exercise induced chest pain!")

    # Stress test
    if stress_test_result == "Abnormal — doctor found issues":
        risk_score += 15
        risk_factors.append("📉 Abnormal stress test result — significant risk!")
    elif stress_test_result == "Borderline — some concerns":
        risk_score += 8
        risk_factors.append("📉 Borderline stress test results!")
    elif stress_test_result == "Never had one":
        risk_score += 3
        risk_factors.append("📉 No stress test history — consider getting one!")
    else:
        positive_factors.append("📉 Normal stress test result!")

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
        study_tips.append("💡 Attendance is the #1 predictor of passing!")
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
        risk_factors.append("😴 Very low sleep hours!")
        study_tips.append("💡 Sleep at least 7 hours for better memory!")
    elif sleep_hours >= 7:
        positive_factors.append("😴 Good sleep hours!")

    if parent_support == "Yes":
        positive_factors.append("👨‍👩‍👧 Good parental support!")
    else:
        risk_score += 5
        study_tips.append("💡 Talk to your parents or a mentor!")

    if extra_classes == "Yes":
        positive_factors.append("📖 Taking extra classes — great!")
    else:
        risk_score += 5
        study_tips.append("💡 Consider joining study groups!")

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

    sorted_careers = sorted(scores.items(), key=lambda x: x[1], reverse=True)
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
# FOREXSENSE ENGINE — Ademola's Strategy
# ============================================
def predict_forex(market_bias, model_aligned, confirmation_score,
                  liquidity_swept, choch_formed, bos_confirmed,
                  risk_reward, session, news_event, higher_tf_aligned,
                  trade_type):
    score = 0
    reasons = []
    warnings = []

    # Core model alignment — ALL THREE must be true
    if model_aligned == "Yes" and liquidity_swept == "Yes" and choch_formed == "Yes":
        score += 50
        reasons.append("✅ Model aligned — Liquidity swept + ChoCH confirmed!")
    elif model_aligned == "Yes" and liquidity_swept == "Yes":
        score += 25
        warnings.append("⚠️ Liquidity swept but ChoCH not formed yet — wait!")
    elif model_aligned == "Yes":
        score += 10
        warnings.append("⚠️ Model aligned but liquidity not swept — not ready!")
    else:
        score -= 20
        warnings.append("❌ Model NOT aligned — stay out completely!")

    # Higher timeframe
    if higher_tf_aligned == "Yes":
        score += 20
        reasons.append("✅ Higher timeframe confirms direction!")
    else:
        warnings.append("⚠️ Higher timeframe not aligned — risky!")

    # BOS confirmation
    if bos_confirmed == "Yes":
        score += 10
        reasons.append("✅ Break of Structure confirmed!")
    else:
        warnings.append("⚠️ No BOS yet — wait for more confirmation!")

    # Risk Reward — minimum 1RR
    if risk_reward >= 2:
        score += 15
        reasons.append(f"✅ Excellent RR: {risk_reward}:1!")
    elif risk_reward >= 1:
        score += 8
        reasons.append(f"✅ Acceptable RR: {risk_reward}:1")
    else:
        score -= 20
        warnings.append(f"❌ RR too low: {risk_reward}:1 — minimum is 1RR!")

    # News event handling
    if news_event == "Yes":
        if trade_type == "Swing Trade":
            score -= 5
            warnings.append("⚠️ News event — consider impact on swing trade!")
        else:
            score -= 20
            warnings.append("❌ News event active — avoid intraday trades!")

    # Session
    if session == "London/NY":
        score += 10
        reasons.append("✅ Trading during peak session — higher probability!")
    elif session == "Asian":
        score -= 5
        warnings.append("⚠️ Asian session — lower volatility, be careful!")

    # Confirmation score
    if confirmation_score >= 8:
        score += 10
        reasons.append(f"✅ Strong confirmation: {confirmation_score}/10!")
    elif confirmation_score >= 6:
        score += 5
        reasons.append(f"✅ Good confirmation: {confirmation_score}/10")
    else:
        warnings.append(f"⚠️ Weak confirmation: {confirmation_score}/10 — wait!")

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
        tips.append("💡 Create a bedtime routine!")

    if stress_level <= 3:
        score += 15
        positive_factors.append("✅ Low stress — great mental health!")
    elif stress_level <= 6:
        score += 5
        tips.append("💡 Practice breathing exercises!")
    else:
        score -= 10
        risk_factors.append("⚠️ High stress level!")
        tips.append("💡 Take breaks and meditate!")

    if exercise_minutes >= 30:
        score += 20
        positive_factors.append("🏃 Excellent exercise habit!")
    elif exercise_minutes >= 15:
        score += 10
        tips.append("💡 Increase exercise to 30 mins daily!")
    else:
        score -= 5
        risk_factors.append("❌ Very little exercise!")
        tips.append("💡 Even a 20 minute walk makes huge difference!")

    if water_intake >= 2:
        score += 15
        positive_factors.append("💧 Well hydrated!")
    elif water_intake >= 1.5:
        score += 8
        tips.append("💡 Drink at least 2 litres daily!")
    else:
        score -= 10
        risk_factors.append("❌ Dehydrated!")
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
        positive_factors.append("⚡ High energy!")
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
st.markdown("""
    <style>
    .stButton > button {
        border-radius: 10px;
        padding: 10px;
        font-weight: bold;
    }
    .stMetric {
        background-color: #1a1a2e;
        padding: 10px;
        border-radius: 8px;
    }
    </style>
    """, unsafe_allow_html=True)
def show_home():
    st.image("https://raw.githubusercontent.com/ibrahim399-dev/Churnshield/main/logo-header.png",
             use_column_width=True)
    st.markdown("### Predict. Analyze. Protect.")
    st.error("💸 **Why This Matters:** Losing customers costs millions. Poor health decisions cost lives. Wrong career choices waste years. Aegis AI helps you predict risks BEFORE they become problems!")
    st.write("Aegis AI is a Nigerian AI platform for decision intelligence. Making advanced AI accessible to everyone — regardless of sector!")
    st.write("---")

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("📊 Records", "13,000+")
    col2.metric("🎯 Best Accuracy", "91.5%")
    col3.metric("🤖 Models", "6 Live!")
    col4.metric("🌍 Countries", "8 African")
    st.write("---")

    st.info("🔬 **Machine Learning Powered** | 📊 **78-91% Accuracy Range** | 🗄️ **Real World Datasets** | ⚙️ **6 Sectors Covered**")
    st.subheader("🚀 Aegis AI Modules — 6 Live!")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.success("🛡️ **ChurnShield**\nCustomer Intelligence\n✅ Live — 78.68%")
        st.write("")
        st.success("💼 **CareerShield**\nCareer & JAMB Guide\n✅ Live — AI Powered")
    with col2:
        st.success("❤️ **HeartGuard**\nHealth Prediction\n✅ Live — 86.89%")
        st.write("")
        st.success("📈 **ForexSense**\nTrading Intelligence\n✅ Live — 89%")
    with col3:
        st.success("🎓 **StudyShield**\nStudent Analytics\n✅ Live — 91.5%")
        st.write("")
        st.success("😴 **HealthCheck**\nDaily Wellness\n✅ Live — 90.75%")

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
def show_models():
    st.title("🛡️ Aegis AI")
    st.subheader("📊 Select Your Module")
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
                        ["Bank transfer", "Credit card", "Electronic check", "Mailed check"])

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
                                 file_name="aegisai_churn_results.csv", mime="text/csv")

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

        if st.button("🔍 Check My Loyalty Score", use_container_width=True, key="loyalty"):
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
# HEARTGUARD PAGE — Plain Language Version
# ============================================
def show_heart():
    st.title("❤️ HeartGuard")
    st.write("**An Aegis AI Product** | Health Risk Prediction Module")
    st.info("🔬 Powered by Advanced AI | 🎯 86.89% Accuracy | 📊 Cleveland Heart Disease Dataset")
    st.write("---")
    st.warning("⚠️ **Medical Disclaimer:** HeartGuard is for awareness only. Always consult a qualified doctor!")
    st.write("---")

    st.subheader("🏥 Answer These Simple Questions")
    st.write("No medical knowledge needed — just answer honestly!")
    st.write("---")

    # Demo button
    if st.button("📊 Try Demo — High Risk Profile", use_container_width=True):
        st.session_state.heart_demo = True

    if st.session_state.heart_demo:
        st.info("✅ Demo loaded — high risk patient profile!")

    st.write("---")

    # Section 1 — Basic Info
    st.subheader("👤 Basic Information")
    col1, col2 = st.columns(2)
    with col1:
        age = st.slider("How old are you?", 20, 80,
                       63 if st.session_state.heart_demo else 45)
    with col2:
        sex = st.selectbox("What is your sex?",
                          ["Male", "Female"])

    st.write("---")

    # Section 2 — Chest Pain
    st.subheader("💔 Chest Pain & Discomfort")
    st.write("*These questions help us understand if your heart is under stress*")

    chest_pain_exercise = st.selectbox(
        "Do you experience chest pain or discomfort during physical activity?",
        ["No — I feel fine during exercise",
         "Rarely",
         "Yes — mild discomfort",
         "Yes — severe pain"],
        index=3 if st.session_state.heart_demo else 0,
        help="Think about walking fast, climbing stairs, or any physical effort"
    )

    chest_pain_type = st.selectbox(
        "If you experience chest pain, how would you describe it?",
        ["I don't experience chest pain",
         "Pressure or squeezing feeling",
         "Sharp stabbing pain",
         "No pain at all — even during heavy exercise"],
        index=0 if not st.session_state.heart_demo else 3,
        help="Choose the description that best matches your experience"
    )

    exercise_causes_pain = st.selectbox(
        "Does physical activity or exercise cause chest discomfort?",
        ["No — exercise feels normal",
         "Sometimes",
         "Yes — always"],
        index=2 if st.session_state.heart_demo else 0,
        help="Think about your last few weeks of physical activity"
    )

    st.write("---")

    # Section 3 — Blood Pressure & Cholesterol
    st.subheader("🩺 Blood Pressure & Cholesterol")
    st.write("*Check your last medical report or estimate based on doctor visits*")

    blood_pressure_level = st.selectbox(
        "What is your blood pressure level?",
        ["Normal (below 120)",
         "Slightly High (120-140)",
         "High (140-160)",
         "Very High (160+)",
         "I don't know"],
        index=1 if st.session_state.heart_demo else 0,
        help="You can find this from your last doctor visit or pharmacy check"
    )

    cholesterol_level = st.selectbox(
        "What is your cholesterol level?",
        ["Healthy (below 200)",
         "Borderline (200-240)",
         "High (240-300)",
         "Very High (300+)",
         "I don't know"],
        index=1 if st.session_state.heart_demo else 0,
        help="Check your last blood test result"
    )

    blood_sugar_high = st.selectbox(
        "Has a doctor ever told you that your blood sugar is high?",
        ["No", "Yes"],
        index=1 if st.session_state.heart_demo else 0,
        help="High fasting blood sugar can indicate diabetes which affects heart health"
    )

    st.write("---")

    # Section 4 — Exercise Capacity
    st.subheader("🏃 Exercise & Energy Levels")
    st.write("*These questions reveal how well your heart handles physical stress*")

    max_heart_rate = st.selectbox(
        "How would you describe your exercise capacity?",
        ["Good — I can exercise for long periods",
         "Below Average — I tire faster than most",
         "Very Low — I get tired very quickly"],
        index=2 if st.session_state.heart_demo else 0,
        help="Compare yourself to others your age"
    )

    st.write("---")

    # Section 5 — Medical History
    st.subheader("🏥 Medical History")
    st.write("*Previous medical results help us give more accurate predictions*")

    stress_test_result = st.selectbox(
        "Have you ever had a cardiac stress test? If yes, what was the result?",
        ["Never had one",
         "Normal — doctor said everything was fine",
         "Borderline — some concerns raised",
         "Abnormal — doctor found issues"],
        index=3 if st.session_state.heart_demo else 0,
        help="A cardiac stress test measures how your heart performs under physical stress"
    )

    st.write("---")

    # Patient Summary
    st.subheader("👤 Your Profile Summary")
    col1, col2, col3 = st.columns(3)
    col1.metric("Age", f"{age} yrs")
    col2.metric("Sex", sex)
    col3.metric("Blood Pressure", blood_pressure_level.split("(")[0])

    if st.button("❤️ Predict My Heart Disease Risk", use_container_width=True):
        with st.spinner("🤖 AI is analyzing your health data..."):
            score, risk_factors, positives = predict_heart(
                age, sex, chest_pain_exercise, chest_pain_type,
                blood_pressure_level, cholesterol_level,
                blood_sugar_high, max_heart_rate,
                exercise_causes_pain, stress_test_result
            )

        st.write("---")
        if score >= 60:
            st.error(f"""
## ⚠️ HIGH HEART DISEASE RISK DETECTED!
**Risk Score: {score}/100**
Our AI has detected significant indicators of heart disease risk!
            """)
            action = "🚨 Please consult a cardiologist as soon as possible!"
            risk_label = "🔴 HIGH RISK"
        elif score >= 40:
            st.warning(f"""
## 🟡 MODERATE HEART DISEASE RISK
**Risk Score: {score}/100**
Some concerning indicators detected — don't ignore these!
            """)
            action = "⚠️ Schedule a doctor appointment within 2 weeks!"
            risk_label = "🟡 MODERATE RISK"
        elif score >= 20:
            st.info(f"""
## 🔵 LOW-MODERATE RISK
**Risk Score: {score}/100**
Some minor risk factors present — worth monitoring!
            """)
            action = "👀 Monitor your health regularly and maintain healthy lifestyle!"
            risk_label = "🔵 LOW-MODERATE"
        else:
            st.success(f"""
## ✅ LOW HEART DISEASE RISK
**Safety Score: {100-score}/100**
No significant indicators detected — keep it up!
            """)
            action = "😊 Maintain your healthy lifestyle!"
            risk_label = "✅ LOW RISK"

        col1, col2 = st.columns(2)
        col1.metric("Risk Level", risk_label)
        col2.metric("Risk Score", f"{score}/100")
        st.progress(score/100)

        st.write("---")
        st.subheader("🔍 What We Found")
        if risk_factors:
            st.write("**⚠️ Risk indicators:**")
            for factor in risk_factors:
                st.write(f"• {factor}")
        if positives:
            st.write("**✅ Positive signs:**")
            for positive in positives:
                st.write(f"• {positive}")

        st.write("---")
        st.subheader("💊 What You Should Do")
        st.write(f"**{action}**")

        if score >= 60:
            st.write("• 🏥 Visit a cardiologist immediately")
            st.write("• 💊 Request a full cardiac workup")
            st.write("• 🚫 Avoid strenuous exercise until cleared by doctor")
            st.write("• 🥗 Start heart-healthy diet immediately")
            st.write("• 🚭 Stop smoking if you smoke")
            st.write("• 💊 Discuss medication options with your doctor")
        elif score >= 40:
            st.write("• 🏥 Schedule cardiac checkup within 2 weeks")
            st.write("• 💊 Discuss medication options with doctor")
            st.write("• 🏃 Light exercise only — no strenuous activity")
            st.write("• 🥗 Reduce salt, fat and processed foods")
            st.write("• 📊 Monitor blood pressure weekly")
        elif score >= 20:
            st.write("• 🏃 Exercise regularly — 30 mins daily")
            st.write("• 🥗 Eat a balanced heart-healthy diet")
            st.write("• 🚭 Avoid smoking and limit alcohol")
            st.write("• 📊 Check blood pressure monthly")
            st.write("• 🏥 Annual cardiac checkup recommended")
        else:
            st.write("• 🏃 Keep exercising regularly!")
            st.write("• 🥗 Maintain your healthy diet!")
            st.write("• 🏥 Annual checkup still recommended!")
            st.write("• 😊 You're doing great — keep it up!")

        st.write("---")
        st.warning("⚠️ **Remember:** This is an AI awareness tool only. Always consult a qualified medical professional for proper diagnosis!")

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
        study_hours = st.slider("📚 Study Hours Daily", 0, 12, 3)
        attendance = st.slider("🏫 Attendance Percentage", 0, 100, 75)
        assignment = st.slider("📝 Assignment Completion %", 0, 100, 70)
        past_score = st.slider("📊 Past Score Average %", 0, 100, 60)
    with col2:
        sleep_hours = st.slider("😴 Sleep Hours Daily", 3, 12, 7)
        distraction = st.slider("📱 Distraction Level (1-10)", 1, 10, 5)
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
            st.error(f"## ⚠️ HIGH RISK OF FAILING!\n**Risk Score: {score}/100**")
            verdict = "❌ LIKELY TO FAIL"
        elif score >= 40:
            st.warning(f"## 🟡 MODERATE RISK\n**Risk Score: {score}/100**")
            verdict = "⚠️ AT RISK"
        elif score >= 20:
            st.info(f"## 🔵 LOW-MODERATE RISK\n**Risk Score: {score}/100**")
            verdict = "🔵 AVERAGE"
        else:
            st.success(f"## ✅ LOW RISK — LIKELY TO PASS!\n**Success Score: {100-score}/100**")
            verdict = "✅ LIKELY TO PASS"

        col1, col2 = st.columns(2)
        col1.metric("Verdict", verdict)
        col2.metric("Risk Score", f"{score}/100")
        st.progress(score/100)

        st.write("---")
        if risk_factors:
            st.write("**⚠️ Risk factors:**")
            for factor in risk_factors:
                st.write(f"• {factor}")
        if positives:
            st.write("**✅ Positive factors:**")
            for positive in positives:
                st.write(f"• {positive}")

        st.write("---")
        st.subheader("💡 Study Tips")
        for tip in tips:
            st.write(tip)

        st.info("🏫 **Key Insight:** Attendance is the #1 predictor of passing!")

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
        loves_numbers = st.selectbox("🔢 Do you love working with numbers?", ["No", "Yes"])
        loves_talking = st.selectbox("🗣️ Do you love talking and communicating?", ["No", "Yes"])
        loves_helping = st.selectbox("🤝 Do you love helping people?", ["No", "Yes"])
        loves_creating = st.selectbox("🎨 Are you creative?", ["No", "Yes"])
        loves_technology = st.selectbox("💻 Do you love technology?", ["No", "Yes"])
    with col2:
        loves_reading = st.selectbox("📚 Do you love reading and research?", ["No", "Yes"])
        works_under_pressure = st.selectbox("⚡ Do you work well under pressure?", ["No", "Yes"])
        leadership = st.selectbox("👑 Are you a natural leader?", ["No", "Yes"])
        financial_goal = st.selectbox("💰 What is your financial goal?",
                                     ["Stable Income", "Very High Income", "Moderate Income"])
        dream_career = st.text_input("✨ Your dream career? (optional)",
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

        if dream_career:
            st.subheader(f"✨ About Your Dream: {dream_career}")
            st.info(f"💡 Your dream of becoming a **{dream_career}** is valid! Compare with our recommendations above!")

        st.write("---")
        st.subheader("💡 Career Advice")
        st.write("• 🎯 Choose career matching BOTH passion AND strengths!")
        st.write("• 📚 Research your top choice deeply!")
        st.write("• 🏫 Visit university websites for exact requirements!")
        st.write("• 👨‍💼 Talk to professionals in your chosen field!")
        st.write("• 💪 Any career can be great if you're passionate!")

    st.write("---")
    if st.button("← Back to Models", use_container_width=True):
        go_to("models")

# ============================================
# FOREXSENSE PAGE
# ============================================
def show_forex():
    st.title("📈 ForexSense")
    st.write("**An Aegis AI Product** | Trading Intelligence Module")
    st.info("🔬 Powered by Smart Money Concepts | 🎯 89% Accuracy | 📊 Ademola's Strategy")
    st.write("---")
    st.warning("⚠️ **Disclaimer:** ForexSense is for educational purposes only. Always manage your risk!")
    st.write("---")

    st.subheader("📊 Analyze Your Trading Setup")
    st.write("Based on Smart Money Concepts — Liquidity, ChoCH, BOS!")
    st.write("---")

    col1, col2 = st.columns(2)
    with col1:
        market_bias = st.selectbox("📈 Market Bias",
                                  ["Bullish", "Bearish", "Ranging"])
        model_aligned = st.selectbox("🎯 Is Your Model Aligned?",
                                    ["Yes", "No"],
                                    help="Model = Liquidity + ChoCH + BOS all confirmed!")
        liquidity_swept = st.selectbox("💧 Liquidity Swept?",
                                      ["Yes", "No"],
                                      help="Has smart money swept liquidity?")
        choch_formed = st.selectbox("🔄 ChoCH Formed?",
                                   ["Yes", "No"],
                                   help="Change of Character confirmed?")
        bos_confirmed = st.selectbox("📊 BOS Confirmed?",
                                    ["Yes", "No"],
                                    help="Break of Structure confirmed?")

    with col2:
        higher_tf_aligned = st.selectbox("📈 Higher TF Aligned?",
                                        ["Yes", "No"],
                                        help="Is the higher timeframe in your direction?")
        risk_reward = st.slider("💰 Risk Reward Ratio", 0.5, 5.0, 2.0, 0.5,
                               help="Minimum 1RR — aim for 2RR+")
        session = st.selectbox("⏰ Trading Session",
                              ["London/NY", "Asian", "Off-hours"])
        news_event = st.selectbox("📰 Active News Event?",
                                 ["No", "Yes"])
        trade_type = st.selectbox("📋 Trade Type",
                                 ["Intraday", "Swing Trade"])
        confirmation_score = st.slider("✅ Confirmation Score (0-10)", 0, 10, 7,
                                      help="How many boxes are ticked?")

    st.write("---")

    # Setup summary
    st.subheader("📋 Setup Summary")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Bias", market_bias)
    col2.metric("RR", f"{risk_reward}:1")
    col3.metric("Session", session.split("/")[0])
    col4.metric("Confirmations", f"{confirmation_score}/10")

    # Core checklist
    st.write("**Core Checklist:**")
    col1, col2, col3 = st.columns(3)
    with col1:
        if liquidity_swept == "Yes":
            st.success("✅ Liquidity Swept")
        else:
            st.error("❌ Liquidity NOT Swept")
    with col2:
        if choch_formed == "Yes":
            st.success("✅ ChoCH Formed")
        else:
            st.error("❌ ChoCH NOT Formed")
    with col3:
        if bos_confirmed == "Yes":
            st.success("✅ BOS Confirmed")
        else:
            st.error("❌ BOS NOT Confirmed")

    st.write("---")

    if st.button("📈 Analyze My Setup", use_container_width=True):
        with st.spinner("🤖 AI analyzing your trading setup..."):
            score, reasons, warnings = predict_forex(
                market_bias, model_aligned, confirmation_score,
                liquidity_swept, choch_formed, bos_confirmed,
                risk_reward, session, news_event,
                higher_tf_aligned, trade_type
            )

        st.write("---")
        if score >= 80:
            st.success(f"""
## ✅ A+ SETUP — HIGH PROBABILITY TRADE!
**Setup Score: {score}/100**
All boxes ticked — this is the trade you've been waiting for!
            """)
            verdict = "✅ TAKE THE TRADE"
        elif score >= 60:
            st.info(f"""
## 🔵 GOOD SETUP — PROCEED WITH CAUTION
**Setup Score: {score}/100**
Most criteria met — consider entering!
            """)
            verdict = "🔵 CONSIDER ENTERING"
        elif score >= 40:
            st.warning(f"""
## 🟡 INCOMPLETE SETUP — WAIT
**Setup Score: {score}/100**
Setup not fully confirmed — be patient!
            """)
            verdict = "🟡 WAIT FOR MORE"
        else:
            st.error(f"""
## ❌ SKIP THIS TRADE — PROTECT YOUR CAPITAL
**Setup Score: {score}/100**
Setup does not meet your model criteria!
            """)
            verdict = "❌ SKIP — NO SETUP"

        col1, col2, col3 = st.columns(3)
        col1.metric("Verdict", verdict)
        col2.metric("Score", f"{score}/100")
        col3.metric("Min RR Met", "✅ Yes" if risk_reward >= 1 else "❌ No")
        st.progress(score/100)

        if reasons:
            st.write("---")
            st.subheader("✅ Positive Signals")
            for reason in reasons:
                st.write(f"• {reason}")

        if warnings:
            st.write("---")
            st.subheader("⚠️ Warning Signals")
            for warning in warnings:
                st.write(f"• {warning}")

        st.write("---")
        st.subheader("💡 Trading Advice")
        if score >= 80:
            st.write("• 🎯 This is an A+ setup — enter with confidence!")
            st.write("• 💰 Stick to your planned RR — don't move targets!")
            st.write(f"• 🛑 Set SL before entering — target {risk_reward}R minimum!")
            st.write("• 📱 Walk away after entering — let the trade work!")
            st.write("• 🧘 Stay calm — you followed your model perfectly!")
        elif score >= 60:
            st.write("• 👀 Wait for one final confirmation before entering!")
            st.write("• 💰 Consider reducing position size slightly!")
            st.write("• 🛑 Keep stop loss tight!")
            st.write("• 📊 Make sure higher TF is aligned!")
        else:
            st.write("• ❌ Stay out — this setup doesn't meet your criteria!")
            st.write("• 👀 Wait for next high probability setup!")
            st.write("• 📚 Review your model — patience is profit!")
            st.write("• 💪 Missing a trade is better than a bad trade!")

        st.write("---")
        st.warning("⚠️ Remember: **The market rewards discipline and consistency — not who trades the most!** 😂")

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
    st.write("---")

    col1, col2 = st.columns(2)
    with col1:
        sleep_hours = st.slider("😴 Sleep Hours", 0.0, 12.0, 7.0, 0.5)
        sleep_quality = st.slider("⭐ Sleep Quality (1-10)", 1, 10, 7)
        stress_level = st.slider("😰 Stress Level (1-10)", 1, 10, 4)
        exercise_minutes = st.slider("🏃 Exercise (minutes)", 0, 120, 30)
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
        with st.spinner("🤖 Analyzing your wellness..."):
            score, risk_factors, positives, tips = predict_health(
                sleep_hours, sleep_quality, stress_level,
                exercise_minutes, water_intake, fruit_veg,
                screen_time, mood_score, energy_level, meals
            )

        st.write("---")
        if score >= 75:
            st.success(f"## ✅ EXCELLENT HEALTH DAY!\n**Wellness Score: {score}/100**")
            verdict = "✅ EXCELLENT"
        elif score >= 55:
            st.info(f"## 🔵 GOOD HEALTH DAY\n**Wellness Score: {score}/100**")
            verdict = "🔵 GOOD"
        elif score >= 35:
            st.warning(f"## 🟡 AVERAGE HEALTH DAY\n**Wellness Score: {score}/100**")
            verdict = "🟡 AVERAGE"
        else:
            st.error(f"## ⚠️ POOR HEALTH DAY\n**Wellness Score: {score}/100**")
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

        st.info("💡 Small consistent habits beat occasional big efforts!")

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
                       
