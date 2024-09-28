lst0 = ['!', ' there', 'everyone']
expected_result =  ['hello!', 'hello there', 'helloeveryone']
result = test(lst0)
assert result == expected_result, 'Test failed'