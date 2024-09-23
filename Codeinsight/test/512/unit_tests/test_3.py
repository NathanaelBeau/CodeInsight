input_str = "   hello   world   how   are   you   "
expected_result =  "hello world how are you"
result = test(input_str)
assert result==expected_result, 'Test failed'