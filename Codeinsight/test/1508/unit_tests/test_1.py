df = pd.DataFrame(columns=['A', 'B'])
columns = ['A', 'B']
result = test(df, columns)
expected = pd.DataFrame(columns=['A', 'B'])
assert result.equals(expected), 'Test failed'