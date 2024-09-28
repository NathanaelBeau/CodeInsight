import pandas as pd
# Test 2
df0 = pd.DataFrame({'A': ['apple', 'banana', 'cherry', 'dog'], 'B': ['dog', 'apple', 'fish', 'apple']})
var0 = 'B'
lst0 = ['dog', 'fish']
expected_result =  pd.DataFrame({'A': ['apple', 'cherry'], 'B': ['dog', 'fish']}, index=[0, 2])
assert test(df0, var0, lst0).equals(expected_result), 'Test failed'