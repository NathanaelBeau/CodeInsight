data = { 'Mt': ['A', 'A', 'B', 'B', 'C', 'C'], 'value': [10, 15, 25, 20, 5, 8] }
df0 = pd.DataFrame(data)
var0 = 'Mt'
var1 = 'value'
expected_output = df0.loc[[1, 2, 5]]
assert test(df0, var0, var1) .equals(expected_output), 'Test failed'