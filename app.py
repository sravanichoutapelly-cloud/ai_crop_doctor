import streamlit as st
from google import genai
from PIL import Image

# Initialize the correct Google Cloud-compatible client directly
GOOGLE_API_KEY = "AQ.Ab8RN6J7I_B89NUS7RDNeYcjE7y7PZNKiKSx_LiMCtXm5K6K2w"
client = genai.Client(api_key=GOOGLE_API_KEY)

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
            prompt = f"You are an expert agricultural scientist. Analyze this crop image and provide the response in {lang} covering: 1. Disease Identification or Health Status. 2. Clear, simple reasoning for your diagnosis. 3. Practical, actionable advice for the farmer. 4. Warning: If symptoms persist, please consult a local agricultural expert."
            
            # Using the cloud-native generation method
            response = client.models.generate_content(
                model='gemini-2.5-flash',
                contents=[prompt, image]
            )
            st.write(response.text)
        except Exception as e:
            st.error(f"An error occurred: {e}")
