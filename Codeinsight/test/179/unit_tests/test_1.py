arg0 = '\s+'
arg1 = "This is a test string"
expected_output = ['This', 'is', 'a', 'test', 'string']
assert test(arg0, arg1) == expected_output, 'Test failed'