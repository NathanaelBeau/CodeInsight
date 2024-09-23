import pandas as pd
var0 = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]], columns=['A', 'B', 'C'], index=[1, 1, 2])
expected_result =  pd.DataFrame([[5, 7, 9], [7,8,9]], columns=['A', 'B', 'C'], index=[1,2])
result = test(var0)
assert result.equals(expected_result), 'Test failed'