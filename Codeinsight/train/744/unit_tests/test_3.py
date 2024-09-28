import pandas as pd
var0 = pd.DataFrame([[1, 2, 3]], columns=['A', 'B', 'C'])
expected_result =  pd.DataFrame([[1, 2, 3]], columns=['A', 'B', 'C'])
result = test(var0)
assert result.equals(expected_result), 'Test failed'