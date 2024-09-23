def test(var1):
    vowels  = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U' ]
    return ''.join(list(filter(lambda x: x not in vowels, var1)))