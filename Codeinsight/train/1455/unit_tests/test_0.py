my_dict = { 'A': [1, 2, 3, 4], 'B': [5, 6, 7, 8], 'C': [9, 10, 11, 12] }
lst = [3, 7, 15]
expected_output = ['A', 'B']
assert test(my_dict, lst) == expected_output, 'Test failed'