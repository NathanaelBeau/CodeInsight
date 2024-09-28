data = { 'Group': ['X', 'X', 'Y', 'Y', 'Y', 'Z'], 'Value': [5.6, 3.8, 7.2, 6.9, 8.1, 4.5] }
df0 = pd.DataFrame(data)
var0 = 'Group'
var1 = 'Value'
expected_output = df0.loc[[0, 4, 5]]
assert test(df0, var0, var1) .equals(expected_output), 'Test failed'