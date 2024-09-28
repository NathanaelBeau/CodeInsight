import pandas as pd
df0 = pd.DataFrame({'Gender': ['Male', 'Female', 'Male'], 'Year': [2014, 2015, 2014]})
expected_result =  pd.DataFrame({'Gender': ['Male', 'Male'], 'Year': [2014, 2014]}, index=[0, 2])
assert test(df0).equals(expected_result), 'Test failed'