def test(dict1):
    return dict(sorted(dict1.items(),key=lambda x:x[0],reverse = True))