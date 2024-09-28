import pandas as pd
var0 = pd.Series([1, 2, 3, 4, 5])
expected_result =  pd.Series([1, 2, 3, 4, 5])
result = test(var0)
assert result.equals(expected_result), 'Test failed'