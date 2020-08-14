import uuid

def get_random_id():
    id = str(uuid.uuid4())[:8].replace('-','').lower()
    return id