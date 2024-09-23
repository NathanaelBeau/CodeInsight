var0 = 'hello,"world,universe",galaxy,"planet"'
expected_result =  ['hello', 'world,universe', 'galaxy', 'planet']
result = test(var0)
assert result == expected_result, 'Test failed'