dict_test_3 = {'a': [], 'b': '', 'c': []}
result_3 = test(dict_test_3)
expected_3 = 3  # 3 keys + 0 total items
assert result_3 == expected_3, 'Test failed'