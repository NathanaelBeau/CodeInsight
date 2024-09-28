lst0 = [(1,1), (2,2)]
lst1 = [(1,1), (2,2)]
lst2 = []
expected_result =  [(2,2), (4,4)]
result = test(lst0, lst1, lst2)
assert result == expected_result, 'Test failed'