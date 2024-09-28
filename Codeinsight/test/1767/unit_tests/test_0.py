str0 = "hello"
expected_result =  sorted(['h', 'e', 'l', 'o'])
result = sorted(test(str0))
assert result==expected_result, 'Test failed'