lst0 = [{'link': 'example5.com'}, {'link': 'example6.com'}, {'link': 'example7.com'}]
lst1 = []
var0 = 'link'
expected_result =  [{'link': 'example5.com'}, {'link': 'example6.com'}, {'link': 'example7.com'}]
result = test(lst0, lst1, var0)
assert result == expected_result, 'Test failed'