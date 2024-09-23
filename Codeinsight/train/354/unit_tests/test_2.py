lst0 = [['a', 'b'], ['c', 'd', 'e']]
expected_result =  [['e', 'd', 'c'], ['b', 'a']]
result = test(lst0)
assert result == expected_result, 'Test failed'