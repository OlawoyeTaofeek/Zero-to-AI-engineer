import streamlit as st 

pg = st.navigation([
    st.Page("pages/playground.py", title="Playground", icon="🧪"),
    st.Page("pages/history.py",    title="History",    icon="🕓"),
    st.Page("pages/settings.py",   title="Settings",   icon="⚙️"),
])

pg.run()