var0 = "To be or not to be, that is the question."
lst0 = ['a', 'an', 'and', 'is', 'the', 'to', 'in']
expected_result =  "be or not be, that question."
result = test(var0, lst0)
assert result == expected_result, 'Test failed'