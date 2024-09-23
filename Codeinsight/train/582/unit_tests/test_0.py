data = { 'A': [1, 2, 0, 4, 0], 'B': [0, 0, 0, 0, 0], 'C': [0, 3, 0, 5, 0], 'D': [0, 0, 0, 0, 0], 'E': [6, 0, 7, 0, 8] }
df0 = pd.DataFrame(data)
expected_output = df0[['A', 'C', 'E']]
assert test(df0) .equals(expected_output), 'Test failed'