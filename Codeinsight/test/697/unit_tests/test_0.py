import pandas as pd
import numpy as np
df0 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
assert test(df0) == False, 'Test failed'