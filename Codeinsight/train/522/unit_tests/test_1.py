lst0 = ['apple', 'banana', 'orange', 'pear']
lst1 = ['banana', 'grape', 'pear']
expected_output = {'banana', 'pear'}
assert test(lst0, lst1) ==expected_output, 'Test failed'