lst0 = [(5, 10), (3, 15), (5, 8)]
expected_result =  [(5, 8), (5, 10), (3, 15)]
result = test(lst0)
assert result == expected_result, 'Test failed'