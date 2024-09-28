import pandas as pd
df0 = pd.DataFrame({ 'A': [10, 20, 30, 40], 'B': [5, 6, 7, 8] })
var0 = 'A'
var1 = 10
expected_result2 = pd.DataFrame({ 'A': [20, 30, 40], 'B': [6, 7, 8] }, index=[1, 2, 3])
result2 = test(df0, var0, var1)
assert result2.equals(expected_result2), 'Test failed'