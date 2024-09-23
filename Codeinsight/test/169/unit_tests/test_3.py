var0 = "Hello, 123\nworld!\nThis is\na test."
expected_result =  """Hello, 123
world!
This is a test."""
result = test(var0)
assert result == expected_result, 'Test failed'