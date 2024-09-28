df0 = pd.DataFrame({'P': [13], 'Q': [14]}, index=[100])
expected_output = [100]
assert test(df0) == expected_output , 'Test failed'