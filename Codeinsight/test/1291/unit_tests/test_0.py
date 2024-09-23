df1 = pd.DataFrame({ 'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9], 'd': [10, 11, 12] })
lst0_1 = ['a', 'b', 'c', 'd']
lst1_1 = ['b', 'a', 'd', 'c']
expected_output1 = pd.DataFrame({ 'b': [4, 5, 6], 'a': [1, 2, 3], 'd': [10, 11, 12], 'c': [7, 8, 9] })
assert test(df1, lst0_1, lst1_1).equals(expected_output1), 'Test failed'