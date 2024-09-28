lst0 = [(1, 'a'), (2, 'b'), (3, 'c')]
expected_result =  [[1, 2, 3], ['a', 'b', 'c']]
result = test(lst0)
assert result == expected_result, 'Test failed'