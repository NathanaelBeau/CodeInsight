df0 = pd.DataFrame({'m': [5, 7, 6], 'n': ['x', 'z', 'y']})
expected_output = pd.DataFrame({'m': [5, 6, 7], 'n': ['x', 'y', 'z']}).reset_index(drop=True)
assert test(df0).reset_index(drop=True).equals(expected_output), 'Test failed'