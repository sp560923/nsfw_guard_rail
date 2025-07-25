import streamlit as st

st.set_page_config(page_title="Guardrail Validator", page_icon="🛡️", layout="wide")

with open("index.html", "r", encoding="utf-8") as file:
    custom_html = file.read()
st.markdown(custom_html, unsafe_allow_html=True)

with st.container():
    col1, col2, col3 = st.columns([2, 3, 2])
    with col2:
        if st.button("🚀 Proceed to Validation"):
            st.experimental_set_query_params(page="guardrail")

# Optional: display logic based on query params
params = st.experimental_get_query_params()
if params.get("page") == ["guardrail"]:
    st.info("Please click 'guardrail page' in the sidebar to continue.")
