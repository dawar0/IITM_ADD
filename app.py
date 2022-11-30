import streamlit as st
# and print the result
st.write("Add two numbers")

# get input from the user
num = st.text_input("First number")
num2 = st.text_input("Second number")

# add the two numbers
try:
    result = int(num) + int(num2)
    st.write(result)
except (ValueError):
    st.write("Please enter two valid numbers")
