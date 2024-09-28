lst0 = [1, 2, 3]
lst1 = ['a', 'b', 'c']
expected_result =  [1, 'a', 2, 'b', 3, 'c']
result = test(lst0, lst1)
assert result == expected_result, 'Test failed'