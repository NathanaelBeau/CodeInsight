import pandas
import sklearn
arg = (pandas, sklearn)
expected_output = (pandas.__version__, sklearn.__version__)
assert test(*arg) == expected_output, 'Test failed'