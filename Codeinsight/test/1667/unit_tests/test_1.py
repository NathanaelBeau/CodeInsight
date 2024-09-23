df0 = pd.DataFrame({ 'col1': ['10', '20'] })
var0 = 'col1'
var1 = 'int32'
expected_result =  pd.DataFrame({ 'col1': [10, 20] }, dtype='int32')
assert test(df0.copy(), var0, var1).equals(expected_result), 'Test failed'