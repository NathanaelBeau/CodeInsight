lst0 = [{'link': 'example1.com'}, {'link': 'example2.com'}, {'link': 'example3.com'}]
lst1 = ['example1.com', 'example4.com']
var0 = 'link'
expected_result =  [{'link': 'example2.com'}, {'link': 'example3.com'}]
result = test(lst0, lst1, var0)
assert result == expected_result, 'Test failed'