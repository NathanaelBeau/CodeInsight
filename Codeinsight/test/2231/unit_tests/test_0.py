import pandas as pd
df = pd.DataFrame({'year': [2022], 'month': [1], 'day': [1]})
expected_result =  pd.DataFrame({'year': [2022], 'month': [1], 'day': [1]})
result = test(df)
assert result.equals(expected_result), 'Test failed'