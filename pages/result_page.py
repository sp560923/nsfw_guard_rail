# File: pages/result_page.py
import streamlit as st

st.set_page_config(page_title="Validation Result", page_icon="✅")
st.title("✅ Validation Results")

input_text = st.session_state.get('input_text', "")
validator = st.session_state.get('validator', "NSFW")
model = st.session_state.get('model', "GPT-4")
validation_result = st.session_state.get('validation_result', "No result found.")

st.markdown(f"""
**Selected Validator:** `{validator}`  
**Selected Model:** `{model}`
""")

st.markdown("### 🧾 Prompt Submitted:")
st.code(input_text, language="text")

if "✔️" in validation_result:
    st.success(validation_result)
else:
    st.error(validation_result)
