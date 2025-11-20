import faiss
import numpy as np
import json
import os

def create_index(dim):
    index = faiss.IndexFlatL2(dim)
    return index

def save_index(index, embeddings, mapping):
    os.makedirs("vector_store", exist_ok=True)
    faiss.write_index(index, "vector_store/index.faiss")
    np.save("vector_store/embeddings.npy", embeddings)
    with open("vector_store/mapping.json", "w") as f:
        json.dump(mapping, f)

def load_index():
    index = faiss.read_index("vector_store/index.faiss")
    embeddings = np.load("vector_store/embeddings.npy")
    with open("vector_store/mapping.json", "r") as f:
        mapping = json.load(f)
    return index, embeddings, mapping
