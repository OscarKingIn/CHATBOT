import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_response(message, history, context):
    messages = [
        {"role": "system", "content": "You are an AI assistant."},
    ]

    # Add context (RAG)
    if context:
        messages.append({
            "role": "system",
            "content": f"Context: {context}"
        })

    # Add history
    for h in history:
        messages.append({"role": "user", "content": h["user"]})
        messages.append({"role": "assistant", "content": h["bot"]})

    messages.append({"role": "user", "content": message})

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages
    )

    return response.choices[0].message.content