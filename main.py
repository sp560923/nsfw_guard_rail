import streamlit as st

# --- Page Config ---
st.set_page_config(page_title="Guardrails Landing", page_icon="🛡️", layout="wide")

# --- Inject Custom UI HTML ---
with open("index.html", "r", encoding="utf-8") as file:
    html = file.read()
st.markdown(html, unsafe_allow_html=True)

# --- Landing Button ---
st.markdown("<br><br>", unsafe_allow_html=True)
if st.button("🚀 Proceed to Validation"):
    st.switch_page("pages/guardrail_page.py")
