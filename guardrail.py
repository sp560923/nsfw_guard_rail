# File: guardrail.py
import streamlit as st
from transformers import pipeline
import re

def run():
    st.set_page_config(page_title="Guardrail Validator", page_icon="🔍")
    st.markdown("""
        <h1 style='text-align: center; color: #333;'>🔍 Guardrail Validator</h1>
        <p style='text-align: center; font-size:18px; color: #666;'>Scan and validate prompts for content risks before LLM usage</p>
        <hr>
    """, unsafe_allow_html=True)

    # Sidebar config
    st.sidebar.header("⚙️ Configuration")
    validator = st.sidebar.selectbox("Choose a Validator", ["NSFW", "Profanity", "Sensitive Data"])
    model = st.sidebar.selectbox("Choose an LLM", ["GPT-4", "GPT-3.5", "Claude 2", "Claude 3", "Ollama (LLaMA 3)", "Gemini Pro"])
    hf_token = st.sidebar.text_input("🔑 Enter your HF Token (HF_TOKEN):", type="password")

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
            results = []

            for sent in sentences(text):
                result = nsfw_classifier(sent)[0]
                label = result["label"].lower()
                score = result["score"]

                results.append({
                    "sentence": sent,
                    "label": label,
                    "score": score,
                    "flagged": label in NSFW_LABELS and score >= threshold
                })

                if label in NSFW_LABELS and score >= threshold:
                    flagged.append(sent)

            return results, flagged

        st.markdown("### 📝 Enter Prompt for Validation")
        text_input = st.text_area("Paste your input prompt below:", height=180, placeholder="e.g., Write a story about...")

        if st.button("🚀 Validate Prompt") and text_input:
            try:
                results, flagged = guard_nsfw(text_input)
                st.session_state['validation_results'] = results
                st.session_state['flagged'] = flagged
                st.session_state['input_text'] = text_input
                st.session_state['validator'] = validator
                st.session_state['model'] = model
                #st.switch_page("result.py")  # ✅ Only switch, no display here               
                st.session_state.page = 'result'  # Navigation
                st.experimental_rerun()
            except Exception as e:
                st.session_state['validation_results'] = []
                st.session_state['flagged'] = []
                st.session_state['error'] = str(e)
                st.session_state['input_text'] = text_input
                #st.switch_page("result.py") 
                st.session_state.page = 'result'  # Navigation
                st.experimental_rerun()

    else:
        st.warning("Please enter your HF API token in the sidebar to start.")
