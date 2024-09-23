df0 = pd.DataFrame({ 'prod_type': ['respon', 'r', 'other'] })
var0 = 'prod_type'
dict0 = {'respon': 'responsive', 'r': 'responsive'}
expected_output = pd.DataFrame({ 'prod_type': ['responsive', 'responsive', 'other'] })
assert test(df0, var0, dict0) .equals(expected_output), 'Test failed'