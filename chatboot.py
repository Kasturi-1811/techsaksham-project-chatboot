import streamlit as st
import pandas as pd
import joblib
import numpy as np

model=joblib.load("blood_model.pkl")

def chatbot(qurie):
    food_recommendations={
        "low_hemoglobin": ["Spinach, Beetroot, Red Meat, Eggs, Beans, Dark Chocolate"],
        "high_bp": ["Reduce Salt, Avoid Caffeine, Eat Bananas, Spinach, Avocado"],
        "low_bp": ["Increase Water Intake, Eat Salty Foods, Drink Coffee, Consume Almonds"]
    }

    if "blood" and "men" in qurie:
        return "It should be between 13.8 - 17.2 g/dL"
    elif "blood" and "women" in qurie:
        return "It should be between 12.7 - 15.9 g/dL"
    elif "blood" and "child" in qurie:
        return "It should be between 11 - 13 g/dL"
    elif "blood" and "pregnant" in qurie:
        return "It should be between 11 - 15 g/dL"
    elif "blood" and "elder" in qurie:
        return "It should be between 12 - 16 g/dL"
    elif "hemoglobin" and "food" and "low" in qurie:
        return f"Food To take: {food_recommendations['low_hemoglobin']}"
    elif "blood" and "pressure" and "high" in qurie:
        return f"Food To take: {food_recommendations['high_bp']}"
    elif "blood" and "pressure" and "low" in qurie:
        return f"Food to take: {food_recommendations['low_bp']}"
    else:
        return "Please enter the correct blood level"

def main():

    food_recommendations={
        "low_hemoglobin": ["Spinach, Beetroot, Red Meat, Eggs, Beans, Dark Chocolate"],
        "high_bp": ["Reduce Salt, Avoid Caffeine, Eat Bananas, Spinach, Avocado"],
        "low_bp": ["Increase Water Intake, Eat Salty Foods, Drink Coffee, Consume Almonds"]
    }

    st.title("AI BLOOD DONATION ELIGIBLITY CHECKER")
    st.subheader("Health Assistant ")


    st.sidebar.header("Enter Your Health details.")


    age=st.sidebar.number_input("Age",min_value=18,max_value=70,step=0)
    weight=st.sidebar.number_input("Weight",min_value=50,max_value=100,step=0)
    lastdonation=st.sidebar.number_input("Last Donation",min_value=0,max_value=365,step=1)
    bloodlevel=st.sidebar.number_input("Blood Level",min_value=11.5,max_value=15.5,step=0.1)
    blood_pressure = st.sidebar.selectbox("Blood Pressure", ["Normal", "High", "Low"])
    recent_illness = st.sidebar.radio("Recent Illness (Past 3 Months)?", ["No", "Yes"])
    chronic_disease = st.sidebar.radio("Any Chronic Disease?", ["No", "Yes"])
    bp={"Normal":0,"High":1,"Low":2}
    bp_value=bp[blood_pressure]
    recent_illness_value=1 if recent_illness=="Yes" else 0
    chronic_disease_value=1 if chronic_disease=="Yes" else 0

    if st.sidebar.button("Eligibility"):
        user_data=np.array([[age,weight,lastdonation,bloodlevel,bp_value,recent_illness_value,chronic_disease_value]])
        print(f"user_data shape: {user_data.shape}")
        print(f"user_data content: {user_data}")
        print(f'User data for prediction: {user_data}') 
        prediction=model.predict(user_data)
        print(f'Prediction: {prediction[0]} (1: Eligible, 0: Not Eligible)')

        if prediction[0] == 1:
            st.success(" You are Eligible to donate blood!")
            
        else:
            
            st.error("You are NOT Eligible to donate blood.")
            st.subheader("Reason(s) for Ineligibility:")

            


            # Collect reasons why the user is ineligible
            reasons = []
            if age < 18 or age > 70:
                reasons.append("Age must be between 18 and 70.")
            if weight < 50:
                reasons.append("Weight must be at least 50 kg.")
            if lastdonation < 90:
                reasons.append("You must wait at least 90 days between donations.")
            if bloodlevel < 12.5:
                reasons.append("Your hemoglobin level is too low (min: 12.5 g/dL).")
                
            if blood_pressure == "High":
                reasons.append("High blood pressure detected. Consult a doctor before donating.")
                
            if blood_pressure == "Low":
                reasons.append("Low blood pressure detected. Ensure proper hydration and diet.")
                
            if recent_illness_value:
                reasons.append("You have had a recent illness. Please recover fully before donating.")
            if chronic_disease_value:
                reasons.append("Chronic disease detected. Consult a doctor before donating.")
            
            # Display reasons
            if reasons:
                for reason in reasons:
                    st.warning(reason)

            qurie=st.text_input("Any Queries ? ")
            button1=st.button("Submit")
            if button1:
                if qurie:
                    try:
                        response=chatbot(qurie)
                        st.write("Chatbot: ",response)
                       
                    except Exception as e:
                        st.error("An error occurred: " + str(e))
            

main()
st.write("🔹 Powered by AI Health Assistant")