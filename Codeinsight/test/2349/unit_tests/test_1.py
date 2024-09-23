import numpy as np
import pandas as pd
df2 = pd.DataFrame({ 'X': [np.nan, np.nan, np.nan], 'Y': [np.nan, np.nan, np.nan] })
expected_result2 = pd.DataFrame({ 'X': [0.0, 0.0, 0.0], 'Y': [0.0, 0.0, 0.0] })
assert test(df2).equals(expected_result2), 'Test failed'