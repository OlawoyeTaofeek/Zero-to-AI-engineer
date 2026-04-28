import streamlit as st
col1, col2 = st.columns(2)          # two equal columns

with col1:
    st.write("I am in the left box")

with col2:
    st.write("I am in the right box")

col1, col2, col3 = st.columns([1, 2, 1])  # middle column is twice as wide

# Wrap content in a visible bordered box
with st.container(border=True):
    st.write("This is inside a bordered box")
    st.write("Everything here is grouped visually")

col1, col2 = st.columns(2)

with col1:
    with st.container(border=True):
        st.write("Box A")

with col2:
    with st.container(border=True):
        st.write("Box B")

name = st.text_input("Your name", placeholder="e.g. John")
st.write(f"Hello {name}")

prompt = st.text_area("System prompt", height=150, placeholder="You are a helpful assistant...")
st.write(prompt)

if st.button("Click me"):
    st.write("Button was clicked!")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Run A"):
        st.write("Running A...")

with col2:
    if st.button("Run B"):
        st.write("Running B...")

with col3:
    if st.button("Run Both"):
        st.write("Running both...")

choice = st.selectbox(
    "Choose your favorite pet",
    ["Dog", "Cat", "Fish"]
)
st.write("You selected:", choice)

temperature = st.slider("Temperature", min_value=0.0, max_value=1.0, value=0.7, step=0.1)
st.write(f"Selected: {temperature}")

models = ["gemini-2.5-flash", "gpt-3.5-turbo", "claude-4-5-sonnet"]
selected_model = st.radio("Choose model", models)
st.write("Selected model:", selected_model)

max_tokens = st.slider("Max tokens", min_value=256, max_value=4096, value=1024, step=256)

if st.button("Submit", type="primary"):
    st.write(f"Max tokens: {max_tokens}, Model: {selected_model}")

model = st.selectbox("Choose a model", ["gpt-4o", "gpt-4o-mini", "claude-sonnet-4"])
st.write(f"You picked: {model}")