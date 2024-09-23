df2 = pd.DataFrame({ 'A': [0, 0, 0], 'B': [0, 1, 0], 'C': [0, 0, 2] })
expected_result2 = (1.5, 1.5)
assert test(df2) == expected_result2, 'Test failed'