lst0 = [100, 200, 300, 400]
lst1 = ['one', 'two', 'three', 'four']
expected_output = {100: 'one', 200: 'two', 300: 'three', 400: 'four'}
assert test(lst0, lst1) ==expected_output, 'Test failed'