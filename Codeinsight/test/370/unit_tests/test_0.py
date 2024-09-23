lst0 = [(1, 1), (2, 0), (3, 1), (4, 1)]
expected_result =  [(1, 1), (3, 1), (4, 1)]
result = test(lst0)
assert result == expected_result, 'Test failed'