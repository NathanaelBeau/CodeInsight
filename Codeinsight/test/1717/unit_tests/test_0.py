import numpy as np
arr0 = np.array([[3, 2], [1, 4], [5, 3]])
expected_result =  np.array([[3, 2], [5, 3], [1, 4]])
assert np.array_equal(test(arr0), expected_result), 'Test failed'