def test(var1):
    vowels = "aeiou"
    return sum(char in vowels for char in var1)