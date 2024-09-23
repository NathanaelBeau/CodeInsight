dict0 = {'1': 'One', '2': 'Two', '3': 'Three'}
dict1 = {'1': 'I', '2': 'II', '3': 'III'}
expected_output = {'One': 'I', 'Two': 'II', 'Three': 'III'}
assert test(dict0, dict1) ==expected_output, 'Test failed'