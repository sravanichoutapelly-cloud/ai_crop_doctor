import streamlit as st
import requests
import base64
from PIL import Image
import io

st.set_page_config(page_title="AI Crop Doctor", layout="centered")
st.title("🌱 AI Crop Doctor & Advisor")
st.write("Upload a leaf photo to get a disease diagnosis and expert local advice.")

lang = st.selectbox("Choose Language / भाषा चुनें", ["English", "Hindi (हिंदी)", "Telugu (తెलुगु)"])
uploaded_file = st.file_uploader("Take or Upload a Photo of the Leaf", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Crop Image", use_container_width=True)
    
    with st.spinner("Analyzing crop health... please wait..."):
        try:
            # Convert image to bytes
            img_byte_arr = io.BytesIO()
            image.save(img_byte_arr, format='JPEG')
            img_bytes = img_byte_arr.getvalue()
            base64_image = base64.b64encode(img_bytes).decode('utf-8')
            
            # Construct the HTTP Request payload bypassing library locks
            api_key = ""AIzaSy..." # AQ.Ab8RN6LBc3f0Ht8HYnqy8VGybnasK-R38IctmUc4s9cYyY0kvQ"
            url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={api_key}"
            
            prompt = f"You are an expert agricultural scientist. Analyze this crop image and provide the response in {lang} covering: 1. Disease Identification or Health Status. 2. Clear, simple reasoning for your diagnosis. 3. Practical, actionable advice for the farmer. 4. Warning: If symptoms persist, please consult a local agricultural expert."
            
            payload = {
                "contents": [{
                    "parts": [
                        {"text": prompt},
                        {
                            "inlineData": {
                                "mimeType": "image/jpeg",
                                "data": base64_image
                            }
                        }
                    ]
                }]
            }
            
            response = requests.post(url, json=payload)
            res_json = response.json()
            
            # Display text out cleanly
            if "candidates" in res_json:
                output_text = res_json["candidates"][0]["content"]["parts"][0]["text"]
                st.write(output_text)
            else:
                st.error(f"API Error: {res_json}")
                
        except Exception as e:
            st.error(f"An error occurred: {e}")
