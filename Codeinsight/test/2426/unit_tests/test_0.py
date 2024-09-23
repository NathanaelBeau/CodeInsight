str0 = "apple-orange-banana"
str1 = "-"
expected_result =  ["apple-orange", "banana"]
result = test(str0, str1)
assert result == expected_result, 'Test failed'