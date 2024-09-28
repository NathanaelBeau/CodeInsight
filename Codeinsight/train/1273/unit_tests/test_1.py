df0 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
result = test(df0.copy(), 'A', 1, 'B')
assert result.equals(pd.DataFrame({'A': [1, 2, 3], 'B': [1, 5, 6]})), 'Test failed'