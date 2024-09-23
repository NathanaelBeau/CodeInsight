var0 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
lst0 = [7, 8, 9]
expected_result =  pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'new_column': [7, 8, 9]})
result = test(var0, lst0)
assert result.equals(expected_result), 'Test failed'