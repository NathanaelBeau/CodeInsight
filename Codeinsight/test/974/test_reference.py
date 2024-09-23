def test(lst0):
    s_words = sorted([word for word in lst0 if word.startswith('s')])
    non_s_words = sorted([word for word in lst0 if not word.startswith('s')])
    return s_words + non_s_words
