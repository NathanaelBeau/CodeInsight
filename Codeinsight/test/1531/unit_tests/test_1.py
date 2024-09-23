result = test("Hello World! hello Universe!", "hello", "hi", True)
expected = "hi World! hi Universe!"
assert result == expected, 'Test failed'