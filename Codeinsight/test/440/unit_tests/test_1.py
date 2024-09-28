df0 = pd.DataFrame(columns=['A', 'B'])
df1 = pd.DataFrame(columns=['A', 'B'])
result = test(df0, df1)
expected = pd.DataFrame(columns=['A', 'B'])
assert result.equals(expected), 'Test failed'