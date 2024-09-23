lst0 = [1, 1, 1, 1]
lst1 = [1, 1, 1, 1]
lst2 = [1, 1, 1, 1]
lst3 = [1, 1, 1, 1]
var0 = ['a', 'b', 'c', 'd']
expected_output = ['a, b, c, d', 'a, b, c, d', 'a, b, c, d', 'a, b, c, d']
assert test(lst0, lst1, lst2, lst3, var0) ==expected_output, 'Test failed'