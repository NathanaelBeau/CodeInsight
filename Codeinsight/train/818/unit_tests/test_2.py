df = pd.DataFrame({'A': [1, 2, 3], 'B': [4.0, 5.0, 6.0], 'C': ['seven', 'eight', 'nine']})
arg = (df, {'B': str})
expected_output = df.astype({'A': int, 'B': str, 'C': str})
assert test(*arg).equals(expected_output), 'Test failed'