str0 = b'@#$%^&*()'
expected_output = ['@', '#', '$', '%', '^', '&', '*', '(', ')']
assert test(str0) == expected_output, 'Test failed'