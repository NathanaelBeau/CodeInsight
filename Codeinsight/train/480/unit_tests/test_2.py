var0 = "Hello,\nworld!\nThis is\na test."
expected_result =  """Hello,
world!
This is a test."""
result = test(var0)
assert result == expected_result, 'Test failed'