import redis

r = redis.Redis(host='localhost', port=6379, password='redis123', decode_responses=True)
keys = r.keys()

token_key = []
for key in keys:
    if key.islower() and len(key) == 36:
        token_key.append(key)

for token in token_key:
    r.delete(token)
