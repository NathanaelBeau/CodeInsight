df0 = pd.DataFrame({'A': [7, 8, 9], 'B': [10, 11, 12]}, index=['a', 'b', 'c'])
df2 = test(df0)
assert df2.empty and (df2.index == df0.index).all(), 'Test failed'