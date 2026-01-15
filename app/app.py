import streamlit as st
from pipeline.pipeline import TVShowRecommendationPipeline
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="TV Show Recommender", page_icon=":tv:", layout="wide")

@st.cache_resource
def initialize_pipeline():
    return TVShowRecommendationPipeline()

pipeline = initialize_pipeline()

st.title("TV Show Recommender System")
st.write("Get personalized TV show recommendations based on your preferences!")

query = st.text_input("Enter your TV show preferences: eg. 'sci-fi and mystery shows'")

if query:
    with st.spinner("Getting your recommendations..."):
        try:
            recommendations = pipeline.recommend(query)
            st.success("Here are your recommendations:")
            st.markdown("### Recommendations")
            # for idx, show in enumerate(recommendations, start=1):
            #     st.write(f"{idx}. {show}")
            st.write(recommendations)
        except Exception as e:
            st.error(f"An error occurred while fetching recommendations: {str(e)}")