def test(var0):
    reversed_str = str(var0)[::-1]
    formatted_str = " ".join(reversed_str[i:i+3] for i in range(0, len(reversed_str), 3))
    formatted_str = formatted_str[::-1].replace('.', ',')
    return formatted_str

