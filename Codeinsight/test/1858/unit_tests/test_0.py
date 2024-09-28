var0 = ['x', 'y', 'z']
var1 = [
    np.array([10, 20, 30]),
    np.array([40, 50, 60]),
    np.array([70, 80, 90])
]
expected_output = pd.DataFrame({'x': var1[0], 'y': var1[1], 'z': var1[2]})
assert test(var0, *var1) .equals(expected_output), 'Test failed'