col0 = 'team'
df0 = pd.DataFrame({'team': ['red sox', 'yankees', 'dodgers']})
expected_output = pd.DataFrame({'team': ['RED SOX', 'YANKEES', 'DODGERS']})
assert test(df0, col0).equals(expected_output), 'Test failed'