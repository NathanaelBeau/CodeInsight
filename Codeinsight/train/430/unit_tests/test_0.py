import pandas as pd
data = {'A': [1, 2, 3], 'B': [1, 1, 1]}
df0 = pd.DataFrame(data)
var0 = 'A'
var1 = 'B'
expected_result =  6
result = test(df0, var0, var1)
assert result == expected_result, 'Test failed'