dict0 = {'x': 'apple', 'y': 'banana', 'z': 'apple'}
expected_result =  {'apple': ['x', 'z']}
assert test(dict0) == expected_result, 'Test failed'