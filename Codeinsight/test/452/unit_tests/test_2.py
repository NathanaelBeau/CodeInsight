lst0 = [[1, 2, 3], [4, 5]]
expected_result =  [(1, 4), (1, 5), (2, 4), (2, 5), (3, 4), (3, 5)]
result = test(lst0)
assert result == expected_result, 'Test failed'