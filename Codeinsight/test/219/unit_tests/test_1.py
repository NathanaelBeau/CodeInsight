var0 = ("a", "b")
var1 = ("c",)
expected_output=("a", "b", (("c",)))
assert test(var0,var1) ==expected_output, 'Test failed'