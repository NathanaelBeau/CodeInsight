import numpy as np 
var0 = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
expected_result =  np.array([[0., 0., 0.],
                           [0., 0., 0.],
                           [0., 0., 0.]])
result = test(var0)
assert np.allclose(result, expected_result), 'Test failed'