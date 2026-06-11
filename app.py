import streamlit as st
import requests
from PIL import Image
import io

# Paste your 'AQ.' key directly inside these quotes
API_KEY = "PASTE_YOUR_AQ_KEY_HERE"

st.set_page_config(page_title="AI Crop Doctor", layout="centered")
st.title("🌱 AI Crop Doctor & Advisor")
st.write("Upload a leaf photo to get a disease diagnosis and expert local advice.")

lang = st.selectbox("Choose Language / भाषा चुनें", ["English", "Hindi (हिंदी)", "Telugu (తెలుగు)"])
uploaded_file = st.file_uploader("Take or Upload a Photo of the Leaf", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Crop Image", use_container_width=True)
    
    # Convert image to bytes for the API request
    img_byte_arr = io.BytesIO()
    image.save(img_byte_arr, format='JPEG')
    img_bytes = img_byte_arr.getvalue()
    
    with st.spinner("Analyzing crop health... please wait..."):
        try:
            # Constructing direct HTTP payload compatible with AQ. tokens
            url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={API_KEY}"
            
            headers = {"Content-Type": "application/json"}
            
            import base64
            base64_image = base64.b64encode(img_bytes).decode('utf-8')
            
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
            
            response = requests.post(url, headers=headers, json=payload)
            res_data = response.json()
            
            if response.status_code == 200:
                output_text = res_data['candidates'][0]['content']['parts'][0]['text']
                st.write(output_text)
            else:
                st.error(f"API Error ({response.status_code}): {res_data.get('error', {}).get('message', 'Unknown error')}")
                
        except Exception as e:
            st.error(f"An error occurred: {e}")
