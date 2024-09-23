import re

def test(var0):
    def repl(match):
        return '' if len(match.group(0)) >= 3 else match.group(0)
    
    return re.sub(r'(.)\1*', repl, var0)

