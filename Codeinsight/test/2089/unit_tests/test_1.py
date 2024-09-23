df2 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
result_2 = test(df2, 2, 'A')
expected_2 = 3
assert result_2 == expected_2, 'Test failed'