df0 = pd.DataFrame({ 'date_str': ['2022-05-09 13:45:00', '2022-05-10 14:15:00', '2022-05-11 15:30:00'] })
expected_output = pd.DataFrame({ 'date_str': [pd.Timestamp('2022-05-09 13:45:00'), pd.Timestamp('2022-05-10 14:15:00'), pd.Timestamp('2022-05-11 15:30:00')] })
assert test(df0, 'date_str').equals(expected_output), 'Test failed'