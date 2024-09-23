lst0 = ['apple', 'banana', 'orange', 'grape']
dict0 = {'apple': 3, 'banana': 1, 'orange': 2, 'grape': 4}
expected_output = ['banana', 'orange', 'apple', 'grape']
assert test(lst0, dict0) ==expected_output, 'Test failed'