var0 = "The quick brown fox jumps over the lazy dog."
lst0 = ['a', 'an', 'and', 'is', 'the', 'to', 'in']
expected_result =  "quick brown fox jumps over lazy dog."
result = test(var0, lst0)
assert result == expected_result, 'Test failed'