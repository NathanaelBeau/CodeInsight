import numpy as np
df0 = pd.DataFrame({ 'A': [1, np.nan, 3], 'B': [4, 5, np.nan] })
expected_result =  pd.DataFrame({ 'A': [1.0, 2.0, 3.0], 'B': [4.0, 5.0, 4.5] })
assert test(df0).equals(expected_result), 'Test failed'