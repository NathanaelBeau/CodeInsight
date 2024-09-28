dict0 = {'a': (2, 4), 'b': (5, 1), 'c': (7, 3)}
expected_result =  {'b': (5, 1), 'c': (7, 3), 'a': (2, 4)}
result = test(dict0)
assert result == expected_result, 'Test failed'