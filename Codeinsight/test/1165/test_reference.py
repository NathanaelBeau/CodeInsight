import re
def test(dict1):
    def key_func(k):
        parts = re.split(r'(\d+)', k) # split key into non-digit and digit parts
        return [int(part) if part.isdigit() else part for part in parts] # convert digit parts to int, leave non-digit parts as str
    return sorted(dict1.keys(), key=key_func)


