import re

def test(var0, var1, var2, var3):
    count = [0]
    
    def replace_match(match):
        count[0] += 1
        return var2 if count[0] == var3 else match.group(0)
    
    return re.sub(r'\b' + var1 + r'\b', replace_match, var0)

