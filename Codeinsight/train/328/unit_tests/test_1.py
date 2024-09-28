df2 = pd.DataFrame({ 'a': [13, 14, 15], 'b': [16, 17, 18], 'x': [19, 20, 21], 'y': [22, 23, 24] })
expected_output2 = pd.DataFrame({ 'x': [19, 20, 21], 'y': [22, 23, 24], 'a': [13, 14, 15], 'b': [16, 17, 18] })
assert test(df2).equals(expected_output2), 'Test failed'