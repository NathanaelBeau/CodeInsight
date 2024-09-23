df0 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
result = test(df0)
assert set(result['A']) == set(df0['A']) and set(result['B']) == set(df0['B']), 'Test failed'