test_set_2 = {0, -1, -2, -3, 3}
result_2 = test(test_set_2)
expected_2 = [-3, -2, -1, 0, 3]
assert result_2 == expected_2, 'Test failed'