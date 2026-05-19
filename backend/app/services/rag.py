from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings

embeddings = OpenAIEmbeddings()

vector_store = FAISS.load_local("faiss_index", embeddings)

def get_context(query):
    docs = vector_store.similarity_search(query, k=3)
    return "\n".join([d.page_content for d in docs])

def ingest_docs(texts):
    db = FAISS.from_texts(texts, embeddings)
    db.save_local("faiss_index")