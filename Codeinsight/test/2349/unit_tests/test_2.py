import numpy as np
df3 = pd.DataFrame({'P': [11, 12], 'Q': [13, 14]})
expected_result3 = pd.DataFrame({'P': [11, 12], 'Q': [13, 14]})  # No NaN values to replace
result3 = test(df3)
assert result3.equals(expected_result3), 'Test failed'