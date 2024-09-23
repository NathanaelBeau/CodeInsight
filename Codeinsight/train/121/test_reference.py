def test(var1):
    counts = dict()
    words = var1.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts
