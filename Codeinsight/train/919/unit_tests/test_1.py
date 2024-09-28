str0 = 'Hello! How are you? Good, right.'
expected_result =  ['Hello', ' How are you', ' Good', ' right', '']
result = test(str0)
assert result == expected_result, 'Test failed'