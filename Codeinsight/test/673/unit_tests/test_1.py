lst0 = [('a', 'b'), ('c', 'd'), ('e', 'f')]
expected_result =  [['a', 'c', 'e'], ['b', 'd', 'f']]
result = test(lst0)
assert result == expected_result, 'Test failed'