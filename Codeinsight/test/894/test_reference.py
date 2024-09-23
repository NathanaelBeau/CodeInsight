def test(str0, str1):
    if any(str1 in s for s in str0):
        matching = [s for s in str0 if str1 in s]
        return matching
 
