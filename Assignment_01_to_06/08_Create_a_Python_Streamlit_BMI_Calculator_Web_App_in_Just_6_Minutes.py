import streamlit as st 


st.title("BMI Calculator")

st.write("This is a simple BMI (Body Mass Index) calculator to help you determine your BMI.")


weight = st.number_input("Enter your weight (in kg): ", min_value = 1.0 )
height = st.number_input("Enter your height (in cm): ", min_value = 1.0 )


def calculate_bmi(weight, height):

    height_meter = height / 100 
    bmi = weight / (height_meter ** 2)
    return bmi



if weight > 0 and height > 0 :
    bmi = calculate_bmi(weight, height)
    st.success(f"Your BMI is: {bmi:.2f}")


    if bmi < 18.5:
        st.write("You are underweight.")
    elif 18.5 <= bmi < 24.9:
        st.write("You have a normal weight.")
    elif 25 <= bmi < 29.9:
        st.write("You are overweight.")
    else:
        st.write("You are obese.")


st.write("This tool is intended for informational purposes only. Please consult a healthcare provider for personalized advice.")
