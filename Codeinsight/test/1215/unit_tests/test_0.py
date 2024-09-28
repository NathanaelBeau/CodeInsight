buckets = ['abcdefghijkl', 'mnopqrstuvwx', 'yz1234567890']
var0 = 2
var1 = 5
expected_output = ['cde', 'opq', '123']
assert test(buckets, var0, var1) == expected_output, 'Test failed'