import pandas as pd
trace_df1 = pd.DataFrame({'ratio': [-0.2, -0.5, 0, -1]})
assert test(trace_df1) == 0, 'Test failed'