import pandas as pd
df0 = pd.DataFrame({'A': [4, 5, 6], 'Value': [False, False, False]})
assert test(df0).empty, 'Test failed'