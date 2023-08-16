import streamlit as st

# Define your NewsAPI.org API key
api_key = "pub_27492aab2f2ae3b24de7a73a5c1d952d82ace"



# Set page configuration to wide layout
st.set_page_config(page_title="Homepage",page_icon="🏠", layout="wide")
 
with st.container():
        
        # Embedding the image using the URL you provided
        image_url = "https://i.postimg.cc/zBgxpt6D/Global-news-bell.png"
        st.image(image_url, caption="Embedded Image", use_column_width=True)

