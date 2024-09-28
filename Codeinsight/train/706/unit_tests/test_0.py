var0 = pd.DataFrame({'variable': [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]})
expected_output = pd.Series({4: 4, 3: 3, 2: 2, 1: 1}, name='variable')
assert test(var0).equals(expected_output), 'Test failed'