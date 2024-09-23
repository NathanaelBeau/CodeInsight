df0 = pd.DataFrame({'col1': [1, 2, 3], 'col2': [4, 5, 6]})
expected_output = ['0', '1', '2']
assert test(df0) ==expected_output, 'Test failed'