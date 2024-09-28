data = {'P': [9, 5, 1], 'Q': [8, 4, 0], 'R': [7, 3, -1]}
df0 = pd.DataFrame(data)
expected_output = pd.DataFrame({'P': [9, 5, 1], 'Q': [8, 4, 0], 'R': [7, 3, -1]})
assert test(df0).equals(expected_output), 'Test failed'