var0 = 5
var1 = 2
expected_output = pd.DataFrame(0, index=range(5), columns=range(2))
assert test(var0, var1).equals(expected_output), 'Test failed'