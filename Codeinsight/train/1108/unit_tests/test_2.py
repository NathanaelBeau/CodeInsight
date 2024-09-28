lst0 = [100, 200]
lst1 = ['A', 'B', 'C']
expected_result =  [100, 'A', 200, 'B']
result = test(lst0, lst1)
assert result == expected_result, 'Test failed'