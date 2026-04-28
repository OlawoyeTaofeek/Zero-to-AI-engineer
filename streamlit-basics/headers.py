import streamlit as st

st.set_page_config(layout="wide")

# ── Header bar ─────────────────────────────────────────
left, right = st.columns([6, 2])

with left:
    st.markdown("### 🧪 Prompt playground")

with right:
    btn1, btn2 = st.columns(2)
    with btn1:
        st.button("Export results", use_container_width=True)
    with btn2:
        st.button("Save session", use_container_width=True)

st.divider()  # line under the header