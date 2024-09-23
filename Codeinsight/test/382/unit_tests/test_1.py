import numpy
import sklearn
arg = (numpy, sklearn)
expected_output = (numpy.__version__, sklearn.__version__)
assert test(*arg) == expected_output, 'Test failed'