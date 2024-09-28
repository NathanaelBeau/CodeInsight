import pandas as pd
df0 = pd.DataFrame({'id': [True, False], 'value': [0, 1]})
expected_result =  {True: 0, False: 1}
assert test(df0) == expected_result, 'Test failed'