data = { 'col1': [1, 2, 3, 4], 'col2': [1, -1, 1, -1], 'col3': [1, 1, -1, -1], 'col4': [-1, -1, -1, -1], 'col5': [0, 0, 0, 0], 'col6': [0, 0, 0, 0], 'col7': [0, 0, 0, 0], 'col8': [0, 0, 0, 0], 'col9': [0, 0, 0, 0], 'col10': [0, 0, 0, 0], 'col11': [-1, 1, -1, 1], 'col12': [-1, -1, -1, -1] }
df0 = pd.DataFrame(data)
col = 5
col2 = 11
arg0 = 0
expected_output = df0[(df0.iloc[:, col:col2] == arg0).any(axis=1)]
assert test(df0, arg0, col, col2).equals(expected_output), 'Test failed'