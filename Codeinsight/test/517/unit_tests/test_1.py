df0 = pd.DataFrame({'BrandName': ['ABC', 'DEF', 'AB', 'GHI', 'JKL']})
col0 = 'BrandName'
var0 = ['DEF', 'GHI']
var1 = 'D'
expected_output = pd.DataFrame({'BrandName': ['ABC', 'D', 'AB', 'D', 'JKL']})
assert test(df0, col0, var0, var1) .equals(expected_output), 'Test failed'