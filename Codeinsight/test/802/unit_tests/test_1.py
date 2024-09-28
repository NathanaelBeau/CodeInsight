df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
result = test(df, axis0=1)
expected = pd.DataFrame({'A': [-1.5, -1.5, -1.5], 'B': [1.5, 1.5, 1.5]})
assert result.equals(expected), 'Test failed'