import codecs

def test(var0):
    return codecs.encode(var0, 'unicode_escape').decode('utf-8')
