# Test 2
import pandas as pd
df0 = pd.DataFrame({'A': ['apple', 'banana', 'cherry', 'date', 'fig'], 'B': [100, 200, 300, 400, 500]})
col_name = 'A'
lst0 = ['banana', 'date']
expected_result =  pd.DataFrame({'A': ['banana', 'date'], 'B': [200, 400]})
result = test(df0, col_name, lst0).reset_index(drop=True)
assert result.equals(expected_result), 'Test failed'