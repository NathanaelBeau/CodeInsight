df2 = pd.DataFrame({ 'X': ['a', 'b', 'a', 'c', 'b', 'c', 'c'], 'Y': [1, 2, 1, 3, 2, 3, 3] })
key2 = 'X'
expected_result2 = pd.DataFrame({ 'X': ['a', 'b', 'c'], 'counts': [2, 2, 3] })
assert test(df2, key2).equals(expected_result2), 'Test failed'