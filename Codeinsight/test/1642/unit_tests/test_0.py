df0 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
str0 = 'new_row'
lst0 = [5, 6]
expected_result =  pd.DataFrame({'A': [1, 2, 5], 'B': [3, 4, 6]}, index=[0, 1, 'new_row'])
result = test(df0.copy(), str0, lst0)
assert result.equals(expected_result), 'Test failed'