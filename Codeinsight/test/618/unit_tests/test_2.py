df0 = pd.DataFrame({'A': [13]}, index=['d'])
df2 = test(df0)
assert df2.empty and (df2.index == df0.index).all(), 'Test failed'