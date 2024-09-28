# Test 1
lists = [[1, 2, 3], [4, 5, 6]]
col_names = ['A', 'B']
expected_result =  pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
result = test(lists, col_names)
assert result.equals(expected_result), 'Test failed'