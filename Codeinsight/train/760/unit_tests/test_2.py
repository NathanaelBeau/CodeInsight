lst0 = ['a', 'b', 'c', 'd']
lst1 = ['a', 'e', 'f', 'g']
expected_result =  ['a', 'b', 'c', 'd']
result = test(lst0, lst1)
assert result == expected_result, 'Test failed'