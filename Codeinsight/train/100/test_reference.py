def test(var1, var2):
    if len(var2) > len(var1):
        return 'Notfound'

    for i in range(len(var1)):

        for j in range(len(var2)):

            if var1[i + j] == var2[j] and j == len(var2) - 1:
                return i
                
            elif var1[i + j] != var2[j]:
                break

    return 'Notfound'
