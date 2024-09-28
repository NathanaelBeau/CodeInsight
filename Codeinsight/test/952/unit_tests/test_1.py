dict0 = {'apple': 'red', 'banana': 'yellow', 'grape': 'purple'}
dict1 = {'red': 'fruit', 'yellow': 'fruit', 'purple': 'fruit'}
expected_output = {'apple': 'fruit', 'banana': 'fruit', 'grape': 'fruit'}
assert test(dict0, dict1) ==expected_output, 'Test failed'