def test(str0, str1):
    return sum(1 for i in range(len(str0) - len(str1) + 1) if str0[i:i+len(str1)].lower() == str1.lower())