import streamlit as st
# and print the result
st.write("Add two numbers")

# get input from the user
name = st.text_input("First number")
name2 = st.text_input("Second number")

# add the two numbers
try:
    result = int(name) + int(name2)
    st.write(result)
except:
    st.write("Error")
