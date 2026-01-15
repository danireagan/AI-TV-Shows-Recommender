from src.data_loader import ShowsDataLoader
from src.vector_store import VectorStoreBuilder
from utils.logger import get_logger
from utils.custom_exception import CustomException
from dotenv import load_dotenv

load_dotenv()
logger = get_logger(__name__)

def main():
    try:
        logger.info("Starting the TV Show Recommendation Pipeline build process...")
        
        # Step 1: Load and preprocess data
        data_loader = ShowsDataLoader(original_csv="data/top_rated_2000_shows.csv", processed_csv="data/processed_tv_shows.csv")
        processed_csv = data_loader.load_and_process_data()
        logger.info("Data loaded and processed successfully.")
        
        # Step 2: Build and persist vector store
        vector_store_builder = VectorStoreBuilder(processed_csv)
        vector_store_builder.build_and_save_vector_store()
        logger.info("Vector store built and persisted successfully.")
        
        logger.info("TV Show Recommendation Pipeline build process completed successfully.")
    except Exception as e:
        logger.error(f"Error during pipeline build process: {str(e)}")
        raise CustomException("Failed to build the TV Show Recommendation Pipeline", e)

if __name__ == "__main__":
    main()