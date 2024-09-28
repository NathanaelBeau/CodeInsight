df0 = pd.DataFrame({'X': [10, 20, 30], 'Y': [40, 50, 60]})
result = test(df0)
assert set(result['X']) == set(df0['X']) and set(result['Y']) == set(df0['Y']), 'Test failed'