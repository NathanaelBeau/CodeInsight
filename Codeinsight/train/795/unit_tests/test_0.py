str0 = "Hello (world) (test)"
expected_result =  "Hello world) test)"
result = test(str0)
assert result == expected_result, 'Test failed'