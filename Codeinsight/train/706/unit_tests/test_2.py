var0 = pd.DataFrame({'variable': [True, False, True, True, False]})
expected_output = pd.Series({True: 3, False: 2}, name='variable').sort_index()
assert test(var0).sort_index().equals(expected_output), 'Test failed'