from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

def embed_text(sentences):
    return model.encode(sentences, convert_to_tensor=False)
