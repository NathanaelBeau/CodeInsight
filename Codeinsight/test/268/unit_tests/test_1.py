lst0 = ['a', 'a', 'b', 'c', 'c', 'd', 'e', 'e', 'e']
expected_result =  [['a', 'a'], ['b'], ['c', 'c'], ['d'], ['e', 'e', 'e']]
result = test(lst0)
assert result == expected_result, 'Test failed'