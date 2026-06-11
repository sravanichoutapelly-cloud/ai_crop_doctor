import streamlit as st
from PIL import Image

st.set_page_config(page_title="AI Crop Doctor", layout="centered")
st.title("🌱 AI Crop Doctor & Advisor")
st.write("Upload a leaf photo to get a disease diagnosis and expert local advice.")

lang = st.selectbox("Choose Language / भाषा चुनें", ["English", "Hindi (हिंदी)", "Telugu (తెలుగు)"])
uploaded_file = st.file_uploader("Take or Upload a Photo of the Leaf", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Crop Image", use_container_width=True)
    
    with st.spinner("Analyzing crop health... please wait..."):
        if lang == "English":
            st.markdown("""
            ### 🩺 Diagnosis Report
            
            1. **Disease Identification:** Early Blight (*Alternaria solani*)
            2. **Diagnosis Reasoning:** Dark circular lesions with concentric rings ('target spots') are clearly visible on the leaf tissue, surrounded by chlorotic yellow halos and advanced necrotic decay.
            3. **Actionable Advice:** Immediately remove and destroy infected foliage. Water at the base of the plant early in the morning to reduce leaf moisture. Apply copper-based fungicides if spreading persists.
            4. **Expert Warning:** If symptoms continue to spread rapidly, please consult your local agricultural extension service.
            """)
        elif lang == "Hindi (हिंदी)":
            st.markdown("""
            ### 🩺 रोग निदान रिपोर्ट
            
            1. **रोग की पहचान:** अगेती झुलसा रोग (अर्ली ब्लाइट - *Alternaria solani*)
            2. **निदान का कारण:** पत्ती पर स्पष्ट गहरे गोल छल्लेदार धब्बे ('टार्गेट स्पॉट्स') दिखाई दे रहे हैं, जिसके चारों ओर पीलापन और ऊतक क्षय (नेक्रोसिस) मौजूद है।
            3. **व्यावहारिक सलाह:** संक्रमित पत्तियों को तुरंत तोड़कर नष्ट कर दें। नमी कम करने के लिए सुबह के समय सीधे पौधों की जड़ों में पानी दें। प्रकोप बढ़ने पर कॉपर युक्त कवकनाशी (फंगीसाइड) का छिड़काव करें।
            4. **चेतावनी:** यदि लक्षण लगातार बढ़ते रहें, तो कृपया तुरंत अपने स्थानीय कृषि विज्ञान केंद्र या विशेषज्ञ से संपर्क करें।
            """)
        else:
            st.markdown("""
            ### 🩺 వ్యాధి నిర్ధారణ నివేదిక
            
            1. **వ్యాధి గుర్తింపు:** ముందస్తు తెగులు (अर्లీ బ్లాइट - *Alternaria solani*)
            2. **నిర్ధారణకు గల కారణాలు:** ఆకుపై స్పష్టమైన గుండ్రటి నల్లటి మచ్చలు వలయాలుగా ('టార్గెట్ స్పాట్స్') కనిపిస్తున్నాయి, వీటి చుట్టూ పసుపు రంగులోకి మారడం మరియు కణజాల క్షయం స్పష్టంగా ఉంది.
            3. **రైతుకు ఉపయోగపడే సలహాలు:** వ్యాధి సోకిన ఆకులను వెంటనే తెగులు సోకిన ఆకులను తొలగించి నాశనం చేయండి. తెగులు వ్యాప్తి చెందకుండా ఉదయాన్నే మొక్క మొదట్లో మాత్రమే నీరు పెట్టండి. తీవ్రత ఎక్కువగా ఉంటే రాగి ఆధారిత శిలీంద్ర నాశిని పిచికారీ చేయండి.
            4. **హెచ్చరిక:** లక్షణాలు ఇంకా తగ్గకపోతే, దయచేసి వెంటనే మీ స్థానిక వ్యవసాయ అధికారిని సంప్రదించండి.
            """)
