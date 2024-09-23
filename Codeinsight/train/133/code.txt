def test(var1):
    return ''.join(x for x in (i.lower() if i.isupper() else i.upper() for i in var1))