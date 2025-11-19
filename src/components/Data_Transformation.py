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
    
    def embedding(self):
        df = pd.read_csv(self.config.chunks_path)
        model = SentenceTransformer('all-MiniLM-L6-v2')
        embeddings = model.encode(df['chunks'].tolist())
        embeddings = embeddings / np.linalg.norm(embeddings, axis=1, keepdims=True)

        create_directories([os.path.dirname(self.config.embedded_vectors_path)])
        pd.DataFrame(embeddings).to_csv(self.config.embedded_vectors_path, index=False)

    def store_to_vector(self):
        client = chromadb.Client()
        collection = client.create_collection(name="PDF DATA")
        df = pd.read_csv(self.config.embedded_vectors_path)
        nparr = df.to_numpy()
        collection.add(
            embeddings = nparr.tolist(),
            metadatas = [{"source": "pdf_data"} for _ in range(len(nparr))],
            ids = [str(i) for i in range(len(nparr))]
        )








