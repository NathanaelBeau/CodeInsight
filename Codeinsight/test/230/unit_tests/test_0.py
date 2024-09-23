# Unit Test 1
lst0 = [(1, 2), (3, 1), (4, 3)]
expected_result =  [(4, 3), (1, 2), (3, 1)]
result = test(lst0)
assert result == expected_result, 'Test failed'