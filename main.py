# main.py
import streamlit as st
from pages.guardrail_page import guardrail_ui

st.set_page_config(page_title="AI Prompt Validator", page_icon="🛡️", layout="centered")

st.title("🛡️ AI Prompt Guardrail Interface")
st.markdown("""
Welcome to the **AI Prompt Guardrail** app! 🎯  
This tool helps validate user inputs before sending them to a language model (LLM).

Please choose a validator and a model from the sidebar to begin.
""")

if st.button("Proceed to Validation ➡️"):
    st.switch_page("pages/guardrail_page.py")
