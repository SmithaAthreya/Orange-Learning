import streamlit as st
st.title("Interactive Streamlit App")
name=st.text_input("Enter your name")
if st.button("Submit"):
  st.write(f"Hello, {name}! Welcome to Streamlit")
age=st.number_input("Enter your age")
if st.button("Submit"):
    if st.age>=18:
         st.write("You are eligible to vote")
    else:
         st.write("You are not eligible to vote")
