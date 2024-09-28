import pandas as pd
import numpy as np
df3 = pd.DataFrame({'A': [1, 2, 3, 4], 'B': [5, 6, 7, 8]})
expected_result_3 = df3  # No rows should be dropped
result_3 = test(df3, 'A')
assert result_3.equals(expected_result_3), 'Test failed'