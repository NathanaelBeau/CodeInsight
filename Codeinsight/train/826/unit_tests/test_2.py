var0 = pd.DataFrame({'variable': [True, False, True, True, False]})
expected_output = pd.DataFrame({'variable': [False, True], 'counts': [2, 3]})
assert test(var0).equals(expected_output), 'Test failed'