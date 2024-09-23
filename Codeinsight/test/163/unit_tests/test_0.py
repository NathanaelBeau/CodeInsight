df1 = pd.DataFrame({ 'A': ['x', 'y', 'x', 'y', 'x', 'z'], 'B': [10, 20, 10, 20, 30, 40] })
key1 = 'A'
expected_result1 = pd.DataFrame({ 'A': ['x', 'y', 'z'], 'counts': [3, 2, 1] })
assert test(df1, key1).equals(expected_result1), 'Test failed'