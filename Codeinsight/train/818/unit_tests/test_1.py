lst0 = ["x", "y", "z"]
var0 = 3
expected_output = ['xyz', 'xzy', 'yxz', 'yzx', 'zxy', 'zyx']
assert test(lst0, var0) ==expected_output, 'Test failed'