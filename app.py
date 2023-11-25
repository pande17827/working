import streamlit as st
import pickle
import pandas as pd
import requests
import os
import tempfile

@st.cache(allow_output_mutation=True)
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
    else:
        st.info(f"{file_name} already exists. Using the local file.")

    # Debugging: Print file path and existence
    st.write(f"Temp File Path ({file_name}): {temp_file_path}")
    st.write(f"File Exists: {os.path.exists(temp_file_path)}")

    with open(temp_file_path, 'rb') as f:
        return pickle.load(f)

# Rest of your Streamlit app code...

# Use download_and_load_pkl in your app
# Download and load movies_dic
movies_dict = download_and_load_pkl("1lTLT6oVHcbBsacA43pc4VAsS932TjW0J", 'movies_dic.pkl')
movies = pd.DataFrame(movies_dict)

# Download and load similarity_pkl
similarity = download_and_load_pkl("1sdRQptMMhYVyCJEDM3afS1V9B-qsSCm4", 'similarity_pkl.pkl')

# Continue with the rest of your Streamlit app code...
