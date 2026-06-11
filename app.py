import streamlit as st
import google.generativeai as genai
from PIL import Image

# Paste your copied Gemini key between the quotes below
GOOGLE_API_KEY = "AQ.Ab8RN6KoKjpoXz5FAM2APzX_oZ1QFgFBmWonBKG-U9Fl-Oi32Q"
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

st.set_page_config(page_title="AI Crop Doctor", layout="centered")
st.title("🌱 AI Crop Doctor & Advisor")
st.write("Upload a leaf photo to get a disease diagnosis and expert local advice.")

lang = st.selectbox("Choose Language / भाषा चुनें", ["English", "Hindi (हिंदी)", "Telugu (తెలుగు)"])
uploaded_file = st.file_uploader("Take or Upload a Photo of the Leaf", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Crop Image", use_container_width=True)
    
    prompt = f"""
    You are an expert agricultural scientist. Analyze this crop image and provide:
    1. Disease Identification or Health Status.
    2. Clear, simple reasoning for your diagnosis.
    3. Practical, actionable advice for the farmer.
    4. A clear warning stating: 'Warning: If symptoms persist, please consult a local agricultural expert.'
    
    Provide the entire response in {lang}. Keep the language simple for field users.
    """
    st.write("🔄 Analyzing crop health... please wait...")
    try:
        response = model.generate_content([prompt, image])
        st.success("📋 Diagnosis & Recommendations:")
        st.write(response.text)
    except Exception as e:
        st.error(f"An error occurred: {e}")
