lst0 = ['cat', 'dog', 'elephant']
lst1 = ['meow', 'woof', 'trumpet']
expected_result =  {'cat': 'meow', 'dog': 'woof', 'elephant': 'trumpet'}
result = test(lst0, lst1)
assert result == expected_result, 'Test failed'