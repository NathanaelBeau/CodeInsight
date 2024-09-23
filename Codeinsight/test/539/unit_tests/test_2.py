lst0 = [{'link': 'example8.com'}, {'link': 'example9.com'}]
lst1 = ['example8.com', 'example9.com']
expected_result =  []
result = test(lst0, lst1)
assert result == expected_result, 'Test failed'