import streamlit as st
import pandas as pd
import os
import joblib
from pathlib import Path


# SET THE PAGE TITLE
st.set_page_config(page_title="Sentiment Analysis Application",page_icon="D:\sentiment_analysis\Screenshot 2024-12-31 215335.png")

# APPLICATION TITLE AND DESCRIPTION

st.title("Seniment Analysis Application")
st.write("This apllication analyzes text data from various sources and determine the underlying sentiment, such as positive, negative, or neutral.")
