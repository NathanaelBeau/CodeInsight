import numpy as np
arr0 = np.array([[7, 0], [6, -1], [5, -2]])
expected_result =  np.array([[5, -2], [6, -1], [7, 0]])
assert np.array_equal(test(arr0), expected_result), 'Test failed'