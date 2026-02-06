import os
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

# Load SOP
with open("data/sop.txt", "r", encoding="utf-8") as f:
    sop_text = f.read()

# Split SOP into chunks (roughly 100 words per chunk)
def chunk_text(text, chunk_size=100):
    words = text.split()
    chunks = []
    for i in range(0, len(words), chunk_size):
        chunks.append(" ".join(words[i:i+chunk_size]))
    return chunks

chunks = chunk_text(sop_text)

# Generate embeddings
model = SentenceTransformer('all-MiniLM-L6-v2')
embeddings = model.encode(chunks, convert_to_numpy=True)

# Build FAISS index
dim = embeddings.shape[1]
index = faiss.IndexFlatL2(dim)
index.add(embeddings)

# Save index and chunks
faiss.write_index(index, "data/faiss.index")
import pickle
with open("data/sop_chunks.pkl", "wb") as f:
    pickle.dump(chunks, f)

print("SOP ingestion complete. Chunks:", len(chunks))
