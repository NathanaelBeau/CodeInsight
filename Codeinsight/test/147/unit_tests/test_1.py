import pandas as pd
# Test 3
df0 = pd.DataFrame({'A': ['apple', 'banana', 'cherry', 'dog'], 'B': ['dog', 'apple', 'fish', 'apple']})
var0 = 'A'
lst0 = ['grape', 'orange']
expected_result =  pd.DataFrame(columns=['A', 'B'])
assert test(df0, var0, lst0).equals(expected_result), 'Test failed'