import faiss
import pickle
import numpy as np
from sentence_transformers import SentenceTransformer
import subprocess
import json

# Load FAISS index and chunks
index = faiss.read_index("data/faiss.index")
with open("data/sop_chunks.pkl", "rb") as f:
    chunks = pickle.load(f)

# model = SentenceTransformer('all-MiniLM-L6-v2')
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

def query_sop(question, top_k=3):
    """Return top SOP chunks relevant to the question"""
    q_vec = model.encode([question], convert_to_numpy=True)
    D, I = index.search(q_vec, top_k)
    results = [chunks[i] for i in I[0]]
    return results

# def generate_natural_response(question, sop_chunks):
#     """
#     Summarize SOP chunks using local Mistral (Ollama) to give
#     a concise, natural response.
#     """
#     # Combine top chunks
#     context = "\n".join(sop_chunks)

#     prompt = f"""
# You are an internal operations assistant. 
# Answer the following employee question concisely in natural language
# based on the SOP context. Do not copy full chunks. Be clear and short.

# SOP Context:
# \"\"\"{context}\"\"\"

# Question:
# \"\"\"{question}\"\"\"

# Answer in 2-3 sentences, actionable if possible.
# Only output the answer.
# """

#     try:
#         result = subprocess.run(
#             ["ollama", "run", "mistral"],
#             input=prompt,
#             capture_output=True,
#             text=True,
#             shell=True,
#             encoding="utf-8"
#         )
#         output = result.stdout.strip()
#         return output
#     except Exception as e:
#         print("Ollama summarization failed:", e)
#         return None

def generate_natural_response(user_query, sop_chunks):
    """
    Generates a concise, human-friendly SOP response using local Mistral model.
    """
    # Combine top SOP chunks into context
    context = "\n".join(sop_chunks)

    prompt = f"""
You are an internal operations assistant.
A staff member asked a question: "{user_query}"

You have the following SOP context to help answer:
{context}

Generate a concise, clear, and actionable answer in natural language.
Do not copy SOP verbatim; summarize in your own words.
"""

    try:
        result = subprocess.run(
            ["ollama", "run", "mistral"],
            input=prompt,
            capture_output=True,
            text=True,
            shell=True
        )
        answer = result.stdout.strip()
    except Exception as e:
        answer = "Sorry, I could not retrieve the SOP information at the moment."

    return answer
