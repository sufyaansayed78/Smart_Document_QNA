from src.pipeline.Data_Transformation_Pipeline import DataTransformationPipeline
from src import logger 
import chromadb 
from src.entity.config_entity import RetrieveVectorsConfig
import numpy as np
class RetrieveVectors:
    def __init__(self,config : RetrieveVectorsConfig):
        self.config = config
    def retreive_vectors(self):
        logger.info("Finding vectors with similarities....")
        client = chromadb.Client()
        collection = client.get_collection(name="PDF_DATA")
        results = collection.query(
            query_embeddings = [np.load(self.config.embedded_query_path).tolist()[0]],
            n_results = 5
        )
        logger.info("Vector retrieval completed")
        np.save(self.config.similar_vectors_path, np.array(results['embeddings'][0]))
        logger.info(f"Similar context vectors saved at {self.config.similar_vectors_path}")
    

         








