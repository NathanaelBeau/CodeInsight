var0 = ['cat', 'dog', 'elephant']
var1 = ['meow', 'woof', 'trumpet']
expected_result =  {'cat': 'meow', 'dog': 'woof', 'elephant': 'trumpet'}
result = test(var0, var1)
assert result == expected_result, 'Test failed'