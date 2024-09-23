var0 = 3
var1 = 4
expected_output = pd.DataFrame(0, index=range(3), columns=range(4))
assert test(var0, var1).equals(expected_output), 'Test failed'