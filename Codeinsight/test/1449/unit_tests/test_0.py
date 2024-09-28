# Test 1
var0 = """A,B,C
1,2,3
4,5,6
"""
expected_result =  pd.DataFrame({ 'A': [1, 4], 'B': [2, 5], 'C': [3, 6] })
result = test(var0)
assert result.equals(expected_result), 'Test failed'