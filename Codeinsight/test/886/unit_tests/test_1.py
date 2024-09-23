var0 = "It was the best of times, it was the worst of times."
lst0 = ['a', 'an', 'and', 'is', 'the', 'to', 'in', 'of', 'it', 'was']
expected_result =  "best times, worst times."
result = test(var0, lst0)
assert result == expected_result, 'Test failed'