def test(var1):
        words = var1.split()
        if len(words) == 0:
            return 0
        return len(words[-1])