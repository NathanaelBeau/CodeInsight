df0 = pd.DataFrame({'m': [8, 8, 9], 'n': ['u', 'v', 'w']})
expected_output = pd.DataFrame({'m': [8, 8, 9], 'n': ['u', 'v', 'w']})
assert test(df0).equals(expected_output), 'Test failed'