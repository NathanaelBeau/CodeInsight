def test(var1, var2):
    multidimensional_list = []
    for i in range(var1):
        multidimensional_list.append([])

        for j in range(var2):
             multidimensional_list[i].append(0)

    return multidimensional_list