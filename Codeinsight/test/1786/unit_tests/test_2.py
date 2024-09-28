# Test 2
df0 = pd.DataFrame({'A': ['cat', 'bat', 'rat'], 'B': ['one', 'two', 'three']})
var0 = 'A'
var1 = r'at$'
expected_result =  pd.DataFrame({'A': ['cat', 'bat', 'rat'], 'B': ['one', 'two', 'three']})
assert test(df0, var0, var1).equals(expected_result), 'Test failed'