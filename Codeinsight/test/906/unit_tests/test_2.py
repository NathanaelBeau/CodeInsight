import pandas as pd
var0 = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]], columns=['A', 'B', 'C'], index=[1, 1, 1])
expected_result =  pd.DataFrame([[12, 15, 18]], columns=['A', 'B', 'C'], index=[1])
result = test(var0)
assert result.equals(expected_result), 'Test failed'