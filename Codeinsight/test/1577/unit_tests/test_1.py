lst0 = ['A:1', 'B:2', 'C:3', 'A:4']
expected_output = {'A': '4', 'B': '2', 'C': '3'}
assert test(lst0) ==expected_output, 'Test failed'