tuple0 = (10, 20)
tuple1 = (-10, -20)
expected_result =  (0, 0)
result = test(tuple0, tuple1)
assert result == expected_result, 'Test failed'