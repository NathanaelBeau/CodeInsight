df0 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
expected_result =  [1, 3, 2, 4]
result = test(df0)
assert result == expected_result, 'Test failed'