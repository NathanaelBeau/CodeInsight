import re

def test(str0):
    
    hashtags = re.findall(r'#(\w+)', str0, re.UNICODE)
    return hashtags

