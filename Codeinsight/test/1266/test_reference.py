def test(lst0, var0, var1):
    index0 = 0
    index1 = 0
    result = []
    for val in lst0:
        if val:
            if index0 < len(var0):
                result.append(var0[index0])
                index0 += 1
        else:
            if index1 < len(var1):
                result.append(var1[index1])
                index1 += 1
    return result