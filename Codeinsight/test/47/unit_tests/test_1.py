var0 = {'cat': {'age': 3, 'weight': 5}, 'dog': {'age': 2, 'weight': 7}, 'elephant': {'age': 5, 'weight': 10}}
var1 = 'age'
expected_result =  {'dog': {'age': 2, 'weight': 7}, 'cat': {'age': 3, 'weight': 5}, 'elephant': {'age': 5, 'weight': 10}}
result = test(var0, var1)
assert result == expected_result, 'Test failed'