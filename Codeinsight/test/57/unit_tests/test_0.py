import pandas as pd 
df0 = pd.DataFrame()
expected_result =  pd.DataFrame()
result = test(df0)
assert result.equals(expected_result), 'Test failed'