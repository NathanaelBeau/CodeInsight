import numpy as np
import pandas as pd
df1 = pd.DataFrame({ 'A': [1, 2, np.nan], 'B': [4, np.nan, 6] })
expected_result1 = pd.DataFrame({ 'A': [1, 2, 0.0], 'B': [4, 0.0, 6] })
assert test(df1).equals(expected_result1), 'Test failed'