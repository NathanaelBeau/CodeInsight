# Test 2
var0 = """Name,Age,Grade
John,10,A
Jane,12,B
"""
expected_result =  pd.DataFrame({ 'Name': ['John', 'Jane'], 'Age': [10, 12], 'Grade': ['A', 'B'] })
result = test(var0)
assert result.equals(expected_result), 'Test failed'