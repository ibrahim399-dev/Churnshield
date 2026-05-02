import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

# Train model automatically
@st.cache_resource
def load_model():
    url = "https://raw.githubusercontent.com/IBM/telco-customer-churn-on-icp4d/master/data/Telco-Customer-Churn.csv"
    df = pd.read_csv(url)
    
    df["Churn"] = df["Churn"].map({"Yes": 1, "No": 0})
    df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
    df = df.dropna()
    
    le = LabelEncoder()
    df["Contract_encoded"] = le.fit_transform(df["Contract"])
    df["InternetService_encoded"] = le.fit_transform(df["InternetService"])
    df["PaymentMethod_encoded"] = le.fit_transform(df["PaymentMethod"])
    
    features = ["tenure", "MonthlyCharges", "TotalCharges",
                "SeniorCitizen", "Contract_encoded",
                "InternetService_encoded", "PaymentMethod_encoded"]
    
    X = df[features]
    y = df["Churn"]
    
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42)
    
    model = GradientBoostingClassifier(n_estimators=200, random_state=42)
    model.fit(X_train, y_train)
    return model

# Load model
model = load_model()

# Website
st.title("🛡️ ChurnShield")
st.subheader("Customer Churn Prediction App")
st.write("Enter customer details to predict if they will churn!")

# Inputs
tenure = st.slider("Tenure (months)", 0, 72, 12)
monthly_charges = st.number_input("Monthly Charges ($)", 0.0, 200.0, 50.0)
total_charges = st.number_input("Total Charges ($)", 0.0, 10000.0, 500.0)
senior_citizen = st.selectbox("Senior Citizen?", ["No", "Yes"])
contract = st.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])
internet_service = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
payment_method = st.selectbox("Payment Method", ["Bank transfer", "Credit card", "Electronic check", "Mailed check"])

# Convert inputs
senior_citizen = 1 if senior_citizen == "Yes" else 0
contract = ["Month-to-month", "One year", "Two year"].index(contract)
internet_service = ["DSL", "Fiber optic", "No"].index(internet_service)
payment_method = ["Bank transfer", "Credit card", "Electronic check", "Mailed check"].index(payment_method)

# Predict
if st.button("🔍 Predict Churn"):
    features = np.array([[tenure, monthly_charges, total_charges,
                         senior_citizen, contract,
                         internet_service, payment_method]])
    prediction = model.predict(features)
    probability = model.predict_proba(features)[0][1] * 100
    
    if prediction[0] == 1:
        st.error(f"⚠️ HIGH RISK - {probability:.1f}% chance of churning!")
    else:
        st.success(f"✅ LOW RISK - Only {probability:.1f}% chance of churning!")
