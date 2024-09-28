lst0 = ['a', 'b', 'c']
lst1 = [1, 2, 3]
expected_result =  {'a': 1, 'b': 2, 'c': 3}
result = test(lst0, lst1)
assert result == expected_result, 'Test failed'