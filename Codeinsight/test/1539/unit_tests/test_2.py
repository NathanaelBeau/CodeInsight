lst0 = [(1, 2, 3), (4, 5, 6)]
expected_result =  [(2, 1, 3), (5, 4, 6)]
result = test(lst0)
assert result == expected_result, 'Test failed'