lst0 = ['cat', 'dog', 'cat', 'cat', 'dog', 'dog']
var0 = ['cat']
expected_output = [['dog'], ['dog', 'dog']]
assert test(lst0,  var0) ==expected_output, 'Test failed'