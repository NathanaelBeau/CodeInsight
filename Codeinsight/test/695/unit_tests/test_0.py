import pandas as pd
def multiply_values(row):
    return row['value'] * 2
var0 = multiply_values
var1 = 'result'
df0 = pd.DataFrame({'value': [1, 2, 3]})
expected_result =  pd.DataFrame({'value': [1, 2, 3], 'result': [2, 4, 6]})
result = test(var0, var1, df0)
assert result.equals(expected_result), 'Test failed'