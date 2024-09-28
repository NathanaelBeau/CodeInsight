import numpy as np
arr0 = np.array([11])
arr1 = np.array([12, 13, 14])
expected_output = np.array([11, 12, 13, 14])
assert np.array_equal(test(arr0, arr1), expected_output), 'Test failed'