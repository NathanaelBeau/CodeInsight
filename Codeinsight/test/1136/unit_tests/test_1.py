lst0 = [True, False, True, False, True]
expected_result =  [True, False, False, True]
result = test(lst0)
assert result == expected_result, 'Test failed'