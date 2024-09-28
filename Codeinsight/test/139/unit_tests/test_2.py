lst0 = ['apple', 'banana', 'cherry']
var0 = 3
lst1 = ['dragonfruit', 'elderberry']
expected_result =  ['apple', 'banana', 'cherry', 'dragonfruit', 'elderberry']
result = test(lst0, var0, lst1)
assert result == expected_result, 'Test failed'