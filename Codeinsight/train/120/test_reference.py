def test(dict1):
    return {k :v for k,v in sorted(dict1.items(),key = lambda x : x[1],reverse = True)}