import pandas as pd
var1 = pd.DataFrame([['ny', 2, 3], ['sa', 5, 6], ['la', 8, 9]], columns=['city', 'A', 'B'])
var0 = 'city'
expected_result =  pd.DataFrame([['la', 8, 9], ['ny', 2, 3], ['sa', 5, 6]], columns=['city', 'A', 'B'])
result = test(var0, var1)
assert result.equals(expected_result), 'Test failed'