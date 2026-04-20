import streamlit as st
from PIL import Image
from utils.image_ops import process_diagram
from utils.llm_engine import get_vision_response
from utils.prompts import COT_PROMPT

st.set_page_config(page_title="Vision Grade Pro", layout="wide")

with open("assets/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

if "provider" not in st.session_state:
    st.session_state.provider = "Google Gemini"
if "api_key" not in st.session_state:
    st.session_state.api_key = ""

with st.sidebar:
    st.title("Settings")

    with st.form("config_form"):
        provider = st.selectbox(
            "Choose AI Provider",
            ["Google Gemini", "OpenAI", "Groq"],
            index=["Google Gemini", "OpenAI", "Groq"].index(st.session_state.provider)
        )

        api_key = st.text_input(
            "Enter API Key",
            type="password",
            value=st.session_state.api_key,
            placeholder="Paste your API key here"
        )

        submitted = st.form_submit_button("Save Settings")

        if submitted:
            st.session_state.provider = provider
            st.session_state.api_key = api_key
            st.success("Settings saved")

st.title("Vision Grade Pro")
st.caption("Upload diagrams and get automatic evaluation")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Reference Diagram")
    master_file = st.file_uploader(
        "Upload correct diagram",
        type=["png", "jpg", "jpeg"]
    )
    if master_file:
        st.image(master_file, use_column_width=True)

with col2:
    st.subheader("Student Submission")
    student_file = st.file_uploader(
        "Upload student's diagram",
        type=["png", "jpg", "jpeg"]
    )
    if student_file:
        _, edges = process_diagram(student_file)
        st.image(edges, use_column_width=True)

run = st.button("Evaluate Diagram")

if run:
    if master_file and student_file and st.session_state.api_key:
        with st.spinner("Analyzing diagram..."):
            result = get_vision_response(
                st.session_state.provider,
                st.session_state.api_key,
                Image.open(master_file),
                Image.open(student_file),
                COT_PROMPT
            )

        st.subheader("Evaluation Result")
        st.write(result)
    else:
        st.error("Please upload both diagrams and enter API key")