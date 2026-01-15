from src.vector_store import VectorStoreBuilder
from src.recommender import TVShowRecommender
from config.config import GROQ_API_KEY, MODEL_NAME
from utils.custom_exception import CustomException
from utils.logger import get_logger

logger = get_logger(__name__)

class TVShowRecommendationPipeline:
    def __init__(self, persist_dir: str="chroma_db"):
        try:
            logger.info("Initializing TV Show Recommendation Pipeline...")
            vector_store_builder = VectorStoreBuilder(csv_path="", persist_dir=persist_dir)
            retriever = vector_store_builder.load_vector_store().as_retriever()
            self.recommender = TVShowRecommender(
                retriever=retriever,
                api_key=GROQ_API_KEY,
                model_name=MODEL_NAME
            )
            logger.info("TV Show Recommendation Pipeline initialized successfully.")
        except Exception as e:
            logger.error(f"Error during pipeline initialization {str(e)}")
            raise CustomException("Failed to initialize the TV Show Recommendation Pipeline", e)
    
    def recommend(self, user_query: str):
        try:
            logger.info("Received a user query...")
            recommendations = self.recommender.get_recommendations(user_query)
            logger.info("Recommendations retrieved successfully.")
            return recommendations
        except Exception as e:
            logger.error(f"Error during getting recommendations: {str(e)}")
            raise CustomException("Failed to get recommendations", e)