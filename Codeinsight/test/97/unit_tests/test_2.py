lst0 = ['car', 'bus', 'bicycle', 'train', 'truck', 'motorcycle']
expected_output = {'b': ['bicycle', 'bus'], 'c': ['car'], 'm': ['motorcycle'], 't': ['train', 'truck']}
assert test(lst0) ==expected_output, 'Test failed'