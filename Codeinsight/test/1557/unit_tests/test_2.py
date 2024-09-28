import numpy
import pandas
arg = (numpy, pandas)
expected_output = (numpy.__version__, pandas.__version__)
assert test(*arg) == expected_output, 'Test failed'