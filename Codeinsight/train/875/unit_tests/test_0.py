import pandas as pd
# Test 1
df0 = pd.DataFrame({'A': ['apple', 'banana', 'cherry'], 'B': ['dog', 'cat', 'fish']})
var0 = 'A'
var1 = 'a.p'
expected_result =  True
assert test(df0, var0, var1) == expected_result, 'Test failed'