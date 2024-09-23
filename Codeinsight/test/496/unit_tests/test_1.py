var0 = ['A', 'B', 'C']
var1 = [
    np.array([1, 2, 3]),
    np.array([4, 5, 6]),
    np.array([7, 8, 9])
]
expected_output = pd.DataFrame({'A': var1[0], 'B': var1[1], 'C': var1[2]})
assert test(var0, *var1) .equals(expected_output), 'Test failed'