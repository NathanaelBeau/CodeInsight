var0 = Element('root')
child1 = Element('child1')
var0.append(child1)
expected_result =  [child1]
result = test(var0)
assert result == expected_result, 'Test failed'