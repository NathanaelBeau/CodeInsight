import pandas as pd
df0 = pd.DataFrame({ 'A': ['apple', 'banana', 'cherry', 'apple'], 'B': [1, 2, 3, 4] })
var0 = 'A'
var1 = 'apple'
expected_result1 = pd.DataFrame({ 'A': ['banana', 'cherry'], 'B': [2, 3] }, index=[1, 2])
result1 = test(df0, var0, var1)
assert result1.equals( expected_result1), 'Test failed'