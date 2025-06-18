import streamlit as st


st.title("My First App")
st.header("Welcome to the financial explorer")
st.write("Simple app to explore financials of a Company")

if st.button("Say Hello"):
    st.write("Hello, Streamlit")