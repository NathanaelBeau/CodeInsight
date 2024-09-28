data = { 'column1': ['A', 'A', 'B', 'B', 'A', 'B'], 'column2': [1, 2, 1, 1, 2, 2], 'value': np.random.randint(1, 10, 6) }
df0 = pd.DataFrame(data)
var0 = ['column1', 'column2']
expected_output = pd.DataFrame({ 'count': [1, 2, 2, 1] }, index=pd.MultiIndex.from_tuples([('A', 1), ('A', 2), ('B', 1), ('B', 2)], names=['column1', 'column2']))
assert test(df0, var0).equals(expected_output), 'Test failed'