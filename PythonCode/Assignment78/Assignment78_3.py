import streamlit as st

# Set page title and layout
st.set_page_config(page_title="Simple Interest Calculator", page_icon="💰")

st.title("Simple Interest Calculator")
st.write("Enter the required details below and click **Calculate** to find the Simple Interest and Total Amount.")

# Create input layout using columns for a clean interface
col1, col2, col3 = st.columns(3)

with col1:
    principal = st.number_input("Principal Amount (₹/$):", min_value=0.0, value=1000.0, step=100.0)

with col2:
    rate = st.number_input("Rate of Interest (% per annum):", min_value=0.0, value=5.0, step=0.5)

with col3:
    time = st.number_input("Time Period (in years):", min_value=0.0, value=1.0, step=0.5)

# Calculate button
if st.button("Calculate", type="primary"):
    # Simple Interest Formula: SI = (P * R * T) / 100
    simple_interest = (principal * rate * time) / 100
    total_amount = principal + simple_interest

    st.divider()
    
    # Display results
    st.success(f"**Simple Interest:** ₹ {simple_interest:,.2f}")
    st.info(f"**Total Amount Payable:** ₹ {total_amount:,.2f}")

    # Summary table
    st.markdown("### Summary")
    st.json({
        "Principal Amount": f"{principal:,.2f}",
        "Annual Interest Rate": f"{rate}%",
        "Time Period": f"{time} years",
        "Calculated Interest": f"{simple_interest:,.2f}",
        "Total Return/Payable": f"{total_amount:,.2f}"
    })