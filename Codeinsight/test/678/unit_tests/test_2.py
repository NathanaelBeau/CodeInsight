df = pd.DataFrame({'A': [1, 2, 3], ('col1', 'col2'): [None, None, None], 'B': [4, 5, 6]})
expected_output = True
result = test(df)
assert result == expected_output, 'Test failed'