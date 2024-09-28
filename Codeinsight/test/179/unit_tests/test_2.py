df = pd.DataFrame({'A': [0.1234, 0.5678], 'B': [100, 200]})
result = test(df, ['A'])
expected = pd.DataFrame({'A': ['12.34%', '56.78%'], 'B': [100, 200]})
assert result.equals(expected), 'Test failed'