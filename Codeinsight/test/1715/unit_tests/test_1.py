data = {'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]}
df0 = pd.DataFrame(data)
expected_output = pd.DataFrame({'A': [7, 8, 9], 'B': [4, 5, 6], 'C': [1, 2, 3]})
assert test(df0).equals(expected_output), 'Test failed'