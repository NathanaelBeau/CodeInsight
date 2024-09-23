data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
df0 = pd.DataFrame(data)
expected_data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
expected_output = pd.DataFrame(expected_data)
assert test(df0) .equals(expected_output), 'Test failed'