lst0 = [1, 2, 3, 2, 2, 3, 1, 2, 4, 2]
var0 = 2
var1 = "apple"
expected_output = [1, 'apple', 3, 'apple', 'apple', 3, 1, 'apple', 4, 'apple']
assert test(lst0, var0, var1) ==expected_output, 'Test failed'