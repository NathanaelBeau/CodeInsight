df0 = pd.DataFrame({'M': ['a', 'b', 'c'], 'N': ['d', 'e', 'f']})
result = test(df0)
assert set(result['M']) == set(df0['M']) and set(result['N']) == set(df0['N']), 'Test failed'