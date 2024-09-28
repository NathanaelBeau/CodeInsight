df3 = pd.DataFrame({ 'a': [25, 26, 27], 'b': [28, 29, 30], 'x': [31, 32, 33], 'y': [34, 35, 36] })
expected_output3 = pd.DataFrame({ 'x': [31, 32, 33], 'y': [34, 35, 36], 'a': [25, 26, 27], 'b': [28, 29, 30] })
assert test(df3).equals(expected_output3), 'Test failed'