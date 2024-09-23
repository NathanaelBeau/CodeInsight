import pandas as pd
# Test 1
df0 = pd.DataFrame({'A': ['apple', 'banana', 'cherry', 'dog'], 'B': ['dog', 'apple', 'fish', 'apple']})
var0 = 'A'
lst0 = ['apple', 'banana']
expected_result =  pd.DataFrame({'A': ['apple', 'banana'], 'B': ['dog', 'apple']})
assert test(df0, var0, lst0).equals(expected_result), 'Test failed'