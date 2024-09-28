str0 = 'apple,banana, cherry, date'
expected_output = ['apple,banana,', 'cherry,', 'date']
assert test(str0) == expected_output, 'Test failed'