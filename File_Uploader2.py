# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 13:34:23 2020

@author: Shreyash
"""

try:
    from io import BytesIO, StringIO
    import pandas as pd
    import streamlit as st
    from PIL import Image
except Exception as e:
    print(e)
 
STYLE = """
<style>
img {
    max-width: 100%;
}
</style>
"""
 
def main():
    """Run this function to display the Streamlit app"""
    st.info(__doc__)
    st.markdown(STYLE, unsafe_allow_html=True)
    uploaded_file = st.file_uploader("Upload file", type=["png", "jpg"])
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.')
main()