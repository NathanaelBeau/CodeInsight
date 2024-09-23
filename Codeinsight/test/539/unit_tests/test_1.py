lst0 = [{'link': 'example5.com'}, {'link': 'example6.com'}, {'link': 'example7.com'}]
lst1 = []
expected_result =  [{'link': 'example5.com'}, {'link': 'example6.com'}, {'link': 'example7.com'}]
result = test(lst0, lst1)
assert result == expected_result, 'Test failed'