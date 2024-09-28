class AnotherClass:
    a_string = "Another String Example"
obj0 = AnotherClass()
expected_result2 = "Another String Example"
result2 = test(obj0)
assert result2 == expected_result2, 'Test failed'