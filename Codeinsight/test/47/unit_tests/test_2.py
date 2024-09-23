var0 = {'alpha': {'number': 1, 'symbol': 'A'}, 'beta': {'number': 2, 'symbol': 'B'}, 'gamma': {'number': 3, 'symbol': 'C'}}
var1 = 'number'
expected_result =  {'alpha': {'number': 1, 'symbol': 'A'}, 'beta': {'number': 2, 'symbol': 'B'}, 'gamma': {'number': 3, 'symbol': 'C'}}
result = test(var0, var1)
assert result == expected_result, 'Test failed'