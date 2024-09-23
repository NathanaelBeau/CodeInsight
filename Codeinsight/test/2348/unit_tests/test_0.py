import pandas as pd
var0 = 'A'
var1 = pd.DataFrame([[1, 2, 3], [1, 5, 6], [1, 8, 9]], columns=['A', 'B', 'C'])
expected_result =  pd.DataFrame([[1, 15, 18]], columns=['A', 'B', 'C'])
result = test(var0, var1)
assert result.equals(expected_result), 'Test failed'