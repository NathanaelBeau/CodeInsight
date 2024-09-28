# Test 3
var0 = """X,Y,Z
a,b,c
d,e,f
"""
expected_result =  pd.DataFrame({ 'X': ['a', 'd'], 'Y': ['b', 'e'], 'Z': ['c', 'f'] })
result = test(var0)
assert result.equals(expected_result), 'Test failed'