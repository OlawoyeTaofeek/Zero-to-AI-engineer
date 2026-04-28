import streamlit as st

st.title("Prompt Playground")

prompt = st.text_area("Enter your prompt", height=150, placeholder="What would you like to ask?")

if st.button("Submit"):
    st.write(f"You entered: {prompt}")