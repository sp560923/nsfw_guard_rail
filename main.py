# main.py
import streamlit as st

# --- Page Configuration ---
st.set_page_config(page_title="Guardrail Validator", page_icon="🛡️", layout="wide")

# --- Load and Inject Custom HTML ---
with open("index.html", "r", encoding="utf-8") as file:
    custom_html = file.read()
st.markdown(custom_html, unsafe_allow_html=True)

# --- Page Header ---
st.markdown("""
    <h1 style='text-align: center; color: #4A4A4A;'>🚧 Guardrail Validator</h1>
    <p style='text-align: center; font-size:18px; color: #6C757D;'>Ensure your inputs are compliant with safety and ethical standards</p>
""", unsafe_allow_html=True)

# --- Removed Sidebar ---
# No more option_menu or configuration inputs in sidebar

# --- Main Content ---
st.markdown("### 🧭 Welcome to Guardrails")
st.markdown("""
    Guardrails is a Python framework that helps build **reliable AI applications** by performing two key functions:
    - 🛡️ It runs **Input/Output Guards** that detect, quantify, and mitigate risks.
    - 🧩 It helps generate **structured data** from LLMs.

    This tool helps validate user inputs before sending them to a language model.
""")
# --- Landing Button ---
st.markdown("<br><br>", unsafe_allow_html=True)
if st.button("🚀 Proceed to Validation"):
    st.switch_page("pages/guardrail_page.py")
