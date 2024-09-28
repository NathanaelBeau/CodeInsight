df2 = pd.DataFrame({'X': [5, 6, 7], 'Y': [8, 9, 10]})
expected_result2 = pd.DataFrame({ 'X': [5, 5, 5, 6, 6, 6, 7, 7, 7], 'Y': [8, 8, 8, 9, 9, 9, 10, 10, 10] })
result2 = test(df2, 3)
assert result2.equals(expected_result2), 'Test failed'