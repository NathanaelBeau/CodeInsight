mylist = ['hello', 'hellomy', 'helpme', 'world', 'worlds']
expected_output = [['hello', 'hellomy'], ['helpme'], ['world', 'worlds']]
assert test(mylist) == expected_output, 'Test failed'