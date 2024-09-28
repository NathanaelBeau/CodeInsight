import pandas as pd
data = {'P': [100, 200, 300], 'Q': [1, 0, 1]}
df0 = pd.DataFrame(data)
var0 = 'P'
var1 = 'Q'
expected_result =  400
result = test(df0, var0, var1)
assert result == expected_result, 'Test failed'