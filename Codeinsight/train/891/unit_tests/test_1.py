lst0 = [10, 20, 30]
lst1 = ['X', 'Y', 'Z']
expected_output = ([30, 20, 10], ['Z', 'Y', 'X'])
assert test(lst0, lst1) == expected_output, 'Test failed'