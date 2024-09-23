import re 

def test(var0):
	return " ".join(re.findall("[a-zA-Z]+", var0))