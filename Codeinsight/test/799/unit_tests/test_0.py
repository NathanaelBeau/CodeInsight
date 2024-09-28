var0 = pd.DataFrame({'variable': [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]})
expected_output = pd.DataFrame({'variable': [1, 2, 3, 4], 'counts': [1, 2, 3, 4]})
assert test(var0).equals(expected_output), 'Test failed'