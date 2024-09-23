import numpy as np
arr0 = np.array([7, 8])
arr1 = np.array([9, 10])
expected_output = np.array([7, 8, 9, 10])
assert np.array_equal(test(arr0, arr1), expected_output), 'Test failed'