df0 = pd.DataFrame({'A': [1, 2, 3, 4]})
expected_result =  []
result = test(df0)
assert result == expected_result, 'Test failed'