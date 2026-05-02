import streamlit as st
import pandas as pd
import numpy as np

# Simple rule-based predictor (no sklearn needed!)
def predict_churn(tenure, monthly_charges, total_charges, 
                  senior_citizen, contract, internet_service, payment_method):
    
    risk_score = 0
    
    # Contract type
    if contract == "Month-to-month":
        risk_score += 40
    elif contract == "One year":
        risk_score += 10
    
    # Monthly charges
    if monthly_charges > 70:
        risk_score += 25
    elif monthly_charges > 50:
        risk_score += 10
    
    # Tenure
    if tenure < 12:
        risk_score += 20
    elif tenure < 24:
        risk_score += 10
    
    # Senior citizen
    if senior_citizen == "Yes":
        risk_score += 10
    
    # Internet service
    if internet_service == "Fiber optic":
        risk_score += 5
    
    return risk_score

# Website
st.title("🛡️ ChurnShield")
st.subheader("Customer Churn Prediction App")
st.write("Built by Ajayi Ibrahim Ademola — Data Science & ML, AAUA")
st.write("---")

# Inputs
tenure = st.slider("📅 Tenure (months)", 0, 72, 12)
monthly_charges = st.number_input("💰 Monthly Charges ($)", 0.0, 200.0, 50.0)
total_charges = st.number_input("💳 Total Charges ($)", 0.0, 10000.0, 500.0)
senior_citizen = st.selectbox("👤 Senior Citizen?", ["No", "Yes"])
contract = st.selectbox("📋 Contract Type", ["Month-to-month", "One year", "Two year"])
internet_service = st.selectbox("🌐 Internet Service", ["DSL", "Fiber optic", "No"])
payment_method = st.selectbox("💳 Payment Method", ["Bank transfer", "Credit card", "Electronic check", "Mailed check"])

# Predict button
if st.button("🔍 Predict Churn"):
    score = predict_churn(tenure, monthly_charges, total_charges,
                         senior_citizen, contract, 
                         internet_service, payment_method)
    
    st.write("---")
    st.write(f"**Risk Score: {score}/100**")
    st.progress(score/100)
    
    if score >= 60:
        st.error("⚠️ VERY HIGH RISK - This customer is very likely to churn!")
    elif score >= 40:
        st.warning("🟡 HIGH RISK - This customer may churn soon!")
    elif score >= 20:
        st.info("🔵 MEDIUM RISK - Monitor this customer!")
    else:
        st.success("✅ LOW RISK - This customer is likely to stay!")
