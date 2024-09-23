df0 = pd.DataFrame({ 'col1': [1, 2, 3], 'col2': [4, 5, 6], 'col3': [7, 8, 9] })
lst0 = ['col1', 'col2', 'col1']
expected_output = pd.DataFrame({ 'col3': [7, 8, 9] })
assert test(df0, lst0) .equals(expected_output), 'Test failed'