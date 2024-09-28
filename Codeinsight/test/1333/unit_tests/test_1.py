# Test 3
lst0 = [('red', 1), ('blue', 2), ('green', 3)]
lst1 = ['blue', 'red', 'green']
expected_result =  [('blue', 2), ('red', 1), ('green', 3)]
result = test(lst0, lst1)
assert result == expected_result, 'Test failed'