import pandas as pd 
df0 = pd.DataFrame({'A': [1, 2], 'B': [3, 4], 'C': [5, 6]})
var0 = 1
expected_result =  pd.Series([3, 4], name='B')
result = test(df0, var0)
assert result.equals(expected_result), 'Test failed'