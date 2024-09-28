import numpy as np
a = np.array([10, 20, 110, 120, 130])
expected_output = 0  # No numbers between 25 and 100
assert test(a,25,100) == expected_output, 'Test failed'