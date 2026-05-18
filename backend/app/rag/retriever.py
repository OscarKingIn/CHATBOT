# simple placeholder RAG

documents = [
    "Atlas AI helps businesses automate customer support.",
    "We provide chatbot solutions with AI integration."
]

def get_context(query):
    for doc in documents:
        if query.lower() in doc.lower():
            return doc
    return ""