import re

def test(str0):
    float_regex = r'[\d]+[.,\d]+'
   
    floats = re.findall(float_regex, str0)
    
    return floats


