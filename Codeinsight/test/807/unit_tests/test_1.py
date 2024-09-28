set0 = {5, 6, 7, 8}
expected_result =  {(5, 6, 7), (8, 6, 7), (8, 5, 6), (8, 5, 7)}
result = test(set0)
assert result == expected_result, 'Test failed'