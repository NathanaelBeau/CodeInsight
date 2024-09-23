def test(var0):
        while var0:
            if var0 % 10 == 0:
                var0 //= 10
            else:
                break
        var0 = str(var0)
        lst = list(var0)
        lst.reverse()
        var0 = "".join(lst)
        var0 = int(var0)
        return var0