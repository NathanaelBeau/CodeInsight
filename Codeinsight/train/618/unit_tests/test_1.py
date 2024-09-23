lst0 = ['3', '4', '5']
var0 = 'Y'
var1 = 3
expected_output = {3: ['Y'], 4: ['Y', 'Y'], 5: ['Y', 'Y', 'Y'], 6: ['Y', 'Y'], 7: ['Y']}
assert test(lst0, var0, var1) ==expected_output, 'Test failed'