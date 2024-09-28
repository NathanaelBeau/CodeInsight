df3 = pd.DataFrame({ 'p': [25, 26, 27], 'q': [28, 29, 30], 'r': [31, 32, 33], 's': [34, 35, 36] })
lst0_3 = ['p', 'q', 'r', 's']
lst1_3 = ['s', 'q', 'p', 'r']
expected_output3 = pd.DataFrame({ 's': [34, 35, 36], 'q': [28, 29, 30], 'p': [25, 26, 27], 'r': [31, 32, 33] })
assert test(df3, lst0_3, lst1_3).equals(expected_output3), 'Test failed'