df_input = pd.DataFrame({ 'A': ['apple', 'banana', 'apple', 'apple', 'banana', 'cherry'], 'B': ['red', 'yellow', 'red', 'green', 'yellow', 'red'] })
expected_output = pd.DataFrame({ 'A': ['apple', 'apple', 'banana', 'cherry'], 'B': ['green', 'red', 'yellow', 'red'], 'counts': [1, 2, 2, 1] })
result = test(df_input, ['A', 'B'])
assert result.equals(expected_output), 'Test failed'