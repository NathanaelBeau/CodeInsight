from collections import Counter

def test(var0):
    words = var0.split()
    bigrams = [(words[i], words[i+1]) for i in range(len(words)-1)]
    return Counter(bigrams)
