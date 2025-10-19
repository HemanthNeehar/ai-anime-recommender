import streamlit as st
from pipeline.pipeline import AnimeRecommendationPipeline
from dotenv import load_dotenv

st.set_page_config(page_title='Anime Recommender',layout='wide')

load_dotenv('../.env')

@st.cache_resource
def init_pipeline():
    return AnimeRecommendationPipeline()

# Initialize the pipeline in the beginning only once (cache)
pipeline = init_pipeline()

st.title("Anime Recommender System")

query = st.text_input("Enter your Anime preference, eg. light hearted Anime with school settings.")
if query:
    with st.spinner("Fetching Recommendations for you..."):
        response = pipeline.recommend(query)
        st.markdown("### Recommendations")
        st.write(response)