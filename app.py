import streamlit as st
from extraction import extract_text
from analysis import analyze_text
from metadata import generate_metadata
from io import BytesIO
import json

st.title("Automated Metadata Generation System")
st.write("Upload a document (PDF, DOCX, or TXT) to generate metadata automatically.")

uploaded_file = st.file_uploader("Choose a file", type=['pdf', 'docx', 'txt'])

if uploaded_file:
    file_type = uploaded_file.name.split('.')[-1].lower()
    try:
        with st.spinner("Extracting text..."):
            text = extract_text(BytesIO(uploaded_file.read()), file_type)
        with st.spinner("Analyzing text..."):
            analysis = analyze_text(text)
        metadata = generate_metadata(text, analysis)
        
        st.subheader("Generated Metadata")
        st.write("**Title:**", metadata['title'])
        st.write("**Author:**", metadata['author'])
        st.write("**Date:**", metadata['date'])
        st.write("**Keywords:**", ', '.join(metadata['keywords']))
        st.write("**Summary:**", metadata['summary'])
        
        metadata_json = json.dumps(metadata, indent=4)
        st.download_button(
            label="Download Metadata",
            data=metadata_json,
            file_name="metadata.json",
            mime="application/json"
        )
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")