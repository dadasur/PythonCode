import streamlit as st

# Set page layout and title
st.set_page_config(page_title="Addition App", page_icon="➕")

st.title("Addition of Two Numbers")
st.write("Enter two numbers below and click the **Add** button to calculate their sum.")

# Create a form to organize inputs and button
with st.form("addition_form"):
    num1 = st.number_input("Enter the First Number:", value=0.0, step=1.0)
    num2 = st.number_input("Enter the Second Number:", value=0.0, step=1.0)
    
    # Form submission button
    submit_button = st.form_submit_button(label="Add")

# Calculate and display the result when the button is clicked
if submit_button:
    result = num1 + num2
    st.success(f"**Result:** {num1} + {num2} = **{result}**")