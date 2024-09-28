df = pd.DataFrame({'A': [10], 'B': [20], 'C': [30]})
result = test(df, axis0=1)
expected = pd.DataFrame({'A': [-10.0], 'B': [0.0], 'C': [10.0]})
assert result.equals(expected), 'Test failed'