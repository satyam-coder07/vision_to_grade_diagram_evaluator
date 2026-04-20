import streamlit as st
from PIL import Image
from utils.image_ops import process_diagram
from utils.llm_engine import get_vision_response
from utils.prompts import COT_PROMPT

st.set_page_config(page_title="Vision-Grade Pro", layout="wide")

st.title("Vision-to-Grade AI Pipeline")
st.markdown("Automated evaluation for diagram-based questions.")

with st.sidebar:
    st.header("API Configuration")
    provider = st.selectbox("Model Provider", ["Google Gemini", "OpenAI", "Groq"])
    api_key = st.text_input(f"Enter {provider} API Key", type="password")

col1, col2 = st.columns(2)

with col1:
    m_file = st.file_uploader("Upload Master Diagram", type=['png', 'jpg'])
    if m_file: st.image(m_file, caption="Reference", use_container_width=True)

with col2:
    s_file = st.file_uploader("Upload Student Diagram", type=['png', 'jpg'])
    if s_file:
        processed, edges = process_diagram(s_file)
        st.image(edges, caption="AI Vision Filter", use_container_width=True)

if st.button("Analyze and Grade") and api_key:
    if m_file and s_file:
        with st.spinner(f"Evaluating using {provider}..."):
            result = get_vision_response(provider, api_key, Image.open(m_file), Image.open(s_file), COT_PROMPT)
            st.markdown("### Evaluation Results")
            st.write(result)
    else:
        st.warning("Please upload both diagrams.")
