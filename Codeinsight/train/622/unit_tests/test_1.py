df2 = pd.DataFrame({'X': [7, 8, 9], 'Y': [10, 11, 12]})
expected_result2 = [[7, 10], [8, 11], [9, 12]]
result2 = test(df2)
assert result2 == expected_result2, 'Test failed'