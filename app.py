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

# Continue with the rest of your Streamlit app code...
# Download and load movies_dic
movies_dict = pickle.load(open(movies_result['file_path'], 'rb'))
movies = pd.DataFrame(movies_dict)

# Download and load similarity_pkl
similarity = pickle.load(open(similarity_result['file_path'], 'rb'))

# Continue with the rest of your Streamlit app code...
