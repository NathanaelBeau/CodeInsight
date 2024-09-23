df0 = pd.DataFrame({'A': [7, 8, 9], 'B': [10, 11, 12]})
expected_result =  (3, 2)
result = test(df0)
assert result == expected_result, 'Test failed'