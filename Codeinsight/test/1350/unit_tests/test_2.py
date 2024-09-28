lst0 = [7, 8]
lst1 = ['g', 'h', 'i']
expected_result =  [7, 'g', 8, 'h', 'i']
result = test(lst0, lst1)
assert result == expected_result, 'Test failed'