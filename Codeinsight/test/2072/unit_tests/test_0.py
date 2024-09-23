df0 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
expected_result =  pd.DataFrame({'A': [1, 3], 'B': [4, 6]}, index=[0, 2])
result = test(df0)
assert result.equals(expected_result), 'Test failed'