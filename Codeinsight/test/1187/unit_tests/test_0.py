var0 = 4
var1 = 10
result = test(var0, var1)
expected = np.array([10, 10, 10, 10])
assert (result ==expected).all(), 'Test failed'