import numpy as np
arr0 = np.array([[1, 10], [2, 9], [3, 8]])
expected_result =  np.array([[3, 8], [2, 9], [1, 10]])
assert np.array_equal(test(arr0), expected_result), 'Test failed'