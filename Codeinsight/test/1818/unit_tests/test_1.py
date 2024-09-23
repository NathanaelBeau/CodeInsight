import pandas as pd
df0 = pd.DataFrame({'A': ['1', '2', '3'], 'B': ['4', '5', '6']})
var0 = 'A'
expected_result =  pd.DataFrame(columns=['A', 'B'])
assert test(df0, var0).equals(expected_result), 'Test failed'