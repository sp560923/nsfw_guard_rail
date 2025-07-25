import streamlit as st
from streamlit_extras.switch_page_button import switch_page

# --- Page Configuration ---
st.set_page_config(page_title="Guardrail Validator", page_icon="🛡️", layout="wide")

# --- Handle HTML-triggered redirect ---
query_params = st.query_params
if "proceed" in query_params:
    switch_page("guardrail_page")  # No 'pages/' or '.py'

# --- Load and Inject Custom HTML ---
with open("index.html", "r", encoding="utf-8") as file:
    custom_html = file.read()
st.markdown(custom_html, unsafe_allow_html=True)

# --- Insert a real Streamlit button below the HTML card ---
with st.container():
    col1, col2, col3 = st.columns([2, 3, 2])  # Center the button
    with col2:
        if st.button("🚀 Proceed to Validation"):
            switch_page("guardrail_page")  # Correct usage
