df = pd.DataFrame({'A': [1, 2, 3], ('col1', 'col2'): [10.0, 20.0, 30.0], 'B': [4, 5, 6]})
expected_output = False
result = test(df)
assert result == expected_output, 'Test failed'