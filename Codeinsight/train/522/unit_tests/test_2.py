dict0 = {'X': 'X-ray', 'Y': 'Yogurt', 'Z': 'Zebra'}
dict1 = {'X': 10, 'Y': 20, 'Z': 30}
expected_output = {'X-ray': 10, 'Yogurt': 20, 'Zebra': 30}
assert test(dict0, dict1) ==expected_output, 'Test failed'