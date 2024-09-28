data = { 'A': [1, 0, 0, 0, 0], 'B': [0, 2, 0, 0, 0], 'C': [0, 0, 3, 0, 0], 'D': [0, 0, 0, 4, 0], 'E': [0, 0, 0, 0, 5] }
df0 = pd.DataFrame(data)
expected_output = df0[['A', 'B', 'C', 'D', 'E']]
assert test(df0) .equals(expected_output), 'Test failed'