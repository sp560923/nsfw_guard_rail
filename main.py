# main.py
import streamlit as st
#from pages.guardrail_page import guardrail_ui

st.set_page_config(page_title="AI Prompt Validator", page_icon="🛡️", layout="centered")
#Load and inject HTML from external file
with open("index.html","r",encoding="utf-8") as file:
custom_html = file.read()
st.markdown(custom_html,unsafe_allow_html=True)

#st.title("Guardrails AI")
st.markdown("""
What is Guardrails?
Guardrails is a Python framework that helps build reliable AI applications by performing two key functions:
Guardrails runs Input/Output Guards in your application that detect, quantify and mitigate the presence of specific types of risks. To look at the full suite of risks, check out Guardrails Hub.
Guardrails help you generate structured data from LLMs. 

This tool helps validate user inputs before sending them to a language model (LLM).
Please choose a validator and a model from the sidebar to begin.
""")

if st.button("Proceed to Validation ➡️"):
    st.switch_page("pages/guardrail_page.py")
