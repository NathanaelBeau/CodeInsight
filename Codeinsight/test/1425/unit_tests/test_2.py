import pandas as pd
data = {'P': [100, 200, 300], 'Q': [400, 500, 600]}
df0 = pd.DataFrame(data, index=[1, 1, 2])
expected_result =  pd.DataFrame({'P': [100, 300], 'Q': [400, 600]}, index=[1, 2])
result = test(df0)
assert result.equals(expected_result), 'Test failed'