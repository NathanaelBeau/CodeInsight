import pandas as pd
df0 = pd.DataFrame({ 'color': ['red', 'green', 'blue', 'yellow'], 'value': [100, 200, 300, 400] })
var0 = 'color'
var1 = 'green'
expected_result3 = pd.DataFrame({ 'color': ['red', 'blue', 'yellow'], 'value': [100, 300, 400] }, index=[0, 2, 3])
result3 = test(df0, var0, var1)
assert result3.equals(expected_result3), 'Test failed'