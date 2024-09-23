set0 = {1, 2, 3, 4}
expected_result =  {(1, 2, 3), (1, 2, 4), (1, 3, 4), (2, 3, 4)}
result = test(set0)
assert result == expected_result, 'Test failed'