df0 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
operation = 'mean'
expected_result =  3.5
result = test(df0, operation)
assert result == expected_result, 'Test failed'