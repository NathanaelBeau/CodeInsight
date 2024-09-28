str0 = "^abc"
var0 = """abc first line
Not abc in this line
abc another start"""
expected_result =  ["abc", "abc"]
result = test(str0, var0)
assert result == expected_result, 'Test failed'