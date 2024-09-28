import numpy as np
a = np.array([26, 27, 28, 99, 101])
expected_output = 4  # All values except 101 are between 25 and 100
assert test(a,25,100) == expected_output, 'Test failed'