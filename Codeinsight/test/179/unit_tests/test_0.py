df = pd.DataFrame({'A': [0.1234, 0.5678], 'B': [0.1111, 0.2222]})
columns = ['A', 'B']
result = test(df, columns)
expected = pd.DataFrame({'A': ['12.34%', '56.78%'], 'B': ['11.11%', '22.22%']})
assert result.equals(expected), 'Test failed'