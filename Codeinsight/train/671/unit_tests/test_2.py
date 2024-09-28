import pandas as pd
def multiply_and_add(row, factor=3, constant=2):
    return row['value'] * factor + constant
var0 = multiply_and_add
var1 = 'result'
df0 = pd.DataFrame({'value': [1, 2, 3]})
expected_result =  pd.DataFrame({'value': [1, 2, 3], 'result': [5, 8, 11]})
result = test(var0, var1, df0)
assert result.equals(expected_result), 'Test failed'