lst0 = [1, 2, 3]
lst1 = ['a', 'b', 'c']
expected_result =  pd.DataFrame({'List1': [1, 2, 3], 'List2': ['a', 'b', 'c']})
result = test(lst0, lst1)
assert result.equals(expected_result), 'Test failed'