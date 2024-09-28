import numpy as np
var0 = pd.DataFrame({'A': [1, 2.0, np.nan]})
col0 = 'A'
expected_result =  var0.astype(str)
result = test(var0, col0)
assert result.equals(expected_result), 'Test failed'