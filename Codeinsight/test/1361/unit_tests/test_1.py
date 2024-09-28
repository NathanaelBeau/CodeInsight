lst0 = [(10, 20), (30, 40), (50, 60)]
expected_output = [(20, 10), (40, 30), (60, 50)]
output = test(lst0)
assert output == expected_output, 'Test failed'