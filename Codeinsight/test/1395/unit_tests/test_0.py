lst0 = [1, 2, 3, 4, 5]
lst1 = [10, 20, 30, 40, 50]
lst2 = [100, 200, 300, 400, 500]
lst3 = [1000, 2000, 3000, 4000, 5000]
lst4 = [10000, 20000, 30000, 40000, 50000]
lst5 = [100000, 200000, 300000, 400000, 500000]
expected_output = True
assert test(lst0, lst1, lst2, lst3, lst4, lst5) == expected_output, 'Test failed'