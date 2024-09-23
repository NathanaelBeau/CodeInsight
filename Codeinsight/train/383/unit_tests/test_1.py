import pandas as pd
df0 = pd.DataFrame({'Gender': ['Male', 'Female', 'Male'], 'Year': [2013, 2015, 2016]})
expected_result =  df0[(df0['Gender'] == 'Non-existent') & (df0['Year'] == 9999)]
assert test(df0).equals(expected_result), 'Test failed'