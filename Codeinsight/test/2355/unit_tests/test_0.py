df0 = pd.DataFrame({'A': [3, 1, 2], 'B': [6, 4, 5]}, index=[2, 0, 1])
expected_result =  pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]}, index=[0, 1, 2])
result = test(df0)
assert result.equals(expected_result), 'Test failed'