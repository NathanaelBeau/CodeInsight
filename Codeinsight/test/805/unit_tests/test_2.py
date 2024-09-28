lst0 = [4, 5, 6]
lst1 = [1, 2, 3]
expected_result =  [(4, 1), (4, 2), (4, 3), (5, 1), (5, 2), (5, 3), (6, 1), (6, 2), (6, 3)]
result = test(lst0, lst1)
assert result == expected_result, 'Test failed'