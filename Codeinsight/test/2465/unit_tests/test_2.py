df0 = pd.DataFrame({ 'data_prefix': [10, 20, 30], 'other_data_column': [40, 50, 60], 'column_suffix_1': [70, 80, 90] })
str0= '_prefix'
expected_output = pd.DataFrame({ 'other_data_column': [40, 50, 60], 'column_suffix_1': [70, 80, 90] })
assert test(df0, str0) .equals(expected_output), 'Test failed'