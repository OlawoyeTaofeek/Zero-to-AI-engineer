import streamlit as st

# ── Sidebar ────────────────────────────────
with st.sidebar:
    st.header("Settings")

    model = st.selectbox("Model", ["gpt-4o", "claude-sonnet-4", "gpt-4o-mini"])
    temperature = st.slider("Temperature", 0.0, 1.0, 0.7, 0.1)
    max_tokens = st.slider("Max tokens", 256, 4096, 1024, 256)

    st.divider()
    st.caption("Adjust settings above before running")

# ── Main area ──────────────────────────────
st.title("My App")

user_input = st.text_input("Your message", placeholder="Ask something...")

col1, col2 = st.columns(2)

with col1:
    prompt_a = st.text_area("Prompt A", height=120, placeholder="You are a helpful assistant...")

with col2:
    prompt_b = st.text_area("Prompt B", height=120, placeholder="You are an expert educator...")

col1, col2, col3 = st.columns(3)

with col1:
    run_a = st.button("Run A")
with col2:
    run_b = st.button("Run B")
with col3:
    run_both = st.button("Run Both")

# ── Output boxes ───────────────────────────
out_col1, out_col2 = st.columns(2)

with out_col1:
    with st.container(border=True):
        st.markdown("**Output A**")
        if run_a or run_both:
            st.write(f"Model: {model} | Temp: {temperature}")
        else:
            st.caption("Output will appear here")

with out_col2:
    with st.container(border=True):
        st.markdown("**Output B**")
        if run_b or run_both:
            st.write(f"Model: {model} | Temp: {temperature}")
        else:
            st.caption("Output will appear here")