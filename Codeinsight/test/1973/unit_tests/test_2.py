lst0 = ['1_for_2', '3_and_4', '5_or_6']
expected_output = [['1', '2'], ['3', '4'], ['5', '6']]
assert test(lst0) ==expected_output, 'Test failed'