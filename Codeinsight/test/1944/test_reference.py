def test(str0):
    list1 = []
    for word in str0.split():
        if word[0].isupper():
            list1.append(word)
    return list1

