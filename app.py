import streamlit as st
import pickle
import pandas as pd
import requests
import os
import tempfile

def download_and_load_pkl(file_id, file_name):
    file_url = f"https://drive.google.com/uc?id={file_id}"
    
    # Create a temporary directory
    temp_dir = tempfile.gettempdir()
    
    # Use tempfile.NamedTemporaryFile to create a temporary file
    with tempfile.NamedTemporaryFile(suffix=".pkl", dir=temp_dir, delete=False) as temp_file:
        temp_file_path = temp_file.name
    
    # Check if the file already exists locally
    if not os.path.exists(temp_file_path):
        st.info(f"Downloading {file_name}...")
        with st.spinner('Downloading...'):
            gdown.download(file_url, output=temp_file_path, quiet=False)
        return {"status": "Downloaded", "file_path": temp_file_path, "file_exists": True}
    else:
        return {"status": "Using local file", "file_path": temp_file_path, "file_exists": True}

# Usage of the function outside
movies_result = download_and_load_pkl("1lTLT6oVHcbBsacA43pc4VAsS932TjW0J", 'movies_dic.pkl')
similarity_result = download_and_load_pkl("1sdRQptMMhYVyCJEDM3afS1V9B-qsSCm4", 'similarity_pkl.pkl')

# Display information using Streamlit functions
st.info(movies_result["status"])
st.write(f"Movies File Path: {movies_result['file_path']}")
st.write(f"Movies File Exists: {movies_result['file_exists']}")

st.info(similarity_result["status"])
st.write(f"Similarity File Path: {similarity_result['file_path']}")
st.write(f"Similarity File Exists: {similarity_result['file_exists']}")

# Check if the file exists and has a non-zero size before loading
if os.path.exists(movies_result['file_path']) and os.path.getsize(movies_result['file_path']) > 0:
    with open(movies_result['file_path'], 'rb') as f:
        movies_dict = pickle.load(f)
else:
    st.error(f"Error: The file {movies_result['file_path']} is either empty or doesn't exist.")

# Continue with the rest of your Streamlit app code...
# Download and load movies_dic
movies = pd.DataFrame(movies_dict)

# Check if the file exists and has a non-zero size before loading
if os.path.exists(similarity_result['file_path']) and os.path.getsize(similarity_result['file_path']) > 0:
    with open(similarity_result['file_path'], 'rb') as f:
        similarity = pickle.load(f)
else:
    st.error(f"Error: The file {similarity_result['file_path']} is either empty or doesn't exist.")

# Continue with the rest of your Streamlit app code...
