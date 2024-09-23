def test(var1):
    vowels = 'aeiou'
    return ''.join([ l for l in var1 if l not in vowels])
