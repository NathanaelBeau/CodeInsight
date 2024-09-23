df = pd.DataFrame({'A': [0.1234, 0.5678], 'B': [0.1111, 0.2222]})
result = test(df, [])
assert result.equals(df), 'Test failed'