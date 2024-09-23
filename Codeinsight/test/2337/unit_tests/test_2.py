import pandas as pd
trace_df2 = pd.DataFrame({'ratio': [0.1, 0.2, 0.3, 0.4]})
assert test(trace_df2) == 1, 'Test failed'