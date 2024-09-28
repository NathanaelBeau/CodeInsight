str0 = "Show details1\nShow details2\nShow details3\nShow details4\nShow details5\n"
expected_output = ['show details1', 'show details2', 'show details3', 'show details4', 'show details5']
assert test(str0) ==expected_output, 'Test failed'