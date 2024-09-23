df2 = pd.DataFrame({ 'X': ['a', 'b', 'c'], 'Y': [7, 8, 9] })
expected_result2 = pd.DataFrame({ 'X': ['a', 'b', 'c'], 'Y': [70, 8, 9] })
result2 = test(df2, 'X', 'a', 'Y', 70)
assert result2.equals(expected_result2), 'Test failed'