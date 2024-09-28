dict0 = {'apple': 'fruit', 'carrot': 'vegetable', 'chicken': 'meat'}
expected_result =  {'fruit': 'apple', 'vegetable': 'carrot', 'meat': 'chicken'}
result = test(dict0)
assert result == expected_result, 'Test failed'