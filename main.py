# main.py
import streamlit as st

# --- Page Configuration ---
st.set_page_config(page_title="Guardrail Validator", page_icon="🛡️", layout="wide")

# --- Handle HTML-triggered redirect ---
query_params = st.query_params
if "proceed" in query_params:
    st.switch_page("pages/guardrail_page.py")

# --- Load and Inject Custom HTML ---
with open("index.html", "r", encoding="utf-8") as file:
    custom_html = file.read()
st.markdown(custom_html, unsafe_allow_html=True)
