import streamlit as st

def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

def main():
    st.title("BMI Calculator")

    weight = st.number_input("Enter your weight (kg):", min_value=1.0)
    height = st.number_input("Enter your height (m):", min_value=0.1)

    if st.button("Calculate BMI"):
        bmi = calculate_bmi(weight, height)
        st.write(f"Your BMI is: {bmi:.2f}")
        classification = classify_bmi(bmi)
        st.write(f"Classification: {classification}")

if __name__ == "__main__":
    main()
