# File: result_page.py
import streamlit as st

def run():
    st.set_page_config(page_title="Validation Result", page_icon="✅")
    st.title("✅ Validation Results")

    input_text = st.session_state.get('input_text', "")
    validator = st.session_state.get('validator', "NSFW")
    model = st.session_state.get('model', "GPT-4")
    results = st.session_state.get('validation_results', [])
    flagged = st.session_state.get('flagged', [])
    error = st.session_state.get('error', None)

    # Validator + Model info
    st.markdown(f"""
    **Selected Validator:** `{validator}`  
    **Selected Model:** `{model}`
    """)

    # Submitted prompt
    st.markdown("### 🧾 Prompt Submitted:")
    st.code(input_text, language="text")

    # Error handling (if validation threw ValueError)
    if error:
        st.error(f"⚠️ Validation Error:\n\n{error}")

    # Render results
    if results:
        st.markdown("### 🔍 Sentence-level Analysis")
        for r in results:
            with st.expander(f"📘 {r['sentence']}"):
                st.write(f"**Prediction:** `{r['label']}`")
                st.write(f"**Confidence Score:** `{r['score']:.2f}`")
                if r["flagged"]:
                    st.error("⚠️ This sentence was flagged.")
                else:
                    st.success("✅ Passed")
    else:
        st.warning("No validation results found.")
