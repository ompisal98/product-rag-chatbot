import os
import pandas as pd
import chromadb

from dotenv import load_dotenv
from groq import Groq
from sentence_transformers import SentenceTransformer

# -----------------------------
# 1. Load environment variables
# -----------------------------
load_dotenv()

groq_client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# -----------------------------
# 2. Load product dataset
# -----------------------------
CSV_PATH = "data/cleaned_rag_pipeline.csv"

df = pd.read_csv(CSV_PATH, engine="python")

# Apne CSV ke columns yahan likhna
TEXT_COLUMNS = ["question", "answer"]

documents = []

for _, row in df.iterrows():
    text = " ".join(
        str(row[col])
        for col in TEXT_COLUMNS
        if col in df.columns
    )

    documents.append(text)

print(f"Loaded {len(documents)} documents")

# -----------------------------
# 3. Create embeddings
# -----------------------------
embedding_model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

embeddings = embedding_model.encode(
    documents
).tolist()

# -----------------------------
# 4. Store in ChromaDB
# -----------------------------
chroma_client = chromadb.PersistentClient(
    path="./chroma_db"
)

collection = chroma_client.get_or_create_collection(
    name="product_knowledge"
)

# Avoid duplicate IDs
collection.upsert(
    ids=[f"doc_{i}" for i in range(len(documents))],
    documents=documents,
    embeddings=embeddings
)

print("Knowledge base ready!")

# -----------------------------
# 5. Retrieve relevant documents
# -----------------------------
def retrieve_context(question, top_k=3):

    query_embedding = embedding_model.encode(
        [question]
    ).tolist()

    results = collection.query(
        query_embeddings=query_embedding,
        n_results=top_k
    )

    return results["documents"][0]


# -----------------------------
# 6. Generate answer using Groq
# -----------------------------
def generate_answer(question, context):
    prompt = f"""
    You are a helpful product customer service chatbot.
    Answer the user's question using only the provided context.

    Context:
    {context}

    User question:
    {question}

    If the answer is not in the context, say:
    "Sorry, I don't have enough information about that product."
    """

    response = groq_client.chat.completions.create(
    model="openai/gpt-oss-20b",
    messages=[
        {"role": "user", "content": prompt}
    ],
    temperature=0
)

    return response.choices[0].message.content


# -----------------------------
# 7. Chatbot loop
# -----------------------------
print("\nProduct Customer Service Chatbot")
print("Type 'exit' to stop.\n")

while True:

    question = input("You: ")

    if question.lower() == "exit":
        break

    context = retrieve_context(question)

    answer = generate_answer(question, context)

    print("Bot:", answer)
    print()