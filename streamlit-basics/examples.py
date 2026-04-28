import streamlit as st   

## sidebar

st.sidebar.title("Settings")
st.sidebar.write("I am in the sidebar")

st.write("I am in the main area")

# or 
# with st.sidebar:
#     st.title("Settings")
#     st.write("Everything here goes in the sidebar")