df2 = pd.DataFrame({ 'w': [13, 14, 15], 'x': [16, 17, 18], 'y': [19, 20, 21], 'z': [22, 23, 24] })
lst0_2 = ['w', 'x', 'y', 'z']
lst1_2 = ['y', 'z', 'w', 'x']
expected_output2 = pd.DataFrame({ 'y': [19, 20, 21], 'z': [22, 23, 24], 'w': [13, 14, 15], 'x': [16, 17, 18] })
assert test(df2, lst0_2, lst1_2).equals(expected_output2), 'Test failed'