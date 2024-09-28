df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
result = test(df, axis0=0)
expected = pd.DataFrame({'A': [-1.0, 0.0, 1.0], 'B': [-1.0, 0.0, 1.0]})
assert result.equals(expected), 'Test failed'