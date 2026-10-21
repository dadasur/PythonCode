import streamlit as st

# Set page layout and title
st.set_page_config(page_title="Even or Odd Checker", page_icon="🔢")

st.title("🔢 Even or Odd Number Checker")
st.write("Enter an integer below and click the **Check** button to determine if it is Even or Odd.")

# Input field for integer only
num = st.number_input("Enter an Integer:", value=0, step=1, format="%d")

# Check button
if st.button("Check"):
    if num % 2 == 0:
        st.success(f"**{num}** is an **Even** number.")
    else:
        st.info(f"**{num}** is an **Odd** number.")