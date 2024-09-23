lst0 = [1, 2, 3, 4]
lst1 = [1, 2, 3, 5]
expected_result =  [True, True, True, False]
assert test(lst0, lst1) == expected_result, 'Test failed'