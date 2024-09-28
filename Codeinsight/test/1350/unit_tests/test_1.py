lst0 = [4, 5, 6]
lst1 = ['d', 'e', 'f']
expected_result =  [4, 'd', 5, 'e', 6, 'f']
result = test(lst0, lst1)
assert result == expected_result, 'Test failed'