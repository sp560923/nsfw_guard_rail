# File: pages/guardrail_page.py
import streamlit as st
from transformers import pipeline
import re

# Page layout
st.set_page_config(page_title="Guardrail Validator", page_icon="🔍")
st.title("🔍 Prompt Guardrail Validator")

# Sidebar for validator and model selection
st.sidebar.header("Configuration")

validator = st.sidebar.selectbox(
    "Choose a Validator",
    ["NSFW", "Profanity", "Sensitive Data"],
    index=0
)

model = st.sidebar.selectbox(
    "Choose an LLM",
    ["GPT-4", "GPT-3.5", "Claude 2", "Claude 3", "Ollama (LLaMA 3)", "Gemini Pro"],
    index=0
)

# Info text for current selection
st.info(f"**Validator:** `{validator}`  |  **LLM:** `{model}`")

# Hugging Face token
hf_token = st.sidebar.text_input("Enter your Hugging Face Token (HF_TOKEN):")

if hf_token:
    from huggingface_hub import login
    login(hf_token)
    nsfw_classifier = pipeline("text-classification", model="eliasalbouzidi/distilbert-nsfw-text-classifier")

    def sentences(text: str):
        return re.split(r"(?<=[.!?])\s+(?=[A-Z])", text.strip())

    def guard_nsfw(text: str, threshold: float = 0.8):
        NSFW_LABELS = {"nsfw", "label_1"}
        flagged = []
        for sent in sentences(text):
            result = nsfw_classifier(sent)[0]
            label = result["label"].lower()
            score = result["score"]
            st.write(f"**Sentence:** {sent}\n**Prediction:** {label} (score={score:.2f})")
            if label in NSFW_LABELS and score >= threshold:
                flagged.append(f"{sent}  (score={score:.2f})")
        if flagged:
            raise ValueError("NSFW validation failed for the following sentence(s):\n- " + "\n- ".join(flagged))
        return "✔️ All sentences passed the NSFW check."

    st.markdown("### 📝 Enter Prompt for Validation")
    text_input = st.text_area("Paste your input prompt below:", height=200)
    submit_button = st.button("Validate Prompt")

    if submit_button and text_input:
        try:
            result = guard_nsfw(text_input)
            st.session_state['validation_result'] = result
            st.session_state['input_text'] = text_input
            st.session_state['validator'] = validator
            st.session_state['model'] = model
            st.switch_page("pages/result_page.py")
        except ValueError as e:
            st.session_state['validation_result'] = str(e)
            st.session_state['input_text'] = text_input
            st.session_state['validator'] = validator
            st.session_state['model'] = model
            st.switch_page("pages/result_page.py")
else:
    st.warning("Please enter your Hugging Face API token to start.")
