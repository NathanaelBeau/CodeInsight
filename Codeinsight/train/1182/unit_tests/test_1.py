lst0 = ['a', 'b', 'a', 'c', 'c', 'b', 'b']
expected_result =  ['b', 'b', 'b', 'a', 'a', 'c', 'c']
result = test(lst0)
assert result == expected_result, 'Test failed'