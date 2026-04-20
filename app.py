import streamlit as st
from PIL import Image
from utils.image_ops import process_diagram
from utils.llm_engine import get_vision_response
from utils.prompts import COT_PROMPT

st.set_page_config(
    page_title="Vision Grade Pro",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load custom CSS
with open("assets/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ---------------- SIDEBAR ---------------- #
with st.sidebar:
    st.markdown("## Configuration")

    provider = st.selectbox(
        "Select AI Provider",
        ["Google Gemini", "OpenAI", "Groq"]
    )

    api_key = st.text_input("API Key", type="password")

    st.markdown("---")
    st.markdown("## System Info")
    st.caption("Engine: v1.0.4")
    st.caption("Vision Processing: OpenCV")

    st.markdown("---")
    st.info("Upload both diagrams and click **Evaluate** to begin.")

# ---------------- HEADER ---------------- #
st.title("Diagram Evaluation Engine")
st.caption("Upload a reference diagram and a student submission to generate automated grading and feedback.")

# ---------------- UPLOAD SECTION ---------------- #
col1, col2 = st.columns(2)

with col1:
    st.subheader("Reference Diagram")
    master_file = st.file_uploader(
        "Upload master diagram",
        type=["png", "jpg", "jpeg"],
        key="master"
    )

    if master_file:
        st.image(master_file, use_column_width=True)

with col2:
    st.subheader("Student Submission")
    student_file = st.file_uploader(
        "Upload student diagram",
        type=["png", "jpg", "jpeg"],
        key="student"
    )

    if student_file:
        with st.spinner("Processing diagram..."):
            _, edges = process_diagram(student_file)
        st.image(edges, caption="Processed Output (Edge Detection)", use_column_width=True)

# ---------------- ACTION BUTTON ---------------- #
st.markdown("---")

if st.button("Evaluate Diagram", use_container_width=True):
    
    if not api_key:
        st.error("Please enter your API key in the sidebar.")
    
    elif not master_file or not student_file:
        st.warning("Please upload both diagrams before evaluation.")
    
    else:
        with st.spinner("Analyzing diagrams and generating feedback..."):
            try:
                result = get_vision_response(
                    provider,
                    api_key,
                    Image.open(master_file),
                    Image.open(student_file),
                    COT_PROMPT
                )

                st.success("Evaluation Complete")

                st.markdown("## Evaluation Report")
                st.markdown(result)

            except Exception as e:
                st.error(f"Error during evaluation: {str(e)}")