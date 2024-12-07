import streamlit as st
import google.generativeai as genai

# Set up the Streamlit page
st.set_page_config(
    page_title="Dhruv's AI Bot",
    page_icon="🤖",
    layout="wide"
)

# Configure Gemini API
if "general" not in st.secrets or "API_KEY" not in st.secrets["general"]:
    st.error("API_KEY is missing in the Streamlit secrets!")
    st.stop()
else:
    api_key = st.secrets["general"]["API_KEY"]
    genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-1.5-flash")

# Persona for the chatbot
persona = """
    You are Dhruv AI Bot, a digital assistant representing Dhruv Rajpurohit.
    Speak as Dhruv would—using "I" instead of third-person references.
    If you don't know the answer, respond with "For that, please contact me personally" or "That's a secret" if the question seems confidential.
    Here is more about Dhruv Rajpurohit:
    - I am a final-year computer engineering student at GEC Bhavnagar.
    - My CGPA is 8.7, and I am passionate about Artificial Intelligence and Networking.
    - My skills include:
        • Programming: Python
        • Data Science: Pandas, NumPy, Matplotlib, Seaborn, Plotly
        • Machine Learning: Scikit-learn, TensorFlow, PyTorch
        • Networking: CCNA Certified
        • Robotics: Raspberry Pi, PID Control
        • Others: Git, Power BI, SQL
    - I have worked on projects like:
        • Wall-Following Robot
        • Python Web Scraper
        • AI-Driven Diabetes Readmission Prevention
        • Predictive Maintenance
    - You can ask me about my projects, certifications, or career aspirations.
"""

st.header(":blue[Dhruv's AI Bot]", divider="rainbow")
st.markdown("### Hi there! Ask me anything about myself or my work.")

# Function to map Gemini roles to Streamlit roles
def role_to_streamlit(role):
    if role == "model":
        return "assistant"
    else:
        return role

# Initialize chat session state
if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])

if "const" not in st.session_state:
    st.session_state.const = "firstrun"

if st.session_state.const == "firstrun":
    st.session_state.const = "rerunned"
    st.session_state.chat.send_message(persona)

# Display chat messages from history
for message in st.session_state.chat.history[2:]:
    with st.chat_message(role_to_streamlit(message.role)):
        st.markdown(message.parts[0].text)

# User input for chatbot
if prompt := st.chat_input("What would you like to know about me?"):
    # Display user's input
    st.chat_message("user").markdown(prompt)

    # Get response from Gemini API
    response = st.session_state.chat.send_message(prompt)

    # Display AI's response
    with st.chat_message("assistant"):
        st.markdown(response.text)

# Sidebar for contact information and social links
with st.sidebar:
    st.markdown("""
        <div style="padding: 10px; border: 2px solid #ffffff; border-radius: 5px; background-color: #0E1117; color: #ffffff;">
        📞 Contact: +91 9173672887
        </div>
    """, unsafe_allow_html=True)

    st.write("\n")
    st.subheader("Connect with me:")
    st.markdown("""
        <div style='display: flex; justify-content: left; align-items: center; gap: 10px;'>
            <a href="https://www.linkedin.com/in/dhruvrajpurohitt" target="_blank">
                <img src="https://cdn.jsdelivr.net/npm/simple-icons@3.0.1/icons/linkedin.svg" alt="LinkedIn" width="32" height="32" style="filter: invert(1);">
            </a>
            <a href="https://github.com/RajpurohitDhruv" target="_blank">
                <img src="https://cdn.jsdelivr.net/npm/simple-icons@3.0.1/icons/github.svg" alt="GitHub" width="32" height="32" style="filter: invert(1);">
            </a>
            <a href="mailto:rajpurohitdhruv27@gmail.com" target="_blank">
                <img src="https://cdn.jsdelivr.net/npm/simple-icons@3.0.1/icons/gmail.svg" alt="Email" width="32" height="32" style="filter: invert(1);">
            </a>
            <a href="https://x.com/Dhruv_Purohit27" target="_blank">
                <img src="https://cdn.jsdelivr.net/npm/simple-icons@3.0.1/icons/twitter.svg" alt="Twitter" width="32" height="32" style="filter: invert(1);">
            </a>
        </div>
    """, unsafe_allow_html=True)
