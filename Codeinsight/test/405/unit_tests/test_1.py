lst0 = [[0.12345678, 0.87654321], [9.99999999, 3.14159265]]
expected_output = [['1.23456780e-01', '8.76543210e-01'], ['9.99999999e+00', '3.14159265e+00']]
assert test(lst0) == expected_output, 'Test failed'