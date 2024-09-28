df0 = pd.DataFrame({'BrandName': ['ABC', 'DEF', 'AB', 'GHI', 'JKL']})
col0 = 'BrandName'
var0 = ['XYZ']
var1 = 'X'
expected_output = pd.DataFrame({'BrandName': ['ABC', 'DEF', 'AB', 'GHI', 'JKL']})
assert test(df0, col0, var0, var1) .equals(expected_output), 'Test failed'