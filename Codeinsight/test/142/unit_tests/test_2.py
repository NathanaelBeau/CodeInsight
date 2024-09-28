import numpy as np 
var0 = np.array([[1, 1, 1], [2, 2, 2], [3, 3, 3]])
expected_result =  np.array([[-1.22474487, -1.22474487, -1.22474487],
                           [0., 0., 0.],
                           [1.22474487, 1.22474487, 1.22474487]])
result = test(var0)
assert np.allclose(result, expected_result), 'Test failed'