lst0 = ['cat', 'dog', 'elephant', 'camel', 'lion', 'zebra']
expected_output = {'c': ['camel', 'cat'], 'd': ['dog'], 'e': ['elephant'], 'l': ['lion'], 'z': ['zebra']}
assert test(lst0) ==expected_output, 'Test failed'