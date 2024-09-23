lst0 = ['hel', 'lo', 'bye']
expected_result =  sorted(['hello', 'helbye', 'lobye', 'lohel', 'byehel', 'byelo'])
result = sorted(test(lst0))
assert result == expected_result, 'Test failed'