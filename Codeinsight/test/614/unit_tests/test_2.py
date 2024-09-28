df2 = pd.DataFrame({'P': [100, 200, 300], 'Q': [400, 500, 600]})
lst0 = ['P', 'Q']
expected_output2 = pd.DataFrame({'P': [100, 200, 300], 'Q': [400, 500, 600], 'sum': [500, 700, 900]})
assert test(df2, lst0).equals(expected_output2), 'Test failed'