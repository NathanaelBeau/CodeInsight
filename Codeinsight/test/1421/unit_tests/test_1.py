lst0 = [4, 5]
lst1 = ['d', 'e']
expected_result =  pd.DataFrame({'List1': [4, 5], 'List2': ['d', 'e']})
result = test(lst0, lst1)
assert result.equals(expected_result), 'Test failed'