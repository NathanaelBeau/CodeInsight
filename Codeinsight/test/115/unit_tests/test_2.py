lst0 = [(10, 30), (10, 28), (9, 40)]
expected_result =  [(10, 28), (10, 30), (9, 40)]
result = test(lst0)
assert result == expected_result, 'Test failed'