import numpy as np
var0 = pd.DataFrame({'A': ['-', 14, 15], 'B': [16, 17, 18]})
expected_result =  pd.DataFrame({'A': [np.nan, 14., 15.], 'B': [16., 17., 18.]})
result = test(var0)
assert result.equals(expected_result), 'Test failed'