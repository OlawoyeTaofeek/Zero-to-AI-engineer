import streamlit as st

st.set_page_config(layout="wide")

st.markdown("""
    <style>
        .block-container { 
            padding-top: 0.5rem;
            padding-left: 1rem;
            padding-right: 1rem;
        }
        header[data-testid="stHeader"] {
            height: 0rem;
            visibility: hidden;
        }
        [data-testid="stHorizontalBlock"] {
            align-items: stretch;
        }
    </style>
""", unsafe_allow_html=True)

# ── Full width header ───────────────────────────────────
header_left, header_space, header_btn1, header_btn2 = st.columns([5, 2, 1, 1])

with header_left:
    st.markdown("### 🧪 Prompt playground")
with header_btn1:
    if st.button("Export results", use_container_width=True):
        st.toast("Exporting...")
with header_btn2:
    if st.button("Save session", use_container_width=True):
        st.toast("Session saved!")

st.divider()

# ── Sidebar + Main ──────────────────────────────────────
sidebar, main = st.columns([1, 3])

# ════════════════════════════════════════════════════════
# SIDEBAR
# ════════════════════════════════════════════════════════
with sidebar:

    st.caption("MODEL")
    model = st.selectbox(
        label="model",
        options=["gpt-4o", "gpt-4o-mini", "claude-sonnet-4", "claude-opus-4"],
        label_visibility="collapsed"
    )

    st.write("")
    st.caption("PARAMETERS")

    if "temperature" not in st.session_state:
        st.session_state.temperature = 0.7

    temp_label, temp_val = st.columns([3, 1])
    with temp_label:
        st.write("Temperature")
    with temp_val:
        st.write(f"**{st.session_state.temperature}**")

    st.slider(
        label="Temperature",
        min_value=0.0, max_value=1.0,
        value=0.7, step=0.1,
        label_visibility="collapsed",
        key="temperature"
    )

    if "max_tokens" not in st.session_state:
        st.session_state.max_tokens = 1024

    tok_label, tok_val = st.columns([3, 1])
    with tok_label:
        st.write("Max tokens")
    with tok_val:
        st.write(f"**{st.session_state.max_tokens}**")

    st.slider(
        label="Max tokens",
        min_value=256, max_value=4096,
        value=1024, step=256,
        label_visibility="collapsed",
        key="max_tokens"
    )

    st.write("")
    st.caption("USER MESSAGE")
    user_message = st.text_area(
        label="user message",
        placeholder="Explain how neural networks learn from data.",
        height=120,
        label_visibility="collapsed"
    )

    st.write("")
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

# ════════════════════════════════════════════════════════
# MAIN
# ════════════════════════════════════════════════════════
with main:

    # ── System Prompts ───────────────────────────────
    st.caption("SYSTEM PROMPTS")

    prompt_a_col, prompt_b_col = st.columns(2)

    with prompt_a_col:
        with st.container(border=True):
            head_l, head_r = st.columns([3, 1])
            with head_l:
                st.markdown("**Prompt A**")
            with head_r:
                st.markdown(
                    "<span style='background:#e8f4f0;color:#1D9E75;padding:2px 10px;"
                    "border-radius:20px;font-size:12px;float:right'>active</span>",
                    unsafe_allow_html=True
                )
            prompt_a = st.text_area(
                label="Prompt A",
                value="You are a helpful assistant. Explain things clearly and concisely using simple language anyone can understand.",
                height=120,
                label_visibility="collapsed",
                key="prompt_a"
            )

    with prompt_b_col:
        with st.container(border=True):
            head_l, head_r = st.columns([3, 1])
            with head_l:
                st.markdown("**Prompt B**")
            with head_r:
                st.markdown(
                    "<span style='background:#e8f4f0;color:#1D9E75;padding:2px 10px;"
                    "border-radius:20px;font-size:12px;float:right'>active</span>",
                    unsafe_allow_html=True
                )
            prompt_b = st.text_area(
                label="Prompt B",
                value="You are an expert educator. Use analogies, real-world examples, and a step-by-step structure. Always end with a one-line summary.",
                height=120,
                label_visibility="collapsed",
                key="prompt_b"
            )

    # ── Action Buttons ───────────────────────────────
    st.write("")
    btn1, btn2, btn3, btn4, btn5 = st.columns(5)

    with btn1:
        run_a = st.button("▶ Run A", use_container_width=True)
    with btn2:
        run_b = st.button("▶ Run B", use_container_width=True)
    with btn3:
        run_both = st.button("▶ Run both", use_container_width=True)
    with btn4:
        clear = st.button("Clear", use_container_width=True)
    with btn5:
        save_a = st.button("Save prompt A", use_container_width=True)

    st.write("")

    # ── Outputs ──────────────────────────────────────
    st.caption("OUTPUTS")

    out_a_col, out_b_col = st.columns(2)

    with out_a_col:
        with st.container(border=True):
            head_l, head_r = st.columns([2, 1])
            with head_l:
                st.markdown("**Output A**")
            with head_r:
                st.markdown(
                    "<span style='background:#e8f4f0;color:#1D9E75;"
                    "font-size:12px;float:right'>143 tokens</span>",
                    unsafe_allow_html=True
                )
            st.write(
                "A neural network learns by adjusting its internal weights based on errors. "
                "It makes a prediction, checks how wrong it was, then nudges each weight slightly "
                "in the direction that reduces the error. Repeat millions of times — that's training."
            )
            st.divider()
            s1, s2, s3 = st.columns(3)
            with s1:
                st.caption("Input")
                st.markdown("**312**")
            with s2:
                st.caption("Output")
                st.markdown("**143**")
            with s3:
                st.caption("Est. cost")
                st.markdown("**$0.0004**")

    with out_b_col:
        with st.container(border=True):
            head_l, head_r = st.columns([2, 1])
            with head_l:
                st.markdown("**Output B**")
            with head_r:
                st.markdown(
                    "<span style='background:#e8f4f0;color:#1D9E75;"
                    "font-size:12px;float:right'>198 tokens</span>",
                    unsafe_allow_html=True
                )
            st.markdown(
                "Think of it like learning to ride a bike. At first you fall — that's the error signal. "
                "Your brain adjusts your balance slightly each time.\n\n"
                "**Step 1:** Forward pass — make a prediction.\n\n"
                "**Step 2:** Calculate loss — how wrong were we?\n\n"
                "**Step 3:** Backprop — trace the error back.\n\n"
                "**Step 4:** Update weights — improve slightly.\n\n"
                "*Summary: Neural networks learn by iteratively reducing prediction error.*"
            )
            st.divider()
            s1, s2, s3 = st.columns(3)
            with s1:
                st.caption("Input")
                st.markdown("**338**")
            with s2:
                st.caption("Output")
                st.markdown("**198**")
            with s3:
                st.caption("Est. cost")
                st.markdown("**$0.0006**")