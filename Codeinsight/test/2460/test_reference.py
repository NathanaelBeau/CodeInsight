from operator import itemgetter

def test(var0):
    return max(var0.items(), key=itemgetter(1))[0]
