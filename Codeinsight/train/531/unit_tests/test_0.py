df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
expected_output1 = [{'index': 0, 'A': 1, 'B': 3}, {'index': 1, 'A': 2, 'B': 4}]
assert test(df1) == expected_output1, 'Test failed'