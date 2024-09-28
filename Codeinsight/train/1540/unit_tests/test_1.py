df0 = pd.DataFrame({ 'prefix_1_data': [100, 200, 300], 'prefix_2_data': [400, 500, 600], 'suffix_column': [700, 800, 900] })
str0 = '_data'
expected_output = pd.DataFrame({ 'suffix_column': [700, 800, 900] })
assert test(df0, str0) .equals(expected_output), 'Test failed'