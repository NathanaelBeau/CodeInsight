var0 = Element('root')
child1 = Element('child1')
child2 = Element('child2')
child3 = Element('child3')
var0.extend([child1, child2, child3])
expected_result =  [child1, child2, child3]
result = test(var0)
assert result == expected_result, 'Test failed'