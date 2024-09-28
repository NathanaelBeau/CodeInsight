def determine(x):
    return x % 2 == 0
lst0 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
var0 = determine
expected_output = [1, 3, 5, 7, 9]
assert test(lst0, var0)==expected_output, 'Test failed'