lst0 = [1, 2, 3, 4]
lst1 = [False, False, True, True]
expected_result =  [3, 4]
result = test(lst0, lst1)
assert result == expected_result, 'Test failed'