# main.py
import streamlit as st

# --- Page Configuration ---
st.set_page_config(page_title="Guardrail Validator", page_icon="🛡️", layout="wide")

# --- Redirect via Query Param ---
query_params = st.query_params
if "proceed" in query_params:
    st.switch_page("guardrail")

# --- Load and Inject Custom HTML ---
with open("index.html", "r", encoding="utf-8") as file:
    custom_html = file.read()
st.markdown(custom_html, unsafe_allow_html=True)

# --- Insert a real Streamlit button below the HTML card ---
with st.container():
    col1, col2, col3 = st.columns([2, 3, 2])
    with col2:
        if st.button("🚀 Proceed to Validation"):
            st.switch_page("guardrail")
