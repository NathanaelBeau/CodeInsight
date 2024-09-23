import hashlib

def test(var0, var1):
    hashed = hashlib.sha256(var0.encode()).hexdigest()
    truncated_hash = hashed[:var1]
    return truncated_hash