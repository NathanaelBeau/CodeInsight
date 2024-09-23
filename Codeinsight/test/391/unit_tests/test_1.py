df2 = pd.DataFrame({'a': ['apple', 'banana', 'cherry'], 'b': [7, 8, 9]})
expected_output2 = ['apple', 'banana', 'cherry']
assert test(df2) == expected_output2, 'Test failed'