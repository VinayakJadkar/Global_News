import json
import requests
import streamlit as st

# Define your NewsAPI.org API key
api_key = "pub_27492aab2f2ae3b24de7a73a5c1d952d82ace"




# Set page configuration to wide layout
st.set_page_config(page_title="Search_News",page_icon = "🔍", layout="wide")
 

    
title_html = """
<div style="font-size: 36px; font-weight: bold; margin-bottom: 10px;">Global News Hub</div>
<div style="font-size: 18px; color: #666;">Connecting You to the World's Latest Stories</div>
<hr style="margin-top: 10px; border: 2px solid #3498db;">
"""

st.markdown(title_html, unsafe_allow_html=True)


# Dictionary of country codes and their full names
country_dict = {
    "Afghanistan": "af", "Albania": "al", "Algeria": "dz", "Angola": "ao", "Argentina": "ar", "Australia": "au",
    "Austria": "at", "Azerbaijan": "az", "Bahrain": "bh", "Bangladesh": "bd", "Barbados": "bb", "Belarus": "by",
    "Belgium": "be", "Bermuda": "bm", "Bhutan": "bt", "Bolivia": "bo", "Bosnia And Herzegovina": "ba",
    "Brazil": "br", "Brunei": "bn", "Bulgaria": "bg", "Burkina Faso": "bf", "Cambodia": "kh", "Cameroon": "cm",
    "Canada": "ca", "Cape Verde": "cv", "Cayman Islands": "ky", "Chile": "cl", "China": "cn", "Colombia": "co",
    "Comoros": "km", "Costa Rica": "cr", "Côte d'Ivoire": "ci", "Croatia": "hr", "Cuba": "cu", "Cyprus": "cy",
    "Czech Republic": "cz", "Denmark": "dk", "Djibouti": "dj", "Dominica": "dm", "Dominican Republic": "do",
    "DR Congo": "cd", "Ecuador": "ec", "Egypt": "eg", "El Salvador": "sv", "Estonia": "ee", "Ethiopia": "et",
    "Fiji": "fj", "Finland": "fi", "France": "fr", "French Polynesia": "pf", "Gabon": "ga", "Georgia": "ge",
    "Germany": "de", "Ghana": "gh", "Greece": "gr", "Guatemala": "gt", "Guinea": "gn", "Haiti": "ht",
    "Honduras": "hn", "Hong Kong": "hk", "Hungary": "hu", "Iceland": "is", "India": "in", "Indonesia": "id",
    "Iraq": "iq", "Ireland": "ie", "Israel": "il", "Italy": "it", "Jamaica": "jm", "Japan": "jp", "Jordan": "jo",
    "Kazakhstan": "kz", "Kenya": "ke", "Kuwait": "kw", "Kyrgyzstan": "kg", "Latvia": "lv", "Lebanon": "lb",
    "Libya": "ly", "Lithuania": "lt", "Luxembourg": "lu", "Macau": "mo", "Macedonia": "mk", "Madagascar": "mg",
    "Malawi": "mw", "Malaysia": "my", "Maldives": "mv", "Mali": "ml", "Malta": "mt", "Mauritania": "mr",
    "Mexico": "mx", "Moldova": "md", "Mongolia": "mn", "Montenegro": "me", "Morocco": "ma", "Mozambique": "mz",
    "Myanmar": "mm", "Namibia": "na", "Nepal": "np", "Netherlands": "nl", "New Zealand": "nz", "Niger": "ne",
    "Nigeria": "ng", "North Korea": "kp", "Norway": "no", "Oman": "om", "Pakistan": "pk", "Panama": "pa",
    "Paraguay": "py", "Peru": "pe", "Philippines": "ph", "Poland": "pl", "Portugal": "pt", "Puerto Rico": "pr",
    "Romania": "ro", "Russia": "ru", "Rwanda": "rw", "Samoa": "ws", "San Marino": "sm", "Saudi Arabia": "sa",
    "Senegal": "sn", "Serbia": "rs", "Singapore": "sg", "Slovakia": "sk", "Slovenia": "si", "Solomon Islands": "sb",
    "Somalia": "so", "South Africa": "za", "South Korea": "kr", "Spain": "es", "Sri Lanka": "lk", "Sudan": "sd",
    "Sweden": "se", "Switzerland": "ch", "Syria": "sy", "Taiwan": "tw", "Tajikistan": "tj", "Tanzania": "tz",
    "Thailand": "th", "Tonga": "to", "Tunisia": "tn", "Turkey": "tr", "Turkmenistan": "tm", "Uganda": "ug",
    "Ukraine": "ua", "United Arab Emirates": "ae", "United Kingdom": "gb", "United States of America": "us",
    "Uruguay": "uy", "Uzbekistan": "uz", "Venezuela": "ve", "Vietnam": "vi", "Yemen": "ye", "Zambia": "zm",
    "Zimbabwe": "zw"
}
  



# Sidebar for selecting filters
keyword=st.sidebar.text_input("Search_keyword")
selected_country_code = st.sidebar.selectbox("Country", list(country_dict.keys()))
fetch_result = st.sidebar.button("Show Results")

# Function to fetch news data from the API

# Function to fetch news data from the API with caching
@st.cache_data(ttl=3600)  # Cache for 1 hour
def fetch_news_data_cached(keyword, country):
    url = f"https://newsdata.io/api/1/news?apikey={api_key}&language=en&q={keyword}&country={country}"
    response = requests.get(url)
    news_data = response.json()
    return news_data

# Sidebar for selecting filters
# ... (Sidebar code remains the same)



def render_full_article_page(title, description, content, link):
    st.title(title)
    st.markdown(description, unsafe_allow_html=True)
    st.markdown(content, unsafe_allow_html=True)
    st.markdown(f"[Read Full Article]({link})")

# Fetch and display news data if the Fetch Result button is clicked
if fetch_result:
    selected_country = country_dict[selected_country_code]
    news_data = fetch_news_data_cached(keyword, selected_country)

    # Create dynamic containers using the fetched news data
    for idx, results in enumerate(news_data["results"]):
        col1, col2 = st.columns([3, 1])
        with col1:
            st.header(results["title"])

            # Combine title and description as the label for the expander
            with st.expander("Read More..."):
                st.markdown(f"<h4>{results['description']}</h4>", unsafe_allow_html=True)
                st.markdown(f"<p style='font-size: 16px;'>{results['content']}</p>", unsafe_allow_html=True)
                st.markdown(f"<a href='{results['link']}' target='_blank'>Read Full Article</a>", unsafe_allow_html=True)
                
                

        with col2:
            if results["image_url"]:
                st.image(results["image_url"], width=400)
            else:
                st.write("Image not available")

        st.write("---")

