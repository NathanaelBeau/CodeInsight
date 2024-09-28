var0 = {'cat': 'meow', 'dog': 'woof', 'elephant': 'trumpet'}
expected_result =  [('cat', 'meow'), ('elephant', 'trumpet'), ('dog', 'woof')]
result = test(var0)
assert result == expected_result, 'Test failed'