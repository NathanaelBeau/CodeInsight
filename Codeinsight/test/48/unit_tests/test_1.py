import pandas as pd
data = {'a': [10, 20, 30, 40, 50],
        'b': [5, 15, 25, 35, 45]}
df0 = pd.DataFrame(data)
var0 = ['b']
var1 = [2, 3]
expected_output = pd.DataFrame({'b': [25.0, 35.0]}, index=var1)
output = test(df0, var0, var1)
output = output.round(2)
assert output.equals(expected_output), 'Test failed'