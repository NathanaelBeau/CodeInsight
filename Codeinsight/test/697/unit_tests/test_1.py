import pandas as pd
import numpy as np
df1 = pd.DataFrame({'A': [1, 2, np.nan], 'B': [4, np.nan, 6]})
assert test(df1) == True, 'Test failed'