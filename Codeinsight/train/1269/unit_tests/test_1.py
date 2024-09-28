lst0 = ['apple_1_2', 'apple_2_2', 'banana_1_1', 'banana_2_1', 'cherry_1_2']
expected_output = [['apple_1_2', 'apple_2_2'], ['banana_1_1', 'banana_2_1'], ['cherry_1_2']]
assert test(lst0) ==expected_output, 'Test failed'