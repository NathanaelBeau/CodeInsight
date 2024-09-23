import pandas as pd
data = {}
df0 = pd.DataFrame(data)
expected_result =  pd.DataFrame()
result = test(df0)
assert result.equals(expected_result), 'Test failed'