import numpy as np
df0 = pd.DataFrame({ 'P': [100, 200, 300], 'Q': [400, np.nan, 600] })
expected_result =  pd.DataFrame({ 'P': [100, 200, 300], 'Q': [400.0, 500.0, 600.0] })
assert test(df0).equals(expected_result), 'Test failed'