df3 = pd.DataFrame({ 'A': [1, 0, 0], 'B': [0, 1, 0], 'C': [0, 0, 1] })
expected_result3 = (1, 1)
assert test(df3) == expected_result3, 'Test failed'