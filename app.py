import streamlit as st
import google.generativeai as genai
from PIL import Image
import subprocess
import sys
import os
import json
from datetime import datetime

page_bg = """
<style>
[data-testid="stAppViewContainer"] {
    background-color: #f0f8ff; /* Light blue */
}
[data-testid="stHeader"] {
    background-color: rgba(0,0,0,0); /* Transparent header */
}
</style>
"""

# ------------------- APP SETUP -------------------
st.set_page_config(page_title="NR Image Descriptor", layout="wide")

st.title("🖼️ NR Image Descriptor and Content Modifier")

# ------------------- API KEY -------------------
GEMINI_API_KEY = "AIzaSyACWRc1oFANxMdbJk-NxTs-Y3N7I19e0Uo"   # replace with your key
genai.configure(api_key=GEMINI_API_KEY)

# ------------------- FIXED MODEL -------------------
MODEL_NAME = "gemini-1.5-flash"
model = genai.GenerativeModel(MODEL_NAME)

# ------------------- HISTORY JSON -------------------
HISTORY_FILE = "history.json"

def load_history():
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as f:
            return json.load(f)
    return []

def save_history(entry):
    history = load_history()
    history.append(entry)
    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f, indent=4)

# ------------------- NAVIGATION TABS -------------------
tabs = st.tabs(["🏠 Home", "📜 History", "📞 Contact"])

# ------------------- HOME TAB -------------------
with tabs[0]:
    st.write("Upload an image, then enter a prompt to get a description. Refine it using the chatbot below.")

    uploaded_file = st.file_uploader("📂 Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        try:
            # Display uploaded image (smaller size)
            image = Image.open(uploaded_file)
            st.image(image, caption="Uploaded Image", width=300)

            # Save uploaded image to a temp file
            temp_image_path = "temp_uploaded_image.png"
            image.save(temp_image_path)

            # ------------------- PROMPT -------------------
            prompt = st.text_input("Enter your prompt for image description")

            if st.button("Generate Description") and prompt:
                st.write("⚡ Generating description...")
                response = model.generate_content([prompt, image])
                st.session_state.description = response.text
                st.session_state.image_path = temp_image_path

                st.subheader("📌 Image Description")
                st.write(st.session_state.description)

        except Exception as e:
            st.error(f"Error: {e}")

    # ------------------- CHATBOT -------------------
    if "description" in st.session_state and st.session_state.description:
        st.subheader("💬 Refine Description (Chatbot)")
        if "chat" not in st.session_state:
            st.session_state.chat = model.start_chat(history=[])

        user_input = st.text_input("Enter your modification request:", key="chat_input")

        if st.button("Modify"):
            try:
                full_prompt = f"Here is the current description: {st.session_state.description}\n\nUser request: {user_input}"
                chat_response = st.session_state.chat.send_message(full_prompt)
                st.session_state.description = chat_response.text

                st.subheader("✨ Modified Description")
                st.write(st.session_state.description)
            except Exception as e:
                st.error(f"Error: {e}")

        # ------------------- EMAIL SEND -------------------
        st.subheader("📧 Send Final Description + Image")
        user_name = st.text_input("Enter your Name")
        user_email = st.text_input("Enter your Email")

        if st.button("Send via Email"):
            if user_name and user_email:
                try:
                    result = subprocess.run(
                        [sys.executable, "send_mail.py", user_name, user_email,
                         st.session_state.description, st.session_state.image_path],
                        capture_output=True, text=True
                    )
                    if result.returncode == 0:
                        st.success("✅ Email sent successfully!")

                        # Save history entry
                        entry = {
                            "name": user_name,
                            "email": user_email,
                            "description": st.session_state.description,
                            "image_path": st.session_state.image_path,
                            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        }
                        save_history(entry)
                    else:
                        st.error(f"❌ Failed to send email: {result.stderr}")
                except Exception as e:
                    st.error(f"Error while sending email: {e}")
            else:
                st.warning("Please enter both name and email before sending.")

# ------------------- HISTORY TAB -------------------
with tabs[1]:
    st.subheader("📜 User History")
    history = load_history()
    if history:
        for entry in history:
            st.write(f"**Name:** {entry['name']}")
            st.write(f"**Email:** {entry['email']}")
            st.write(f"**Timestamp:** {entry['timestamp']}")
            st.write(f"**Description:** {entry['description']}")
            if entry.get("image_path") and os.path.exists(entry["image_path"]):
                st.image(entry["image_path"], caption="Uploaded Image", width=300)
            st.markdown("---")
    else:
        st.info("No history found yet.")

# ------------------- CONTACT TAB -------------------
with tabs[2]:
    st.subheader("📞 Contact Information")
    st.write("**Owner:** Naveen Raj K")
    st.write("**Phone:** +91 7501199896")
    st.write("**Address:** Nagercoil, India")
    st.write("**Email:** naveenmadhan86@gmail.com")