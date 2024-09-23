var0 = {'existing_key': 'value'}
var1 = ['apple', 'banana']
var2 = 'fruits'
var3 = [10, 20]
expected_result =  {'existing_key': 'value', 'fruits': {'apple': 10, 'banana': 20}}
result = test(var0, var1, var2, var3)
assert result == expected_result, 'Test failed'