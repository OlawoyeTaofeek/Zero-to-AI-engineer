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

# ── Sidebar ───────────────────────────────

with st.sidebar:

    # ── Model ────────────────────────────────────
    st.caption("MODEL")
    model = st.selectbox(
        label="model",
        options=["gpt-4o", "gpt-4o-mini", "claude-sonnet-4", "claude-opus-4"],
        label_visibility="collapsed"   # hides the label, caption acts as the header
    )

    st.write("")  # small spacer

    # ── Parameters ───────────────────────────────
    st.caption("PARAMETERS")

    temp_col, temp_val = st.columns([3, 1])
    with temp_col:
        st.write("Temperature")
    with temp_val:
        st.write("")

    temperature = st.slider(
        label="Temperature",
        min_value=0.0, max_value=1.0,
        value=0.7, step=0.1,
        label_visibility="collapsed"
    )

    tok_col, tok_val = st.columns([3, 1])
    with tok_col:
        st.write("Max tokens")
    with tok_val:
        st.write("")

    max_tokens = st.slider(
        label="Max tokens",
        min_value=256, max_value=4096,
        value=1024, step=256,
        label_visibility="collapsed"
    )

    st.write("")

    # ── User message ─────────────────────────────
    st.caption("USER MESSAGE")
    user_message = st.text_area(
        label="user message",
        placeholder="Explain how neural networks learn from data.",
        height=120,
        label_visibility="collapsed"
    )

    st.write("")

    # ── Saved prompts ────────────────────────────
    st.caption("SAVED PROMPTS")

    saved_prompts = [
        {"name": "ELI5 explainer",    "color": "#7F77DD"},
        {"name": "Bullet summariser", "color": "#1D9E75"},
        {"name": "Code reviewer",     "color": "#BA7517"},
    ]

    selected_prompt = st.radio(
        label="saved prompts",
        options=[p["name"] for p in saved_prompts],
        label_visibility="collapsed"
    )

    st.write("")

    load_col, delete_col = st.columns(2)
    with load_col:
        if st.button("Load", use_container_width=True):
            st.toast(f"Loaded: {selected_prompt}")
    with delete_col:
        if st.button("Delete", use_container_width=True):
            st.toast(f"Deleted: {selected_prompt}")