df0 = pd.DataFrame({'P': [10, 20, 20, 30, 30, 30], 'Q': [10, 10, 20, 20, 30, 30], 'R': [10, 20, 30, 40, 50, 60]})
lst0 = ['P', 'Q', 'R']
expected_result =  df0.drop_duplicates()
assert test(df0, lst0).equals(expected_result), 'Test failed'