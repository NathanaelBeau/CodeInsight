data = { 'col1': [1, 2, 3, 4], 'col2': [1, -1, 1, -1], 'col3': [1, 1, -1, -1], 'col4': [-1, -1, -1, -1], 'col5': [-1, -1, -1, -1] }
df0 = pd.DataFrame(data)
col = 2
arg0 = -1
expected_output = df0[df0.iloc[:, col] == arg0]
assert test(df0, arg0, col, col+1).equals(expected_output), 'Test failed'