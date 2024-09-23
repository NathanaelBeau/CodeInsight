lst0 = ['a', 'b', 'c', 'd']
lst1 = [4, 3, 2, 1]
expected_result =  ['d', 'c', 'b', 'a']
result = test(lst0, lst1)
assert result == expected_result, 'Test failed'