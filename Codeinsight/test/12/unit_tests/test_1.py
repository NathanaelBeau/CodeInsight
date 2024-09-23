lst0 = [['a', 'b'], ['c', 'd']]
expected_result =  [('a', 'c'), ('a', 'd'), ('b', 'c'), ('b', 'd')]
result = test(lst0)
assert result == expected_result, 'Test failed'