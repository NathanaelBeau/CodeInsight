import re

def test(str0):
    comma_regex = r'[\d]+[.,\d]+' 
   
    comma= re.findall(comma_regex, str0)
    
    return comma


