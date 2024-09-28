import pandas as pd
df0 = pd.DataFrame({'A': ['apple', '1234', 'cherry', '56dog'], 'B': ['dog', '789', 'fish', '345']})
var0 = 'B'
expected_result =  pd.DataFrame({'A': ['apple', 'cherry'], 'B': ['dog', 'fish']}, index=[0,2])
assert test(df0, var0).equals(expected_result), 'Test failed'