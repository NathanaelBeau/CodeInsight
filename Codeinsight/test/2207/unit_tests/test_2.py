lst0 = ["No Tab Here", "Still No Tab", "Not\tEven\tHere"]
expected_result =  ["No Tab Here", "Still No Tab", "Not"]
result = test(lst0)
assert result == expected_result, 'Test failed'