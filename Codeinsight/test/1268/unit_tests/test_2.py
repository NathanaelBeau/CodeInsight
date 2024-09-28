str0 = "Python\nis\nawesome"
expected_result =  ["Python", "is", "awesome"]
result = test(str0)
assert result == expected_result, 'Test failed'