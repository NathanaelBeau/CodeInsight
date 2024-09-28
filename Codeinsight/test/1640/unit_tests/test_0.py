result = test("Hello World! hello Universe!", "hello", "hi", False)
expected = "Hello World! hi Universe!"
assert result == expected, 'Test failed'