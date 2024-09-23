from collections import Counter

def test(lst0):
    word_counter = Counter(lst0)
    popular_words = sorted(word_counter, key=word_counter.get, reverse=True)
    top_3 = popular_words[:3]
    return top_3
