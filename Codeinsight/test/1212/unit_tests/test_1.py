lst0 = ['a', 'b', 'c']
lst1 = ['b', 'c', 'd']
expected_result =  ['a']
result = test(lst0, lst1)
assert result == expected_result, 'Test failed'