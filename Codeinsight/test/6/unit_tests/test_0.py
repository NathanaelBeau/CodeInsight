df1 = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})
expected_output1 = [1, 2, 3]
assert test(df1) == expected_output1, 'Test failed'