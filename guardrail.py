# File: guardrail_page.py
import streamlit as st
from transformers import pipeline
import re

def run():
    # Page layout
    st.set_page_config(page_title="Guardrail Validator", page_icon="🔍")
    st.markdown("""
        <h1 style='text-align: center; color: #333;'>🔍 Guardrail Validator</h1>
        <p style='text-align: center; font-size:18px; color: #666;'>Scan and validate prompts for content risks before LLM usage</p>
        <hr>
    """, unsafe_allow_html=True)

    # Sidebar for configuration
    st.sidebar.header("⚙️ Configuration")
    validator = st.sidebar.selectbox("Choose a Validator", ["NSFW", "Profanity", "Sensitive Data"])
    model = st.sidebar.selectbox("Choose an LLM", ["GPT-4", "GPT-3.5", "Claude 2", "Claude 3", "Ollama (LLaMA 3)", "Gemini Pro"])
    hf_token = st.sidebar.text_input("🔑 Enter your HF Token (HF_TOKEN):", type="password")

    # Info panel
    st.info(f"**Validator:** `{validator}`  |  **LLM:** `{model}`")

    if hf_token:
        from huggingface_hub import login
        login(hf_token)

        nsfw_classifier = pipeline("text-classification", model="eliasalbouzidi/distilbert-nsfw-text-classifier")

        def sentences(text: str):
            return re.split(r"(?<=[.!?])\s+(?=[A-Z])", text.strip())

        def guard_nsfw(text: str, threshold: float = 0.8):
            NSFW_LABELS = {"nsfw", "label_1"}
            flagged = []
            st.markdown("### 🔎 Validation Results")
            for sent in sentences(text):
                result = nsfw_classifier(sent)[0]
                label = result["label"].lower()
                score = result["score"]

                with st.expander(f"📘 Sentence: {sent}"):
                    st.write(f"**Prediction:** `{label}`  \n**Confidence Score:** `{score:.2f}`")
                    if label in NSFW_LABELS and score >= threshold:
                        st.error(f"⚠️ This sentence is flagged (score={score:.2f})")
                        flagged.append(f"{sent}  (score={score:.2f})")
                    else:
                        st.success("✅ Passed")

            if flagged:
                raise ValueError("NSFW validation failed for the following sentence(s):\n- " + "\n- ".join(flagged))
            return "✅ All sentences passed the NSFW check."

        # Prompt Input
        st.markdown("### 📝 Enter Prompt for Validation")
        text_input = st.text_area("Paste your input prompt below:", height=180, placeholder="e.g., Write a story about...")

        submit_button = st.button("🚀 Validate Prompt")

        if submit_button and text_input:
            try:
                result = guard_nsfw(text_input)
                st.session_state['validation_result'] = result
                st.session_state['input_text'] = text_input
                st.session_state['validator'] = validator
                st.session_state['model'] = model
                # Adapt the line below if you refactor result_page too
                 st.switch_page("pages/result_page.py")  ← remove if not using multipage
            except ValueError as e:
                st.session_state['validation_result'] = str(e)
                st.session_state['input_text'] = text_input
                st.session_state['validator'] = validator
                st.session_state['model'] = model
                 st.switch_page("pages/result_page.py")
    else:
        st.warning("Please enter your HF API token in the sidebar to start.")
