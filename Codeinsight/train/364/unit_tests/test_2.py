def determine(x):
    return x == ""
lst0 = ["hello", "", "world", "", "python"]
var0 = determine
expected_output = ["hello", "world", "python"]
assert test(lst0, var0)==expected_output, 'Test failed'