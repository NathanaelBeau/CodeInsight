data = { 'A': [0, 0, 0], 'B': [1, 0, 0], 'C': [0, 2, 0], 'D': [0, 0, 3] }
df0 = pd.DataFrame(data)
expected_output = df0[['B', 'C', 'D']]
assert test(df0) .equals(expected_output), 'Test failed'