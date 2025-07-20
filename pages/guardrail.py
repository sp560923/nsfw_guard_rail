import streamlit as st
from transformers import pipeline
import re

# Streamlit page configuration
st.set_page_config(page_title="NSFW Content Guard Rail", page_icon="🚨")

# Sidebar for Hugging Face token
hf_token = st.sidebar.text_input("Enter your Hugging Face Token (HF_TOKEN):")

# Load the NSFW classification pipeline from Hugging Face
if hf_token:
    from huggingface_hub import login
    login(hf_token)
    nsfw_classifier = pipeline("text-classification", model="eliasalbouzidi/distilbert-nsfw-text-classifier")

    # Function to split text into individual sentences
    def sentences(text: str):
        return re.split(r"(?<=[.!?])\s+(?=[A-Z])", text.strip())

    # Function to check for NSFW content and raise an exception if detected
    def guard_nsfw(text: str, threshold: float = 0.8):
        """
        Raise ValueError if any sentence is classified NSFW with score ≥ threshold.
        Works with models that return either:
            {'label': 'NSFW', 'score': 0.92}
            {'label': 'LABEL_1', 'score': 0.92}   # where LABEL_1 means NSFW
        """
        # Map alternative label names to a canonical form
        NSFW_LABELS = {"nsfw", "label_1"}   # expand if your model uses others
        flagged = []

        for sent in sentences(text):
            result = nsfw_classifier(sent)[0]  # run model
            label = result["label"].lower()
            score = result["score"]
            st.write(f"**Sentence:** {sent}\n**Prediction:** {label} (score={score:.2f})")

            if label in NSFW_LABELS and score >= threshold:
                flagged.append(f"{sent}  (score={score:.2f})")

        if flagged:
            raise ValueError(
                "NSFW validation failed for the following sentence(s):\n- "
                + "\n- ".join(flagged)
            )

        return "✔️ All sentences passed the NSFW check."

    # Streamlit input fields
    st.title("NSFW Content Guard Rail 🚨")
    text_input = st.text_area("Enter the text to be checked:", height=200)
    submit_button = st.button("Check NSFW Content")

    if submit_button and text_input:
        try:
            # Check NSFW content in the input text
            result = guard_nsfw(text_input)
            st.success(result)
        except ValueError as e:
            st.error(str(e))

else:
    st.warning("Please enter your Hugging Face API token to start.")
