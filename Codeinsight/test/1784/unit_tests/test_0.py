lst0 = ['a', 'b', 'c', 'd']
lst1 = [True, False, True, False]
expected_result =  ['a', 'c']
result = test(lst0, lst1)
assert result == expected_result, 'Test failed'