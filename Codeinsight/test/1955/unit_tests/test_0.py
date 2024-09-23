str0 = "1,2,3,4.5,5.6"
expected_result =  [1, 2, 3, 4.5, 5.6]
result = test(str0)
assert result == expected_result, 'Test failed'