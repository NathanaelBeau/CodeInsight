import pandas as pd
data = {'X': [10, 20, 30], 'Y': [0, 0, 0]}
df0 = pd.DataFrame(data)
var0 = 'X'
var1 = 'Y'
expected_result =  0
result = test(df0, var0, var1)
assert result == expected_result, 'Test failed'