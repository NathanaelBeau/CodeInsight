import pandas as pd
df0 = pd.DataFrame({'Gender': ['Male', 'Male', 'Male'], 'Year': [2014, 2014, 2014]})
expected_result =  df0
assert test(df0).equals(expected_result), 'Test failed'