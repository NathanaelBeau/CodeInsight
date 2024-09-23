set0 = {9, 10, 11, 12}
expected_result =  {(9, 10, 11), (9, 10, 12), (9, 11, 12), (10, 11, 12)}
result = test(set0)
assert result == expected_result, 'Test failed'