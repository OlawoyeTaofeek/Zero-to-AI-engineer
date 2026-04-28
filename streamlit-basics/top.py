import streamlit as st

st.set_page_config(layout="wide")

# Remove Streamlit's default top padding
st.markdown("""
    <style>
        .block-container {
            padding-top: 1rem;
        }
        div[data-testid="stVerticalBlock"] button {
            margin-top: 0.4rem;
        }
    </style>
""", unsafe_allow_html=True)

# Header
left, spacer, btn_export, btn_save = st.columns([5, 2, 1, 1])

with left:
    st.markdown("## 🧪 Prompt playground")

with btn_export:
    if st.button("Export results", use_container_width=True):
        st.toast("Exporting...")

with btn_save:
    if st.button("Save session", use_container_width=True):
        st.toast("Session saved!")

st.divider()

st.write("Your content here")