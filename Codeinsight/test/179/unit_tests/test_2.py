arg0 = '\t'
arg1 = "Tab\tSeparated\tText"
expected_output = ['Tab', 'Separated', 'Text']
assert test(arg0, arg1) == expected_output, 'Test failed'