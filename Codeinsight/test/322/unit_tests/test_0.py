df0 = pd.DataFrame({'A': [1, 4, 3], 'B': [4, 5, 6], 'C': [7, 2, 9]})
expected_result =  pd.Series(['C', 'B', 'C'])
result = test(df0)
assert result.equals(expected_result), 'Test failed'