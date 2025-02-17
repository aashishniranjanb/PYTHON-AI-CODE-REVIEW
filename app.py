!pip install google-generativeai

import google.generativeai as genai

!pip install streamlit

import streamlit as st
import google.generativeai as genai
import os

"""CONFIGURE THE GOOGLE GENAI WITH API KEY"""

genai.configure(api_key="AIzaSyBVOM4Pct30jaUcFUiXpbMy4hVOv2f3kKk")

"""Initialize Google Generative AI model

"""

model = genai.GenerativeModel("gemini-pro")

st.set_page_config(page_title="Python Code Reviewer", layout="centered")
st.title("Python Code Reviewer")
st.write("Submit your Python code for analysis and improvement suggestions.")

code_input = st.text_area("Enter your Python code:", height=250)

def review_code(code):
    """Generates a detailed review of the provided Python code using Google Gemini AI."""
    prompt = f"""
    Analyze the following Python code for errors, inefficiencies, and best practices.
    Provide structured feedback including:

    1. Code functionality
    2. Errors and issues
    3. Optimization suggestions
    4. Readability and maintainability improvements
    5. Final rating out of 5

    Code:
    {code}
    """
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error processing request: {str(e)}"

if st.button("Review Code"):
    if code_input.strip():
        with st.spinner("Analyzing your code..."):
            review_result = review_code(code_input)
            st.subheader("Code Review Feedback")
            st.write(review_result)
    else:
        st.warning("Please enter a Python code snippet.")

# Sidebar with instructions
st.sidebar.header("Instructions")
st.sidebar.markdown("""
1. Enter your Python code in the text area.
2. Click 'Review Code' to analyze the script.
3. Review the feedback provided.
""")
