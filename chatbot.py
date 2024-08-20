import streamlit as st

st.header("First Chatbot")

# Upload PDF file
with st.sidebar:
    st.title("Your documents")
    uploaded_file = st.file_uploader("Upload a file", type='pdf')