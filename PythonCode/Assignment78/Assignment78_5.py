import streamlit as st

# Set page title and layout
st.set_page_config(page_title="Celsius to Fahrenheit Converter", page_icon="🌡️")

st.title("🌡️ Temperature Converter")
st.write("Enter a temperature in Celsius and click **Convert** to find its value in Fahrenheit.")

# Input field for Celsius temperature
celsius = st.number_input("Temperature in Celsius (°C):", value=0.0, step=0.1)

# Convert button
if st.button("Convert", type="primary"):
    # Conversion formula: F = (C * 9/5) + 32
    fahrenheit = (celsius * 9/5) + 32
    
    st.divider()
    st.success(f"**{celsius}°C** is equal to **{fahrenheit:.2f}°F**")