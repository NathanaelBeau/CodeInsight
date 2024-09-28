arg = pd.DataFrame({'A': [1, 2, 3], 'B': ['one', 'two', 'three']})
expected_output = {'A': {0: 1, 1: 2, 2: 3}, 'B': {0: 'one', 1: 'two', 2: 'three'}}
assert test(arg) == expected_output, 'Test failed'