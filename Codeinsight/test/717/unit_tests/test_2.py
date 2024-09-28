# Test 2
import pandas as pd
df0 = pd.DataFrame({'A': ['apple', 'banana', 'cherry'], 'B': ['dog', 'cat', 'fish']})
var0 = 'B'
var1 = '^c.*'
expected_result =  True
assert test(df0, var0, var1) == expected_result, 'Test failed'