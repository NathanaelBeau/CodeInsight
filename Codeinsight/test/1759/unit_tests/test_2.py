class YetAnotherClass:
    a_string = "Yet Another String"
obj0 = YetAnotherClass()
expected_result3 = "Yet Another String"
result3 = test(obj0)
assert result3 == expected_result3, 'Test failed'