def test(var1):
     vowels = "AEIOUaeiou"
     return ''.join('_' if c in vowels else c for c in var1)