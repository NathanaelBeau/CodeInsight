var0 = '20M10000N80M'
expected_output = (['20', '10000', '80'], ['M', 'N', 'M'])
assert test(var0) == expected_output, 'Test failed'