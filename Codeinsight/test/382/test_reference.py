from collections import Counter

def test(lst0, var0):
    word_counter = Counter(lst0)
    popular_words = sorted(word_counter, key=word_counter.get, reverse=True)
    top = popular_words[:var0]
    return top