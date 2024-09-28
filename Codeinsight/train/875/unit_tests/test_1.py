# Test 3
import pandas as pd
df0 = pd.DataFrame({'A': ['apple', 'banana', 'cherry'], 'B': ['dog', 'cat', 'fish']})
var0 = 'A'
var1 = 'z.*'
expected_result =  False
assert test(df0, var0, var1) == expected_result, 'Test failed'