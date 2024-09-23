import pandas as pd
def square_value(row):
    return row['value'] ** 2
var0 = square_value
var1 = 'result'
df0 = pd.DataFrame({'value': []})
expected_result =  pd.DataFrame({'value': [], 'result': []})
result = test(var0, var1, df0)
assert result.equals(expected_result), 'Test failed'