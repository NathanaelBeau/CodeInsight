df0 = pd.DataFrame({'col0': [3, 1, 2], 'col1': [6, 4, 5]})
expected_output = pd.DataFrame({'col0': [1, 2, 3], 'col1': [4, 5, 6]})
assert test(df0).values.tolist() == expected_output.values.tolist(), 'Test failed'