import pandas as pd
trace_df0 = pd.DataFrame({'ratio': [0.5, -0.2, 0.7, 0, 1]})
assert test(trace_df0) == 0.6, 'Test failed'