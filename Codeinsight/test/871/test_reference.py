import random
import string


def test(var0):
    return ''.join(random.choice(string.ascii_lowercase) for x in range(var0))

