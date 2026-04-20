import base64
import google.generativeai as genai
from openai import OpenAI
from groq import Groq
from io import BytesIO

def encode_image(image):
    buffered = BytesIO()
    image.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode('utf-8')

def get_vision_response(provider, api_key, master_img, student_img, prompt):
    m_b64 = encode_image(master_img)
    s_b64 = encode_image(student_img)

    try:
        if provider == "Google Gemini":
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel('gemini-1.5-flash')
            response = model.generate_content([prompt, master_img, student_img])
            return response.text

        elif provider == "OpenAI":
            client = OpenAI(api_key=api_key)
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": [
                    {"type": "text", "text": prompt},
                    {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{m_b64}"}},
                    {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{s_b64}"}}
                ]}]
            )
            return response.choices[0].message.content

        elif provider == "Groq":
            client = Groq(api_key=api_key)
            response = client.chat.completions.create(
                model="llama-3.2-11b-vision-preview",
                messages=[{"role": "user", "content": [
                    {"type": "text", "text": prompt},
                    {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{m_b64}"}},
                    {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{s_b64}"}}
                ]}]
            )
            return response.choices[0].message.content

    except Exception as e:
        return f"Error with {provider}: {str(e)}"
