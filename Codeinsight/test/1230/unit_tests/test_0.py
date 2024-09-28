lst0 = [(1,2), (3,4)]
lst1 = [(5,6), (7,8)]
lst2 = []
expected_result =  [(6,8), (10,12)]
result = test(lst0, lst1, lst2)
assert result == expected_result, 'Test failed'