# Test 1
lst0 = [[1, 2], [3, 4]]
expected_result =  [(1, 3), (1, 4), (2, 3), (2, 4)]
result = test(lst0)
assert result == expected_result, 'Test failed'