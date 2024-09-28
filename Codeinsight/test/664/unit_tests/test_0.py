lst0 = [1, 2, 3]
lst1 = ['a', 'b', 'c']
expected_result =  [1, 'c', 2, 'b', 3, 'a']
assert test(lst0, lst1) == expected_result, 'Test failed'