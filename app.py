import streamlit as st
import google.generativeai as genai
from PIL import Image

# Paste your actual AIzaSy key from your Google AI Studio tab right inside these quotes
API_KEY = "AQ.Ab8RN6LBc3f0Ht8HYnqy8VGybnasK-R38IctmUc4s9cYyY0kvQ"

# Configure the library directly using the standard personal key format
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-2.5-flash')

st.set_page_config(page_title="AI Crop Doctor", layout="centered")
st.title("🌱 AI Crop Doctor & Advisor")
st.write("Upload a leaf photo to get a disease diagnosis and expert local advice.")

lang = st.selectbox("Choose Language / भाषा चुनें", ["English", "Hindi (हिंदी)", "Telugu (తెलुగు)"])
uploaded_file = st.file_uploader("Take or Upload a Photo of the Leaf", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Crop Image", use_container_width=True)
    
    with st.spinner("Analyzing crop health... please wait..."):
        try:
            prompt = f"You are an expert agricultural scientist. Analyze this crop image and provide the response in {lang} covering: 1. Disease Identification or Health Status. 2. Clear, simple reasoning for your diagnosis. 3. Practical, actionable advice for the farmer. 4. Warning: If symptoms persist, please consult a local agricultural expert."
            response = model.generate_content([prompt, image])
            st.write(response.text)
        except Exception as e:
            st.error(f"An error occurred: {e}")
