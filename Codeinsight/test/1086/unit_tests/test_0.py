# Test 1
df0 = pd.DataFrame({ 'Group': ['A', 'A', 'B', 'B', 'C', 'C'], 'Value': [10, 20, 30, 25, 50, 55] })
var0 = 'Group'
var1 = 'Value'
expected_result =  pd.DataFrame({ 'Group': ['A', 'B', 'C'], 'Value': [20, 30, 55] }, index=[1,2,5])
result = test(df0, var0, var1)
assert result.equals(expected_result), 'Test failed'