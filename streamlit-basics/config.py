import streamlit as st

st.set_page_config(
    page_title="Prompt Playground",
    page_icon="🧪",
    layout="wide",                    # ← this is the key one
    initial_sidebar_state="expanded"  # or "collapsed"
)