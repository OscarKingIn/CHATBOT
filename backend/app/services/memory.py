import redis
import json

r = redis.Redis(host="redis", port=6379, decode_responses=True)

def save_message(user_id, user_msg, bot_msg):
    key = f"chat:{user_id}"
    data = {"user": user_msg, "bot": bot_msg}
    r.rpush(key, json.dumps(data))

def get_history(user_id):
    key = f"chat:{user_id}"
    items = r.lrange(key, -10, -1)
    return [json.loads(i) for i in items]