import streamlit as st
st.title("Welcome to Streamlit")
username=st.text_input("Enter username")
password=st.text_input("Enter password")
if st.button("Login"):
   if username=="admin":
      if password=="1234":
         st.success("valid user")
      else: 
         st.error("Invalid user")
   else:
       st.error("Invalid username")
