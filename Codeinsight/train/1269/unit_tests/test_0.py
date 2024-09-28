lst0 = ['abc_1_2', 'abc_2_2', 'hij_1_1', 'xyz_1_2', 'xyz_2_2']
expected_output = [['abc_1_2', 'abc_2_2'], ['hij_1_1'], ['xyz_1_2', 'xyz_2_2']]
assert test(lst0) ==expected_output, 'Test failed'