lst0 = [(7, 20), (8, 10), (8, 15)]
expected_result =  [(8, 10), (8, 15), (7, 20)]
result = test(lst0)
assert result == expected_result, 'Test failed'