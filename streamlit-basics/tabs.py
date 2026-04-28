import streamlit as st

tab1, tab2, tab3 = st.tabs(["Playground", "History", "Settings"])


with tab1:
    st.write("Playground content")

with tab2:
    st.write("History content")

with tab3:
    st.write("Settings content")