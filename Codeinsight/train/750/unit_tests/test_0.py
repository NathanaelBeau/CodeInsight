df0 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
expected_result =  (3, 2)
result = test(df0)
assert result == expected_result, 'Test failed'