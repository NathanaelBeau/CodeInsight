def test(str0, str1):
    matching = [s for s in str0 if any(xs in s for xs in str1)]
    return matching
