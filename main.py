# main.py
import streamlit as st
from streamlit_option_menu import option_menu

# --- Page Configuration ---
st.set_page_config(page_title="Guardrail Validator", page_icon="🛡️", layout="wide")

# --- Load and Inject Custom HTML (e.g., Header Banner) ---
with open("index.html", "r", encoding="utf-8") as file:
    custom_html = file.read()
st.markdown(custom_html, unsafe_allow_html=True)

# --- Page Header ---
st.markdown("""
    <h1 style='text-align: center; color: #4A4A4A;'>🚧 Guardrail Validator</h1>
    <p style='text-align: center; font-size:18px; color: #6C757D;'>Ensure your inputs are compliant with safety and ethical standards</p>
""", unsafe_allow_html=True)

# --- Sidebar Navigation & Configuration ---
with st.sidebar:
    selected = option_menu("Navigation", ["Main", "Guardrail Page", "Result Page"],
                           icons=["house", "shield-check", "clipboard-check"],
                           menu_icon="cast", default_index=0)

    st.markdown("---")
    st.subheader("⚙️ Configuration")

    validator = st.selectbox("Choose a Validator", ["NSFW", "Toxicity", "Bias", "Custom"])
    llm_choice = st.selectbox("Choose an LLM", ["GPT-4", "Claude 3", "Gemini", "Mixtral"])
    hf_token = st.text_input("🔑 Enter your HF Token", type="password")

# --- Main Content Area ---
if selected == "Main":
    st.markdown("### 🧭 Welcome to Guardrails")

    st.markdown("""
        Guardrails is a Python framework that helps build **reliable AI applications** by performing two key functions:
        - 🛡️ It runs **Input/Output Guards** that detect, quantify, and mitigate risks.
        - 🧩 It helps generate **structured data** from LLMs.

        This tool helps validate user inputs before sending them to a language model.
        Please choose a **validator** and an **LLM model** from the sidebar to begin.
    """)

    if st.button("🚀 Proceed to Validation"):
        st.switch_page("pages/guardrail_page.py")

elif selected == "Guardrail Page":
    st.markdown("### 🔍 Guardrail Configuration")
    st.info(f"**Validator:** {validator} | **LLM:** {llm_choice}", icon="🔎")

    if not hf_token:
        st.warning("Please enter your HF API token to start validation.", icon="⚠️")
    else:
        st.success("Token accepted. Ready to proceed!", icon="✅")

elif selected == "Result Page":
    st.markdown("### 📊 Validation Results")
    st.info("Results will appear here after validation.")

# --- Footer ---
st.markdown("""
    <hr>
    <center>
        <small>Made with ❤️ using Streamlit | © 2025 Guardrail AI</small>
    </center>
""", unsafe_allow_html=True)
