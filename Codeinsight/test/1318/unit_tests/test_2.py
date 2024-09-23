df0 = pd.DataFrame({'col1': [], 'col2': []})
str0 = 'first_row'
lst0 = [50, 60]
expected_result =  pd.DataFrame({'col1': [50], 'col2': [60]}, index=['first_row'])
result = test(df0.copy(), str0, lst0)
assert result.equals(expected_result), 'Test failed'