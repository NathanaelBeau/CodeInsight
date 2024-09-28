import pandas as pd
import numpy as np
df2 = pd.DataFrame({'A': [1, 2, 3, 4], 'B': [5, np.nan, 7, 8]})
expected_result_2 = df2  # No rows should be dropped since NaN is not in column 'A'
result_2 = test(df2, 'A')
assert result_2.equals(expected_result_2), 'Test failed'