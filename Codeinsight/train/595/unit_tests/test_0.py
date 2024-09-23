df0 = pd.DataFrame({ 'ID': [1, 2, 3], 'Value': [10, 20, 30] })
var0 = 'ID'
expected_output = { 1: [10], 2: [20], 3: [30] }
assert test(df0, var0) ==expected_output, 'Test failed'