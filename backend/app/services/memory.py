memory_store = {}

def get_history(user_id):
    return memory_store.get(user_id, [])

def save_message(user_id, user_msg, bot_msg):
    if user_id not in memory_store:
        memory_store[user_id] = []

    memory_store[user_id].append({
        "user": user_msg,
        "bot": bot_msg
    })