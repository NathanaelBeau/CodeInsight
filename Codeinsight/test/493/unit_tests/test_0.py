class DummyClass:
    a_string = "Hello, World!"
obj0 = DummyClass()
expected_result1 = "Hello, World!"
result1 = test(obj0)
assert result1 == expected_result1, 'Test failed'