import pandas as pd
df = pd.DataFrame({'year': [2021, 2022, 2022], 'month': [12, 1, 2], 'day': [31, 1, 15]})
expected_result =  pd.DataFrame({'year': [2021, 2022, 2022], 'month': [12, 1, 2], 'day': [31, 1, 15]})
result = test(df)
assert result.equals(expected_result), 'Test failed'