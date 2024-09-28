import pandas as pd
data = {'M': [], 'N': []}
df0 = pd.DataFrame(data)
var0 = 'M'
var1 = 'N'
expected_result =  0
result = test(df0, var0, var1)
assert result == expected_result, 'Test failed'