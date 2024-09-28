var0 = {'apple': {'price': 2.5, 'quantity': 10}, 'banana': {'price': 1.5, 'quantity': 5}, 'cherry': {'price': 3.0, 'quantity': 8}}
var1 = 'price'
expected_result =  {'banana': {'price': 1.5, 'quantity': 5}, 'apple': {'price': 2.5, 'quantity': 10}, 'cherry': {'price': 3.0, 'quantity': 8}}
result = test(var0, var1)
assert result == expected_result, 'Test failed'