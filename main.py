# main.py
import streamlit as st

# --- Page Configuration ---
st.set_page_config(page_title="Guardrail Validator", page_icon="🛡️", layout="wide")

# --- Load and Inject Custom HTML ---
with open("index.html", "r", encoding="utf-8") as file:
    custom_html = file.read()
# Inject JavaScript to listen to the button inside the HTML form
custom_html += """
<script>
  const form = document.querySelector('form');
  if (form) {
    form.addEventListener('submit', function(e) {
      e.preventDefault();
      window.location.href = "?proceed=true";
    });
  }
</script>
"""
st.markdown(custom_html, unsafe_allow_html=True)


