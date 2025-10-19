from src.data_loader import AnimeDataLoader
from src.vector_store import VectorStoreBuilder
from dotenv import load_dotenv
from utils.logger import get_logger
from utils.custom_exception import CustomException

load_dotenv('../.env')
logger = get_logger(__name__)

def main():
    try:
        logger.info("Starting to build pipeline..")
        loader = AnimeDataLoader('../data/anime_with_synopsis.csv', '../data/anime_updated.csv')
        processed_csv = loader.load_and_process()

        logger.info('Data loaded and processed')

        vector_store = VectorStoreBuilder(processed_csv)
        vector_store.build_and_store_vectorstore()

        logger.info('Vector store built successfully')
        logger.info('Pipeline built successfully')

    except Exception as e:
        logger.error(f"Failed to build pipeline. {str(e)}")
        raise CustomException("Failed to build pipeline", e)  
    

if __name__=='__main__':
    main()    