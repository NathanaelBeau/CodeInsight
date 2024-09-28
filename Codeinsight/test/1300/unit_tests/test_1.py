import numpy as np
df0 = pd.DataFrame({ 'X': [10, 20, np.nan], 'Y': [np.nan, 50, 60] })
expected_result =  pd.DataFrame({ 'X': [10.0, 20.0, 15.0], 'Y': [55.0, 50.0, 60.0] })
assert test(df0).equals(expected_result), 'Test failed'