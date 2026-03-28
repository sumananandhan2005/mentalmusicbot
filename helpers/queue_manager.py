queues = {}

def get_queue(chat_id):
    return queues.setdefault(chat_id, [])

def add_to_queue(chat_id, url, title):
    get_queue(chat_id).append({"url": url, "title": title})

def pop_queue(chat_id):
    q = get_queue(chat_id)
    return q.pop(0) if q else None

def clear_queue(chat_id):
    queues[chat_id] = []

def queue_list(chat_id):
    return get_queue(chat_id)
