def determine(x):
    return x > 5
lst0 = [2, 6, 8, 3, 7, 1, 9]
var0 = determine
expected_output = [2, 3, 1]
assert test(lst0, var0)==expected_output, 'Test failed'