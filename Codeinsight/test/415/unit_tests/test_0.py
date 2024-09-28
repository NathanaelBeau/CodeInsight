str0 = "hello 42.1 I'm a 32.1 string 30.1"
expected_output = ['42.1', '32.1', '30.1']
result = test(str0)
assert result == expected_output, 'Test failed'