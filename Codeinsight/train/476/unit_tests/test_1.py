lst0 = ['Hello', 'World', 'world', 'HELLO']
expected_result =  ['hello', 'world']
result = test(lst0)
assert result == expected_result, 'Test failed'