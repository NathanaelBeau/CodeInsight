var0 = 'a,b,"c,d,e",f'
expected_result =  ['a', 'b', 'c,d,e', 'f']
result = test(var0)
assert result == expected_result, 'Test failed'