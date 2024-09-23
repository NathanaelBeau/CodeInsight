lst0 = ['apple', 'banana', 'cherry', 'blueberry', 'coconut', 'avocado']
expected_output = {'a': ['apple', 'avocado'], 'b': ['banana', 'blueberry'], 'c': ['cherry', 'coconut']}
assert test(lst0) ==expected_output, 'Test failed'