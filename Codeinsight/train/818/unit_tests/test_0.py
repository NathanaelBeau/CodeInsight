df = pd.DataFrame({'A': [1, 2, 3], 'B': [4.0, 5.0, 6.0], 'C': ['seven', 'eight', 'nine']})
arg = (df, {'A': float, 'B': int, 'C': str})
expected_output = df.astype({'A': float, 'B': int, 'C': str})
assert test(*arg).equals(expected_output), 'Test failed'