df1 = pd.DataFrame({'A': [10, 20, 30], 'B': [40, 50, 60]})
result_1 = test(df1, 0, 'A')
expected_1 = 10
assert result_1 == expected_1, 'Test failed'