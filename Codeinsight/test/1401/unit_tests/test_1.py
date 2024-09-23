var0 = 10
var1 = 1
result = test(var0, var1)
expected = np.array([1, 1, 1, 1 ,1, 1 ,1, 1,1, 1])
assert (result ==expected).all(), 'Test failed'