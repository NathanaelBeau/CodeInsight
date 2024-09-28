lst0 = [1, 2, 3]
lst1 = [True, False, True]
expected_result =  {1: True, 2: False, 3: True}
result = test(lst0, lst1)
assert result == expected_result, 'Test failed'