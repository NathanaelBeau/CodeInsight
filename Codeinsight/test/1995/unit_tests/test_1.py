col0 = 'city'
df0 = pd.DataFrame({'city': ['new york', 'los angeles', 'chicago']})
expected_output = pd.DataFrame({'city': ['NEW YORK', 'LOS ANGELES', 'CHICAGO']})
assert test(df0, col0).equals(expected_output), 'Test failed'