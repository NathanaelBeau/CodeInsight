def test(lst0):
    return ' '.join([word for i, word in enumerate(lst0) if word not in lst0[:i]])
