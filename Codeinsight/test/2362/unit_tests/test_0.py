df0 = pd.DataFrame({ 'date_str': ['2022-05-09', '2022-05-10', '2022-05-11'] })
expected_output = pd.DataFrame({ 'date_str': [pd.Timestamp('2022-05-09'), pd.Timestamp('2022-05-10'), pd.Timestamp('2022-05-11')] })
assert test(df0, 'date_str').equals(expected_output), 'Test failed'