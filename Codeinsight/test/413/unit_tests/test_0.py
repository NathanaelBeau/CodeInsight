df1 = pd.DataFrame({'A': [10, 20, 30], 'B': [40, 50, 60]})
result_1 = test(df1, 1, 'B')
expected_1 = 50
assert result_1 == expected_1, 'Test failed'