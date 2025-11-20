from src.utils.common import create_directories
from src.entity.config_entity import DataTransformationConfig
from sentence_transformers import SentenceTransformer
import os 
import pandas as pd
import numpy as np
import chromadb
class DataTransformation:
    def __init__(self,config : DataTransformationConfig):
        self.config = config
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
    
    def embedding(self):
        df = pd.read_csv(self.config.chunks_path)
        
        embeddings = self.model.encode(df['chunks'].tolist())
        embeddings = embeddings / np.linalg.norm(embeddings, axis=1, keepdims=True)

        create_directories([os.path.dirname(self.config.embedded_vectors_path)])
        pd.DataFrame(embeddings).to_csv(self.config.embedded_vectors_path, index=False)

    def store_to_vector_db(self):
        client = chromadb.Client()
        collection = client.create_collection(name="PDF DATA",embedding_function=None,metadata={
        "hnsw:space": "cosine",
        "hnsw:M": 32,
        "hnsw:efConstruction": 200,
        "hnsw:ef": 20
        })
        df = pd.read_csv(self.config.embedded_vectors_path)
        nparr = df.to_numpy()
        collection.add(
            embeddings = nparr.tolist(),
            ids = [str(i) for i in range(len(nparr))]
        )

    def question_to_query(self):
        query_embedding = self.model.encode([self.config.query])
        query_embedding = query_embedding / np.linalg.norm(query_embedding, axis=1, keepdims=True)
        return query_embedding


    





