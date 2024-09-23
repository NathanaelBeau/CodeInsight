var0 = Element('root')
child1 = Element('child1')
child2 = Element('child2')
var0.extend([child1, child2])
expected_result =  [child1, child2]
result = test(var0)
assert result == expected_result, 'Test failed'