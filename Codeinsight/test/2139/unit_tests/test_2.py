str0 = "^abc"
var0 = """abc first line
Not abc in this line
abc another start"""
expected_result =  ["abc", "abc"]
assert test(str0, var0) == expected_result, 'Test failed'