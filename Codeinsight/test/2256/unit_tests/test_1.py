arr1 = np.array([-5, 0, 5, 10])
var2 = -1
var3 = 1
expected_output_1 = np.array([-1.  ,       -0.33333333 , 0.33333333 , 1.        ])
assert np.allclose(test(arr1, var2, var3), expected_output_1), 'Test failed'