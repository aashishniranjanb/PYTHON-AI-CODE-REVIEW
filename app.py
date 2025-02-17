! pip install google-generativeai
! pip install streamlit

import streamlit as st
import google.generativeai as genai
import os

# Set up page config
st.set_page_config(
    page_title="AI Code Reviewer",
    page_icon="✨",
    layout="wide"
)

# Load API Key
api_key = os.getenv("AIzaSyBVOM4Pct30jaUcFUiXpbMy4hVOv2f3kKk")
if not api_key:
    st.error("API key not found. Please set GENAI_API_KEY in the environment.")
    st.stop()

# Configure Google Gemini AI
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-pro")

# Page Title
st.markdown("<h1 style='text-align: center;'>AI Code Reviewer</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: gray;'>Analyze and optimize your Python code effortlessly</h4>", unsafe_allow_html=True)

# Layout
col1, col2 = st.columns([3, 2])

with col1:
    st.markdown("### Paste Your Python Code Here:")
    code_input = st.text_area("Enter your Python code", height=300, label_visibility="collapsed")

with col2:
    st.markdown("### AI Code Review Output:")
    review_output = st.empty()

# Function to Review Code
def review_code(code):
    """Generates a detailed review of the provided Python code using Google Gemini AI."""
    prompt = f"""
    Analyze the following Python code and identify:
    
    1. Code functionality
    2. Errors and issues
    3. Performance improvements
    4. Readability and maintainability enhancements
    5. Final rating out of 5
    
    Code:
    {code}
    """
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error processing request: {str(e)}"

# Button to Process the Code
st.markdown("---")
center_button = st.columns([2, 1, 2])[1]
with center_button:
    if st.button("🔍 Review Code", use_container_width=True):
        if code_input.strip():
            with st.spinner("Reviewing your code... Please wait."):
                review_result = review_code(code_input)
                review_output.write(review_result)
        else:
            st.warning("Please enter a Python code snippet.")

# Sidebar
st.sidebar.title("📌 How to Use")
st.sidebar.info("""
1. Paste your Python code in the input box.
2. Click the 'Review Code' button.
3. AI will analyze and provide feedback.
4. Use suggestions to optimize your code.
""")

st.sidebar.markdown("---")
st.sidebar.markdown("💡 **Powered by Google Gemini AI**")

# Footer
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: gray;'>Made with ❤️ using Streamlit & Gemini AI</p>", unsafe_allow_html=True)
