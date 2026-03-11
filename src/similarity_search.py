import pandas as pd
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

# Load dataset
df = pd.read_csv("data/startups.csv")

startup_names = df["name"].tolist()
startup_descriptions = df["description"].tolist()

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Create embeddings
startup_embeddings = model.encode(startup_descriptions)

# Create FAISS index
dimension = startup_embeddings.shape[1]

index = faiss.IndexFlatL2(dimension)
index.add(np.array(startup_embeddings))


def find_similar_startups(query, k=3):

    query_vector = model.encode([query])

    distances, indices = index.search(query_vector, k)

    results = []

    for i in indices[0]:
        results.append(startup_names[i])

    return results