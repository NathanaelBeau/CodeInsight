df0 = pd.DataFrame({ 'column1_prefix': [1, 2, 3], 'column2_prefix': [4, 5, 6], 'other_column': [7, 8, 9] })
str0 = '_prefix'
expected_output = pd.DataFrame({ 'other_column': [7, 8, 9] })
assert test(df0, str0) .equals(expected_output), 'Test failed'