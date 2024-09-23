df0 = pd.DataFrame({'m': [3, 1, 2], 'n': ['a', 'c', 'b']})
expected_output = pd.DataFrame({'m': [1, 2, 3], 'n': ['c', 'b', 'a']}).reset_index(drop=True)
assert test(df0).reset_index(drop=True).equals(expected_output), 'Test failed'