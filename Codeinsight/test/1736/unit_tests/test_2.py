df0 = pd.DataFrame({ 'prod_type': ['respon', 'r', 'other', 'respon'] })
var0 = 'prod_type'
dict0 = {'other': 'othertype'}
expected_output = pd.DataFrame({ 'prod_type': ['respon', 'r', 'othertype', 'respon'] })
assert test(df0, var0, dict0) .equals(expected_output), 'Test failed'