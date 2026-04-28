import streamlit as st

st.set_page_config(
    page_title="Prompt Playground",
    page_icon="🧪",
    layout="wide",
    initial_sidebar_state="expanded"
)

tab1, tab2 = st.tabs(["🧪 Playground", "🕓 History"])

with tab1:
    col1, col2 = st.columns(2)
    with col1:
        st.write("Left side")
    with col2:
        st.write("Right side")

with tab2:
    st.write("History goes here")