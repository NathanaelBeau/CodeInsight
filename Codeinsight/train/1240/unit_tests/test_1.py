str0 = "10.1,20,30.2"
expected_result =  [10.1, 20, 30.2]
result = test(str0)
assert result == expected_result, 'Test failed'