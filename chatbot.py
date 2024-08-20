import streamlit as st
from PyPDF2 import PdfReader

st.header("First Chatbot")

# Upload PDF file
with st.sidebar:
    st.title("Your documents")
    uploaded_file = st.file_uploader("Upload a file", type='pdf')

# Extract text
if uploaded_file is not None:
    pdf = PdfReader(uploaded_file)
    text = ""
    for page in pdf.pages:
        text += page.extract_text()
    # st.write(text)
