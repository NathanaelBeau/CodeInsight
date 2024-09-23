from collections import Counter

def test(lst0):
    words_to_count = (word for word in lst0 if word.isalpha())
    c = Counter(words_to_count)
    return c.most_common()