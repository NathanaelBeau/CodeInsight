lst0 = [(True, 0.1), (False, 0.9), (True, 0.5)]
expected_result =  [(False, 0.9), (True, 0.5), (True, 0.1)]
result = test(lst0)
assert result == expected_result, 'Test failed'