import pandas as pd
import numpy as np
df1 = pd.DataFrame({'A': [1, 2, np.nan, 4], 'B': [5, np.nan, 7, 8]})
expected_result_1 = pd.DataFrame({'A': [1.0, 2.0, 4.0], 'B': [5.0, np.nan, 8.0]}).reset_index(drop=True)
result_1 = test(df1, 'A').reset_index(drop=True)
assert result_1.equals(expected_result_1), 'Test failed'