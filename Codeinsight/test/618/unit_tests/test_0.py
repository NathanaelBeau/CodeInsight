df0 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]}, index=['x', 'y', 'z'])
df2 = test(df0)
assert df2.empty and (df2.index == df0.index).all(), 'Test failed'