import streamlit as st

# Set page title and layout
st.set_page_config(page_title="Student Result Calculator", page_icon="🎓")

st.title("🎓 Student Result Calculator")
st.write("Enter the student's name and marks in three subjects to compute their total, percentage, and pass/fail status.")

# Student name input
name = st.text_input("Student Name:")

# Input marks for three subjects
col1, col2, col3 = st.columns(3)

with col1:
    sub1 = st.number_input("Subject 1 Marks:", min_value=0.0, max_value=100.0, value=50.0, step=1.0)

with col2:
    sub2 = st.number_input("Subject 2 Marks:", min_value=0.0, max_value=100.0, value=50.0, step=1.0)

with col3:
    sub3 = st.number_input("Subject 3 Marks:", min_value=0.0, max_value=100.0, value=50.0, step=1.0)

# Calculate button
if st.button("Calculate Result", type="primary"):
    if not name.strip():
        st.warning("Please enter the student's name.")
    else:
        # Calculations
        total_marks = sub1 + sub2 + sub3
        percentage = (total_marks / 300.0) * 100.0
        
        # Check passing criteria (minimum 40 marks in each subject)
        passed_subjects = (sub1 >= 40) and (sub2 >= 40) and (sub3 >= 40)
        
        st.divider()
        st.markdown(f"### Result Summary for **{name}**")
        
        st.metric(label="Total Marks", value=f"{total_marks:.2f} / 300")
        st.metric(label="Percentage", value=f"{percentage:.2f}%")
        
        if passed_subjects:
            st.success("🎉 **Status: PASS** (Secured 40 or more marks in all subjects)")
        else:
            st.error("❌ **Status: FAIL** (Failed to achieve the minimum 40 marks requirement in one or more subjects)")