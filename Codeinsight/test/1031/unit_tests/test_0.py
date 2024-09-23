df1 = pd.DataFrame({ 'A': [0, 1, 2], 'B': [3, 0, 4], 'C': [5, 0, 0] })
expected_result1 = (1.0, 0.8)
assert test(df1) == expected_result1, 'Test failed'