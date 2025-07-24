# main.py
import streamlit as st
import guardrail_page  # Make sure guardrail_page.py is in the same directory

# --- Page Configuration ---
st.set_page_config(page_title="Guardrail Validator", page_icon="🛡️", layout="wide")

# --- Session State for Navigation ---
if "show_guardrail" not in st.session_state:
    st.session_state["show_guardrail"] = False

# --- Redirect if query param is present ---
query_params = st.query_params
if "proceed" in query_params:
    st.session_state["show_guardrail"] = True
    st.rerun()

# --- Navigation Control ---
if st.session_state["show_guardrail"]:
    guardrail_page.run()  # Call function defined inside guardrail_page.py
    st.stop()

# --- Load and Inject Custom HTML ---
with open("index.html", "r", encoding="utf-8") as file:
    custom_html = file.read()
st.markdown(custom_html, unsafe_allow_html=True)

# --- Insert a real Streamlit button below the HTML card ---
with st.container():
    col1, col2, col3 = st.columns([2, 3, 2])
    with col2:
        if st.button("🚀 Proceed to Validation"):
            st.session_state["show_guardrail"] = True
            st.rerun()
