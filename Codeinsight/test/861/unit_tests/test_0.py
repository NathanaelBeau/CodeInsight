import numpy as np
a = np.array([10, 20, 30, 40, 110])
expected_output = 2  # 30 and 40 are the numbers between 25 and 100
assert test(a,25,100) == expected_output, 'Test failed'