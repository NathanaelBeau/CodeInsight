var0 = """This is a text
with multiple lines
and several newlines."""
expected_result =  ['\n', '\n']
result = test(var0)
assert result == expected_result, 'Test failed'