# Vision Grade Evaluator

Vision Grade Evaluator is a computer vision + multimodal AI system designed to automatically evaluate hand-drawn diagrams. It compares a student’s submission against a reference diagram and generates structured feedback with reasoning.

The goal of this project is to move beyond simple image matching and provide explainable, step-by-step grading similar to how a human evaluator would assess diagrams.

---

## Live Demo

https://diagramevaluator.streamlit.app/

---

## What This Does

- Compares a reference diagram with a student submission  
- Processes noisy, hand-drawn images using OpenCV  
- Uses multimodal LLMs to evaluate correctness  
- Generates detailed reasoning for marks deduction  
- Provides an intuitive side-by-side comparison UI  

---

## System Overview

The system is built in three main stages:

### 1. Image Processing
- Converts input diagrams into structured visual representations  
- Applies edge detection and noise reduction  
- Improves clarity for downstream model understanding  

### 2. AI Evaluation Engine
- Sends both diagrams to a multimodal model  
- Uses structured prompts for:
  - label matching  
  - spatial reasoning  
  - correctness verification  
- Generates a reasoning-based evaluation output  

### 3. User Interface
- Built with Streamlit  
- Displays:
  - reference diagram  
  - processed student diagram  
  - final evaluation report  

---

## Tech Stack

- **Frontend**: Streamlit  
- **Computer Vision**: OpenCV  
- **LLM Providers**: Gemini, OpenAI, Groq  
- **Image Handling**: PIL  
- **Architecture**: Modular utility-based design  

---

## Project Structure

```bash
vision-grade-evaluator/
├── app.py                  # Main Streamlit application
├── utils/
│   ├── image_ops.py        # Image preprocessing (OpenCV)
│   ├── llm_engine.py       # Multi-provider LLM logic
│   └── prompts.py          # Evaluation prompts
├── assets/
│   └── style.css           # Custom UI styling
└── requirements.txt
```

---

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/your-username/vision-grade-evaluator.git
cd vision-grade-evaluator
```

### 2. Create environment

```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Configuration

Provide an API key for one of the supported providers:

- Google Gemini  
- OpenAI  
- Groq  

You can enter the key directly in the app sidebar.

---

## Running the App

```bash
streamlit run app.py
```

---

## How to Use

1. Upload a reference (master) diagram  
2. Upload a student submission  
3. Select AI provider and enter API key  
4. Click **Evaluate Diagram**  
5. View:
   - processed image  
   - evaluation reasoning  
   - grading insights  

---

## Key Design Choices

- Focused on **explainability over black-box scoring**  
- Used edge detection to improve structural understanding  
- Designed prompts to enforce step-by-step evaluation  
- Supported multiple LLM providers for flexibility  

---

## Limitations

- Performance depends on image quality  
- Complex diagrams with heavy annotations may reduce accuracy  
- Requires API access to external LLM providers  

---

## Future Improvements

- Automated scoring system (marks out of 10)  
- Diagram-specific evaluation templates  
- Batch processing of submissions  
- Improved spatial alignment detection  

---

## Use Cases

- Academic diagram grading  
- AI-assisted evaluation tools  
- EdTech platforms  
- Visual reasoning research  

---

## Disclaimer

This tool is intended for educational use. Results may vary depending on input quality and model behavior.
