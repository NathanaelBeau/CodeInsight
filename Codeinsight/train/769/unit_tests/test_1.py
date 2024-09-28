import pandas as pd
data = {'X': [10, 20, 30], 'Y': [40, 50, 60]}
df0 = pd.DataFrame(data, index=[100, 200, 300])
expected_result =  pd.DataFrame({'X': [10, 20, 30], 'Y': [40, 50, 60]}, index=[100, 200, 300])
result = test(df0)
assert result.equals(expected_result), 'Test failed'