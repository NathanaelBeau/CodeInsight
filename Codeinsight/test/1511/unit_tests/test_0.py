df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
expected_output1 = [{'A': 1, 'B': 3}, {'A': 2, 'B': 4}]
assert test(df1) == expected_output1, 'Test failed'