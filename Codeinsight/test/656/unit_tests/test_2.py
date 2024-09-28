lst0 = [[], [1, 2], [2, 2, 2]]
expected_result =  [True, False, True]
result = test(lst0)
assert result == expected_result, 'Test failed'