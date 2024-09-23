tuple0 = (-1, -2, -3)
tuple1 = (1, 2, 3)
expected_result =  (0, 0, 0)
result = test(tuple0, tuple1)
assert result == expected_result, 'Test failed'