arr2 = np.array([10, 20, 30, 40])
var4 = 5
var5 = 10
expected_output_2 = np.array([ 5.,  6.66666667,  8.33333333, 10.])
assert np.allclose(test(arr2, var4, var5), expected_output_2), 'Test failed'