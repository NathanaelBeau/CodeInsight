arg = pd.DataFrame({'A': [1, 2, 3], 'B': [4.0, 5.0, 6.0]})
expected_output = pd.Series({'A': int, 'B': float})
assert test(arg).equals(expected_output), 'Test failed'