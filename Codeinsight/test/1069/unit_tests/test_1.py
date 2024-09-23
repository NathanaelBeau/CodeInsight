# Test 3
lst0 = [[1, 2, 3], ['a', 'b']]
expected_result =  [(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b'), (3, 'a'), (3, 'b')]
result = test(lst0)
assert result == expected_result, 'Test failed'