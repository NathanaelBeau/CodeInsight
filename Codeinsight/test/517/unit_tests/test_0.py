df0 = pd.DataFrame({'BrandName': ['ABC', 'DEF', 'AB', 'GHI', 'JKL']})
col0 = 'BrandName'
var0 = ['ABC', 'AB']
var1 = 'A'
expected_output = pd.DataFrame({'BrandName': ['A', 'DEF', 'A', 'GHI', 'JKL']})
assert test(df0, col0, var0, var1) .equals(expected_output), 'Test failed'